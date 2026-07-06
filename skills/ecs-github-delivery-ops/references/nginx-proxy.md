# Nginx 反向代理

> Read references/nginx-proxy.md when configuring Nginx reverse proxy, SPA subpath, or ecs-manage proxy.

将 ECS 上 Docker 服务暴露为 **80/443 下的路径前缀**（如 `http://<host>/tools/<service>/`），避免用户记端口。

### 执行前收集

| 参数 | 说明 | 来源 |
|------|------|------|
| `<location_prefix>` | 公网路径，如 `/tools/myapp` | 用户指定 → 仓库 `deploy/nginx-*.conf` |
| `<host_port>` | compose `HOST_PORT`，反代到 `127.0.0.1:<host_port>` | `.env.runtime` / compose |
| `<health_path>` | 经 Nginx 可 curl 的健康检查，如 `/tools/myapp/api/health` | 仓库文档 |
| `<snippet_name>` | ECS 片段文件名，如 `myapp-locations.conf` | 仓库 `deploy/` |
| 前端 subpath | `VITE_BASE=<prefix>/`；`VITE_API_BASE=<prefix>`（若 API 路径已含 `/api/`） | SPA 经 Nginx 前缀访问时**必须** |

### 标准片段模板（仓库内 `deploy/nginx-<service>-locations.conf`）

```nginx
# 无尾斜杠 → 带尾斜杠
location = <location_prefix> {
    return 301 <location_prefix>/;
}

# 健康检查（可选，便于监控）
location = <location_prefix>/api/health {
    proxy_pass http://127.0.0.1:<host_port>/api/health;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}

# 静态 + API（前缀剥离后转发）
location <location_prefix>/ {
    client_max_body_size 50m;
    proxy_pass http://127.0.0.1:<host_port>/;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Prefix <location_prefix>;
    proxy_connect_timeout 10s;
    proxy_send_timeout 120s;
    proxy_read_timeout 120s;
}
```

### ECS 安装步骤

1. 将仓库片段复制到 ECS：

```bash
scp deploy/nginx-<service>-locations.conf <ssh-alias>:/tmp/<service>-locations.conf
```

2. 安装片段、写入 `sites-enabled/default`、重载（**幂等**）：

```bash
ssh <ssh-alias> bash -s <<'REMOTE'
set -euo pipefail
SNIPPET="/etc/nginx/snippets/<service>-locations.conf"
DEFAULT="/etc/nginx/sites-enabled/default"
MARKER="<service>-locations.conf"
install -m 644 /tmp/<service>-locations.conf "${SNIPPET}"
if ! grep -q "${MARKER}" "${DEFAULT}"; then
  sed -i '/ecs-service-manage-generated-locations.conf/i\    include /etc/nginx/snippets/<service>-locations.conf;' "${DEFAULT}"
fi
nginx -t
systemctl reload nginx
REMOTE
```

3. **验收**（必须两条都过）：

```bash
ssh <ssh-alias> "curl -fsS http://127.0.0.1:<host_port><app-health-path>"
ssh <ssh-alias> "curl -fsS http://127.0.0.1<location_prefix>/api/health"
curl -fsS "http://<public-host><location_prefix>/api/health"
```

4. SPA 还需验证首页：`curl -fsS -o /dev/null -w '%{http_code}' http://<public-host><location_prefix>/` 为 `200`。
5. SPA **必须**验证 `index.html` 内 asset 路径（防 Git Bash 白屏）：

```bash
curl -s "http://<public-host><location_prefix>/" | grep -E 'src=|href='
# 期望：/tools/myapp/assets/...  禁止：Program Files 或 /Git/
curl -fsS -o /dev/null -w '%{http_code}\n' "http://<public-host><location_prefix>/assets/<从index取出的js文件名>"
```

### 与部署脚本集成

仓库若有 `scripts/install-nginx-*.sh` 或 `deploy-to-ecs.*` 已含 Nginx 步骤，**优先执行仓库脚本**，顺序为：

1. `compose up -d`（容器监听 `HOST_PORT`）
2. 安装 / 更新 Nginx 片段
3. `nginx -t && systemctl reload nginx`
4. curl 直连端口 + curl Nginx 公网路径

前端构建在 **Nginx subpath 模式** 下：

**首选**在仓库 `frontend/.env.production` 固定：

```dotenv
VITE_BASE=/tools/myapp/
VITE_API_BASE=/tools/myapp
```

若 deploy 脚本内 `export`，**必须先**：

```bash
export MSYS_NO_PATHCONV=1
export MSYS2_ARG_CONV_EXCL='*'
export VITE_BASE="<location_prefix>/"
export VITE_API_BASE="<location_prefix>"
npm run build   # 或仓库等价命令
```

构建后 **必须** `grep` 验 `frontend/dist/index.html` 中 asset 路径（见「SPA subpath 构建 · 构建后强制门禁」）。

React Router 等需配置 `basename`（去掉尾斜杠），与 `VITE_BASE` 一致。

### 常见问题

- Nginx 200 但页面白屏 → **先** `curl` 看 `index.html` 里 `src=`/`href=`：若含 `Program Files` 或 `/Git/`，是 Git Bash 路径转换；改 `.env.production` + `MSYS_NO_PATHCONV=1` 后重构建（见「SPA subpath 构建」）。若 asset 无前缀 → 前端未用 subpath 构建。
- `404` 经 Nginx、直连端口正常 → 片段未 include 或未 reload；或 `proxy_pass` 末尾缺 `/` 导致路径未剥离。
- `conflicting server name` 警告 → 现网已知，不影响 `nginx -t`；勿重复添加相同 `server_name` 块。

