#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检测系统工具硬依赖；失败时可生成 Markdown 报告。退出码 0=通过，1=存在硬依赖缺失。"""
from __future__ import annotations

import argparse
import json
import os
import platform
import socket
import subprocess
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.dirname(SCRIPT_DIR)


def run(cmd: list[str] | str, shell: bool = False) -> tuple[bool, str]:
    try:
        r = subprocess.run(
            cmd,
            shell=shell,
            capture_output=True,
            text=True,
            timeout=15,
        )
        out = (r.stdout or "").strip()
        err = (r.stderr or "").strip()
        text = out or err
        return r.returncode == 0, text.splitlines()[0] if text else ""
    except Exception as e:
        return False, str(e)


def check_qoder_cn() -> dict:
    ok, ver = run(["qoder-cn", "--version"])
    return {
        "id": "D1",
        "name": "Qoder CN",
        "status": "pass" if ok else "fail",
        "detail": ver if ok else "command not found",
        "remediation": "请先安装 Qoder CN 企业版客户端后再运行本 skill",
    }


def check_curl(is_windows: bool) -> dict:
    cmd = ["curl.exe", "--version"] if is_windows else ["curl", "--version"]
    ok, ver = run(cmd)
    return {
        "id": "D2",
        "name": "curl",
        "status": "pass" if ok else "fail",
        "detail": ver if ok else "curl not found",
        "remediation": "Win10+ 通常自带 curl.exe；Linux/macOS 请安装 curl 包",
    }


def check_archive(is_windows: bool) -> dict:
    tools: list[str] = []
    if is_windows:
        ok_ps, _ = run(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "(Get-Command Expand-Archive -ErrorAction SilentlyContinue).Source",
            ]
        )
        if ok_ps:
            tools.append("Expand-Archive")
        ok_tar, ver_tar = run(["tar", "--version"])
        if ok_tar:
            tools.append(f"tar ({ver_tar[:30]})")
        ok_unzip, _ = run(["where", "unzip"], shell=True)
        if ok_unzip:
            tools.append("unzip")
    else:
        ok_tar, ver_tar = run(["tar", "--version"])
        if ok_tar:
            tools.append(f"tar ({ver_tar[:30]})")
        ok_unzip, ver_unzip = run(["unzip", "-v"])
        if ok_unzip:
            tools.append(f"unzip ({ver_unzip[:30]})")
        ok_py, _ = run(["python3", "-c", "import zipfile"])
        if ok_py:
            tools.append("python3-zipfile")
        ok_ditto, _ = run(["ditto", "-h"])
        if ok_ditto:
            tools.append("ditto")

    ok = len(tools) > 0
    return {
        "id": "D3",
        "name": "解压工具",
        "status": "pass" if ok else "fail",
        "detail": ", ".join(tools) if tools else "none",
        "remediation": "Windows: 需要 PowerShell Expand-Archive 或 tar；Linux/macOS: 安装 unzip 或确保 python3 可用",
    }


def check_shell(is_windows: bool) -> dict:
    if is_windows:
        ok, out = run(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "$PSVersionTable.PSVersion.ToString()",
            ]
        )
        major = 0
        if ok and out:
            try:
                major = int(out.split(".")[0])
            except ValueError:
                pass
        pass_ok = ok and major >= 5
        return {
            "id": "D4",
            "name": "PowerShell",
            "status": "pass" if pass_ok else "fail",
            "detail": out if ok else "powershell not found",
            "remediation": "需要 PowerShell 5.1 或更高版本",
        }
    ok, ver = run(["bash", "--version"])
    return {
        "id": "D4",
        "name": "bash",
        "status": "pass" if ok else "fail",
        "detail": ver if ok else "bash not found",
        "remediation": "需要 bash 以执行 set_gitlab_token.sh 等脚本",
    }


def check_git() -> dict:
    ok, ver = run(["git", "--version"])
    return {
        "id": "C1",
        "name": "git",
        "status": "pass" if ok else "fail",
        "detail": ver if ok else "not installed (MinGit available on Windows in node 4)",
        "remediation": "Windows 可选 MinGit；Linux/macOS 需安装 git 或使用 Zip 安装路径",
    }


