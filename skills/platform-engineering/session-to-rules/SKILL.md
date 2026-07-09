---
name: session-to-rules
description: Extracts durable knowledge from the current workspace project only into that project's .cursor/rules/ as .mdc files (never global or user-home rules), and removes session-only artifacts within the same repo. Use when the user asks to 沉淀会话、保存规则到本项目、capture session to project rules、项目规则沉淀、清理临时文件、distill and cleanup, or wants repo-local conventions for this project only—not ~/.cursor/rules or personal skills. 不适用于：创建 Agent Skill（走 skill-bootstrap）、用户全局 ~/.cursor/rules、跨项目 skills 维护（走 ecc-rules-distill）。
---


# Session to Rules

将**当前工作区项目**（当前打开的 repo / workspace root）里、本次会话中值得长期复用的内容，提炼成 **本项目** 的 Cursor Rules（`<项目根>/.cursor/rules/*.mdc`），并清理**本仓库内**的临时工具代码与路径。

**硬性范围：仅本项目。** 不得写入用户全局规则、个人 skills、或其他 repo。

与 `ecc-save-session`（会话交接）和 `ecc-rules-distill`（skills 批量蒸馏）不同：本 skill 处理**本次对话**的 durable 约定 + **本仓库一次性产物清理**。


<HARD-GATE>
写入 rules 或删除文件前必须完成 Step 0 锁定 PROJECT_ROOT 并向用户展示提案；禁止未经确认写入 ~/.cursor/rules 或删除 PROJECT_ROOT 外路径。
</HARD-GATE>

## 项目范围（必读，违反即失败）

### 唯一允许的 rules 输出位置

```
{PROJECT_ROOT}/.cursor/rules/*.mdc
```

`PROJECT_ROOT` = 当前 Cursor **Workspace Path**（`user_info` 中的 workspace），或该目录下 `git rev-parse --show-toplevel` 的结果。二者不一致时，**以 git 仓库根为准**并告知用户。

### 禁止写入（Never）

