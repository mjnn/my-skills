---
name: feishu-bitable-ops
description: >-
  飞书开放平台多维表格 (Bitable) API 操作：首次初始化引导配置开放平台 App ID/Secret、
  新建 Base 后自动授予用户可管理权限、操作他人表格的协作者配置、用户车 VIN 过筛。
  Use when the user mentions 飞书、Feishu、Lark、多维表格、Bitable、base URL、添加文档应用、
  grant-access、VIN 过筛、埋点导出需求收集表、配置飞书应用、App ID。
  不适用于：飞书即时消息/日历/审批、仅浏览器手工填表（无 API）、Lark 国际版未配置开放平台、
  纯 Excel 本地处理不碰飞书、飞书文档 Docx 正文编辑（非 Bitable）。
---

# 飞书多维表格操作

通过开放平台 API（`tenant_access_token` + 自建应用）读写飞书多维表格；**不是**用浏览器打开分享链接。

<HARD-GATE>
1. 写操作（建表、改记录、上传附件、授权）前必须 `EnterSpecMode` 输出计划，用户 `ExitSpecMode` 确认后再执行。
2. 应用身份 **新建** 多维表格后，交付 URL 前必须 `ensure_user_full_access` 且 `permission.verified=true`。
3. 操作 **他人创建** 的表：仅给链接不够，必须确认应用已加为「文档应用」协作者（见 references/access-others-tables.md）。
4. Secret 只放 `.env`，禁止提交、禁止在对话粘贴完整 token。
5. 向用户收集任务类型、凭证状态或权限不明时，必须用 AskUserQuestion，禁止纯文本罗列选项。
6. **首次使用 / `auth` 失败 / 无 `.env`**：必须先完成阶段 0 初始化（引导创建开放平台应用并配置 App ID、Secret），验证 `auth` 通过后才能执行业务 API。
</HARD-GATE>

## Gotchas

1. **链接分享 ≠ API 权限** — 设「互联网获得链接可编辑」只对人打开网页有效，应用调 API 仍报 `1063002`。**纠正：必须「添加文档应用」为协作者，见 access-others-tables.md。**

2. **新建表不给用户授权** — `create-app` 后默认只有应用是所有者，用户只能只读。**纠正：必调 `ensure_user_full_access`；`.env` 配 `FEISHU_OWNER_OPEN_ID` 或 `FEISHU_OWNER_EMAIL`。**

3. **Python 连不上飞书** — Windows 下 `urllib` 走失效代理，`ConnectionRefusedError`。**纠正：执行前 `$env:NO_PROXY='*'`。**

4. **list 接口死循环** — 用 `page_token` 为空当终止条件，飞书在最后一页仍可能返回 token。**纠正：以 `has_more=false` 终止，见 api-pitfalls.md。**

5. **过筛 0 行** — 埋点导出附件是 Tab 分隔，按逗号读全空。**纠正：用 `filter_vin_upload.py` 的 Sniffer，禁止假定 CSV。**

6. **操作他人表只给 URL** — 应用不在协作者列表，读写全失败。**纠正：请表管理员在「…→添加文档应用」加入本应用；按任务给 可阅读/可编辑/可管理。**

7. **高级权限未给应用** — 云文档协作者已加，但表开了高级权限仍 403。**纠正：在高级权限设置里给应用或含应用的群组「可管理」。**

8. **控制台中文乱码** — PowerShell 直接 print 中文记录。**纠正：`PYTHONIOENCODING=utf-8` 或写入 UTF-8 JSON 再 Read。**

9. **跳过开放平台初始化** — 用户未建应用、未给 App ID/Secret 就直接 `list-records`。**纠正：先走阶段 0 引导建应用、写 `.env`、`auth` 通过后再继续。**

## 流程

### 阶段 0：初始化（首次使用必做）

<HARD-GATE>
在 `scripts/.env`（或工作区 `工具/feishu_bitable/.env`）配置完成且 `feishu_bitable.py auth` 返回 `ok: true` 之前，**禁止**调用任何 Bitable 业务 API。
</HARD-GATE>

**0.1 定位脚本**

1. 工作区 `工具/feishu_bitable/feishu_bitable.py`（BI_Dashboard 等）
2. 本 skill `scripts/feishu_bitable.py`

**0.2 检查是否已有凭证**

检查同目录是否存在 `.env` 且含非空的 `FEISHU_APP_ID`、`FEISHU_APP_SECRET`。若无或 `auth` 失败 → 进入 **0.3**。

**0.3 引导用户配置飞书开放平台应用**

必读 [references/app-setup.md](references/app-setup.md)，并用自然语言带用户完成：

1. 打开 https://open.feishu.cn/app → **创建企业自建应用**
2. **权限管理** 开通 `bitable:app`；若需新建表授权则再加 `docs:permission.member:create`、`docs:permission.member:transfer`
3. **发布版本并安装到企业**
4. 在 **凭证与基础信息** 复制 **App ID**、**App Secret**

调用 AskUserQuestion（2 个问题）：

| 问题 | header | 选项 |
|------|--------|------|
| 飞书开放平台应用是否已创建并安装到企业？ | 应用状态 | 已完成（推荐）/ 还没有，需要引导创建 / 已创建但未安装 |
| 你希望如何提供凭证？ | 凭证方式 | 我稍后自行写入 .env（推荐）/ 现在提供 App ID（对话中可提供）/ 不确定 App ID 在哪 |

**收集规则：**

- **App ID**（`cli_` 开头）：用户可在对话中提供
- **App Secret**：**禁止在对话中粘贴**；指示用户自行写入 `.env`，或 Agent 在用户确认路径后**仅写入文件、不在回复中回显**
- **飞书邮箱**（推荐）：写入 `FEISHU_OWNER_EMAIL`，用于新建表后自动授权

