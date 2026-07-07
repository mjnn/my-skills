# 创建多维表格后授权（必做）

## 背景

使用 `tenant_access_token`（应用身份）调用 `POST /bitable/v1/apps` 创建的多维表格，**默认只有应用自己是所有者**，用户打开链接通常只有只读或无法编辑。

因此：**任何「新建多维表格」任务在返回 URL 给用户之前，必须完成用户全量授权。**

## 目标权限

| 项 | 值 |
|---|---|
| 协作者权限 | `full_access`（可管理） |
| 所有权 | 转移给用户本人 |
| 应用保留 | `remove_old_owner=false`，`old_owner_perm=edit`（脚本后续可继续写入） |

## 配置（`.env`）

至少配置应用凭证；所有者建议显式配置（通讯录仅 1 人时可自动推断）：

```env
FEISHU_APP_ID=cli_xxx
FEISHU_APP_SECRET=xxx

# 推荐：明确指定获得全量权限的用户（二选一）
FEISHU_OWNER_OPEN_ID=ou_xxxxxxxx
# FEISHU_OWNER_EMAIL=you@company.com
```

解析优先级：`FEISHU_OWNER_OPEN_ID` → `FEISHU_OWNER_EMAIL` → 通讯录仅 1 人。

## 标准调用

### CLI

```powershell
$env:NO_PROXY='*'
$env:PYTHONIOENCODING='utf-8'

# 新建（内置授权）
python 工具/feishu_bitable/feishu_bitable.py create-app --name "我的多维表格"

# 对已有 Base 补授权
python 工具/feishu_bitable/feishu_bitable.py grant-access --app-token APP_TOKEN

# 校验协作者列表
python 工具/feishu_bitable/feishu_bitable.py list-permissions --app-token APP_TOKEN
```

### Python

```python
from feishu_bitable import build_client, ensure_user_full_access

client = build_client()
app = client.create_app("我的多维表格")
ensure_user_full_access(client, app["app_token"])  # 失败则抛错，不得跳过
```

## 完成标准（门禁）

向用户交付前必须全部满足：

1. `ensure_user_full_access` 返回 `verified: true`
2. `list-permissions` 中目标用户 `perm` 为 `full_access`
3. 日志/JSON 输出中包含 `permission` 字段
4. **禁止**使用 `--skip-grant`（除非用户明确要求且知情）

## 开放平台权限

应用需开通（满足其一即可）：

- `bitable:app`
- `docs:permission.member:create`
- `docs:permission.member:transfer`

## 故障排查

| 现象 | 处理 |
|------|------|
| 1063002 Permission denied | 开放平台补权限并发布安装 |
| 无法解析 open_id | 设置 `FEISHU_OWNER_OPEN_ID` 或 `FEISHU_OWNER_EMAIL` |
| 通讯录有多人 | 必须显式配置 `FEISHU_OWNER_*`，禁止猜测 |
| 用户仍无法编辑 | 执行 `grant-access`；让用户刷新页面 |
| Python 连不上飞书 | 设置 `$env:NO_PROXY='*'` |