| 禁止路径 | 说明 |
|----------|------|
| `~/.cursor/rules/`、`%USERPROFILE%\.cursor\rules\` | 用户全局 rules |
| `~/.cursor/skills/`、`~/.cursor/skills-cursor/` | 个人 / 内置 skills |
| `~/.cursor/rules/*.mdc` 任意用户目录下的 rules | 跨项目全局 |
| 其他 repo 的 `.cursor/rules/` | 非当前 workspace |
| `~/.cursor/AGENTS.md`、用户 home 下任意 AGENTS.md | 全局 agent 配置 |
| 本项目外的绝对路径 | 任何沉淀产物 |

需要通用格式说明时，**只读** [create-rule](~/.cursor/skills-cursor/create-rule/SKILL.md) 的 `.mdc` 语法，**不得**把 rule 文件写到 create-rule 文档所在目录或用户 home。

### Step 0: 解析并锁定项目根（任何读写前必做）

```bash
# 在 workspace 根执行
git rev-parse --show-toplevel
```

1. 记录 `PROJECT_ROOT` 绝对路径
2. 提案与摘要中**必须展示完整目标路径**，例如：
   `D:/AIG_Projects/rosbag_to_labels_pipline/.cursor/rules/config-paths.mdc`
3. 写入前校验：`target_path.startswith(PROJECT_ROOT)`，否则 **Stop** 并报告，不得写入
4. 若不在 git repo 内，用 Workspace Path 作为 `PROJECT_ROOT`；无法确定则 **先问用户**，不得猜测写到 home

### Cleanup 范围

临时文件/目录的删除与还原**仅限 `PROJECT_ROOT` 以内**。不得删除 workspace 外的路径（含用户提供的 `D:/temp/` 等），除非用户明确要求且仅作「用户自行处理」提示，不由 agent 执行 Delete。

## When to Use

- 会话结束前：「沉淀一下」「写到 rules 并清理临时文件」
- 刚敲定架构/约定，希望后续 session 默认遵守，且去掉调试脚本
- 长会话上下文将满：把 durable 部分迁出 rules，删掉已吸收进规则的临时代码

## When NOT to Use

| 内容类型 | 应去向 |
|---------|--------|
| WIP、TODO、未合并 diff 状态 | `ecc-save-session` |
| 跨 skills 通用原则批量维护 | `ecc-rules-distill` |
| 用户仍要保留的实验脚本 | 不删；可移入 `scripts/` 或标注为正式工具 |

## Gotchas

1. **写入用户全局 rules** — 污染所有项目。**纠正：仅 {PROJECT_ROOT}/.cursor/rules/。**
2. **未展示提案就写入** — 用户未批准。**纠正：Step 4 提案含完整绝对路径，用 AskUserQuestion 等确认。**
3. **删除无 rule 承接的调试脚本** — 知识丢失。**纠正：每条删除对应 rule 或正式代码。**
4. **与 skill-bootstrap 混淆** — 用户要建 Skill 却沉淀 rules。**纠正：新 Skill 走 skill-bootstrap。**
5. **git clean -fdx 批量清理** — 误删生产数据。**纠正：Never 批量 clean，逐条提案。**

## 流程

```
Task Progress:
- [ ] Step 0: 解析 PROJECT_ROOT，确认仅本项目
- [ ] Step 1: 扫描会话，列出 rule 候选
- [ ] Step 2: 扫描本仓库，列出 cleanup 候选
- [ ] Step 3: 读取 {PROJECT_ROOT}/.cursor/rules/，去重与归类
- [ ] Step 4: 向用户展示合并提案（含完整绝对路径）
- [ ] Step 5: 用户确认后：写入本项目 rules → 执行本仓库 cleanup
- [ ] Step 6: 展示变更摘要（含 PROJECT_ROOT）
```

---

### Step 1: 从会话提取 rule 候选

回顾当前对话，只保留满足**全部**条件的条目：

1. **可复用** — 下次同类工作仍成立
2. **可执行** — 「做 X / 不做 Y」
3. **有违反代价** — 忽略会重复踩坑
4. **项目相关** — 本仓库约定或域知识

**优先捕获：** 用户说「以后都这样做」、架构/配置最终决定、已验证 fix 背后的**原则**（非长代码块）。

**排除：** 未决方案、secrets、仅本次任务的临时代码（进 Step 2 清理清单，不进 rules）。

---

### Step 2: 扫描 cleanup 候选（工具代码 + 路径）

沉淀 = **知识进 rules，过程性产物出仓库**。系统扫描本会话可能创建或修改的内容。

#### 2a. 识别会话产生的临时工具代码

结合 `git status`、会话中创建/编辑的文件列表、import 关系，标记：

| 信号 | 示例 |
|------|------|
| 命名 | `tmp_*`, `debug_*`, `scratch_*`, `probe_*`, `check_*_once.py`, `test_manual_*` |
| 位置 | 项目根目录一次性 `.py`/`.sh`；`.cursor/scratch/`；未纳入正式 `scripts/` 的孤立文件 |
| 用途 | 仅用于本次排查：打印 schema、试 API、手动查 db、硬编码路径的 ad-hoc 脚本 |
| 引用 | **无**被正式代码 import；**无** CI/README 引用；**无**用户明确说要保留 |
| 会话来源 | 对话里 agent 为 debug 新建，且结论已写入 rule 或正式模块 |

```bash
git status --short
git diff --name-only
# 可选：确认无引用（示例）
# rg -l "from tmp_debug" . --glob '!*.venv/**'
```

**保留（不删）：** 已合并进主流程的模块、用户说「留着」的文件、有测试覆盖的工具、正式 `scripts/` 下文档化的 CLI。

#### 2b. 识别应删除或还原的路径

| 类型 | 处理 |
|------|------|
| 硬编码绝对路径（调试时写入 config/code） | **还原**为相对路径 / config 占位 / env；无法还原则删该行并记入 rule |
| 临时输出目录（`output_test/`, `tmp/`, `_scratch/`） | **Delete** 目录（确认非生产数据） |
| config 中本会话新增的废弃 key | **Delete** key；必要约定写入 rule |
| `.gitignore` 应覆盖但未忽略的临时产物 | 追加 ignore + 删文件 |
| 写进 rule 前的冗余注释块、DEBUG 开关 | **Delete** 或还原为 false |

**路径脱敏：** 写入 rule 时用 `config.yaml` 键名或 `{project_root}/...`，不写用户本机绝对路径。

#### 2c. 安全门槛（删除前必须满足）

- [ ] 该文件/路径的**知识**已在 rule 候选或正式代码中
- [ ] 不在 `git diff` 里与用户未完成的工作冲突（有 WIP 则 Skip 并说明）
- [ ] 非 `data/`、`clips/` 等生产数据（除非用户明确说是临时测试数据）
- [ ] 不删 `.cursor/rules/`、正式源码、依赖清单、`.env.example`
- [ ] 删除文件用 Delete 工具或 `git rm`；删目录前列出内容供用户确认

**Never** 批量 `git clean -fdx` 或删未在提案表中的文件。

---

### Step 3: 读取现有 rules（仅本项目）

在 **`PROJECT_ROOT`** 下操作，不要用相对路径写到 cwd 之外：

```bash
mkdir -p "{PROJECT_ROOT}/.cursor/rules"
```

列出 `{PROJECT_ROOT}/.cursor/rules/*.mdc`（不存在则视为空）。对 rule 候选判断 verdict：New File / Append / Revise / Already Covered / Skip。

单文件正文建议 **≤50 行**，一事一文件。

---

### Step 4: 向用户展示合并提案（必须）

**未经用户确认，不得写入 rules，不得删除任何文件。**

使用 AskUserQuestion 收集确认（禁止纯文本「请回复批准全部」）：

调用 AskUserQuestion（2 个问题）：

| 问题 | header | 选项 |
|------|--------|------|
| Rules 提案是否批准？ | Rules | 批准全部（推荐）/ 批准部分 / 跳过全部 |
| Cleanup 提案是否批准？ | Cleanup | 批准全部 / 批准部分 / 跳过全部 / 跳过 cleanup |

```markdown
# Session → Rules + Cleanup 提案

## 项目范围
**PROJECT_ROOT:** `D:/AIG_Projects/rosbag_to_labels_pipline`
**Rules 输出目录:** `{PROJECT_ROOT}/.cursor/rules/`（仅此目录，非全局）

## 摘要
Rules: 候选 {N} | 建议写入 {M} | 跳过 {K}
Cleanup: 删文件 {F} | 删目录 {D} | 还原路径/配置 {P} | 跳过 {S}

---

## A. Rules

| # | 原则 | Verdict | 目标文件（完整路径） | 作用域 |
|---|------|---------|----------------------|--------|
| 1 | ... | New File | `{PROJECT_ROOT}/.cursor/rules/xxx.mdc` | alwaysApply |

### 详情 …

---

## B. Cleanup

| # | 类型 | 路径 | 动作 | 理由 |
|---|------|------|------|------|
| C1 | 临时脚本 | `debug_db.py` | Delete | 结论已沉淀至 db-sync.mdc |
| C2 | 临时目录 | `tmp/parse_test/` | Delete dir | 一次性解析输出 |
| C3 | 硬编码路径 | `config.yaml` → `paths.scratch` | Remove key | 调试残留，正式路径见 rule #2 |
| C4 | 绝对路径 | `parse_rosbag.py` L42 | Revert | 恢复为 `resolve_path(project_root, ...)` |

**保留（不删）：** `scripts/inspect_bag.py` — 用户要求保留

---

请回复：
- Rules: 批准全部 / 批准 1,3 / 跳过全部
- Cleanup: 批准全部 / 批准 C1,C2 / 跳过 C3 / 跳过全部
```

用户可只批准 rules 不批准 cleanup，或反之。

---

### Step 5: 执行（顺序固定）

0. **路径校验** — 每个将写入的 `.mdc` 必须在 `{PROJECT_ROOT}/.cursor/rules/` 下；否则中止
1. **先写 rules** — 只写入 `{PROJECT_ROOT}/.cursor/rules/`
2. **再 cleanup** — 仅删除/还原 `PROJECT_ROOT` 内、且用户批准的路径
3. **还原优先于删除** — 配置/源码中的调试路径先 revert，再删纯临时文件
4. **删目录** — 先列顶层内容，再递归删除
5. **跑快速验证**（若项目有）— 如 `python -m py_compile` 受影响文件、或用户指定的 smoke 命令

---

### Step 6: 完成摘要

报告：

**项目**
- `PROJECT_ROOT` 绝对路径
- 确认未写入全局 / 用户 home rules

**Rules**
- 新建/修改的 `.mdc` **完整绝对路径**与 frontmatter

**Cleanup**
- 已删除文件/目录列表
- 已还原的配置/代码位置
- 跳过项及原因

**后续**
- 若仍有 WIP，提示 `ecc-save-session`
- 若删了调试脚本，确认正式入口命令仍可用

---

## Rule 文件格式

遵循 [create-rule](~/.cursor/skills-cursor/create-rule/SKILL.md)：

```markdown
---
description: 一句话说明（含触发关键词）
globs: **/*.py
alwaysApply: false
---

