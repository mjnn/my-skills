---
name: vehicle-tracking-design
description: 为车端应用生成完整埋点设计方案。基于功能 SPEC（DOCX/PDF/Markdown）和可选 UE 设计 PDF，输出含四大 Sheet 的标准化 Excel（事件、用户路径、转化漏斗、关联埋点）。适用于中控、副驾屏、后排屏、SDS 语音、HUD 等车端场景。当用户提到埋点设计、埋点方案、埋点生成、事件埋点、tracking design、基于 SPEC 设计埋点、埋点 UE 校验时使用。不适用于：已有埋点 Excel 的简单格式转换、非车端 Web/App 通用 analytics、神策/GA 等 SDK 代码接入、纯数据分析报表制作、评估/审计已有 skill 质量。
---

# 车端埋点设计

基于功能 SPEC 和可选 UE 设计 PDF，生成标准化埋点设计 Excel（四大 Sheet：事件、用户路径、转化漏斗、关联埋点）。

<HARD-GATE>
1. 信息收集完成前，禁止读取 SPEC、生成 JSON 或输出 xlsx。
2. 生成/修改文件前，必须调用 EnterSpecMode 输出执行计划，用户审核并调用 ExitSpecMode 确认后才可执行。
3. 向用户提问时必须使用 AskUserQuestion 工具，禁止纯文本罗列问题。
4. 必须使用 `scripts/generate_tracking_xlsx.py` 生成 xlsx（优先 openpyxl 样式引擎，无 openpyxl 时回退纯 OOXML），禁止手工拼 Excel。
5. xlsx 生成后脚本必须自动校验通过（openpyxl 可读、行数达标、zip 结构完整）；校验失败禁止交付，需修复脚本后重生成。
6. UE 校验报告必须同时交付 `.md` 与 `.docx` 两种格式。
</HARD-GATE>

## Gotchas

**1. Axure/Figma 导出 PDF 直接文本提取**
Agent 对 UE PDF 做 pdftotext 或文本提取，得到空内容或乱码后跳过 UE 校验。纠正：用 PyMuPDF 渲染为 PNG，Read 工具逐页分析 UI 元素与流程图。见 `references/ue-validation.md`。

**2. 有 UE PDF 却只做 SPEC 埋点**
用户提供了 UE 设计但 Agent 只基于 SPEC 交付，漏掉 UE 中的按钮、弹窗、分支路径。纠正：Step 0 必须做 UE ↔ 埋点对照校验，输出差异报告并修正 JSON。

**3. 车端多屏漏 screen / trigger_method**
Agent 生成的事件参数不含 `screen`、`trigger_method`，导致多屏/语音/按键场景无法区分。纠正：车端事件默认包含这两项，见 `references/vehicle-specific.md`。

**4. 事件 ID 不按模块分段**
Agent 随意编号如 EVT_1、EVT_2，与团队规范冲突。纠正：按 `[APP前缀]_[模块编号]` 分段，见 `references/event-numbering.md`。

**5. 跳过 JSON 中间层直接写 Excel**
Agent 手工填 Excel 或调用 openpyxl，格式不一致且难迭代。纠正：先产出 JSON → 脚本生成 xlsx。

**6. 漏斗步骤与 UE 实际操作不一致**
Agent 按 SPEC 文字想象步骤，步骤数或顺序与 UE 流程图不符。纠正：有 UE 时必须对照流程图节点逐步对齐。

**7. 隐私参数未标注脱敏**
Agent 在参数中直接上报手机号、VIN 等明文。纠正：个人信息参数在参数说明中标注脱敏要求。

**8. sharedStrings 写入顺序导致 xlsx 损坏**
Agent 用手写 OOXML 生成 xlsx 时，先写空的 `sharedStrings.xml` 再写 sheet，单元格索引指向空表，Excel/WPS 打开报损坏或空白。纠正：必须先构建全部 sheet XML 填充字符串表，再写 sst；必须含 `styles.xml`；生成后运行脚本内置校验。见 `references/xlsx-generation.md`。

**9. UE 校验报告只输出 Markdown**
Agent 只写 `ue_validation_report.md`，团队需要 Word 版本时无法直接使用。纠正：Markdown 报告写完后必须同步调用 `scripts/generate_report_docx.py` 生成同名 `.docx`。

**10. 手写 OOXML 样式导致 Office/WPS 报损坏**
Agent 用手写 zip+xml 做 xlsx/docx 样式（列宽、背景色），XML 结构或属性不符合 Office 规范，Excel/Word 打开报损坏。纠正：xlsx 优先用 **openpyxl** 写样式；docx 必须用 **python-docx**；纯 OOXML 仅作 openpyxl 不可用时的 xlsx 回退。见 `references/xlsx-generation.md`。

## 触发条件

- 为车端应用设计/生成埋点方案
- 基于 SPEC 生成埋点设计
- 创建埋点事件表/埋点文档
- 分析某个 APP 需要哪些埋点事件
- 「帮我设计 XX APP 的埋点」

## 流程

### 阶段 0：信息收集

调用 AskUserQuestion（4 个问题）：

| 问题 | header | 选项 |
|------|--------|------|
| 目标 APP 名称与前缀？ | APP信息 | 账号APP(ACC)（推荐）/ 导航APP(NAV) / 其他（Other 输入） |
| SPEC 文档路径或格式？ | SPEC来源 | 工作区 DOCX（推荐）/ PDF / Markdown / 尚未提供 |
| 是否提供 UE 设计 PDF？ | UE设计 | 有，需校验（推荐）/ 无，仅 SPEC / 稍后补充 |
| 输出路径偏好？ | 输出位置 | output/{APP}/ 目录（推荐）/ 与 SPEC 同目录 / 指定路径（Other） |