def check_mingit_bundle(is_windows: bool) -> dict:
    if not is_windows:
        return {
            "id": "C2",
            "name": "MinGit 内置包",
            "status": "skip",
            "detail": "N/A on non-Windows",
            "remediation": "",
        }
    git_dir = os.path.join(SKILL_ROOT, "assets", "git")
    found = False
    name = ""
    if os.path.isdir(git_dir):
        for f in os.listdir(git_dir):
            if f.startswith("MinGit-") and f.endswith("-64-bit.zip"):
                found = True
                name = f
                break
    return {
        "id": "C2",
        "name": "MinGit 内置包",
        "status": "pass" if found else "fail",
        "detail": name if found else "MinGit-*-64-bit.zip not found in assets/git/",
        "remediation": "确保 skill 包完整，assets/git/ 含 MinGit 便携 zip",
    }


def check_gitlab_token() -> dict:
    val = os.environ.get("GITLAB_TOKEN", "")
    if not val and platform.system() == "Windows":
        try:
            import winreg

            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as key:
                val, _ = winreg.QueryValueEx(key, "GITLAB_TOKEN")
        except OSError:
            val = ""
    configured = bool(val and str(val).strip())
    return {
        "id": "C3",
        "name": "GITLAB_TOKEN",
        "status": "pass" if configured else "pending",
        "detail": "configured" if configured else "not set (will collect in node 2)",
        "remediation": "节点 2 信息收集阶段配置，非节点 0 阻断项",
    }


def check_post_kit() -> dict:
    tools_root = os.environ.get(
        "QODER_TOOLS_ROOT", os.path.join(os.path.expanduser("~"), ".qoder-cn", "tools", "skill-kit")
    )
    python_exe = os.environ.get("QODER_PYTHON", os.path.join(tools_root, "python", "python.exe"))
    git_exe = os.environ.get("QODER_GIT", os.path.join(tools_root, "git", "cmd", "git.exe"))

    py_ok = os.path.isfile(python_exe)
    git_ok = os.path.isfile(git_exe)
    py_detail = python_exe if py_ok else "not found"
    git_detail = git_exe if git_ok else "not found"
    if py_ok:
        ok, ver = run([python_exe, "-c", "import sys; print(sys.version.split()[0])"])
        if ok:
            py_detail = ver

    hard = [
        {
            "id": "K1",
            "name": "QODER_PYTHON",
            "status": "pass" if py_ok else "fail",
            "detail": py_detail,
            "remediation": "运行 install_skill_kit.ps1",
        },
        {
            "id": "K2",
            "name": "QODER_GIT",
            "status": "pass" if git_ok else "fail",
            "detail": git_detail,
            "remediation": "运行 install_skill_kit.ps1（需 MinGit zip）",
        },
    ]
    hard_pass = all(item["status"] == "pass" for item in hard)
    return {
        "os": f"{platform.system()} {platform.release()}",
        "hostname": socket.gethostname(),
        "timestamp": datetime.now().astimezone().isoformat(timespec="seconds"),
        "hard_dependencies": hard,
        "conditional_dependencies": [],
        "hard_gate": "pass" if hard_pass else "fail",
        "message": "skill-kit 便携工具已就绪" if hard_pass else "skill-kit 安装不完整",
        "mode": "post-kit",
    }


def build_report(is_windows: bool) -> dict:
    os_info = f"{platform.system()} {platform.release()}"
    hard = [
        check_qoder_cn(),
        check_curl(is_windows),
        check_archive(is_windows),
        check_shell(is_windows),
    ]
    conditional = [
        check_git(),
        check_mingit_bundle(is_windows),
        check_gitlab_token(),
    ]
    hard_pass = all(item["status"] == "pass" for item in hard)
    return {
        "os": os_info,
        "hostname": socket.gethostname(),
        "timestamp": datetime.now().astimezone().isoformat(timespec="seconds"),
        "hard_dependencies": hard,
        "conditional_dependencies": conditional,
        "hard_gate": "pass" if hard_pass else "fail",
        "message": "所有硬依赖已满足，可进入配置流程"
        if hard_pass
        else "硬依赖未全部满足，禁止进入配置流程，请先修复缺失项",
    }


def _status_icon(status: str) -> str:
    return {"pass": "✅ PASS", "fail": "❌ FAIL", "pending": "⏳ 待配置", "skip": "— N/A"}.get(
        status, status
    )