### ecs-manage：反向代理目录（与 Nginx 配置同步，强制）

用户 ECS 上 **ecs-service-manage**（面板入口 `http://<public-host>/ops/ecs-manage/`）维护「反向代理」列表。  
**每次**为服务新增/修改/删除 Nginx 公网路径时，除安装 `deploy/nginx-*.conf` 片段外，**必须同步更新**该目录，否则面板与真实路由不一致。

| 项 | 路径 / 说明 |
|----|-------------|
| 面板 URL | `http://<public-host>/ops/ecs-manage/` |
| 容器名 | `ecs-service-manage`（宿主机端口 **3100** → 容器 3000） |
| 映射数据文件（宿主机） | `/opt/ecs_service_management/proxy-mappings.json` |
| 由面板「应用」生成的 Nginx | `/etc/nginx/snippets/ecs-service-manage-generated-locations.conf` |
| API（需 Basic 认证，`PANEL_USERNAME` / `PANEL_PASSWORD`） | `GET/PUT http://127.0.0.1:3100/api/proxy/mappings`、`POST .../api/proxy/apply` |

#### 映射字段（与面板表单一致）

```json
{
  "containerName": "<compose container_name，如 fund_chart>",
  "host": "47.116.180.173",
  "path": "/finance/fund-chart/",
  "targetPort": 8088,
  "listenPort": 80,
  "upstreamPath": "/"
}
```

- `path`：**必须**以 `/` 结尾（如 `/finance/fund-chart/`）。
- `targetPort`：容器**内部**监听端口（compose 的 `CONTAINER_PORT`），不是随意写的宿主机映射；`apply` 时会 `docker port <container> <targetPort>/tcp` 解析到 `127.0.0.1:<published>`。
- `upstreamPath`：反代到上游的路径后缀（多数为 `/`；若上游只在 `/docs` 则填 `/docs`，参考现网 `fund_value_em`）。

#### 标准流程（配置 Nginx 时一并执行）

1. **安装/更新**仓库内 `deploy/nginx-<service>-snippet.conf` → `/etc/nginx/snippets/...`，在 `sites-enabled/default` 中 `include`（仍在 `ecs-service-manage-generated-locations.conf` **之前**）。
2. **写入代理目录**（二选一，推荐 A）：
   - **A. 直接改 JSON（无需面板密码，适合 Agent）**：SSH 到 ECS，合并进 `proxy-mappings.json`（按 `path` 或 `containerName` 去重更新）。
   - **B. 经 API**：`PUT /api/proxy/mappings` 传完整 `mappings` 数组（需 Basic 认证，凭证在容器 env `PANEL_USERNAME` / `PANEL_PASSWORD`，勿在对话中回显）。
3. **是否 `POST /api/proxy/apply`**（见下「两种 Nginx 策略」）。
4. `nginx -t && systemctl reload nginx`（若仅改了 JSON、未改 snippet，可跳过 reload）。
5. **验收**：`curl` 公网路径 + 打开 `/ops/ecs-manage/` 确认列表中出现该 `path` 与 `containerName`。

**合并写入示例（在 ECS 上执行）**：

```bash
ssh <ssh-alias> 'python3 - <<'"'"'PY'"'"'
import json
path = "/opt/ecs_service_management/proxy-mappings.json"
entry = {
    "containerName": "<container>",
    "host": "<public-host>",
    "path": "<location_prefix>/",
    "targetPort": <container_port>,
    "listenPort": 80,
    "upstreamPath": "/",
}
with open(path, encoding="utf-8") as f:
    mappings = json.load(f)
idx = next((i for i, m in enumerate(mappings)
            if m.get("path") == entry["path"] or m.get("containerName") == entry["containerName"]), None)
(mappings.append(entry) if idx is None else mappings.__setitem__(idx, entry))
with open(path, "w", encoding="utf-8") as f:
    json.dump(mappings, f, indent=2)
    f.write("\n")
print("proxy-mappings updated:", entry["path"])
PY'
```

#### 两种 Nginx 策略（与 ecs-manage 的关系）

| 策略 | 何时用 | ecs-manage `apply` | 说明 |
|------|--------|-------------------|------|
| **仅 generated** | 简单反代、无特殊 header/重定向 | **要** `POST /api/proxy/apply` | 只维护 `proxy-mappings.json`，由面板生成 `ecs-service-manage-generated-locations.conf` |
| **专用 snippet + 目录登记** | 需 `X-Forwarded-Prefix`、大 body、旧路径 301 等（如 `fund-chart-proxy.conf`、`dsms-locations.conf`） | **通常不 apply** | 流量走专用 snippet（须在 generated **之前** `include`）；**仍要**更新 `proxy-mappings.json` 以便面板展示与文档一致 |

现网示例：`fund_chart` 使用 `fund-chart-proxy.conf` 承接流量，同时在 `proxy-mappings.json` 登记 `/finance/fund-chart/` → `fund_chart:8088`，**不**对 fund_chart 再 `apply`（避免 generated 与 snippet 重复 `location`）。

#### 删除 / 变更路径

1. 从 `proxy-mappings.json` 移除或改条目（API PUT 或 Python 合并的逆操作）。
2. 删除或更新对应 `/etc/nginx/snippets/<service>-*.conf` 与 `default` 中的 `include`。
3. 若该服务曾仅靠 generated：再 `POST /api/proxy/apply` 重写 generated 文件。
4. `nginx -t && systemctl reload nginx`。

#### 任务结束必报（有 Nginx 时）

在回报中增加一行：**ecs-manage 代理目录**：`<path>` → `<containerName>:<targetPort>`（已写入 `proxy-mappings.json`：是/否）。

---