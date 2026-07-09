# 用户车 VIN 过筛上传

将「埋点导出需求收集」表中 **导出的数据** 附件按白名单筛 VIN，写入 **过筛用户车6.16VIN后的数据** 列。

目标列名以 `list-fields` 为准；脚本常量 `DST_FIELD` 在 `filter_vin_upload.py` 顶部，列改名后须同步。

## 脚本

`工具/feishu_bitable/filter_vin_upload.py`

| 参数 | 作用 |
|------|------|
| `--check` | 只审计：有源附件是否都有过筛附件；缺则 exit 1 |
| `--dry-run` | 列出将要处理的 record，不上传 |
| `--force` | 覆盖已有「过筛用户车6.16VIN后的数据」 |
| `--record-id recXXX` | 只处理单条 |

## 标准闭环

```
auth → --check →（若有 missing）执行全量 → --check 确认 0 missing
```

```powershell
python 工具/feishu_bitable/feishu_bitable.py auth
python 工具/feishu_bitable/filter_vin_upload.py --check
python 工具/feishu_bitable/filter_vin_upload.py
python 工具/feishu_bitable/filter_vin_upload.py --check
```

日志：`工具/feishu_bitable/vin_filter_upload_log.json`

## 过筛规则

| 项 | 值 |
|---|---|
| 白名单 | `参考/4.25-6.16用户车VIN清单.csv`（7043 VIN） |
| VIN 列 | 列名含 `vin`（如 `vin`、`vin_code`） |
| 匹配 | `strip().upper()` 后在白名单 set 中 |
| 分隔符 | 自动 sniff：Tab 或逗号（导出多为 TSV） |
| 输出名 | `{原文件名 stem}_用户车.csv` |

## 附件 API（`feishu_bitable.py`）

| 方法 | 说明 |
|------|------|
| `download_file(url)` | Bearer 下载，大文件 300s 超时 + 重试 |
| `upload_bitable_file(app_token, name, bytes)` | ≤20MB `upload_all`；更大走分片 |

分片流程：`upload_prepare` → `upload_part`（4MB）→ `upload_finish` → 得 `file_token` → `update_record` 写入附件字段。

## 已知表

- app_token: `PWuRb5y3Ja4TppsWU15cHjIbnEe`
- table_id: `tbl79TnTbiZQ8M0N`
- 源列 / 目标列：`导出的数据` / `过筛用户车6.16VIN后的数据`

## 常见现象

| 现象 | 原因 |
|------|------|
| 过筛后 0 行 | 源 CSV 被当成逗号分隔，实际为 Tab → 已用 Sniffer 修复 |
| HTTP 400 1061002 上传 | 过筛结果 >20MB → 自动分片 |
| 下载 Errno 10054 | 源文件过大 → `download_file` 重试 |
| `--check` missing | 新上传了「导出的数据」但未跑脚本 → 再执行全量 |