def render_markdown(report: dict) -> str:
    hard = report["hard_dependencies"]
    cond = report["conditional_dependencies"]
    fails = [x for x in hard if x["status"] == "fail"]
    hard_pass = report["hard_gate"] == "pass"
    passed = sum(1 for x in hard if x["status"] == "pass")
    cond_notes = sum(1 for x in cond if x["status"] in ("fail", "pending"))

    lines = [
        "# Qoder Skills 环境依赖不满足报告",
        "",
        f"> 生成时间：{report['timestamp']}",
        f"> 检测主机：{report.get('hostname', 'unknown')}",
        f"> 操作系统：{report['os']}",
    ]
    if hard_pass:
        lines.append("> **硬依赖门禁：已通过 — 可进入配置流程**")
    else:
        lines.append("> **硬依赖门禁：未通过 — 配置流程已暂停**")
    lines.extend(["", "## 摘要", "", "| 指标 | 数值 |", "|------|------|"])
    lines.append("| 硬依赖总数 | 4 |")
    lines.append(f"| 已通过 | {passed} |")
    lines.append(f"| **未通过** | **{len(fails)}** |")
    lines.append(f"| 条件依赖待关注 | {cond_notes} |")
    lines.extend(["", "## 硬依赖检测结果", ""])
    lines.append("| ID | 依赖 | 状态 | 检测详情 | 修复指引 |")
    lines.append("|----|------|------|---------|---------|")
    for item in hard:
        fix = "—" if item["status"] == "pass" else item["remediation"]
        lines.append(
            f"| {item['id']} | {item['name']} | {_status_icon(item['status'])} | {item['detail']} | {fix} |"
        )

    if fails:
        lines.extend(["", "## 未通过项明细（需用户或 IT 处理）", ""])
        for item in fails:
            lines.extend(
                [
                    f"### {item['id']} — {item['name']}",
                    "",
                    f"- **当前状态**：{item['detail']}",
                    f"- **影响**：配置流程无法继续，需修复后方可安装 skill",
                    f"- **建议操作**：",
                    f"  1. {item['remediation']}",
                    f"  2. 修复后执行 `python scripts/check_system_deps.py --report-auto` 重新检测",
                    f"  3. 或对本 skill 说「重新检测依赖」",
                    "",
                ]
            )

    lines.extend(["## 条件依赖（不阻断，供后续参考）", ""])
    lines.append("| ID | 依赖 | 状态 | 说明 |")
    lines.append("|----|------|------|------|")
    for item in cond:
        lines.append(
            f"| {item['id']} | {item['name']} | {_status_icon(item['status'])} | {item['detail']} |"
        )

    lines.extend(
        [
            "",
            "## 下一步",
            "",
        ]
    )
    if hard_pass:
        lines.append("1. 硬依赖已全部满足，可继续「配置 Qoder Skills 环境」流程（节点 1 起）")
    else:
        lines.extend(
            [
                "1. 按上表「未通过项明细」逐项修复（可转发本报告给 IT）",
                "2. 修复后运行：`python scripts/check_system_deps.py --report-auto`",
                "3. 硬依赖全部通过后，重新发起环境配置",
            ]
        )
    lines.extend(["", "---", "*本报告由 skill-env-setup 节点 0 自动生成。*", ""])
    return "\n".join(lines)


def write_report(report: dict, path: str) -> str:
    # 通过时用 dependency-pass 前缀
    if report["hard_gate"] == "pass":
        path = path.replace("dependency-fail", "dependency-pass")
    md = render_markdown(report)
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(md)
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Check system dependencies for skill-env-setup")
    parser.add_argument("--report", metavar="PATH", help="Write Markdown report to PATH")
    parser.add_argument(
        "--report-auto",
        action="store_true",
        help="Write report to ~/.qoder-cn/reports/dependency-fail-{timestamp}.md",
    )
    parser.add_argument(
        "--post-kit",
        action="store_true",
        help="After skill-kit install: verify QODER_PYTHON and QODER_GIT only",
    )
    parser.add_argument("--json-only", action="store_true", help="Print JSON only (no Markdown file)")
    args = parser.parse_args()

    if args.post_kit:
        report = check_post_kit()
    else:
        is_windows = platform.system() == "Windows"
        report = build_report(is_windows)
    hard_pass = report["hard_gate"] == "pass"

    report_path = None
    if args.report_auto:
        home = os.path.expanduser("~")
        report_dir = os.path.join(home, ".qoder-cn", "reports")
        os.makedirs(report_dir, exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        prefix = "dependency-pass" if hard_pass else "dependency-fail"
        report_path = os.path.join(report_dir, f"{prefix}-{stamp}.md")
        write_report(report, report_path)
    elif args.report:
        report_path = write_report(report, args.report)

    out = dict(report)
    if report_path:
        out["report_file"] = report_path
        out["report_markdown"] = render_markdown(report)

    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if hard_pass else 1


if __name__ == "__main__":
    sys.exit(main())
