# 参考（用户基础设施默认值）

以下为用户环境的**默认约定**，可在对话中被用户显式覆盖。

## GitHub（本机 svw / mjnn）

| 项 | 值 |
|----|-----|
| 默认 remote | `git@github.com:<owner>/<repo>.git` |
| my-skills | `git@github.com:mjnn/my-skills.git` |
| SSH 密钥 | `~/.ssh/id_ed25519_github`（勿用 KeyForAgent.pem） |
| 账号 | `mjnn` |
| 指纹 | `SHA256:NtjZ5te0PJybwqFJdXpSLjEaVki+FAWOIf5//tbXOOA` |

**本机**：HTTPS `443` 可能超时；`git push` 必须用 SSH。push 前验收见 **github-connect**。

## SSH

| 项 | 默认值 |
|----|--------|
| 别名 | `ecs-main`（`~/.ssh/config`） |
| 主机 | `47.116.180.173` |
| 用户 | `root` |

## ECS 目录与编排

| 项 | 约定 |
|----|------|
| 服务根 | `/srv/apps/<service>/` |
| 编排 | `compose.yaml` + `.env.runtime` |
| Compose | ECS 上优先 `docker-compose`（v1）；探测后再定，勿默认 `docker compose --project-name` |
| `.env.runtime` | 必须含非空 `IMAGE=`；`HOST_PORT` / `SERVICE_NAME` 与 compose 一致 |
| 容器名 | 以 compose 中 `container_name` 为准；未写则用 `<project>-<service>-N` |

## 宿主机端口（HOST_PORT）冲突检查

部署前在 ECS 上确认 `HOST_PORT` 未被**其他**服务占用。

```bash
# 拟用端口（从 compose / .env.runtime / 部署脚本读取）
HOST_PORT=8011

# 当前 Docker 端口映射
ssh ecs-main "docker ps --format 'table {{.Names}}\t{{.Ports}}'"

# 宿主机是否在监听
ssh ecs-main "ss -tlnp | grep -E ':8011\\s' || true"

# 各 app 已声明的 HOST_PORT
ssh ecs-main "grep -h '^HOST_PORT=' /srv/apps/*/.env.runtime 2>/dev/null"
```

| 结果 | 处理 |
|------|------|
| 端口空闲 | 继续部署 |
| 同 `container_name` 已占用 | 原地更新，可 `compose up` |
| 其他容器/进程占用 | **停止部署**，报告占用者，等用户换端口或下线旧服务 |
| 改 `HOST_PORT` | 同步 Nginx `proxy_pass` 与 `.env.runtime`，再 reload |

**禁止**未确认就 `docker rm -f` 占用端口的容器（遵守容器白名单）。

## 镜像路径解析（用于 ACR 门禁）

完整引用示例：

```text
crpi-xxxxx.cn-shanghai.personal.cr.aliyuncs.com/mirror_ns/my-app:1.0.0
```

| 段 | 含义 | 须在 ACR 已存在 |
|----|------|----------------|
| `crpi-....aliyuncs.com` | 镜像实例（Registry） | 容器镜像服务实例 / 登录地址 |
| `mirror_ns` | 命名空间 Namespace | 是 |
| `my-app` | 仓库 Repository | 是 |
| `1.0.0` | Tag | 首次 push 前无需预建 tag |

多镜像部署（如 host + 多个 tool 镜像）：**每个** `<namespace>/<repo>` 都要列入确认表。

## 阿里云 ACR：用户须在控制台完成（Agent 只询问、不代替创建）

部署前由用户自行确认（Agent 用对话表格列出路径后等待回复）：

