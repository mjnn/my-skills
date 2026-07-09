#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Download latest Hub Release zip for one skill and extract over local install dir."""
from __future__ import annotations

import argparse
import io
import json
import os
import platform
import re
import sys
import zipfile
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

sys.stdout.reconfigure(encoding="utf-8")

GITLAB_HOST = "epfa-gitlab.csvw.com"
PROJECT_PATH = "ecc-2/qoder-skills"
PROJECT_ENC = PROJECT_PATH.replace("/", "%2F")
API_RELEASES = f"https://{GITLAB_HOST}/api/v4/projects/{PROJECT_ENC}/releases"
SKILLS_DIR = os.path.join(os.path.expanduser("~"), ".qoder-cn", "skills")
TAG_RE = re.compile(r"^([^/]+)/v(.+)$")


def get_token() -> str:
    token = os.environ.get("GITLAB_TOKEN", "").strip()
    if token:
        return token
    if platform.system() == "Windows":
        try:
            import winreg

            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as key:
                token, _ = winreg.QueryValueEx(key, "GITLAB_TOKEN")
                return (token or "").strip()
        except OSError:
            pass
    return ""


def latest_release_for(skill: str, token: str) -> dict | None:
    req = Request(API_RELEASES, headers={"PRIVATE-TOKEN": token})
    with urlopen(req, timeout=30) as resp:
        releases = json.loads(resp.read().decode("utf-8"))
    best = None
    best_ver = ""
    for rel in releases:
        tag = rel.get("tag_name", "")
        m = TAG_RE.match(tag)
        if not m or m.group(1) != skill:
            continue
        ver = "v" + m.group(2)
        if ver > best_ver:
            best_ver = ver
            best = rel
    return best


def pick_zip_url(release: dict) -> str | None:
    for link in release.get("assets", {}).get("links", []):
        url = link.get("url", "")
        name = link.get("name", "")
        if name.endswith(".zip") or ".zip" in url:
            return url
    for src in release.get("assets", {}).get("sources", []):
        if src.get("format") == "zip":
            return src.get("url")
    return None


def extract_zip_to_skill(zip_bytes: bytes, skill: str) -> str:
    dest = os.path.join(SKILLS_DIR, skill)
    os.makedirs(dest, exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
        members = zf.namelist()
        prefix = None
        for m in members:
            parts = m.replace("\\", "/").split("/")
            if len(parts) >= 2 and parts[-1] == "SKILL.md":
                prefix = "/".join(parts[:-1]) + "/"
                break
        for m in members:
            if m.endswith("/"):
                continue
            rel = m.replace("\\", "/")
            if prefix and rel.startswith(prefix):
                rel = rel[len(prefix) :]
            elif "/" in rel:
                rel = rel.split("/", 1)[-1]
            target = os.path.join(dest, rel.replace("/", os.sep))
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with zf.open(m) as src, open(target, "wb") as out:
                out.write(src.read())
    return dest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", required=True)
    args = parser.parse_args()
    skill = args.skill.strip()
    token = get_token()
    if not token:
        print(json.dumps({"ok": False, "error": "GITLAB_TOKEN missing"}, ensure_ascii=False))
        return 1
    rel = latest_release_for(skill, token)
    if not rel:
        print(json.dumps({"ok": False, "error": f"No release for {skill}"}, ensure_ascii=False))
        return 1
    zip_url = pick_zip_url(rel)
    if not zip_url:
        print(json.dumps({"ok": False, "error": "No zip asset on release"}, ensure_ascii=False))
        return 1
    req = Request(zip_url, headers={"PRIVATE-TOKEN": token})
    try:
        with urlopen(req, timeout=120) as resp:
            data = resp.read()
    except (HTTPError, URLError) as e:
        print(json.dumps({"ok": False, "error": str(e)}, ensure_ascii=False))
        return 1
    dest = extract_zip_to_skill(data, skill)
    tag = rel.get("tag_name", "")
    ver = "unknown"
    m = TAG_RE.match(tag)
    if m:
        ver = "v" + m.group(2)
        with open(os.path.join(dest, ".installed-version"), "w", encoding="utf-8") as f:
            f.write(ver)
    print(json.dumps({"ok": True, "skill": skill, "version": ver, "path": dest}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