# 标题

- 可执行要点

## 来源
沉淀自 session YYYY-MM-DD；相关代码：`path/to/file`
```

命名：`kebab-case.mdc`。

---

## Rule 正文模板

```markdown
---
description: [描述 + 关键词]
alwaysApply: false
---

# [主题]

## 必须遵守
- ...

## 禁止
- ...

## 参考
- 配置：`config.yaml` → `section.key`
- 入口：`python parse_rosbag.py --config config.yaml`
```

---

## 质量门槛

**范围**
- [ ] 已执行 Step 0，`PROJECT_ROOT` 明确
- [ ] 所有 rule 路径均在 `{PROJECT_ROOT}/.cursor/rules/` 下
- [ ] 未触碰 `~/.cursor/rules`、`~/.cursor/skills` 等全局位置
- [ ] 提案表含完整绝对路径，用户可见将写入本项目

**Rules**
- [ ] 忽略它有明确后果
- [ ] 无 secret；rule 正文用相对路径 / config 键，不用本机绝对路径
- [ ] 与现有 rules 不矛盾

**Cleanup**
- [ ] 每条删除都有对应 rule 或正式代码承接
- [ ] 提案表涵盖所有将删路径
- [ ] 生产数据与保留文件未误伤

---

## 与 save-session 的配合

| 维度 | session-to-rules | ecc-save-session |
|------|------------------|------------------|
| 目的 | 长期约定 + 清理临时产物 | 短期续作交接 |
| 位置 | **`{PROJECT_ROOT}/.cursor/rules/`**（仅本项目） | `~/.cursor/session-data/`（用户级） |

先沉淀 + 清理，再 save-session 记录剩余 WIP。

---

## 完整示例

**会话：** 用 `debug_topics.py` 探 rosbag topic；确认输出布局后决定 `output/{bag_stem}/`；在 `config.yaml` 加了 `paths.debug_output: D:/temp/out`。

**提案：**

| Rules | |
|-------|---|
| 1 | 输出目录 `output/{bag_stem}/` → `label-output-layout.mdc` |

| Cleanup | |
|---------|---|
| C1 | Delete `debug_topics.py` |
| C2 | Remove `config.yaml` → `paths.debug_output` |
| C3 | workspace 外 `D:/temp/out` | **Skip（不删）** | 超出 PROJECT_ROOT；提示用户自行清理 |

**用户：** 「Rules 批准全部；Cleanup 批准 C1,C2；跳过 C3」

**执行：** 写入 `{PROJECT_ROOT}/.cursor/rules/label-output-layout.mdc` → 删本仓库内 `debug_topics.py` → 改 `config.yaml` → 摘要报告。

## 执行后复盘（自迭代钩子）

每次完成本 skill 的全部步骤后，Agent 必须自动执行以下动作，不询问用户：

1. **反思**：本轮执行中，是否遇到了 skill 正文和 Gotchas 都没覆盖的坑？
2. **记录**：有则追加到 `evals/PITFALLS_LOG.md`，无则跳过。格式：

| 日期 | 场景摘要 | 犯了什么错误 | 如果早知道__就不会犯 | 临时补救方式 |
|------|---------|-------------|-------------------|------------|
| YYYY-MM-DD | 一句话 | Agent 具体做了什么 | 缺失的知识/规则 | 怎么绕过去的 |

3. **不提交**：`PITFALLS_LOG.md` 是个人本地文件，不提交到 skill registry。

> 这个复盘步骤不打断用户工作流。Agent 在后台完成，用户无感知。
