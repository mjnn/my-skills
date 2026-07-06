---
name: ecs-connect
description: >-
  Connects to the user's Alibaba Cloud ECS via SSH (alias ecs-main, KeyForAgent
  key pair), verifies connectivity, and runs read-only inspection (docker ps,
  /srv/apps, nginx -t). Handles Windows OpenSSH setup and troubleshooting.
  Use for ECS, SSH, 连接 ECS, 连服务器, ecs-main, KeyForAgent, 密钥对, 巡检,
  看日志, 能不能连上. For deploy/push/Nginx/ACR use ecs-github-delivery-ops instead.
  不适用于：Docker 部署、镜像推送、Nginx 配置、git push（走 ecs-github-delivery-ops）。
---

# ECS 连接

仅负责 **SSH 连通、密钥配置、只读巡检**。部署、镜像推送、Nginx、GitHub 见 [ecs-github-delivery-ops](../../ecs-github-delivery-ops/ecs-github-delivery-ops/SKILL.md)。


<HARD-GATE>
执行 SSH 命令、读取私钥或修改 ~/.ssh/config 前必须获得用户明确同意；禁止在未确认连通性前假设 ECS 可达。
</HARD-GATE>

## Gotchas

1. **未跑连通性检查就执行远程命令** — 后续步骤基于错误假设。**纠正：先 ssh BatchMode echo ok，失败查 reference 故障表。**
2. **回显私钥或 .pem 全文** — 安全风险。**纠正：只报路径，公钥仅一行 ssh-keygen -y。**
3. **PowerShell 用 && 链式命令** — 旧版 PS 报错。**纠正：用分号 ; 分隔。**
4. **与 ecs-github-delivery-ops 混淆** — 用户要部署却只做连接。**纠正：部署/镜像/Nginx 转 delivery-ops。**
5. **未 IdentitiesOnly 导致错密钥** — Permission denied。**纠正：config 中 IdentitiesOnly yes + 正确 IdentityFile。**



## 全局约束

- **禁止**回显或提交：私钥内容、`.pem` 全文、`authorized_keys` 中的敏感注释。
- **禁止**在未获用户确认时：`docker rm -f`、改 Nginx、改 `/srv/apps` 下生产配置。
- 公钥可在对话中核对；私钥只读路径，不粘贴内容。

## 默认连接参数

| 项 | 默认值 | 覆盖方式 |
|----|--------|----------|
| SSH 别名 | `ecs-main` | 用户指定或改 `~/.ssh/config` |
| 主机 | `47.116.180.173` | 用户指定 |
| 用户 | `root` | 用户指定 |
| 密钥 | `~/.ssh/KeyForAgent.pem` | 阿里云密钥对 **KeyForAgent** 下载的私钥 |
| 超时 | `ConnectTimeout 15` | config 或 `-o` |

详情与故障表：[reference.md](reference.md)

## 首次配置（Windows）

用户已在阿里云创建密钥对 **KeyForAgent** 并下载 `.pem` 时：

1. 私钥放到 `~/.ssh/KeyForAgent.pem`（可从 `Downloads/KeyForAgent.pem` 复制）。
2. 收紧权限（PowerShell）：

```powershell
icacls "$env:USERPROFILE\.ssh\KeyForAgent.pem" /inheritance:r /grant:r "${env:USERNAME}:(R)"
```

3. 写入 `~/.ssh/config`（不存在则创建）：

```
Host ecs-main
    HostName 47.116.180.173
    User root
    IdentityFile ~/.ssh/KeyForAgent.pem
    IdentitiesOnly yes
    ConnectTimeout 15
```

4. 校验公钥匹配（只显示导出的公钥一行，不读私钥全文）：

```powershell
ssh-keygen -y -f "$env:USERPROFILE\.ssh\KeyForAgent.pem"
```

应与用户在阿里云控制台看到的 **KeyForAgent 公钥** 一致（`ssh-rsa AAAAB3...` 段相同）。

5. 确认密钥对已**绑定到目标 ECS 实例**（控制台 → 实例 → 密钥对）。

**Agent 操作私钥/复制 `.pem` 前**：属凭证处理，需用户明确同意后再执行。

## 连通性检查（必做）

按序执行；任一步失败则查 [reference.md · 故障](reference.md) 对应行，**不要**假设已连上。

```powershell
# 1. 快速握手
ssh -o ConnectTimeout=15 -o BatchMode=yes ecs-main "echo ok"

# 2. 主机信息
ssh ecs-main "hostname && uname -a"

# 3. 只读巡检（可选，用户要「看看 ECS 状态」时）
ssh ecs-main "docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'"
ssh ecs-main "ls -la /srv/apps 2>/dev/null | head -20"
ssh ecs-main "nginx -t 2>&1"
```

别名不可用时，直连（需 config 中 HostName/User/IdentityFile 等效）：

```powershell
ssh -o ConnectTimeout=15 -i "$env:USERPROFILE\.ssh\KeyForAgent.pem" root@47.116.180.173 "hostname"
```

## 常见只读操作

```bash
# 容器日志（最近 100 行）
ssh ecs-main "docker logs --tail 100 <container_name>"

# 某服务 compose 目录
ssh ecs-main "ls -la /srv/apps/<service>/"

# 宿主机端口占用
ssh ecs-main "ss -tlnp | head -30"

# 磁盘
ssh ecs-main "df -h /"
```

PowerShell 链式命令用 `;`，不用 `&&`（旧版不支持）。

## 故障速查

| 现象 | 常见原因 | 动作 |
|------|----------|------|
| `Could not resolve hostname ecs-main` | 无 `~/.ssh/config` | 按上文创建 config |
| `Host key verification failed` | 首次连接 | `-o StrictHostKeyChecking=accept-new` 一次，或让用户确认指纹后写入 `known_hosts` |
| `Permission denied (publickey)` | 无私钥、未绑定密钥对、错用户 | 检查 `.pem` 路径、`IdentitiesOnly yes`、控制台密钥绑定 |
| `Connection timed out` | 安全组/实例关机/网络 | 查阿里云安全组 22、实例状态；勿反复暴力重试 |
| `WARNING: UNPROTECTED PRIVATE KEY FILE` | Windows 权限过宽 | 运行上文 `icacls` |
| 别名 OK 但部署失败 | 超出本 Skill 范围 | 转 **ecs-github-delivery-ops** |

完整说明：[reference.md](reference.md)

## 任务结束回报

```markdown
## ECS 连接
- 别名: ecs-main（或用户指定）
- 主机: <ip>
- 密钥: KeyForAgent.pem（已配置: 是/否）
- 连通: pass / fail（<错误摘要>）
- 巡检: <docker 容器数、/srv/apps 是否存在等，若已执行>
- 下一步: <仅连接 / 转部署 skill / 用户需控制台操作>
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
