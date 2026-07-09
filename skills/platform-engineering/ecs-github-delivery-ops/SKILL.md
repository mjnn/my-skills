---
name: ecs-github-delivery-ops
description: >-
  Connects to the user's ECS via SSH, deploys services with Docker Compose,
  configures Nginx reverse-proxy URL paths, and pushes git to GitHub. Before
  docker push or ECS deploy, requires the user to confirm Alibaba Cloud Container
  Registry (namespace and repository) already exists. SPA subpath deploys on
  Windows must use frontend/.env.production or MSYS_NO_PATHCONV=1 to avoid Git
  Bash turning VITE_BASE into /Program Files/Git/... (white screen). Use for ECS,
  部署, 镜像推送, 阿里云镜像仓库, docker compose, Nginx 反向代理, Vite subpath,
  Git Bash 白屏, 端口冲突, HOST_PORT, ecs-manage 代理目录, GitHub.
  不适用于：仅 SSH 连通测试（走 ecs-connect）、仅 GitHub 认证配置（走 github-connect）。
---

# ECS + GitHub 交付运维

**绝对通用**：不绑定任何单一产品或仓库。所有项目名、镜像仓库、健康检查路径、部署脚本均以**当前工作区**或**用户当次说明**为准。


<HARD-GATE>
docker push 或 ECS compose 部署前必须确认阿里云 ACR 命名空间与仓库已存在且用户已确认；禁止 git push --force 到 main/master。
涉及 docker build/push、ECS compose up、Nginx 变更或 git push 前，必须 EnterSpecMode 生成部署计划并经用户确认后 ExitSpecMode，才能执行。
</HARD-GATE>

## Gotchas

