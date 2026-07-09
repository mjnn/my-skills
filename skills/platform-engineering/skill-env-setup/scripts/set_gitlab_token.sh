#!/usr/bin/env bash
# 将 GitLab Access Token 写入用户环境变量（macOS/Linux）
set -euo pipefail

if [[ $# -lt 1 || -z "${1:-}" ]]; then
  echo "用法: $0 <gitlab-access-token>" >&2
  exit 1
fi

TOKEN="$1"
EXPORT_LINE="export GITLAB_TOKEN='${TOKEN//\'/\'\\\'\'}'"

for rc in "$HOME/.bashrc" "$HOME/.zshrc"; do
  if [[ -f "$rc" ]]; then
    if grep -q '^export GITLAB_TOKEN=' "$rc" 2>/dev/null; then
      sed -i.bak '/^export GITLAB_TOKEN=/d' "$rc"
    fi
    echo "$EXPORT_LINE" >> "$rc"
    echo "已更新 $rc"
  fi
done

export GITLAB_TOKEN="$TOKEN"
echo "GITLAB_TOKEN 已配置。请执行 source ~/.bashrc 或重新打开终端。"
