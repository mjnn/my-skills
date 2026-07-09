#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""维护者：将多个 skill 目录打入 assets/init-skills/初始化技能包.zip"""
from __future__ import annotations

import json
import os
import sys
import zipfile
from datetime import date

sys.stdout.reconfigure(encoding="utf-8")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.dirname(SCRIPT_DIR)
OUT_ZIP = os.path.join(SKILL_ROOT, "assets", "init-skills", "init-skills-bundle.zip")
OUT_ZIP_CN = os.path.join(SKILL_ROOT, "assets", "init-skills", "初始化技能包.zip")


def main() -> int:
    import argparse

    p = argparse.ArgumentParser(description="Build 初始化技能包.zip")
    p.add_argument("skill_dirs", nargs="+", help="Paths to skill directories (each contains SKILL.md)")
    p.add_argument("--bundle-version", default=date.today().isoformat())
    args = p.parse_args()

    manifest_skills = []
    os.makedirs(os.path.dirname(OUT_ZIP), exist_ok=True)

    with zipfile.ZipFile(OUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zf:
        for d in args.skill_dirs:
            d = os.path.abspath(d)
            name = os.path.basename(d.rstrip("/\\"))
            if not os.path.isfile(os.path.join(d, "SKILL.md")):
                print(f"skip (no SKILL.md): {d}", file=sys.stderr)
                continue
            ver = "unknown"
            sc = os.path.join(d, "SELF_CHECK.md")
            if os.path.isfile(sc):
                import re

                m = re.search(r"v(\d+\.\d+\.\d+)", open(sc, encoding="utf-8").read())
                if m:
                    ver = "v" + m.group(1)
            manifest_skills.append({"name": name, "version": ver})
            skip_names = {os.path.basename(OUT_ZIP), os.path.basename(OUT_ZIP_CN)}
            for root, _, files in os.walk(d):
                for f in files:
                    if f in skip_names:
                        continue
                    full = os.path.join(root, f)
                    arc = os.path.join(name, os.path.relpath(full, d))
                    zf.write(full, arc)

        manifest = {"bundle_version": args.bundle_version, "skills": manifest_skills}
        zf.writestr("manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))

    import shutil

    shutil.copy2(OUT_ZIP, OUT_ZIP_CN)

    print(
        json.dumps(
            {"ok": True, "zip": OUT_ZIP, "zip_cn": OUT_ZIP_CN, "skills": manifest_skills},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
