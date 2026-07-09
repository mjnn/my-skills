#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GitLab 全权限连通验证（节点 5）。退出码 0=全部通过，1=存在失败项。"""
from __future__ import annotations

import argparse
import json
import os
import platform
import re
import subprocess
import sys
from datetime import datetime
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

sys.stdout.reconfigure(encoding="utf-8")

GITLAB_HOST = "epfa-gitlab.csvw.com"
PROJECT_PATH = "ecc-2/qoder-skills"
REPO_URL = f"https://{GITLAB_HOST}/{PROJECT_PATH}.git"
API_PROJECT = f"https://{GITLAB_HOST}/api/v4/projects/{PROJECT_PATH.replace('/', '%2F')}"


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


def api_get(url: str, token: str) -> tuple[bool, str, int]:
    req = Request(url, headers={"PRIVATE-TOKEN": token})
    try:
        with urlopen(req, timeout=20) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return True, body, resp.status
    except HTTPError as e:
        return False, e.read().decode("utf-8", errors="replace")[:500], e.code
    except URLError as e:
        return False, str(e.reason), 0


def run_git(args: list[str]) -> tuple[bool, str]:
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=30)
        out = (r.stdout or r.stderr or "").strip()
        return r.returncode == 0, out.splitlines()[0] if out else ""
    except Exception as e:
        return False, str(e)


def check_g1_token() -> dict:
    token = get_token()
    ok = bool(token)
    return {
        "id": "G1",
        "name": "GITLAB_TOKEN",
        "status": "pass" if ok else "fail",
        "detail": "configured" if ok else "not set",
        "remediation": "运行 set_gitlab_token 脚本写入用户环境变量",
    }


def check_g2_user(token: str) -> dict:
    if not token:
        return {"id": "G2", "name": "API /user", "status": "fail", "detail": "no token", "remediation": "配置 GITLAB_TOKEN"}
    ok, body, code = api_get(f"https://{GITLAB_HOST}/api/v4/user", token)
    username = ""
    if ok:
        try:
            username = json.loads(body).get("username", "")
        except json.JSONDecodeError:
            pass
    return {
        "id": "G2",
        "name": "API /user",
        "status": "pass" if ok and username else "fail",
        "detail": f"user={username}" if ok else f"HTTP {code}: {body[:120]}",
        "remediation": "Token 需含 api scope",
    }


def check_g3_project(token: str) -> dict:
    if not token:
        return {"id": "G3", "name": "项目可读", "status": "fail", "detail": "no token", "remediation": "配置 GITLAB_TOKEN"}
    ok, body, code = api_get(API_PROJECT, token)
    return {
        "id": "G3",
        "name": "项目可读",
        "status": "pass" if ok else "fail",
        "detail": "OK" if ok else f"HTTP {code}: {body[:120]}",
        "remediation": "确认 Token 有 read_repository/api，且有项目访问权限",
    }


def check_g4_releases(token: str) -> dict:
    if not token:
        return {"id": "G4", "name": "Releases 可读", "status": "fail", "detail": "no token", "remediation": "配置 GITLAB_TOKEN"}
    ok, body, code = api_get(f"{API_PROJECT}/releases", token)
    count = 0
    if ok:
        try:
            count = len(json.loads(body))
        except json.JSONDecodeError:
            pass
    return {
        "id": "G4",
        "name": "Releases 可读",
        "status": "pass" if ok else "fail",
        "detail": f"{count} releases" if ok else f"HTTP {code}: {body[:120]}",
        "remediation": "Token 需 api scope",
    }


def check_g5_ls_remote(token: str) -> dict:
    if not token:
        return {"id": "G5", "name": "git ls-remote", "status": "fail", "detail": "no token", "remediation": "配置 GITLAB_TOKEN"}
    url = REPO_URL.replace("https://", f"https://oauth2:{token}@")
    ok, out = run_git(["git", "ls-remote", url, "HEAD"])
    return {
        "id": "G5",
        "name": "git ls-remote",
        "status": "pass" if ok else "fail",
        "detail": out if ok else out or "ls-remote failed",
        "remediation": "配置 read_repository；内网执行 http.sslVerify false",
    }


