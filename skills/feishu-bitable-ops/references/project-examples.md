# BI_Dashboard 项目已知多维表格（示例）

> 非密钥；`app_token` 出现在浏览器 URL 中。无 BI_Dashboard 工作区时可忽略本节。

## 埋点导出需求收集

| 项 | 值 |
|---|---|
| 名称 | 埋点导出需求收集 |
| app_token | `PWuRb5y3Ja4TppsWU15cHjIbnEe` |
| table_id | `tbl79TnTbiZQ8M0N` |
| view_id | `vewt8y9oRL` |

关键列：`所属功能模块` · `目标事件eventname` · `需要导出的属性字段` · `状态` · `导出的数据` · `过筛用户车6.16VIN后的数据` · `备注`

## 座舱数据分析指标体系（多表）

Base：`PWuRb5y3Ja4TppsWU15cHjIbnEe`（同 app，多 data table）

详见 BI_Dashboard 项目内 `setup_indicator_schema.py` 的 `TABLES` 字典。

## 关联脚本（工作区内）

| 脚本 | 用途 |
|------|------|
| `filter_vin_upload.py` | VIN 过筛上传 |
| `import_event_sql_xlsx.py` | Excel → Bitable |
| `import_tracking_to_feishu.py` | 埋点需求表 V0.0.1 导入（tracking_point_requirement_merge） |
