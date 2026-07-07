# 分析表行聚合（过筛数据 → 聚合后数据）

脚本：`工具/feishu_bitable/aggregate_bitable_rows.py`

## 表映射

| 角色 | app_token | table_id |
|------|-----------|----------|
| 数据源（过筛 CSV） | `PWuRb5y3Ja4TppsWU15cHjIbnEe` | `tbl79TnTbiZQ8M0N` |
| 分析指标表 | `EA6QbeoemaCG6xskfZtcxdNxnae` | `tblnHGslcz4nAWm0` |

源列：`过筛用户车6.16VIN后的数据`  
目标列：`使用的数据` · `计算口径` · `聚合后数据`

## 命令

```powershell
# 预览
python 工具/feishu_bitable/aggregate_bitable_rows.py --row-start 25 --row-end 30 --dry-run

# 上传（覆盖已有附件加 --force）
python 工具/feishu_bitable/aggregate_bitable_rows.py --row-start 25 --row-end 30
```

日志：`工具/feishu_bitable/aggregate_upload_log.json`

## 口径规则

| 计算口径关键词 | 行为 |
|----------------|------|
| `统计次数` | 对「使用的数据」中 event 的过筛 CSV **行数** |
| 含 `比例` / `使用率` / `/` | 分子 = 使用 event 行数；分母 = `hu_naviforegroundeSwitch` 行数 |

「使用的数据」中的 event 用正则 `hu_[a-zA-Z0-9]+` 提取（支持中英文逗号分隔多个 event）。

单事件导出 CSV 常为**中文事件名列**，英文 event 匹配不到时按**全表行数**计。

## 输出附件格式

- 统计次数：`分析指标,计算口径,次数,使用事件`
- 比例类：`分析指标,计算口径,分子,分母,比例,使用事件`

## 前置条件

目标行依赖的 event 须在源表存在 `过筛用户车6.16VIN后的数据` 附件；缺失时上传 error 说明 CSV 到 `聚合后数据`。
