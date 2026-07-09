#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""对比 Hub 已发布 skill 与用户已安装 skill 版本（节点 6）。"""
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


def fetch_hub_skills(token: str) -> dict[str, str]:
    """Return {skill_name: latest_version_tag} from GitLab releases."""
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


def scan_installed() -> dict[str, dict]:
    result = {}
    if not os.path.isdir(SKILLS_DIR):
        return result
    for name in os.listdir(SKILLS_DIR):
        path = os.path.join(SKILLS_DIR, name)
        if os.path.isdir(path) and os.path.isfile(os.path.join(path, "SKILL.md")):
            result[name] = {"version": read_installed_version(path), "path": path}
    return result


def compare(hub: dict[str, str], installed: dict[str, dict]) -> dict:
    rows = []
    all_names = sorted(set(hub) | set(installed))
    for name in all_names:
        hub_ver = hub.get(name)
        inst = installed.get(name)
        inst_ver = inst["version"] if inst else None
        if not hub_ver:
            status = "hub_unknown"
        elif not inst_ver:
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
    outdated = [r for r in rows if r["status"] == "outdated"]
    not_installed = [r for r in rows if r["status"] == "not_installed"]
    return {
        "skills_dir": SKILLS_DIR,
        "hub_count": len(hub),
        "installed_count": len(installed),
        "outdated_count": len(outdated),
        "not_installed_count": len(not_installed),
        "rows": rows,
        "outdated": outdated,
        "not_installed": not_installed,
    }


def main() -> int:
    token = get_token()
    hub = fetch_hub_skills(token)
    if not hub:
        # fallback: references/recommended-skills.md 静态表由 Agent 读取
        print(
            json.dumps(
                {
                    "ok": False,
                    "error": "无法从 GitLab API 获取 Releases，请确认 GITLAB_TOKEN 与节点 5 已通过",
                    "installed": scan_installed(),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 1

    installed = scan_installed()
    result = compare(hub, installed)
    result["ok"] = True
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