def check_g6_push(token: str) -> dict:
    if not token:
        return {"id": "G6", "name": "git push 权限", "status": "fail", "detail": "no token", "remediation": "配置 GITLAB_TOKEN"}
    ok, body, code = api_get(f"https://{GITLAB_HOST}/api/v4/personal_access_tokens/self", token)
    if ok:
        try:
            scopes = json.loads(body).get("scopes", [])
            has_write = "write_repository" in scopes or "api" in scopes
            return {
                "id": "G6",
                "name": "git push 权限",
                "status": "pass" if has_write else "fail",
                "detail": f"scopes={scopes}",
                "remediation": "Token 需 write_repository 或 api scope",
            }
        except json.JSONDecodeError:
            pass
    ok2, _, code2 = api_get(f"{API_PROJECT}/repository/branches", token)
    return {
        "id": "G6",
        "name": "git push 权限",
        "status": "pass" if ok2 else "fail",
        "detail": "branch API OK (proxy)" if ok2 else f"HTTP {code2}; self endpoint HTTP {code}",
        "remediation": "Token 需 write_repository",
    }


def check_g7_ssl(g5_passed: bool) -> dict:
    if g5_passed:
        return {"id": "G7", "name": "SSL", "status": "pass", "detail": "ls-remote OK", "remediation": ""}
    return {
        "id": "G7",
        "name": "SSL",
        "status": "fail",
        "detail": "ls-remote failed (likely SSL or auth)",
        "remediation": "git config --global http.sslVerify false（内网自签名）",
    }


def check_g8_identity() -> dict:
    ok_name, name = run_git(["git", "config", "--global", "user.name"])
    ok_email, email = run_git(["git", "config", "--global", "user.email"])
    ok = ok_name and ok_email and name and email
    return {
        "id": "G8",
        "name": "Git 身份",
        "status": "pass" if ok else "fail",
        "detail": f"{name} <{email}>" if ok else "name or email missing",
        "remediation": "git config --global user.name / user.email",
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# GitLab 连通验证报告",
        "",
        f"> 生成时间：{report['timestamp']}",
        f"> GitLab Hub：{REPO_URL}",
        f"> 门禁：{'通过' if report['gate'] == 'pass' else '未通过'}",
        "",
        "| ID | 检查项 | 状态 | 详情 |",
        "|----|--------|------|------|",
    ]
    for item in report["checks"]:
        icon = "OK" if item["status"] == "pass" else "FAIL"
        lines.append(f"| {item['id']} | {item['name']} | {icon} | {item['detail']} |")
    fails = [x for x in report["checks"] if x["status"] == "fail"]
    if fails:
        lines.extend(["", "## 未通过项修复指引", ""])
        for item in fails:
            lines.append(f"- **{item['id']} {item['name']}**：{item['remediation']}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report-auto", action="store_true")
    args = parser.parse_args()

    token = get_token()
    g5 = check_g5_ls_remote(token)
    checks = [
        check_g1_token(),
        check_g2_user(token),
        check_g3_project(token),
        check_g4_releases(token),
        g5,
        check_g6_push(token),
        check_g7_ssl(g5["status"] == "pass"),
        check_g8_identity(),
    ]
    gate = "pass" if all(c["status"] == "pass" for c in checks) else "fail"
    report = {
        "timestamp": datetime.now().astimezone().isoformat(timespec="seconds"),
        "gate": gate,
        "checks": checks,
    }

    report_path = None
    if args.report_auto:
        home = os.path.expanduser("~")
        d = os.path.join(home, ".qoder-cn", "reports")
        os.makedirs(d, exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        prefix = "gitlab-access-pass" if gate == "pass" else "gitlab-access-fail"
        report_path = os.path.join(d, f"{prefix}-{stamp}.md")
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(render_markdown(report))

    out = dict(report)
    if report_path:
        out["report_file"] = report_path
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if gate == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