1. **未确认 ACR 仓库就 push** — repository does not exist。**纠正：列出镜像表，等用户回复「已创建，可继续」。**
2. **Git Bash 下 VITE_BASE 被转成 /Program Files/Git/** — SPA 白屏。**纠正：用 MSYS_NO_PATHCONV=1 或 .env.production。**
3. **compose up 前未查端口冲突** — 502/端口占用。**纠正：ss -tlnp 核对 HOST_PORT。**
4. **与 ecs-connect 混淆** — 仅测 SSH 却启动完整部署。**纠正：只读连接走 ecs-connect。**
5. **未经确认 git commit** — 违反用户规则。**纠正：仅用户明确要求时 commit。**



## 全局约束

- **禁止**回显或提交：明文密码、完整数据库连接串、registry token、`.env` 内容。
- **禁止** `git push --force` 到 `main`/`master`，除非用户明确要求。
- **禁止**未经用户明确要求就 `git commit`。
- ECS 服务统一目录：`/srv/apps/<service>/`，文件：`compose.yaml` + `.env.runtime`；**禁止**长期依赖裸 `docker run`。
- 删除容器前必须确认**白名单**（用户维护，见 [reference.md](reference.md)）。

## 执行前收集（缺则询问）

| 参数 | 来源优先级 |
|------|------------|
| SSH 目标 | 用户指定 → `~/.ssh/config` 别名 → [reference.md](reference.md) 默认值 |
| 服务名 `<service>` | 用户指定 → `compose.yaml` 所在目录名 → `/srv/apps` 下列表 |
| 镜像 `<registry>/<namespace>/<repo>:<tag>` | 用户指定 → compose / CI / 部署脚本中的 `image` |
| 宿主机端口 `HOST_PORT` | compose `ports` / `.env.runtime` / 部署脚本默认值 |
| 健康检查 URL | 用户指定 → compose healthcheck → 常见 `/health`（仅作尝试） |
| Git 远程与分支 | `git remote get-url origin`、`git branch --show-current` |

**仓库自有部署能力**：若存在 `scripts/*deploy*`、`deploy/**/compose.yaml`、`**/DEPLOY*.md`、`**/RELEASE*.md`，**优先阅读并执行该仓库文档与脚本**，不在本 Skill 中臆造步骤。

### Spec 模式（部署动作前必做）

涉及 `docker build`/`push`、ECS `compose up`、Nginx 配置变更或 `git push` 前：

1. 信息收集完成后，调用 `EnterSpecMode` 进入 spec 模式
2. Spec 必须包含：目标 `<service>`、完整镜像列表、HOST_PORT、健康检查 URL、Git 远程/分支、将修改的文件路径
3. 用户审核 Spec 后调用 `ExitSpecMode` 确认，**才能**执行部署命令

### 镜像仓库门禁（push 与 ECS 部署前强制）

镜像路径决定阿里云 ACR 上是否已有对应**命名空间**与**仓库**。未确认前 **禁止** `docker push`、**禁止** ECS 上 `compose pull` / 部署。

1. **解析**本次将推送/拉取的全部镜像（可能多个 tag），对每个完整引用列出：
   - Registry 地址（登录域名）
   - 命名空间（Namespace）
   - 仓库名（Repository）
   - Tag
2. **向用户发起确认**（必须等待回复，不得自行假定）— 使用 AskUserQuestion：

调用 AskUserQuestion（1 个问题）：

| 问题 | header | 选项 |
|------|--------|------|
| 以下镜像对应的 ACR 命名空间与仓库是否已在阿里云创建？ | ACR确认 | 已创建，可继续（推荐）/ 尚未创建，暂停 / 取消部署 |

同时展示镜像清单表格：

| 完整镜像引用 | Registry | 命名空间 | 仓库名 | Tag |
|-------------|----------|----------|--------|-----|
| ...         | ...      | ...      | ...    | ... |

3. **仅在用户明确表示已创建**（或等价肯定）后，才执行：
   - `docker login <registry>`（密码用 `--password-stdin`，勿回显）
   - `docker build` / `docker push`
   - ECS `compose pull` / `up -d` / 仓库部署脚本
4. **首次**推送到某 `<namespace>/<repo>` 时，提醒用户在控制台新建仓库（类型、地域、公网访问与 ECS 拉取权限与现网一致）。
5. 若 `docker push` 报错 `repository does not exist`、`name unknown`、`denied` 等 → **立即停止**后续 ECS 步骤，提示先创建仓库或修正路径，**不得**用错误镜像名继续部署。

仅「访问 ECS、看日志、GitHub push、不涉及新镜像推送」时，可跳过本门禁。

### 端口冲突门禁（ECS `compose up` 前强制）

在 ECS 上执行 `docker-compose up -d`、写入 `.env.runtime` 的 `HOST_PORT`、或安装 Nginx upstream **之前**，必须确认宿主机监听端口与容器名无冲突。

#### 解析本次将占用的端口

从以下来源读取（优先级同上）：

| 来源 | 典型字段 |
|------|----------|
| `.env.runtime` / 部署脚本 | `HOST_PORT=8011` |
| `compose.yaml` | `"${HOST_PORT}:${CONTAINER_PORT}"` |
| Nginx 片段 | `proxy_pass http://127.0.0.1:<host_port>/` |
| ecs-manage | `targetPort` 为**容器内**端口；宿主机映射仍以 `HOST_PORT` 为准 |

记录：`<service>`、`<container_name>`、`<HOST_PORT>`、`<CONTAINER_PORT>`。

#### ECS 巡检命令（部署前必跑）

```bash
ssh <ssh-alias> "docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'"
ssh <ssh-alias> "ss -tlnp | grep -E ':<HOST_PORT>\\s' || true"
# ss 不可用时：
ssh <ssh-alias> "netstat -tlnp 2>/dev/null | grep ':<HOST_PORT> ' || true"
# 各服务已配置的 HOST_PORT（更新部署时对照）
ssh <ssh-alias> "grep -h '^HOST_PORT=' /srv/apps/*/.env.runtime 2>/dev/null || true"
```

#### 判定规则

| 情况 | 结论 | 动作 |
|------|------|------|
| 端口未被占用 | 通过 | 继续部署 |
| 端口由**本服务**同名容器占用（`container_name` 一致） | 通过 | 视为原地更新，`compose up` 会 recreate |
| 端口被**其他**容器 / 进程占用 | **冲突** | **停止** `compose up`；向用户报告占用者名称与端口 |
| 新服务首次上线，端口已被占 | **冲突** | 换 `HOST_PORT` 或请用户确认下线旧服务；**同步改** Nginx `proxy_pass` 与 ecs-manage 登记 |
| `container_name` 已被其他镜像占用 | **冲突** | 改 `SERVICE_NAME` / `container_name` 或先停旧容器（须用户确认，遵守白名单） |

