# GitHub 连接参考

用户环境默认值；对话中可被用户显式覆盖。

## 本机已验证环境（svw / mjnn）

> 2026-07-09 验收通过。Agent 在本机操作 GitHub 时**优先使用以下默认值**，勿重复生成密钥。

| 项 | 值 |
|----|-----|
| GitHub 账号 | `mjnn` |
| SSH 私钥 | `C:\Users\svw\.ssh\id_ed25519_github` |
| SSH 公钥 | `C:\Users\svw\.ssh\id_ed25519_github.pub` |
| 密钥注释 | `svw-github` |
| 公钥指纹 (SHA256) | `SHA256:NtjZ5te0PJybwqFJdXpSLjEaVki+FAWOIf5//tbXOOA` |
| `ssh -T` 验收 | `Hi mjnn! You've successfully authenticated...` |
| 推荐 remote | `git@github.com:<owner>/<repo>.git` |
| my-skills 仓库 | `git@github.com:mjnn/my-skills.git` |

**本机网络注意**：HTTPS `443` 可能无法连接 GitHub（超时）；`git push` / `git clone` **必须用 SSH**（22 端口）。若 remote 为 HTTPS 且失败：

```powershell
git remote set-url origin git@github.com:<owner>/<repo>.git
```

核对 GitHub Settings 中公钥指纹与上表 SHA256 一致即表示密钥配对正确。

## SSH / Git 文件（Windows）

| 文件 | 典型路径 |
|------|----------|
| SSH config | `C:\Users\<user>\.ssh\config` |
| GitHub 私钥 | `C:\Users\<user>\.ssh\id_ed25519_github` |
| GitHub 公钥 | `C:\Users\<user>\.ssh\id_ed25519_github.pub` |
| ECS 私钥（勿用于 GitHub） | `C:\Users\<user>\.ssh\KeyForAgent.pem` |
| known_hosts | 含 `github.com` ED25519 指纹 |
| 全局 Git 配置 | `C:\Users\<user>\.gitconfig` |

## 推荐 `~/.ssh/config` 片段

```
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_github
    IdentitiesOnly yes
    ConnectTimeout 15

Host ecs-main
    HostName 47.116.180.173
    User root
    IdentityFile ~/.ssh/KeyForAgent.pem
    IdentitiesOnly yes
    ConnectTimeout 15
```

## Git 安装

| 项 | 值 |
|----|-----|
| 推荐包 | `winget install --id Git.Git -e` |
| 典型版本 | 2.54.x（随 winget 更新） |
| 二进制 | `C:\Program Files\Git\bin\git.exe` |
| PATH | 安装器默认加入；旧终端需重开 |

## 验收标准

| 检查 | 通过条件 |
|------|----------|
| `git --version` | 输出版本号 |
| `Test-NetConnection github.com -Port 443` | `TcpTestSucceeded : True` |
| `git ls-remote https://github.com/git/git.git HEAD` | 输出 commit hash |
| `ssh -T git@github.com` | 含 `Hi <username>! You've successfully authenticated` |
| `git ls-remote git@github.com:<owner>/<private>.git` | 私有库需 SSH 已认证且有权限 |

## 故障排查详解

### 1. git 命令找不到

- 安装 Git for Windows 后未刷新 PATH。
- 修复：新开 PowerShell / Cursor；或手动刷新 Machine+User PATH（见 SKILL.md）。

### 2. HTTPS 通、SSH publickey 失败

| 检查 | 方法 |
|------|------|
| 公钥是否在 GitHub | 用户确认 Settings → SSH keys |
| 本地公钥文件 | `Get-Content ~/.ssh/id_ed25519_github.pub` |
| config 指向正确 | `IdentityFile ~/.ssh/id_ed25519_github` |
| 未误用 ECS 密钥 | `IdentitiesOnly yes` |
| 代理干扰 | `ssh -vT git@github.com` 看 Offering public key 哪一把 |

### 3. Host key verification failed

首次连接 GitHub：

```powershell
ssh -o StrictHostKeyChecking=accept-new -T git@github.com
```

官方 ED25519 指纹见 GitHub 文档；用户可从 https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints 核对。

### 4. ssh -T 成功但 git push 失败

- 403 / denied：仓库 write 权限、组织 SSO 授权、分支保护。
- 需 HTTPS token 或检查 remote 是 SSH 还是 HTTPS。
- 转 **ecs-github-delivery-ops** 处理 push/PR 流程。

### 5. commit 失败：user.name / user.email unknown

与「连接 GitHub」无关，但首次 commit 常见：

```powershell
git config --global user.name "Display Name"
git config --global user.email "email@example.com"
```

邮箱可用 GitHub noreply：`<id>@users.noreply.github.com`。

### 6. gh CLI

本 Skill 不依赖 `gh`。用户要 PR/issue 时可另装 [GitHub CLI](https://cli.github.com/) 并 `gh auth login`；deploy 流程见 **ecs-github-delivery-ops**。

## 安全

- 私钥、PAT、Fine-grained token 不进 Git、不进聊天记录。
- 不要在仓库 `.env` 或脚本里硬编码 token。
- Git Credential Manager 已随 Git for Windows 安装时可缓存 HTTPS 凭据；Agent 不读取凭据存储内容。

## 相关 Skill

| Skill | 用途 |
|-------|------|
| **github-connect** | 本 Skill：连通与认证 |
| **ecs-connect** | ECS SSH |
| **ecs-github-delivery-ops** | push、部署、ACR、Nginx |