若 SPEC 尚未提供，暂停并提示用户上传后再继续。

### 阶段 1：Spec 模式计划审核

信息收集完成后，调用 **EnterSpecMode**，Spec 必须包含：

1. APP 名称、事件 ID 前缀、SPEC/UE 文件路径
2. 是否执行 Step 0 UE 校验
3. 预期事件模块分布（认证/控制/服务等）
4. 输出 JSON 与 xlsx 路径
5. 交付摘要格式（事件数、路径数、漏斗数、关联数）

用户审核后调用 **ExitSpecMode** 确认，再进入执行。

### Step 0：UE 设计 PDF 校验（可选，有 UE 时必做）

Read `references/ue-validation.md`，渲染 PDF → 逐页分析 → UE ↔ 埋点对照校验 → 差异报告。

### Step 1：读取 SPEC 文档

读取用户提供的 SPEC（DOCX/PDF/Markdown），提取：
- 功能模块清单
- 页面层级结构
- 可操作控件/按钮列表
- 业务流程（注册、绑定、登录等）
- 系统交互（语音唤醒、远程触发、跨应用跳转）

DOCX 无 pandas 时可用 zipfile 读 `word/document.xml` 提取文本。

### Step 2：分析 SPEC 并设计四维埋点

Read `references/event-numbering.md` 与 `references/vehicle-specific.md`。

针对 SPEC 每个功能点设计：
- **A. 事件**（页面浏览、操作交互、流程节点、状态变更、异常）
- **B. 用户路径**（首次使用、核心功能、异常恢复、跨模块）
- **C. 转化漏斗**（3-6 步关键流程）
- **D. 关联埋点**（消息→功能、跳转→转化、异常→重试）

### Step 3：构建 JSON

Read `references/json-schema.md`，产出嵌套格式 JSON（推荐），保存到 `output/{APP简称}/` 目录（如 `output/导航/navigation_tracking.json`）。

### Step 4：生成 Excel

Read `references/xlsx-generation.md` 与 `references/excel-schema.md`。

```bash
python .cursor/skills/vehicle-tracking-design/scripts/generate_tracking_xlsx.py output/{APP简称}/{app}_tracking.json output/{APP简称}/{APP名称}_埋点设计.xlsx
```

脚本生成后**自动校验**（sharedStrings 非空、索引不越界、sheet 行数、列宽定义、样式表、文件大小）。exit 0 方可交付。

脚本自动应用样式：**表头深蓝底白字**、**斑马纹数据行**、**自动列宽**（中英文混排估算）、**冻结首行**、**筛选器**、**自动换行**。

用户反馈 xlsx 损坏时，先用 `--validate-only` 诊断：

```bash
python .cursor/skills/vehicle-tracking-design/scripts/generate_tracking_xlsx.py --validate-only <output_xlsx>
```

### Step 4.5：生成 UE 校验报告（Word）

Step 0 产出 `ue_validation_report.md` 后，**必须同步生成 Word 版本**：

```bash
python .cursor/skills/vehicle-tracking-design/scripts/generate_report_docx.py output/{APP简称}/ue_validation_report.md output/{APP简称}/ue_validation_report.docx
```

Word 版含标题层级、表格表头着色、斑马纹行，便于评审归档。

依赖安装（首次使用前）：

```bash
python -m pip install openpyxl python-docx
```

### Step 5：交付汇报

向用户汇报：
- 事件总数及模块分布
- 路径、漏斗、关联数量
- UE 校验差异摘要（如有）
- 输出文件路径

**每个 APP 标准交付物（`output/{APP简称}/`）**：

| 文件 | 说明 |
|------|------|
| `{app}_tracking.json` | 埋点中间层 JSON |
| `build_*_tracking.py` | JSON 构建脚本（可选，便于迭代） |
| `{APP名称}_埋点设计.xlsx` | 四大 Sheet 埋点 Excel（样式化） |
| `ue_validation_report.md` | UE 校验差异报告（Markdown） |
| `ue_validation_report.docx` | UE 校验差异报告（Word） |
| `_prd_extract.txt` / `_ue_extract.txt` | SPEC/UE 文本提取（如有） |

## references

- `references/json-schema.md`：Step 3 构建 JSON 时读取
- `references/excel-schema.md`：Step 4 生成 Excel 或汇报列结构时读取
- `references/xlsx-generation.md`：Step 4 生成/校验 xlsx，或用户反馈文件损坏时读取
- `references/event-numbering.md`：Step 2 设计事件编号与类型时读取
- `references/vehicle-specific.md`：生成车端参数或校验覆盖时读取
- `references/ue-validation.md`：用户提供 UE PDF 时读取
- `references/example_account_app.md`：需要参考完整案例规模时读取

## scripts

| 脚本 | 用途 |
|------|------|
| `scripts/generate_tracking_xlsx.py` | JSON → 样式化 xlsx（openpyxl 优先） |
| `scripts/generate_report_docx.py` | Markdown 报告 → Word docx |

## 执行后复盘（自迭代钩子）

每次完成埋点设计交付后，Agent 自动执行：

1. **反思**：本轮是否遇到正文和 Gotchas 未覆盖的坑（如 SPEC 格式异常、脚本报错）？
2. **记录**：有则追加到 `evals/PITFALLS_LOG.md`（本地文件，不提交）：

| 日期 | 场景摘要 | 犯了什么错误 | 如果早知道__就不会犯 | 临时补救方式 |

3. **无新坑则跳过记录**
