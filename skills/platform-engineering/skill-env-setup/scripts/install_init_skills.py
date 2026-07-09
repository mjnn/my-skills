#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""解压 assets/init-skills/初始化技能包.zip 到 ~/.qoder-cn/skills/"""
from __future__ import annotations

import json
import os
import shutil
import sys
import tempfile
import zipfile

sys.stdout.reconfigure(encoding="utf-8")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.dirname(SCRIPT_DIR)
ZIP_CANDIDATES = [
    os.path.join(SKILL_ROOT, "assets", "init-skills", "init-skills-bundle.zip"),
    os.path.join(SKILL_ROOT, "assets", "init-skills", "初始化技能包.zip"),
]
SKILLS_DIR = os.path.join(os.path.expanduser("~"), ".qoder-cn", "skills")


def resolve_zip_path() -> str | None:
    for path in ZIP_CANDIDATES:
        if os.path.isfile(path):
            try:
                with zipfile.ZipFile(path, "r") as zf:
                    zf.namelist()
                return path
            except zipfile.BadZipFile:
                continue
    init_dir = os.path.join(SKILL_ROOT, "assets", "init-skills")
    if os.path.isdir(init_dir):
        zips = [
            os.path.join(init_dir, f)
            for f in os.listdir(init_dir)
            if f.lower().endswith(".zip")
        ]
        for path in sorted(zips, key=os.path.getmtime, reverse=True):
            try:
                with zipfile.ZipFile(path, "r") as zf:
                    zf.namelist()
                return path
            except zipfile.BadZipFile:
                continue
    return None


def load_manifest(extract_root: str) -> dict | None:
    manifest_path = os.path.join(extract_root, "manifest.json")
    if os.path.isfile(manifest_path):
        with open(manifest_path, encoding="utf-8") as f:
            return json.load(f)
    return None


def find_skill_dirs(root: str) -> list[str]:
    dirs = []
    for name in os.listdir(root):
        path = os.path.join(root, name)
        if os.path.isdir(path) and os.path.isfile(os.path.join(path, "SKILL.md")):
            dirs.append(name)
    return sorted(dirs)


def version_for_skill(manifest: dict | None, skill_name: str) -> str:
    if manifest and "skills" in manifest:
        for item in manifest["skills"]:
            if item.get("name") == skill_name:
                return item.get("version", "unknown")
    return "unknown"


def main() -> int:
    zip_path = resolve_zip_path()
    if not zip_path:
        print(
            json.dumps(
                {
                    "ok": False,
                    "error": "init skills bundle not found or corrupt",
                    "expected": ZIP_CANDIDATES,
                },
                ensure_ascii=False,
            )
        )
        return 1

    os.makedirs(SKILLS_DIR, exist_ok=True)

    installed: list[dict] = []
    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(tmp)

        manifest = load_manifest(tmp)
        skill_names = find_skill_dirs(tmp)

        if not skill_names:
            print(json.dumps({"ok": False, "error": "no skill directories with SKILL.md in bundle"}, ensure_ascii=False))
            return 1

        for name in skill_names:
            src = os.path.join(tmp, name)
            dst = os.path.join(SKILLS_DIR, name)
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            ver = version_for_skill(manifest, name)
            if ver != "unknown":
                with open(os.path.join(dst, ".installed-version"), "w", encoding="utf-8") as vf:
                    vf.write(ver.strip())
            installed.append({"name": name, "version": ver, "path": dst})

    result = {
        "ok": True,
        "zip": zip_path,
        "skills_dir": SKILLS_DIR,
        "installed_count": len(installed),
        "installed": installed,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
