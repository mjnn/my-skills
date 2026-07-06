# UE 设计 PDF 校验

> Read when: 用户同时提供了 UE 设计 PDF 时（Step 0）

## 0.1 PDF 渲染（PyMuPDF）

UE 设计 PDF 通常从 Axure/Figma 导出，文字可能为矢量曲线（无法文本提取）。使用 **PyMuPDF** 渲染为 PNG 图片：

```python
import fitz
doc = fitz.open("/path/to/ue_design.pdf")
for i in range(len(doc)):
    page = doc[i]
    mat = fitz.Matrix(0.25, 0.25)  # 大画布用 0.25，小画布可 0.5
    pix = page.get_pixmap(matrix=mat)
    pix.save(f"/tmp/ue_pages/ue_p{i+1}.png")
```

**注意事项：**
- Windows 使用 `python -m pip install pymupdf` 后 `python` 运行
- 跳过封面、目录、修订历史等非功能性页面
- 不要用纯文本提取 Axure/Figma 导出 PDF

## 0.2 图片分析

渲染后使用 Read 工具逐页分析 PNG，提取：
- 页面模块名称（左侧导航栏的模块列表）
- 流程图中的节点和判断条件
- UI Mockup 中的按钮文案、弹窗名称、状态说明
- 页面间跳转关系

## 0.3 UE ↔ 埋点对照校验

| 校验维度 | 检查项 |
|---------|--------|
| 覆盖完整性 | UE 中每个可交互元素是否都有对应埋点事件 |
| 事件准确性 | 事件触发场景是否与 UE 流程图一致 |
| 参数完整性 | UE 中标注的状态码、错误类型是否都已纳入参数 |
| 路径正确性 | 用户路径是否与 UE 流程图的分支逻辑一致 |
| 漏斗对齐 | 漏斗步骤是否匹配 UE 的实际操作步骤 |

输出差异报告并据此修正 JSON 数据。

## 0.4 报告双格式交付

Markdown 报告写完后，**必须同步生成 Word 版本**：

```bash
python .cursor/skills/vehicle-tracking-design/scripts/generate_report_docx.py \
  output/{APP}/ue_validation_report.md \
  output/{APP}/ue_validation_report.docx
```

依赖 `python-docx`（`python -m pip install python-docx`）。

| 格式 | 路径 | 用途 |
|------|------|------|
| Markdown | `ue_validation_report.md` | 版本管理、Agent 迭代 |
| Word | `ue_validation_report.docx` | 评审归档、对外交付 |

## 参考产出规模

账号APP UE Design V0.1 + SPEC v0.10 校验版：23 个事件、6 条路径、14 条漏斗步骤、10 条关联，覆盖 UE 全部 10 个功能模块。