**0.4 写入 `.env`**

```env
FEISHU_APP_ID=cli_xxxxxxxx
FEISHU_APP_SECRET=xxxxxxxx
FEISHU_OWNER_EMAIL=you@company.com
```

从 `scripts/.env.example` 复制生成；`.env` 已 gitignore，勿提交。

**0.5 验证**

```powershell
$env:NO_PROXY='*'
$env:PYTHONIOENCODING='utf-8'
python <path>/feishu_bitable.py auth
```

- 成功 → 进入阶段 1
- 失败 → 对照 app-setup.md 排查（权限未发布、Secret 错误、NO_PROXY）

### 阶段 1：确认任务类型

调用 AskUserQuestion（1 个问题）：

| 问题 | header | 选项 |
|------|--------|------|
| 本次飞书多维表格任务？ | 任务类型 | 只读导出/分析（推荐先选）/ 增删改记录 / 新建 Base 并导入 / 操作他人已有表 / VIN 过筛上传 |

- **操作他人已有表** → 必读 [references/access-others-tables.md](references/access-others-tables.md)，确认应用已是协作者再继续。
- **VIN 过筛** → 跳阶段 6。

### 阶段 2：Spec 模式计划审核

写操作前 **EnterSpecMode**。Spec 须含：

1. `app_token` / `table_id`（来自 URL `parse-url`）
2. 操作类型（读/写/建表/导入行数）
3. 他人表格时：协作者是否已添加、所需权限级别
4. 新建表时：表名、字段 schema、是否 `ensure_user_full_access`
5. 预期输出（JSON 摘要、URL、权限校验结果）

用户 **ExitSpecMode** 后再执行。

### 阶段 3：读表（用户给 URL）

```
parse-url → list-fields → list-records →（按需）get-record
```

```powershell
python feishu_bitable.py parse-url "https://my.feishu.cn/base/APP?table=TBL&view=VIEW"
python feishu_bitable.py list-fields --app-token APP --table-id TBL
python feishu_bitable.py list-records --app-token APP --table-id TBL
```

写 CRUD 前必须 `list-fields` 对齐真实中文列名。CLI 全集 → [references/cli-commands.md](references/cli-commands.md)。

### 阶段 4：新建 Base + 授权

```powershell
python feishu_bitable.py create-app --name "表名"
```

或 Python：

```python
from feishu_bitable import build_client, ensure_user_full_access
client = build_client()
app = client.create_app("表名")
ensure_user_full_access(client, app["app_token"])
```

授权细则 → [references/post-create-permissions.md](references/post-create-permissions.md)。

补授权：`python feishu_bitable.py grant-access --app-token APP`

### 阶段 5：批量写入

- 批量记录：`batch-create` / `batch-update`（每批 ≤500）
- 附件：`upload_bitable_file` + 字段值 `[{"file_token":"..."}]`
- 大表导入：脚本参考 BI_Dashboard `import_event_sql_xlsx.py` 模式（建表带字段 → 分批 `batch_create_records`）

### 阶段 6：VIN 过筛（BI_Dashboard 专用）

完整说明 → [references/vin-filter-upload.md](references/vin-filter-upload.md)

<HARD-GATE>
1. `feishu_bitable.py auth`
2. `filter_vin_upload.py --check`
3. `missing_dst_count > 0` → `filter_vin_upload.py`（`--force` 覆盖）
4. 再 `--check` 至 `missing_dst_count: 0`
</HARD-GATE>

### 阶段 7：交付

输出须含：

- 多维表格 URL
- 行数 / 表 ID
- **新建表**：`permission.verified=true` 或 `list-permissions` 截图级摘要
- **他人表**：提醒若失败需加「文档应用」

## 代码内调用

```python
import sys
from pathlib import Path

# 优先工作区工具，否则 skill scripts
for p in [Path("工具/feishu_bitable"), Path(__file__).resolve().parent / "scripts"]:
    if (p / "feishu_bitable.py").is_file():
        sys.path.insert(0, str(p))
        break

from feishu_bitable import build_client, parse_bitable_url, ensure_user_full_access

client = build_client()
ids = parse_bitable_url(url)
records = client.list_records(ids["app_token"], ids["table_id"])
```

扩展 API：改 `FeishuBitableClient`，再补 CLI 子命令。

## references

- `references/app-setup.md`：飞书开放平台建应用、开权限、配置 App ID/Secret（**阶段 0 必读**）
- `references/cli-commands.md`：CLI 子命令与字段 type 码（阶段 3、5 读取）
- `references/post-create-permissions.md`：新建表后 `ensure_user_full_access`（阶段 4 必读）
- `references/access-others-tables.md`：他人表格 / 链接分享 vs API 协作者（阶段 1、2 读取）
- `references/api-pitfalls.md`：分页、权限错误码、附件、NO_PROXY（遇错时读取）
- `references/vin-filter-upload.md`：VIN 过筛全流程（阶段 6 读取）
- `references/aggregate-rows.md`：过筛后行聚合（按需）
- `references/project-examples.md`：BI_Dashboard 已知表 token 示例（按需）

## 执行后复盘（自迭代钩子）

每次完成飞书 Bitable 任务后自动执行：

1. **反思**：是否遇到正文与 Gotchas 未覆盖的问题（如新错误码、新权限模型）？
2. **记录**：有则追加 `evals/PITFALLS_LOG.md`（格式：日期 | 场景 | 错误 | 可避免条件 | 补救）
3. **不提交**：`PITFALLS_LOG.md` 仅本地，不上传 registry
