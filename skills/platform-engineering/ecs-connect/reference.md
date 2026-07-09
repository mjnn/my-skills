# ECS 连接参考

用户环境默认值；对话中可被用户显式覆盖。

## SSH

| 项 | 值 |
|----|-----|
| 别名 | `ecs-main` |
| HostName | `47.116.180.173` |
| User | `root` |
| IdentityFile | `~/.ssh/KeyForAgent.pem` |
| 阿里云密钥对名称 | `KeyForAgent` |
| 公钥类型 | `ssh-rsa`（控制台可见；用于与 `ssh-keygen -y` 输出核对） |

## 本机路径（Windows）

| 文件 | 典型路径 |
|------|----------|
| SSH config | `C:\Users\<user>\.ssh\config` |
| 私钥 | `C:\Users\<user>\.ssh\KeyForAgent.pem` |
| 首次下载 | `C:\Users\<user>\Downloads\KeyForAgent.pem` |
| known_hosts | `C:\Users\<user>\.ssh\known_hosts` |

## ECS 只读路径（连通后可用）

| 路径 | 说明 |
|------|------|
| `/srv/apps/` | Docker Compose 服务根目录 |
| `/srv/apps/<service>/compose.yaml` | 编排文件 |
| `/srv/apps/<service>/.env.runtime` | 运行时 env（含 `IMAGE=`、`HOST_PORT`；勿回显密钥） |
| `/etc/nginx/snippets/` | Nginx 片段 |
| `/opt/ecs_service_management/proxy-mappings.json` | ecs-manage 代理目录 |
| 面板 | `http://47.116.180.173/ops/ecs-manage/`（宿主机端口 3100） |

## 故障排查详解

### 1. Could not resolve hostname ecs-main

- `~/.ssh/config` 不存在或缺少 `Host ecs-main` 块。
- 修复：写入 [SKILL.md](SKILL.md) 中的 config 模板；或临时用 `root@47.116.180.173` + `-i` 指定 pem。

### 2. Host key verification failed

- 首次连该 IP，或 `known_hosts` 中指纹与服务器不一致（重装系统、换实例）。
- 修复：用户确认服务器身份后，`ssh -o StrictHostKeyChecking=accept-new ecs-main "echo ok"`。
- 若怀疑中间人攻击，**不要**自动删 `known_hosts`；让用户在控制台核对实例 IP。

### 3. Permission denied (publickey)

| 检查项 | 命令 / 位置 |
|--------|-------------|
| 私钥是否存在 | `Test-Path ~/.ssh/KeyForAgent.pem` |
| config 是否指向该私钥 | `IdentityFile ~/.ssh/KeyForAgent.pem` + `IdentitiesOnly yes` |
| 公钥是否与控制台一致 | `ssh-keygen -y -f ~/.ssh/KeyForAgent.pem` |
| 密钥对是否绑定实例 | 阿里云 ECS 控制台 → 实例详情 → 密钥对 |
| 是否用错用户 | 默认 `root`；部分镜像为 `ecs-user` 等 |

仍失败：让用户在控制台「重置实例密码」或重新绑定密钥对（需用户操作，Agent 不能代替）。

### 4. Connection timed out

- 实例停止、弹性 IP 变更、本机防火墙、安全组未放行 **22/TCP**。
- 修复：控制台启动实例、核对公网 IP、安全组入方向 22 对当前出口 IP 或 `0.0.0.0/0`（后者由用户决定）。

### 5. UNPROTECTED PRIVATE KEY FILE

OpenSSH 要求私钥仅当前用户可读：

```powershell
icacls "$env:USERPROFILE\.ssh\KeyForAgent.pem" /inheritance:r /grant:r "${env:USERNAME}:(R)"
```

### 6. 连上但 docker/nginx 命令失败

- `docker: command not found` → 实例未装 Docker 或非 root 无权限。
- `nginx -t` 失败 → 配置问题，属运维/部署范畴，见 **ecs-github-delivery-ops**。

## 与 ecs-github-delivery-ops 的分工

| 任务 | 使用 Skill |
|------|------------|
| 测试 SSH、配密钥、docker ps、看日志 | **ecs-connect**（本 Skill） |
| compose 部署、ACR push、Nginx、GitHub | **ecs-github-delivery-ops** |
| 端口冲突门禁、镜像仓库门禁 | **ecs-github-delivery-ops** |

## 安全

- 私钥 `.pem` 仅保存在本机 `~/.ssh/`，不进 Git、不进聊天记录。
- 不要在对话中粘贴 `docker login` 密码、`.env.runtime` 全文、面板 `PANEL_PASSWORD`。