**禁止**在未确认的情况下 `docker rm -f` 占用端口的容器。

#### 冲突时与用户沟通（示例）

```markdown
部署 `<service>` 需要宿主机端口 **8011**，但 ECS 上已被占用：

| 端口 | 当前占用者 | 状态 |
|------|-----------|------|
| 8011 | fund_chart | Up 3 days |

请回复：
- 改用其他端口（如 8012）— 我将同步 Nginx / `.env.runtime`；或
- 确认可替换 fund_chart — 我将先停旧服务再部署。
```

#### 与 Nginx / ecs-manage 的一致性

`HOST_PORT` 变更时，**同一轮部署**内必须一并更新：

1. `/srv/apps/<service>/.env.runtime` 的 `HOST_PORT`
2. `/etc/nginx/snippets/<service>-*.conf` 中 `127.0.0.1:<HOST_PORT>`
3. `proxy-mappings.json` 中对应条目（`targetPort` 仍为容器内端口，一般不变）

改端口后 `nginx -t && systemctl reload nginx`，再 `curl` 直连新端口与 Nginx 公网路径。

---

## 能力一：访问 ECS

```bash
ssh <ssh-alias> "hostname && uname -a"
```

默认别名与主机见 [reference.md](reference.md)（可被用户覆盖）。

巡检（按需）：

```bash
ssh <ssh-alias> "docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'"
ssh <ssh-alias> "ls -la /srv/apps"
ssh <ssh-alias> "nginx -t 2>&1"
```

---

## 能力二：部署 / 更新服务

### 标准流程（默认）

1. **连通性**：`hostname && uname -a`
2. **端口冲突门禁**：解析 `HOST_PORT` / `container_name` → SSH 巡检（见上文）→ 无冲突或用户确认后再继续
3. **镜像仓库门禁**：解析 `<registry>/<namespace>/<repo>:<tag>` → **询问用户确认 ACR 已创建**（见上文）；未确认则停止。
4. **构建并推送镜像**（用户确认后，本机）：

```bash
docker login <registry>   # 已登录且未过期可跳过
docker build -t <registry>/<namespace>/<repo>:<tag> .
docker push <registry>/<namespace>/<repo>:<tag>
```

5. **ECS 上更新 compose**（镜像 tag 写入 `.env.runtime` 的 `IMAGE=`；**ECS 优先用 `docker-compose`**，见下「Compose 命令」）：

```bash
ssh <ssh-alias> "mkdir -p /srv/apps/<service>"
# 将 compose.yaml、.env.runtime 同步到 ECS（scp/rsync/或仓库脚本）
ssh <ssh-alias> "cd /srv/apps/<service> && docker-compose --env-file .env.runtime -f compose.yaml pull"
ssh <ssh-alias> "cd /srv/apps/<service> && docker-compose --env-file .env.runtime -f compose.yaml up -d --remove-orphans"
```

6. **验收**（必须；**不可仅信脚本打印 Done**）：

```bash
# .env.runtime 中 IMAGE 非空
ssh <ssh-alias> "grep '^IMAGE=' /srv/apps/<service>/.env.runtime"
# 容器在跑
ssh <ssh-alias> "docker ps --filter name=<service>"
# 直连端口健康检查
ssh <ssh-alias> "curl -fsS http://127.0.0.1:<host_port><health-path>"
# 若配置了 Nginx，再验公网路径（见能力四）
curl -fsS "http://<public-host><location_prefix>/..."
# 若含 SPA + Nginx subpath：必须验 index 内 asset 路径（见「SPA subpath 构建」）
curl -s "http://<public-host><location_prefix>/" | grep -E 'src=|href='
```

7. 若涉及 **Nginx 反代**：见「能力四」；**必须同步 ecs-manage 代理目录**（见「能力四 · ecs-manage」）；`nginx -t` → `reload` → `curl` 公网入口 URL。

### 新服务首次上线

1. **端口冲突门禁**：确认拟用 `HOST_PORT` 在 ECS 上未被占用（见上文）
2. 在 ECS 创建 `/srv/apps/<service>/`
3. 写入 `compose.yaml`、`.env.runtime`（密钥仅放 ECS，不进 Git）
4. `up -d` + 验收
5. 需要对外域名/路径时，按「能力四」增加 Nginx `location` 片段并安装，并同步 **ecs-manage** 反向代理页

