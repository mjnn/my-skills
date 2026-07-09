---
name: github-connect
description: >-
  Verifies GitHub connectivity on Windows: Git CLI install, HTTPS/SSH network
  checks, SSH key setup (id_ed25519_github), ssh -T and git ls-remote validation.
  Use for GitHub, git, 连接 GitHub, SSH 密钥, clone, push 认证, 能不能连上,
  git ls-remote, Permission denied publickey. For commit/push/PR/deploy use
  ecs-github-delivery-ops instead.
  不适用于：git commit/push/PR（走 ecs-github-delivery-ops）、ECS SSH（走 ecs-connect）。
---

# GitHub 连接

仅负责 **Git 客户端、网络连通、SSH/HTTPS 认证配置与验证**。`git commit`、push 流程、PR、ECS 部署见 [ecs-github-delivery-ops](../../ecs-github-delivery-ops/ecs-github-delivery-ops/SKILL.md)。


<HARD-GATE>
生成/覆盖 SSH 私钥或安装 Git 前必须获得用户同意；禁止未经明确要求执行 git commit/push。
</HARD-GATE>

## Gotchas

1. **ssh -T exit 1 误判为失败** — GitHub 设计返回 1 但含 Hi username。**纠正：检查 stderr 含 Hi 即 pass。**
2. **SSH 使用 ECS 密钥 KeyForAgent** — Permission denied。**纠正：github.com 块 IdentitiesOnly + id_ed25519_github。**
3. **Git 安装后未刷新 PATH** — 当前会话找不到 git。**纠正：重装后刷新 Machine+User PATH 或新开终端。**
4. **公钥未加 GitHub 就宣布成功** — 后续 push 失败。**纠正：等用户确认 Settings 已添加。**
5. **与 ecs-github-delivery-ops 混淆** — 仅测连接却执行部署。**纠正：commit/push/ECS 转 delivery-ops。**
6. **HTTPS push 超时仍用 https remote** — 本机 443 可能不通。**纠正：remote 改为 `git@github.com:...`；见 [reference.md · 本机环境](reference.md)。**

## 本机已验证（svw / mjnn）

本机已配置 `id_ed25519_github`，GitHub 账号 **mjnn**，指纹 `SHA256:NtjZ5te0PJybwqFJdXpSLjEaVki+FAWOIf5//tbXOOA`。  
**跳过密钥生成**，直接 `ssh -T` 验收；push/clone 用 SSH remote。详情：[reference.md · 本机环境](reference.md)。

## 流程

按序执行；失败则查 [reference.md · 故障](reference.md)。

1. **检测 Git** — 刷新 PATH，`git --version`；未安装则经用户同意后 winget 安装
2. **网络检查** — Test-NetConnection 443/22；HTTPS `git ls-remote` 测公开库
3. **SSH 配置**（如需）— 生成/确认 `id_ed25519_github` → 写入 config → 用户添加公钥到 GitHub Settings
4. **SSH 认证验证** — `ssh -T`（exit 1 但含 `Hi username` 仍算 pass）
5. **任务结束回报** — 输出标准摘要；若用户要 push/部署则转 **ecs-github-delivery-ops**

## 全局约束

- **禁止**回显或提交：私钥全文、Personal Access Token、`.env`、凭据管理器中的密码。
- **禁止**未经用户明确要求就 `git commit` / `git push`。
- 公钥可展示一行供用户粘贴到 GitHub；私钥只报路径。
- GitHub SSH 密钥与 ECS 密钥**分开**（勿把 `KeyForAgent.pem` 加到 GitHub）。

## 默认连接参数

| 项 | 默认值 | 覆盖方式 |
|----|--------|----------|
| GitHub SSH Host | `github.com` | `~/.ssh/config` |
| SSH 私钥 | `~/.ssh/id_ed25519_github` | 用户指定或重新 `ssh-keygen` |
| SSH 公钥 | `~/.ssh/id_ed25519_github.pub` | 同上 |
| 密钥注释 | `svw-github` | `ssh-keygen -C` |
| 本机公钥指纹 | `SHA256:NtjZ5te0PJybwqFJdXpSLjEaVki+FAWOIf5//tbXOOA` | 与 GitHub Settings 核对 |
| GitHub 账号（本机） | `mjnn` | `ssh -T` 输出 Hi mjnn |
| my-skills remote | `git@github.com:mjnn/my-skills.git` | 本机勿用 HTTPS（443 可能超时） |
| Git 安装 | Git for Windows（winget `Git.Git`） | 用户指定路径 |
| 推荐克隆 URL | `git@github.com:<owner>/<repo>.git` | 或 HTTPS |

详情：[reference.md](reference.md)

## Git 未安装或不在 PATH

PowerShell 中检测：

```powershell
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
git --version
```

未找到时安装（需用户同意、可能弹出 UAC）：

```powershell
winget install --id Git.Git -e --source winget --accept-package-agreements --accept-source-agreements --disable-interactivity
```

安装后**新开终端**或刷新 PATH 再测。旧会话可能仍找不到 `git`。

## SSH 密钥首次配置（Windows）

本机已有 `id_ed25519_github` 时跳过生成，只做验证。

### 1. 生成密钥（尚无专用 GitHub 密钥时）

```powershell
ssh-keygen -t ed25519 -C "svw-github" -f "$env:USERPROFILE\.ssh\id_ed25519_github" -N '""'
```

