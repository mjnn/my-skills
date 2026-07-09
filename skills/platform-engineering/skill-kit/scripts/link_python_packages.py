#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Link skill vendor/python-packages into portable Python site-packages via .pth files."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")


def find_site_packages(tools_root: str) -> str | None:
    base = os.path.join(tools_root, "python", "Lib", "site-packages")
    return base if os.path.isdir(base) else None


def skill_name_from_dir(skill_dir: str) -> str:
    return os.path.basename(os.path.abspath(skill_dir))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-dir", required=True, help="Root directory of the skill")
    parser.add_argument(
        "--tools-root",
        default=os.environ.get("QODER_TOOLS_ROOT", ""),
        help="skill-kit install root (default: QODER_TOOLS_ROOT)",
    )
    args = parser.parse_args()

    skill_dir = os.path.abspath(args.skill_dir)
    tools_root = args.tools_root or os.path.join(os.path.expanduser("~"), ".qoder-cn", "tools", "skill-kit")
    vendor = os.path.join(skill_dir, "vendor", "python-packages")
    site = find_site_packages(tools_root)

    if not site:
        print(json.dumps({"ok": False, "error": f"site-packages not found under {tools_root}"}, ensure_ascii=False))
        return 1

    skill_name = skill_name_from_dir(skill_dir)
    safe = re.sub(r"[^a-zA-Z0-9_-]", "-", skill_name)
    pth_name = f"qoder-skill-{safe}.pth"
    pth_path = os.path.join(site, pth_name)

    if not os.path.isdir(vendor):
        # No vendor packages — remove stale pth if any
        if os.path.isfile(pth_path):
            os.remove(pth_path)
        print(
            json.dumps(
                {"ok": True, "skill": skill_name, "linked": False, "reason": "no vendor/python-packages"},
                ensure_ascii=False,
            )
        )
        return 0

    # One line per package subdirectory (allows multiple roots in one pth)
    lines: list[str] = []
    for name in sorted(os.listdir(vendor)):
        pkg_path = os.path.join(vendor, name)
        if os.path.isdir(pkg_path):
            lines.append(pkg_path)

    if not lines:
        print(json.dumps({"ok": False, "error": "vendor/python-packages is empty"}, ensure_ascii=False))
        return 1

    os.makedirs(site, exist_ok=True)
    with open(pth_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    state_dir = os.path.join(tools_root, "state")
    os.makedirs(state_dir, exist_ok=True)
    state_file = os.path.join(state_dir, f"{safe}.json")
    with open(state_file, "w", encoding="utf-8") as f:
        json.dump(
            {"skill": skill_name, "skill_dir": skill_dir, "pth": pth_path, "packages": lines},
            f,
            ensure_ascii=False,
            indent=2,
        )

    print(
        json.dumps(
            {"ok": True, "skill": skill_name, "pth": pth_path, "package_paths": lines},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
