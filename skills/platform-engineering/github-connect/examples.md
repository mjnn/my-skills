# GitHub 连接示例

## 用户：测一下能不能连上 GitHub

Agent 应：

1. 刷新 PATH，`git --version`。
2. `Test-NetConnection` 443/22，`git ls-remote` HTTPS 公开库。
3. `ssh -T git@github.com`（BatchMode）。
4. 按 SKILL 回报模板汇总；SSH 失败时区分「网络通但未加公钥」与「git 未装」。

## 用户：帮我配置 SSH 密钥

Agent 应：

1. 检查是否已有 `id_ed25519_github`；无则 **经用户同意** `ssh-keygen`。
2. 合并写入 `~/.ssh/config`（保留 `ecs-main` 块，`IdentitiesOnly yes`）。
3. 输出 `.pub` **一行**供用户粘贴 GitHub。
4. **等待用户确认已添加** 后再 `ssh -T` 验收。

## 用户：Permission denied (publickey)

Agent 查 [reference.md](reference.md) § HTTPS 通 SSH 失败，不建议把 KeyForAgent.pem 上传到 GitHub。

## 用户：帮我 push 到 GitHub

Agent 先 `ssh -T` / `git remote -v` 确认连接与 remote，然后切换 **ecs-github-delivery-ops**（含 commit 须用户明确要求、禁止 force push main 等规则）。

## 用户：安装 git

```powershell
winget install --id Git.Git -e --source winget --accept-package-agreements --accept-source-agreements --disable-interactivity
```

安装后新开终端，`git --version` 验收。