带 passphrase 时把 `-N '""'` 改为交互式（让用户自行输入）。

**Agent 生成/覆盖私钥前**：需用户明确同意。

### 2. 写入 `~/.ssh/config`

与 ECS 的 `ecs-main` 块**并存**；`github.com` 建议写在文件**前面**：

```
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_github
    IdentitiesOnly yes
    ConnectTimeout 15
```

`IdentitiesOnly yes` 避免 SSH 把 ECS 的 `KeyForAgent.pem` 发给 GitHub。

### 3. 用户将公钥添加到 GitHub

展示公钥**一行**（勿读私钥）：

```powershell
Get-Content "$env:USERPROFILE\.ssh\id_ed25519_github.pub"
```

用户操作：GitHub → [Settings → SSH and GPG keys](https://github.com/settings/keys) → **New SSH key** → 粘贴 → 保存。

**必须等用户确认已添加**后再宣布 SSH 认证通过。

### 4. HTTPS 备选（用户不用 SSH 时）

- 克隆：`https://github.com/<owner>/<repo>.git`
- push 密码处填 **Personal Access Token**（非登录密码）
- Token 创建：Settings → Developer settings → Personal access tokens（`repo`  scope）
- **禁止**在对话中粘贴 token

## 连通性检查（必做）

按序执行；失败则查 [reference.md · 故障](reference.md)。

```powershell
# 刷新 PATH（当前 PowerShell 会话）
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# 1. Git 客户端
git --version

# 2. 网络（443 / 22）
Test-NetConnection github.com -Port 443 | Select-Object TcpTestSucceeded
Test-NetConnection github.com -Port 22 | Select-Object TcpTestSucceeded

# 3. HTTPS 读公开仓库（无需账号）
git ls-remote https://github.com/git/git.git HEAD

# 4. SSH 认证（公钥已加 GitHub 后应成功）
ssh -o BatchMode=yes -T git@github.com
```

PowerShell 验收 `ssh -T`：exit 1 但 stderr 含 `Hi <username>!` 仍算 **pass**（GitHub 设计如此）。

公网 HTTP（可选）：

```powershell
curl.exe -sI --connect-timeout 10 https://github.com | Select-Object -First 1
```

## 常见只读操作

```powershell
# 测某仓库 SSH 读权限（公开库即可）
git ls-remote git@github.com:<owner>/<repo>.git HEAD

# 当前目录是否 Git 仓库
git rev-parse --is-inside-work-tree 2>$null
git remote -v

# 全局 identity（未配置时 commit 会失败，属正常）
git config --global user.name
git config --global user.email
```

Windows：链式命令用 `;`；公网 curl 用 `curl.exe`。

## 故障速查

| 现象 | 常见原因 | 动作 |
|------|----------|------|
| `git` 不是内部或外部命令 | 未安装或未进 PATH | winget 安装；新开终端 |
| `git ls-remote` HTTPS 失败 | 网络/代理/DNS | 查防火墙、代理；测 443 |
| `Host key verification failed`（github.com） | 首次 SSH | `-o StrictHostKeyChecking=accept-new` 一次 |
| `Permission denied (publickey)` | 公钥未加 GitHub、错密钥 | 查 `id_ed25519_github` 与 config；让用户确认 Settings 已添加 |
| SSH 用了 ECS 密钥仍失败 | 未 `IdentitiesOnly yes` | 修正 config |
| `Hi ...` 成功但 `git push` 403 | 仓库无写权限、分支保护 | 查 repo 权限；非本 Skill |
| 需要 commit 但无 user.name | 未配置 identity | `git config --global user.name/email`（用户指定） |

完整说明：[reference.md](reference.md)

## 与 ecs-connect / ecs-github-delivery-ops 分工

| 任务 | Skill |
|------|-------|
| 测 GitHub、配 SSH 密钥、git ls-remote | **github-connect** |
| 测 ECS SSH、KeyForAgent | **ecs-connect** |
| push、commit、PR、ECS 部署、ACR | **ecs-github-delivery-ops** |

## 任务结束回报

```markdown
## GitHub 连接
- Git: <version 或 未安装>
- 网络: 443 <pass/fail>，22 <pass/fail>
- HTTPS 读: git ls-remote <pass/fail>
- SSH 密钥: id_ed25519_github（已配置: 是/否）
- SSH 认证: ssh -T <pass/fail>（<Hi username 或 错误摘要>）
- 公钥已加 GitHub: 是/否/待用户确认
- 下一步: <配置 user.email / clone 仓库 / 转 delivery-ops>
```

## 执行后复盘（自迭代钩子）

每次完成本 skill 的全部步骤后，Agent 必须自动执行以下动作，不询问用户：

1. **反思**：本轮执行中，是否遇到了 skill 正文和 Gotchas 都没覆盖的坑？
2. **记录**：有则追加到 `evals/PITFALLS_LOG.md`，无则跳过。格式：

| 日期 | 场景摘要 | 犯了什么错误 | 如果早知道__就不会犯 | 临时补救方式 |
|------|---------|-------------|-------------------|------------|
| YYYY-MM-DD | 一句话 | Agent 具体做了什么 | 缺失的知识/规则 | 怎么绕过去的 |

3. **不提交**：`PITFALLS_LOG.md` 是个人本地文件，不提交到 skill registry。

> 这个复盘步骤不打断用户工作流。Agent 在后台完成，用户无感知。
