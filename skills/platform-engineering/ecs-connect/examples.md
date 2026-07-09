# ECS 连接示例

## 用户：检查一下能不能连上 ECS

Agent 应：

1. 读 [SKILL.md](SKILL.md)，确认 `~/.ssh/config` 与 `KeyForAgent.pem` 是否存在。
2. 运行 `ssh -o BatchMode=yes ecs-main "hostname && uname -a"`。
3. 可选：`docker ps`、`ls /srv/apps`。
4. 按 SKILL 末尾模板回报 pass/fail。

## 用户：刚创建了阿里云密钥对 KeyForAgent

Agent 应：

1. 找 `Downloads/KeyForAgent.pem`（或问用户私钥路径）。
2. **经用户同意**后复制到 `~/.ssh/`，`icacls` 收紧权限，写 config。
3. `ssh-keygen -y` 核对公钥与用户提供的控制台公钥一致。
4. 测试 `ssh ecs-main "echo ok"`。
5. 提醒：密钥对须绑定到目标 ECS 实例。

## 用户：Permission denied (publickey)

Agent 应逐项查 [reference.md](reference.md) § Permission denied，不猜测密码登录（默认密钥实例可能禁用密码）。

## 用户：帮我在 ECS 上部署 xxx

Agent 应说明连接类任务已完成或先确保连通，然后**切换**到 **ecs-github-delivery-ops** 执行部署流程（ACR 门禁、端口门禁等）。
