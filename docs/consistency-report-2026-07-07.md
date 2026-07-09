# Qoder Skills Hub 一致性检查报告

> 检查时间：2026-07-07
> 检查范围：skills/ 目录、README.md、docs/skill-browser.md、CATALOG.md、assets/

---

## 总体结论

**4 个数据源（skills/ 目录、技能浏览器、CATALOG.md、assets/ zip）完全一致。**
**2 处不一致在 README.md 中。**

---

## 对比矩阵

| 技能 | skills/ 目录 | 技能浏览器 | CATALOG.md | README "已上架" | README 目录树 | assets zip |
|------|------------|-----------|------------|---------------|-------------|------------|
| **ask-before-act** | v0.1.0 | v0.1.0 | v0.1.0 | 未列出 | 未列出 | v0.1.0 |
| **gitlab-repo-upload** | v0.3.0 | v0.3.0 | v0.3.0 | v0.3.0 | 有 | v0.3.0 |
| **skill-bootstrap** | v0.2.1 | v0.2.1 | v0.2.1 | v0.2.1 | 有 | v0.2.1 |
| **skill-discipline** | v0.1.0 | v0.1.0 | v0.1.0 | 未列出 | **目录树缺失** | v0.1.0 |
| **skill-env-setup** | v0.4.0 | v0.4.0 | v0.4.0 | 未列出 | 有 | v0.4.0 |
| **skill-update** | v0.1.0 | v0.1.0 | v0.1.0 | 未列出 | 有 | v0.1.0 |
| **svw-ppt-generator** | v0.1.0 | v0.1.0 | v0.1.0 | v0.1.0 | 有 | v0.1.0 |
| **requirement-briefing** | v0.1.0 | v0.1.0 | v0.1.0 | 未列出 | **目录树空域** | v0.1.0 |
| **writing-plans** | v0.1.0 | v0.1.0 | v0.1.0 | 未列出 | **目录树空域** | v0.1.0 |
| **verification-before-completion** | v0.1.0 | v0.1.0 | v0.1.0 | 未列出 | 有 | v0.1.0 |
| **subagent-driven-development** | v0.1.0 | v0.1.0 | v0.1.0 | 未列出 | 有 | v0.1.0 |
| **separate-employee-extraction** | v1.0.0 | v1.0.0 | v1.0.0 | v1.0.0 | 有 | v1.0.0 |

---

## 发现的 2 处不一致

### 1. README.md 目录结构 -- platform-engineering 域缺少 `skill-discipline`

**实际 skills/ 目录有 6 个技能在 platform-engineering：**
- ask-before-act, gitlab-repo-upload, skill-bootstrap, skill-discipline, skill-env-setup, skill-update

**README 目录树只列出 5 个，缺少 `skill-discipline`：**
```
    platform-engineering/
        gitlab-repo-upload/
        skill-bootstrap/
        ask-before-act/
        skill-update/
        skill-env-setup/
```
**应补上 `skill-discipline/`**

---

### 2. README.md 目录结构 -- project-management 域为空

**实际 skills/ 目录有 2 个技能在 project-management：**
- requirement-briefing
- writing-plans

**README 目录树中 project-management 域为空：**
```
    project-management/
    data-analysis/
    archive/
```
**应补上：**
```
    project-management/
        requirement-briefing/
        writing-plans/
```

---

## 关于 README "已上架 Skill" 表格（5个 vs 12个）

README 第206行明确说明：**"超过 5 个时仅保留最新 5 条"**，这是设计意图，不是 bug。

当前表格的 5 个技能与版本号是跟云上一致的：
- separate-employee-extraction v1.0.0
- gitlab-repo-upload v0.3.0
- skill-bootstrap v0.2.1
- svw-ppt-generator v0.1.0
- ask-before-act v0.1.0

---

## CATALOG.md 最后更新日期

CATALOG.md 中各技能"最后更新"日期：
| 技能 | CATALOG 日期 | 今天（2026-07-07）是否修改？ |
|------|------------|------------------------|
| gitlab-repo-upload | 2026-07-06 | 否 |
| skill-bootstrap | 2026-07-03 | 是（依赖检查更新）|
| skill-update | 2026-07-04 | 是（依赖检查更新）|
| skill-env-setup | 2026-07-07 | 是（依赖检查更新）|
| requirement-briefing | 2026-07-05 | 是（依赖检查更新）|
| writing-plans | 2026-07-05 | 是（依赖检查更新）|

**建议：** 如果今天修改了 SKILL.md，CATALOG.md 的"最后更新"列应同步更新为今天日期。

---

## 修复建议

1. **修复 README 目录结构（2处）：**
   - platform-engineering 域添加 `skill-discipline/`
   - project-management 域添加 `requirement-briefing/` 和 `writing-plans/`

2. **同步 CATALOG.md 最后更新日期（5 个技能需更新）：**
   - skill-bootstrap -> 2026-07-07
   - skill-update -> 2026-07-07
   - skill-env-setup -> 2026-07-07（已经是今天）
   - requirement-briefing -> 2026-07-07
   - writing-plans -> 2026-07-07
