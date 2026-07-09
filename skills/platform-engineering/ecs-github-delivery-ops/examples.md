# 调用示例（通用）

## 连接 ECS

```text
@ecs-github-delivery-ops 连 ECS，看 docker 和 /srv/apps 里有什么
```

## 部署当前仓库（含 ACR 确认）

```text
@ecs-github-delivery-ops 构建镜像 crpi-xxx.cn-shanghai.personal.cr.aliyuncs.com/my_ns/myapp:2.1.0 部署到 ECS
```

Agent 应先列出 Registry / 命名空间 / 仓库名 / Tag，**SSH 检查 HOST_PORT 无冲突**，**等待用户回复「已创建，可继续」** 后再 `docker push` 与 ECS 部署。

```text
用户：尚未创建
Agent：暂停 push/部署，说明需在 ACR 控制台创建命名空间与仓库，创建完成后告知再继续。
```

## 部署当前仓库（路径已确认）

```text
@ecs-github-delivery-ops 镜像 myregistry/myapp:2.1.0 部署到 ECS，ACR 仓库已建好，服务名 myapp
```

## 按仓库脚本部署

```text
@ecs-github-delivery-ops 按本仓库的 deploy 脚本发布 tag 2.1.0
```

Agent 应先查找 `scripts/*deploy*`、`deploy/**`、README，再执行，不编造命令。

## 推送 GitHub

```text
@ecs-github-delivery-ops 检查 git 状态，我确认后提交并 push
```

## 配置 Nginx 反向代理

```text
@ecs-github-delivery-ops 给 ECS 上 myapp 配 Nginx，路径 /tools/myapp/，后端端口 8010
```

Agent 应：读仓库 `deploy/nginx-*.conf` → 安装片段 → **同步** `/opt/ecs_service_management/proxy-mappings.json`（ecs-manage 反向代理页）→ reload → curl 公网路径验收；在 `/ops/ecs-manage/` 确认列表已更新。

## 本机 Docker 不可用、改 ECS 构建

```text
@ecs-github-delivery-ops 我本机 docker build 拉不到 docker.io，按仓库脚本在 ECS 上 build 并部署
```

Agent 应：本机构前端（若有）→ tar 上传 → ECS `docker build/push` → 确认 `IMAGE=` → `docker-compose up -d` → 双 URL 验收。

## 部署失败后续跑（镜像已在 ACR）

```text
@ecs-github-delivery-ops 镜像已经 push 了，但 ECS 服务没起来，帮我只做 compose 和 nginx
```

Agent 应：SSH 检查 `.env.runtime` 的 `IMAGE` → 补写 → `docker-compose up -d` → `curl` 直连端口与 Nginx 路径；**不要**重复全量 build。

## SSH 超时后续传

```text
@ecs-github-delivery-ops scp 超时了，看看 ECS 上 build 有没有跑完
```

Agent 应：`ssh -o ConnectTimeout=15` 探测 → 查 `/tmp/*-build`、`docker images`、容器状态 → 从断点继续。

## SPA 白屏（Git Bash 路径转换）

```text
@ecs-github-delivery-ops Nginx 首页 200 但白屏，index 里 asset 是 /Program Files/Git/...
```

Agent 应：

1. `curl` 公网 `index.html`，确认 `src=` 是否被 MSYS 污染
2. 在仓库加/改 `frontend/.env.production`（`VITE_BASE=/tools/myapp/`）
3. deploy 脚本 build 段加 `MSYS_NO_PATHCONV=1`
4. 重构建 → `grep dist/index.html` → 重部署 → 验 JS URL 200

## 端口冲突（部署前）

```text
@ecs-github-delivery-ops 部署 myapp 到 ECS，HOST_PORT 8011
```

Agent 应：

1. `docker ps` + `ss -tlnp | grep 8011` 查占用
2. 若被其他容器占用 → 报告占用者，**不** `compose up`，等用户换端口或确认下线
3. 若仅本服务容器占用 → 继续原地更新
4. 改端口时同步 Nginx 片段与 `.env.runtime`

## 组合

```text
@ecs-github-delivery-ops 先 push 当前分支，再 SSH 更新 ECS 上 myapp 服务为 tag 2.1.0
```
