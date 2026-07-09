#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Environment check for svw-ppt-generator (portable Python + vendor packages)."""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")


def check() -> None:
    errors: list[str] = []
    py = sys.executable
    print(f"[INFO] Python: {py}")

    for mod, label in [
        ("pptx", "python-pptx"),
        ("matplotlib", "matplotlib"),
        ("PIL", "Pillow"),
    ]:
        try:
            m = __import__(mod)
            ver = getattr(m, "__version__", "unknown")
            print(f"[OK] {label} ({ver})")
        except ImportError:
            errors.append(
                f"[ERROR] {label} missing. Bundle under vendor/python-packages/ "
                f"and run init_skill_python.ps1 (see skill-kit maintainer-bundle.md)"
            )

    try:
        skill_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        browser_root = os.path.join(skill_dir, "vendor", "playwright-browsers")
        os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", browser_root)
        import playwright  # noqa: F401

        print("[OK] playwright")
        if os.path.isdir(browser_root) and any(
            name.startswith("chromium") for name in os.listdir(browser_root)
        ):
            print(f"[OK] playwright browsers: {browser_root}")
        else:
            errors.append(f"[ERROR] playwright browsers missing under {browser_root}")
    except ImportError:
        errors.append(
            "[ERROR] playwright missing. Bundle wheels under vendor/python-packages/ "
            "and run init_skill_python.ps1"
        )

    skill_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(skill_dir, "templates", "模板.pptx")
    chart_template_path = os.path.join(skill_dir, "templates", "全品类图表模板_v1.0.html")
    if os.path.exists(template_path):
        print(f"[OK] template: {template_path}")
    else:
        errors.append(f"[ERROR] template missing: {template_path}")
    if os.path.exists(chart_template_path):
        print(f"[OK] chart template: {chart_template_path}")
    else:
        errors.append(f"[ERROR] chart template missing: {chart_template_path}")

    if errors:
        print("\n--- FAILED ---")
        for e in errors:
            print(e)
        sys.exit(1)
    print("\n--- OK: svw-ppt-generator runtime ready ---")
    sys.exit(0)


if __name__ == "__main__":
    check()
