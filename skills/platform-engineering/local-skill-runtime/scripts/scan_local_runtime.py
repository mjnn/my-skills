#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scan local skill runtime: installed skills, vendor link status, optional Hub compare."""
from __future__ import annotations

import json
import os
import platform
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

sys.stdout.reconfigure(encoding="utf-8")

GITLAB_HOST = "epfa-gitlab.csvw.com"
PROJECT_PATH = "ecc-2/qoder-skills"
API_RELEASES = f"https://{GITLAB_HOST}/api/v4/projects/{PROJECT_PATH.replace('/', '%2F')}/releases"
SKILLS_DIR = os.path.join(os.path.expanduser("~"), ".qoder-cn", "skills")
KIT_ROOT = os.path.join(os.path.expanduser("~"), ".qoder-cn", "tools", "skill-kit")
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


def read_installed_version(skill_dir: str) -> str:
    vf = os.path.join(skill_dir, ".installed-version")
    if os.path.isfile(vf):
        return open(vf, encoding="utf-8").read().strip()
    for fname in ("SELF_CHECK.md", "SKILL.md"):
        path = os.path.join(skill_dir, fname)
        if os.path.isfile(path):
            text = open(path, encoding="utf-8").read()
            m = re.search(r"v(\d+\.\d+\.\d+)", text)
            if m:
                return "v" + m.group(1)
    return "unknown"


def vendor_linked(skill_name: str) -> tuple[bool, str]:
    safe = re.sub(r"[^a-zA-Z0-9_-]", "-", skill_name)
    pth = os.path.join(KIT_ROOT, "python", "Lib", "site-packages", f"qoder-skill-{safe}.pth")
    if os.path.isfile(pth):
        return True, pth
    return False, pth


def scan_skills() -> list[dict]:
    rows = []
    if not os.path.isdir(SKILLS_DIR):
        return rows
    for name in sorted(os.listdir(SKILLS_DIR)):
        path = os.path.join(SKILLS_DIR, name)
        if not os.path.isdir(path):
            continue
        skill_md = os.path.join(path, "SKILL.md")
        if not os.path.isfile(skill_md):
            continue
        vendor_dir = os.path.join(path, "vendor", "python-packages")
        has_vendor = os.path.isdir(vendor_dir) and any(
            os.path.isdir(os.path.join(vendor_dir, d)) for d in os.listdir(vendor_dir)
        )
        linked, pth_path = vendor_linked(name) if has_vendor else (True, "")
        status = "ok"
        if has_vendor and not linked:
            status = "vendor_unlinked"
        rows.append(
            {
                "name": name,
                "path": path,
                "version": read_installed_version(path),
                "has_vendor": has_vendor,
                "vendor_linked": linked,
                "pth_path": pth_path if has_vendor else None,
                "status": status,
            }
        )
    return rows


def fetch_hub_skills(token: str) -> dict[str, str]:
    if not token:
        return {}
    req = Request(API_RELEASES, headers={"PRIVATE-TOKEN": token})
    try:
        with urlopen(req, timeout=30) as resp:
            releases = json.loads(resp.read().decode("utf-8"))
    except (HTTPError, URLError, json.JSONDecodeError):
        return {}

    latest: dict[str, tuple[str, str]] = {}
    for rel in releases:
        tag = rel.get("tag_name", "")
        m = TAG_RE.match(tag)
        if not m:
            continue
        name, ver = m.group(1), "v" + m.group(2)
        if name not in latest or ver > latest[name][1]:
            latest[name] = (tag, ver)
    return {name: ver for name, (_, ver) in latest.items()}


def compare_versions(hub: dict[str, str], installed: list[dict]) -> list[dict]:
    inst_map = {s["name"]: s for s in installed}
    rows = []
    for name in sorted(set(hub) | set(inst_map)):
        hub_ver = hub.get(name)
        inst = inst_map.get(name)
        inst_ver = inst["version"] if inst else None
        if not hub_ver:
            status = "hub_unknown"
        elif not inst:
            status = "not_installed"
        elif inst_ver == "unknown" or inst_ver != hub_ver:
            status = "outdated"
        else:
            status = "current"
        rows.append(
            {
                "name": name,
                "hub_version": hub_ver,
                "installed_version": inst_ver,
                "status": status,
            }
        )
    return rows


def main() -> int:
    compare_hub = "--compare-hub" in sys.argv
    skills = scan_skills()
    unlinked = [s for s in skills if s["status"] == "vendor_unlinked"]
    result: dict = {
        "ok": len(unlinked) == 0,
        "skills_dir": SKILLS_DIR,
        "kit_root": KIT_ROOT,
        "installed_count": len(skills),
        "skills": skills,
        "vendor_unlinked": unlinked,
        "vendor_unlinked_count": len(unlinked),
    }

    if compare_hub:
        token = get_token()
        hub = fetch_hub_skills(token)
        if not hub:
            result["hub_compare"] = {
                "ok": False,
                "error": "无法从 GitLab API 获取 Releases，请确认 GITLAB_TOKEN",
            }
        else:
            version_rows = compare_versions(hub, skills)
            outdated = [r for r in version_rows if r["status"] == "outdated"]
            not_installed = [r for r in version_rows if r["status"] == "not_installed"]
            result["hub_compare"] = {
                "ok": True,
                "hub_count": len(hub),
                "outdated_count": len(outdated),
                "not_installed_count": len(not_installed),
                "rows": version_rows,
                "outdated": outdated,
                "not_installed": not_installed,
            }
            if outdated or not_installed:
                result["ok"] = False

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    sys.exit(main())