### 使用仓库脚本

当用户说「按项目脚本部署」或仓库内已有现成脚本时：

```bash
# 示例：在仓库根目录执行（具体以该仓库 README 为准）
./scripts/deploy.sh
# 或
bash scripts/deploy-to-ecs.sh <tag>
```

执行前阅读脚本用法（`--help` 或脚本头部注释），不替换为臆造命令。

脚本若会 `docker push` 或向 ECS 写入 `IMAGE=...`：**仍须先完成镜像仓库门禁**（从脚本/compose 中提取全部镜像路径并让用户确认），再执行脚本。

### 构建在哪里做（本机 vs ECS）

按环境选择，**禁止**在 ECS 上跑耗时的多阶段前端构建（易 SSH 超时、会话断开）：

| 场景 | 推荐做法 |
|------|----------|
| 含 Vite/Webpack 的 SPA | **本机构建** `frontend/dist` → 打进 tar → ECS 上 **单阶段** Dockerfile 只 COPY dist |
| 本机无法 `docker build`（拉不到 docker.io） | 本机构前端 + `tar` 上传 → **在 ECS 上** `docker build` + `docker push` ACR |
| 纯 Python/Go 无前端 | 本机或 ECS build 均可；ECS build 时 Dockerfile 避免 `# syntax=docker.io/...` |
| 数据/表文件较大 | tar 时排除 `node_modules`、`.git`、`backend/.env`、可选 `local_data/sources` |

**ECS 远程 build 流程（本机 Docker 不可用时）**：

```bash
# 本机
npm run build   # 或仓库等价命令
tar -czf /tmp/deploy.tgz --exclude=node_modules --exclude=.git --exclude=backend/.env -C . .
scp /tmp/deploy.tgz <ssh-alias>:/tmp/
# ECS
ssh <ssh-alias> 'cd /tmp && rm -rf build && mkdir build && tar xzf deploy.tgz -C build && cd build && docker build -t <image> . && docker push <image>'
```

Dockerfile 在 ECS/国内网络建议：基础镜像用镜像站（如 `m.daocloud.io/docker.io/library/...`），pip 用清华源；**不要**在 ECS 镜像构建阶段再 `npm ci && npm run build`。

### Compose 命令（ECS 兼容性）

用户 ECS 常见情况：**仅有 `docker-compose`（v1）**，`docker compose` 报 `unknown command` 或 `unknown flag: --project-name`。

1. 部署前先探测：`ssh <alias> "docker compose version 2>/dev/null || docker-compose version"`
2. ECS 上统一用：`docker-compose --env-file .env.runtime -f compose.yaml pull|up -d`
3. 项目名由 compose 文件所在目录或 `-p <service>` 决定，**不要**假设 v2 的 `--project-name` 可用

### `.env.runtime` 与「假成功」

常见陷阱：镜像已 push，但 compose 未起来，脚本仍打印 Done。

| 现象 | 原因 | 处理 |
|------|------|------|
| `service "app" has neither an image nor a build context` | `.env.runtime` 里 `IMAGE=` 为空 | `sed` 写入完整镜像名后重新 `up -d` |
| `unknown flag: --project-name` | 用了 docker compose v2 语法 | 改用 `docker-compose` |
| push/build 成功但 8010 无响应 | compose 步骤失败被忽略 | 验收必须 `docker ps` + `curl` 直连端口 |
| PowerShell 部署脚本 IMAGE 未写入 | heredoc 中 `$REG` 被 PowerShell 提前展开 | 远程 bash 里用 `` `$REG `` 转义，或改用 `bash deploy-to-ecs.sh` |
| Nginx 首页 200 但浏览器白屏 | Git Bash 把 `VITE_BASE=/tools/...` 转成 `/Program Files/Git/tools/...` | 见下「SPA subpath 构建 · Git Bash 路径转换」；部署后 curl index 验 asset 路径 |
| `compose up` 成功但 curl 端口失败 / 连到错误服务 | `HOST_PORT` 与其他容器冲突，或 Nginx upstream 端口未同步 | 部署前跑端口门禁；冲突则停部署；改端口后同步 Nginx |

写入 `IMAGE` 推荐模式（远程 bash）：

```bash
if grep -q '^IMAGE=' .env.runtime; then
  sed -i "s|^IMAGE=.*|IMAGE=${REG}|" .env.runtime
