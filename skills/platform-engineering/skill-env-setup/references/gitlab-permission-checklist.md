# GitLab 全权限验证 Checklist

> Read this when: 节点 5「GitLab 连通验证」阶段，配置完成后的门禁

## 完成标准

**全部勾选通过**，才允许进入节点 6（技能清单对比）。任一项失败 → 返回节点 2/4 修复，禁止声称「环境已就绪」。

## Token 权限要求（创建时勾选）

在 GitLab → User Settings → Access Tokens 创建 Personal Access Token，**必须勾选**：

| 权限 scope | 用途 |
|------------|------|
| `api` | 查询 Releases、项目信息 |
| `read_repository` | git fetch / ls-remote / clone |
| `write_repository` | git push / 贡献 skill |

或使用等效**全量权限** Token。

## 验证 Checklist

| # | 检查项 | 验证方式 | 通过条件 |
|---|--------|---------|---------|
| G1 | GITLAB_TOKEN 已配置 | 读用户环境变量 | 非空且已持久化 |
| G2 | GitLab API 可达 | `GET /api/v4/user` + PRIVATE-TOKEN | HTTP 200，返回 username |
| G3 | 项目可读 | `GET /api/v4/projects/ecc-2%2Fqoder-skills` | HTTP 200 |
| G4 | Releases 可读 | `GET /api/v4/projects/ecc-2%2Fqoder-skills/releases` | HTTP 200，返回 releases 列表 |
| G5 | Git 拉取可用 | `git ls-remote` 仓库 HEAD | 成功返回 ref，无认证错误 |
| G6 | Git 推送可用 | 对临时分支 dry-run 或 `git push --dry-run`（可选） | 无 403/401；若无写权限则 fail |
| G7 | SSL 已处理 | 内网 GitLab 克隆/拉取 | 无 certificate 错误（已配置 sslVerify 或信任证书） |
| G8 | Git 身份已配置 | `git config user.name/email` | 均有值 |

## 自动化脚本

```bash
python scripts/check_gitlab_access.py --report-auto
```

- 通过：写入 `~/.qoder-cn/reports/gitlab-access-pass-{timestamp}.md`
- 失败：写入 `~/.qoder-cn/reports/gitlab-access-fail-{timestamp}.md`

## 失败处理

| 失败项 | 修复指引 |
|--------|---------|
| G1 | 节点 2 重新收集 Token，运行 set_gitlab_token 脚本 |
| G2/G3/G4 | 检查 Token 是否含 `api` scope；检查内网连通 |
| G5/G7 | 执行 `git config --global http.sslVerify false`；确认 Token 含 read_repository |
| G6 | Token 需 `write_repository`；联系管理员确认项目权限 |
| G8 | 配置 `git config --global user.name/email` |

## 报告模板（摘要）

```
GitLab 连通验证报告
════════════════════════════════════════
GitLab Hub: https://epfa-gitlab.csvw.com/ecc-2/qoder-skills
用户：      {username}
Token：     已配置（scopes: ...）
════════════════════════════════════════
[G1] GITLAB_TOKEN     OK
[G2] API /user        OK
[G3] 项目可读         OK
[G4] Releases 可读    OK
[G5] git ls-remote    OK
[G6] git push 权限    OK
[G7] SSL              OK
[G8] Git 身份         OK
════════════════════════════════════════
门禁：通过 — 可进入技能清单对比
```
