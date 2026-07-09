# 飞书 Bitable CLI 完整参考

入口：`python 工具/feishu_bitable/feishu_bitable.py <command> [options]`

全局选项（多数命令）：
- `--app-token`：多维表格 token（URL `/base/` 后）；或 env `FEISHU_BITABLE_APP_TOKEN`
- `--table-id`：数据表 ID（URL 参数 `table=`）

## 鉴权与解析

```powershell
$env:NO_PROXY='*'
python 工具/feishu_bitable/feishu_bitable.py auth
python 工具/feishu_bitable/feishu_bitable.py parse-url "https://my.feishu.cn/base/APP?table=TBL&view=VIEW"
```

## 新建 Base 与授权

```powershell
# 新建多维表格（默认自动授予 FEISHU_OWNER_* 用户 full_access + 转移所有权）
python 工具/feishu_bitable/feishu_bitable.py create-app --name "埋点事件清单需求表 V0.0.1"

# 对已有 Base 补授权
python 工具/feishu_bitable/feishu_bitable.py grant-access --app-token APP
python 工具/feishu_bitable/feishu_bitable.py grant-access --app-token APP --email you@company.com

# 查看协作者
python 工具/feishu_bitable/feishu_bitable.py list-permissions --app-token APP
```

详见 [post-create-permissions.md](post-create-permissions.md)。

## 元数据

```powershell
python 工具/feishu_bitable/feishu_bitable.py app-info --app-token APP
python 工具/feishu_bitable/feishu_bitable.py list-tables --app-token APP
python 工具/feishu_bitable/feishu_bitable.py list-fields --app-token APP --table-id TBL
```

## 记录 CRUD

```powershell
# Read
python 工具/feishu_bitable/feishu_bitable.py list-records --app-token APP --table-id TBL --view-id VIEW
python 工具/feishu_bitable/feishu_bitable.py list-records --app-token APP --table-id TBL --filter 'CurrentValue.[状态]="待处理"'
python 工具/feishu_bitable/feishu_bitable.py get-record --app-token APP --table-id TBL --record-id recXXX

# Create
python 工具/feishu_bitable/feishu_bitable.py create-record --app-token APP --table-id TBL --fields "{\"目标事件eventname\":\"Hu_Test\"}"

# Update
python 工具/feishu_bitable/feishu_bitable.py update-record --app-token APP --table-id TBL --record-id recXXX --fields "{\"状态\":\"已完成\"}"

# Delete
python 工具/feishu_bitable/feishu_bitable.py delete-record --app-token APP --table-id TBL --record-id recXXX
```

### 批量

`batch-create`：`--file records.json`，内容为 `[{"列A":"v1"}, ...]`（每项为 fields 对象）

`batch-update`：`--file updates.json`，内容为 `[{"record_id":"recXXX","fields":{"列A":"v2"}}, ...]`

`batch-delete`：`--ids '["recA","recB"]'`

## 表 / 字段

```powershell
python 工具/feishu_bitable/feishu_bitable.py create-table --app-token APP --name "新表"
python 工具/feishu_bitable/feishu_bitable.py update-table --app-token APP --table-id TBL --name "重命名"
python 工具/feishu_bitable/feishu_bitable.py delete-table --app-token APP --table-id TBL

python 工具/feishu_bitable/feishu_bitable.py create-field --app-token APP --table-id TBL --name "列名" --type 1
python 工具/feishu_bitable/feishu_bitable.py delete-field --app-token APP --table-id TBL --field-id fldXXX
```

### 常用字段 type

| type | 含义 |
|------|------|
| 1 | 文本 |
| 2 | 数字 |
| 3 | 单选 |
| 5 | 日期 |
| 7 | 复选框 |
| 17 | 附件 |
| 18 | 关联 / 父记录 |

## 用户车 VIN 过筛

```powershell
python 工具/feishu_bitable/filter_vin_upload.py --check
python 工具/feishu_bitable/filter_vin_upload.py
python 工具/feishu_bitable/filter_vin_upload.py --record-id recXXX --force
```

详见 [vin-filter-upload.md](../.cursor/skills/feishu-bitable-ops/references/vin-filter-upload.md)（Skill 内路径：`references/vin-filter-upload.md`）。

## 读表汇总脚本模板

Windows 下汇总中文时，写入 JSON 再 Read：

```python
import json, sys
from pathlib import Path
from collections import Counter
sys.path.insert(0, str(Path("工具/feishu_bitable").resolve()))
from feishu_bitable import build_client, parse_bitable_url

url = "..."  # 用户给的 URL
ids = parse_bitable_url(url)
c = build_client()
fields = c.list_fields(ids["app_token"], ids["table_id"])
records = c.list_records(ids["app_token"], ids["table_id"], view_id=ids.get("view_id"))

summary = {
    "field_names": [f["field_name"] for f in fields],
    "record_count": len(records),
    "status_counts": dict(Counter(r["fields"].get("状态") for r in records)),
}
Path("工具/feishu_bitable/_read_summary.json").write_text(
    json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
)
```
