# xlsx 生成与校验

> Read when: Step 4 生成 Excel，或用户反馈 xlsx 损坏/空白时

## 生成命令

```bash
python .cursor/skills/vehicle-tracking-design/scripts/generate_tracking_xlsx.py <input.json> <output.xlsx>
```

优先使用 **openpyxl** 写入样式（Office/WPS 兼容性最佳）；环境无 openpyxl 时回退纯 OOXML。安装：`python -m pip install openpyxl`

脚本内置 `--validate-only` 可单独校验已有文件；生成后**自动校验**，失败则 exit 1。

## OOXML 写入顺序（关键）

纯 zip+xml 手写 xlsx 时，**必须先构建全部 sheet 再写 sharedStrings.xml**：

```
错误顺序：写 sst(空) → 写 sheet(填充 sst) → Excel 打开损坏/空白
正确顺序：构建全部 sheet XML(填充 sst) → 写 sst → 写 sheet XML
```

单元格使用 `t="s"` 时，`<v>` 是 sharedStrings 的**从 0 开始的索引**。sst 为空或索引越界时，Excel/WPS 报「文件损坏」或显示空白。

## 必需 OOXML 部件

| 部件 | 说明 |
|------|------|
| `[Content_Types].xml` | 声明 workbook / worksheet / styles / sharedStrings |
| `xl/workbook.xml` + `xl/_rels/workbook.xml.rels` | 4 个 sheet + styles + sharedStrings 关系 |
| `xl/styles.xml` | 最小样式表，缺了部分 Excel 版本报错 |
| `xl/sharedStrings.xml` | 所有字符串单元格的值 |
| `xl/worksheets/sheetN.xml` | 含 `<dimension>` + `<sheetData>` |

## 样式规范（脚本自动应用）

| 元素 | 说明 |
|------|------|
| 表头行 | 深蓝底 `#2F5496`、白字加粗、居中、自动换行 |
| 数据行 | 奇偶斑马纹（白 / 浅灰 `#F2F2F2`）、细边框、左对齐换行 |
| 列宽 | 按单元格内容估算（中文约 2.2 字符宽），范围 10–55 |
| 冻结 | 首行冻结，便于滚动浏览 |
| 筛选 | 表头行启用 autoFilter |
| 字体 | 微软雅黑 11pt |

## 生成后自动校验项

脚本 `validate_xlsx()` 检查：

1. zip 内必需部件齐全（含 `styles.xml`）
2. `sharedStrings.xml` 的 `uniqueCount > 0`
3. sheet1 字符串单元格索引 `< uniqueCount`（无越界）
4. sheet1 行数 ≥ 事件数 + 1（表头）
5. 文件大小 > 8KB（空 sst 的旧 bug 产物约 6KB）
6. `styles.xml` 含格式化 cellXfs（count=4）
7. sheet1 含 `<cols>` 列宽定义

## 手动复验（可选）

若环境有 openpyxl：

```bash
python -c "import openpyxl; wb=openpyxl.load_workbook('output/xxx.xlsx'); print(wb.sheetnames, wb.active.max_row)"
```

## 常见问题

| 现象 | 原因 | 处理 |
|------|------|------|
| Excel 提示损坏 | sst 写入顺序错误或缺 styles | 用最新脚本重生成 |
| 打开空白 | sst uniqueCount=0 | 检查 JSON 是否有 events |
| WPS 正常 Excel 异常 | 缺 dimension/styles | 升级脚本到含 styles 版本 |