else
  echo "IMAGE=${REG}" >> .env.runtime
fi
grep '^IMAGE=' .env.runtime   # 部署后必须非空
```

### SSH / 上传可靠性

- 部署前：`ssh -o ConnectTimeout=15 <alias> "echo ok"`；失败则**重试**，不要立刻放弃。
- `scp` 传大 tar 可能长时间无输出；会话超时会导致 **exit 255**，不等于 ECS 上 build 失败——先 SSH 上去看 `/tmp/*-build` 与 `docker images`。
- 可拆分步骤：仅更新 Nginx（`install-nginx-*.sh`）、仅 `compose up`（镜像已存在时），避免每次都全量 tar。

### Windows 开发机

- PowerShell **不支持** `&&` 链式命令，用 `;` 或分开执行。
- 验收公网 URL 用 **`curl.exe`**，避免 alias 到 `Invoke-WebRequest` 参数不兼容。
- 优先在 Git Bash / WSL 跑 `deploy-to-ecs.sh`；若用 `.ps1`，注意远程脚本变量转义。
- **Git Bash 部署 SPA subpath 时**：必须在构建前 `export MSYS_NO_PATHCONV=1`（见「SPA subpath 构建」）；或改用 PowerShell 设 `$env:VITE_BASE` 再 `npm run build`；**禁止**在未验 `index.html` asset 路径的情况下宣布部署成功。

### SPA subpath 构建（Nginx 路径前缀 + Vite/Webpack）

经 Nginx 以 `<location_prefix>/`（如 `/tools/myapp/`）对外暴露时，前端构建必须让 `index.html` 内 JS/CSS 引用带此前缀。

#### 推荐：仓库内固定 `.env.production`（首选，免 shell 污染）

在 `frontend/.env.production`（可提交 Git）写入：

```dotenv
VITE_BASE=/tools/myapp/
# 服务挂载前缀（不含 /api）；前端 request 路径若已写 /api/xxx 则 base 勿再加 /api
VITE_API_BASE=/tools/myapp
```

变量名以项目为准（`VITE_API_BASE_URL`、`PUBLIC_URL` 等）。`npm run build` 时 Vite 直接读文件，**不依赖** deploy 脚本里的 `export`，可彻底避开 Git Bash 路径转换。

#### 部署脚本内 export（若仍用 shell 传参）

**在 `npm run build` 之前**必须禁用 MSYS 路径转换：

```bash
export MSYS_NO_PATHCONV=1
export MSYS2_ARG_CONV_EXCL='*'
  export VITE_BASE="${NGINX_PREFIX}/"
  export VITE_API_BASE="${NGINX_PREFIX}"
npm run build
```

#### Git Bash 路径转换（白屏根因，必知）

| 项 | 说明 |
|----|------|
| **现象** | 首页 HTTP 200，浏览器白屏；`index.html` 里出现 `src="/Program Files/Git/tools/myapp/assets/..."` |
| **原因** | Git Bash（MSYS）把以 `/` 开头的 `VITE_BASE="/tools/myapp/"` 当成 MSYS 路径，映射到 `C:/Program Files/Git/tools/myapp/` |
| **错误信号** | asset URL 含 `Program Files`、`/Git/`；或 Vite 警告 `"base" option should start with a slash` 且 base 异常 |
| **正确信号** | `src="/tools/myapp/assets/index-xxxxx.js"`（与 Nginx `<location_prefix>/` 一致） |

#### 构建后强制门禁（Agent 必须执行，通过后再 push 镜像）

```bash
# 1. 本地或 CI 构建后立即检查
grep -E 'src=|href=' frontend/dist/index.html
# 必须包含 <location_prefix>/assets/
# 不得包含 Program Files 或 /Git/

# 2. 部署后验公网（PowerShell 用 curl.exe）
curl -s "http://<public-host><location_prefix>/" | grep -E 'src=|href='
# 从 index 取出 js 路径，再验 200：
curl -fsS -o /dev/null -w '%{http_code}\n' "http://<public-host><location_prefix>/assets/index-xxxxx.js"
```

任一步失败 → **停止**后续 ECS 步骤，修正 `.env.production` 或 `MSYS_NO_PATHCONV` 后重新构建，**不得**用错误 dist 打镜像。

#### vite.config 建议

`base` 从 `loadEnv` 读取后规范化：必须以 `/` 开头、subpath 时以 `/` 结尾，避免 deploy 脚本传参不一致。

React Router 等需配置 `basename`（去掉尾斜杠），与 `VITE_BASE` 一致。

### 失败兜底

- 容器反复重启 / 日志 `connection refused` → 查应用 → 数据库端口（常见 5432/3306）从 ECS 是否可达。
- `docker compose` 不存在 → **改用 `docker-compose`**（v1）；不要用 `--project-name`。
- 镜像拉取失败 → 在 ECS 上 `docker login`，勿在聊天中粘贴密码；若因仓库不存在 → 回到镜像仓库门禁，勿反复 `pull`。
- SSH `Connection timed out` → 检查 ECS 是否开机、安全组 22/业务端口；恢复后从失败步骤续跑，不必总是从头 tar。
- 本机 `docker build` 拉 `auth.docker.io` 超时 → 改 ECS 远程 build，或配置镜像加速；**不要**在 ECS 上跑 npm 多阶段构建代替。

---

## 能力四：Nginx 反向代理

Read `references/nginx-proxy.md` when configuring Nginx reverse proxy URL paths, SPA subpath (VITE_BASE), ecs-manage 代理目录, or upstream 端口冲突排查。

## 能力三：推送到 GitHub

以**当前仓库**为准，不假设 org/repo 名称：

```bash
git remote get-url origin
git branch --show-current
git status
git diff
git log -3 --oneline
```

**仅用户要求时** `git add` → `git commit`（遵守 `.gitignore`，不提交密钥与构建垃圾）→：

```bash
git push origin HEAD
```

已配置上游时可用 `git push`。

**合并前检查**：读取 `.github/workflows/*`，在本地跑与 CI 等价的一条命令（如 `npm test`、`pytest`、`go test` 等）；无 CI 则按用户验收要求执行。

**Pull Request**：用户要求时用 `gh pr create`，先 `git push -u origin HEAD`。

---

## 任务结束回报

```markdown
## 仓库
- origin: <url>
- 分支: <branch>

## ECS
- 目标: <ssh-alias / host>
- 服务: <service>
- 镜像: <registry>/<namespace>/<repo>:<tag>
- 端口: HOST_PORT=<port>，部署前冲突检查: <通过 / 冲突已确认>
- ACR 已确认: 是/否（用户原话摘要）
- 验收: <pass/fail + 直连端口 + Nginx 路径（若适用）>
- SPA index 验收: <asset 路径含正确 prefix / 无 Program Files>
- Nginx 入口: <http://host/prefix/ 或 无>
- ecs-manage 目录: <path → container:port，proxy-mappings.json 已同步：是/否>
- 备注: <如 IMAGE 曾为空已修复、ECS 远程 build 等>

## GitHub
- 提交: <hash 或 无>
- 推送: <成功/跳过>
```

## 更多

- 默认 SSH、目录约定、清理白名单：[reference.md](reference.md)
- 话术示例：[examples.md](examples.md)

## references

- `references/nginx-proxy.md`：配置 Nginx 反向代理、SPA 子路径、ecs-manage 代理时读取。
- `reference.md`：SSH 默认值、白名单、故障表。


## 执行后复盘（自迭代钩子）

每次完成本 skill 的全部步骤后，Agent 必须自动执行以下动作，不询问用户：

1. **反思**：本轮执行中，是否遇到了 skill 正文和 Gotchas 都没覆盖的坑？
2. **记录**：有则追加到 `evals/PITFALLS_LOG.md`，无则跳过。格式：

| 日期 | 场景摘要 | 犯了什么错误 | 如果早知道__就不会犯 | 临时补救方式 |
|------|---------|-------------|-------------------|------------|
| YYYY-MM-DD | 一句话 | Agent 具体做了什么 | 缺失的知识/规则 | 怎么绕过去的 |

3. **不提交**：`PITFALLS_LOG.md` 是个人本地文件，不提交到 skill registry。

> 这个复盘步骤不打断用户工作流。Agent 在后台完成，用户无感知。