1. 登录 [容器镜像服务 ACR](https://cr.console.aliyun.com/)
2. 对应地域的**实例**可访问（个人版 / 企业版与 `docker login` 域名一致）
3. **命名空间**已创建，名称与 push 路径一致
4. **镜像仓库**已创建，仓库名与 push 路径一致（注意大小写）
5. 若 ECS 需拉取：仓库/实例的**公网拉取**或**专有网络 VPC** 策略与 ECS 网络匹配
6. 本机与 ECS 已对 registry 执行 `docker login`（凭证未过期）

Agent **不得**在未获用户确认时假设「仓库已存在」。

## 镜像仓库（技术操作）

从以下来源解析镜像地址，不假定固定 registry：

1. 用户当次说明
2. 当前仓库 `compose.yaml` / `Dockerfile` / CI / 部署脚本中的 `IMAGE` / `image:`

```bash
docker login <registry>
echo "<password>" | docker login <registry> --username <user> --password-stdin
docker push <registry>/<namespace>/<repo>:<tag>
```

## 容器清理白名单

批量删除前排除用户指定的常驻容器名（示例：`get_dp_data`、`srs`）。

## Nginx 反向代理（ECS 宿主机）

| 项 | 约定 |
|----|------|
| 主配置 | `/etc/nginx/sites-enabled/default` |
| 服务片段 | `/etc/nginx/snippets/<service>-locations.conf` |
| 引入方式 | 在 `default` 的 `server {}` 内、`ecs-service-manage-generated-locations.conf` **之前** `include` |
| 公网路径风格 | `/tools/<service>/` 或 `/finance/<app>/`（以仓库 `deploy/nginx-*.conf` 为准） |
| 后端 upstream | `http://127.0.0.1:<HOST_PORT>/`（与 compose `.env.runtime` 一致） |
| 安装后 | `nginx -t` → `systemctl reload nginx` |
| SPA subpath | `VITE_BASE=<prefix>/`；`VITE_API_BASE=<prefix>`（路径已含 `/api/...`，勿重复 `/api`）；**优先** `frontend/.env.production` |

## SPA subpath 与 Git Bash（Windows 必防白屏）

| 项 | 说明 |
|----|------|
| 根因 | Git Bash 将 `export VITE_BASE="/tools/foo/"` 转为 `C:/Program Files/Git/tools/foo/` |
| 错误 index | `src="/Program Files/Git/tools/foo/assets/..."` → JS 404 → 白屏 |
| 首选修复 | 仓库提交 `frontend/.env.production`，不依赖 shell export |
| 脚本修复 | build 前 `export MSYS_NO_PATHCONV=1` 与 `MSYS2_ARG_CONV_EXCL='*'` |
| 部署门禁 | 构建后 + 公网 curl：`grep src= index.html`，禁止 `Program Files`；验 JS URL 200 |

PowerShell 构建可设 `$env:VITE_BASE="/tools/foo/"` 后 `npm run build`，无 MSYS 问题。

## ecs-service-manage（反向代理目录，与 Nginx 同步）

| 项 | 约定 |
|----|------|
| 面板 | `http://47.116.180.173/ops/ecs-manage/` |
| 数据文件 | `/opt/ecs_service_management/proxy-mappings.json` |
| 生成片段 | `/etc/nginx/snippets/ecs-service-manage-generated-locations.conf` |
| API 端口 | 宿主机 `3100`（`PANEL_USERNAME` / `PANEL_PASSWORD`，勿泄露） |
| Agent 默认写法 | 改 `proxy-mappings.json` 登记路径；有专用 snippet 时**不** `apply` |

配置任意服务 Nginx 路径时：**snippet/include + proxy-mappings.json** 两步都做。详见 [SKILL.md](SKILL.md)「能力四 · ecs-manage」。

## 构建与打包（经验默认值）

| 项 | 建议 |
|----|------|
| 前端 | 本机 `npm run build`，Dockerfile 只 `COPY frontend/dist` |
| SPA subpath | **优先** `frontend/.env.production`；Git Bash 脚本须 `MSYS_NO_PATHCONV=1` |
| tar 排除 | `node_modules`、`.git`、`backend/.env`、大体量可选目录 |
| 基础镜像 | 国内 ECS 可用 `m.daocloud.io/docker.io/library/...` |
| Python 依赖 | `-i https://pypi.tuna.tsinghua.edu.cn/simple` |
| 避免 | ECS 上 Dockerfile 内 `npm ci && npm run build`（易 SSH 断连） |
| 本机 Docker 不可用 | tar 上传后在 ECS `docker build && docker push` |

## 部署检查清单

- [ ] 镜像路径已解析为 registry / namespace / repo / tag
- [ ] **HOST_PORT 部署前无冲突**（或用户已确认替换/换端口）
- [ ] **用户已确认 ACR 命名空间与仓库已创建**
- [ ] `docker push` 成功（若本次需要推送）
- [ ] `/srv/apps/<service>/` compose 指向正确镜像
- [ ] `.env.runtime` 中 `grep '^IMAGE='` **非空**
- [ ] `docker ps` 目标容器 **Up (healthy)**（若有 healthcheck）
- [ ] `curl` 直连 `HOST_PORT` 健康检查通过
- [ ] `up -d` 与验收 URL 通过
- [ ] （若需 Nginx）片段已安装、`include` 已写入、`nginx -t` 通过
- [ ] **ecs-manage**：`proxy-mappings.json` 已登记该 `path` / `containerName` / `targetPort`
- [ ] （若 SPA）经 Nginx 公网路径 curl 健康检查与首页均 200
- [ ] （若 SPA subpath）`index.html` 内 asset 为 `<prefix>/assets/...`，**不含** `Program Files` 或 `/Git/`
- [ ] （若 SPA subpath）从 index 取出的 JS URL curl 返回 200
