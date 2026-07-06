---
name: skill-bootstrap
description: 当用户要求新建、创建、编写或做一个 Agent Skill 时触发。引导作者按 7 门禁质量标准从零创建高质量 Agent Skill，覆盖领域确认、Gotchas 提炼、正文+eval 交替编写、自检清单、格式预检、产出报告全链路。不适用于：修改已有 skill（走 skill-update）、单纯讨论 skill 设计而不创建、评估第三方 skill（走 skill-audit 流程）、已有 skill 的归档管理。
---

# Skill 创建引导（Skill Bootstrap）

引导作者按 7 门禁质量标准从零创建一个高质量 Agent Skill。走 5 步流程，每一步都是门禁——不通过不进入下一步。

<HARD-GATE>
1. 在完成第三步（自检清单全部通过）之前，禁止将 skill 提交到 skill registry、禁止声称 skill 已就绪、禁止跳过任何门禁步骤。
2. 涉及信息收集时，必须使用 AskUserQuestion 工具提供结构化选项，禁止纯文本提问。
3. 涉及执行动作的 skill 必须指示使用 EnterSpecMode/ExitSpecMode，禁止跳过计划审核。
</HARD-GATE>

## 能力边界与引导

本技能专注于**从零创建新 skill**。如果目标 skill 已存在于仓库中，请引导用户使用对应的技能。

| 场景 | 使用技能 | 说明 |
|------|---------|------|
| 从零创建新 skill | **skill-bootstrap**（本技能） | 全新技能，从领域确认到发布全流程 |
| 更新/修改/迭代/升级已有 skill | **skill-update** | 已有技能的版本升级、内容修改、eval 迭代、旧 Release 清理 |
| 评估 skill 质量 | skill-audit | 对已有 skill 的独立质量审计 |
| skill 归档管理 | 手动归档 | 标记 DEPRECATED，移至 archive/ 域 |

> **关键判别**：如果目标 skill 已存在于仓库中（有 SKILL.md 文件），引导用户使用 **skill-update**；如果是全新的（从零开始），使用 **skill-bootstrap**（本技能）。

## Gotchas

1. **跳过 Gotchas 直接写正文** — Agent 不知道自己的盲区，Gotchas 是 skill 最有价值的部分。没有 Gotchas 的 skill 等同于没有安全网。**纠正：创建时先让作者列出 3 条曾踩过的坑，再从坑中提炼 Gotchas。正文可以改，Gotchas 是灵魂。**

2. **eval 用例和正文脱节** — 写完正文再补 eval 时，eval 测的是理想路径，和正文实际覆盖的场景不一致。**纠正：正文和 eval 交替推进。写完一段正文立刻出一两条 eval。一次性口述完所有正文但不提供 eval——明确拒绝进入第三步。**

3. **所有内容堆在 SKILL.md** — 正文超过 300 行时提醒拆分，超过 500 行自检不过。**纠正：参考资料、字段说明、决策表拆到 references/。不是"超过才拆"，创建时就有意识分层。**

4. **description 太泛导致误触发** — "Use when user asks about data" 会和几十个 skill 重叠。**纠正：description 必须包含明确的触发场景关键词、不应触发的边界说明、按实际复杂度判断。**

5. **near-miss 触发测试缺失** — 只测 should-trigger 不测 should-not-trigger，或者 should-not-trigger 里没有 near-miss。**纠正：near-miss（共享关键词但不该触发的查询）>= 4 条，这才是考验 description 质量的试金石。**

6. **忘记写"不适用场景"** — description 只有触发条件没有排除条件。**纠正：description 必须包含"不适用于"段落，列出至少 3 个不应触发的场景。**

7. **正文中用纯文本提问而非 AskUserQuestion** — 写 `> "请确认：1.xxx 2.xxx"` 导致用户需要手动输入。**纠正：所有面向用户的提问，必须明确指示使用 AskUserQuestion 工具，提供 2-4 个选项。**

## 流程

### 第零步：确认领域

1. 确认 skill 所属功能域（从以下域分类中选择，或新建一个域）：
   - `platform-engineering` — 平台工程与 DevOps
   - `general-office` — 通用办公与文件管理
   - `development-testing` — 功能开发与测试
   - `project-management` — 项目与功能管理
   - `data-analysis` — 数据分析与处理
   - `archive` — 已废弃 skill
2. 确认 skill 名称（小写字母+数字+连字符，1-64 字符）
3. 在本地 skill 目录下创建目录结构骨架：
   ```
   {skill-name}/
   ├── SKILL.md
   ├── references/       # 可选
   ├── scripts/          # 可选
   └── evals/
       ├── evals.json
       └── eval_queries.json
   ```

### 第一步：提炼 Gotchas

先不做任何其他事，让作者回忆并写出 3-5 条"Agent 在没有这个 skill 时会犯的具体错误"。再从这些错误中提炼 Gotchas。

每一条 Gotchas 必须满足：
- 描述 Agent 具体会犯什么错误（不是泛泛的"注意质量"）
- 给出纠正方案（Agent 应该怎么做）
- 基于真实经验，不编造

Read references/gotchas-criteria.md for detailed criteria.

### 第二步：编写正文 + 同步设计 eval 资产

**核心原则：正文、触发测试、eval 用例三者交替推进，不写完正文再补 eval。**

**2a. 交替节奏**

每完成 SKILL.md 的一个模块，立刻做两件事：
- 出 1-2 条 eval 用例草稿（追加到 evals.json）
- 出 2-3 条触发测试草稿（追加到 eval_queries.json）

**交替是不可能妥协的硬约束。** 如果作者试图一次性口述完所有正文但不提供对应 eval——明确拒绝进入第三步。

**2b. SKILL.md 编写规范**

1. **frontmatter**：name（与目录名一致）、description（含触发关键词 + 排除场景）
2. **HARD-GATE**：如果 skill 涉及执行动作，必须有禁止在批准前执行的硬门禁
3. **正文**：按"触发条件 -> 前置检查 -> 操作步骤 -> 输出格式 -> 异常处理"的结构组织
   - 正文超过 **300 行**时提醒拆分到 references/，超过 **500 行**自检查不过
4. **references/**：条件加载指令（"Read references/xxx.md if ..." 放在正文中）
5. **执行后自迭代钩子（必装）**：每个 skill 的流程末尾必须包含复盘步骤

Read references/skill-structure.md for detailed structure requirements.

**2c. Interview 机制规范（必装）**

如果 skill 涉及向用户提问/信息收集，**必须**在正文中指示使用 `AskUserQuestion` 工具，禁止纯文本提问。

**AskUserQuestion 工具规范：**
- 每次调用可包含 1-4 个问题
- 每个问题提供 2-4 个选项
- 推荐选项放在第一个，标注"（推荐）"
- header 标签控制在 12 字符以内

**在 skill 正文中的写法：**

```markdown
调用 AskUserQuestion（4个问题）：

| 问题 | header | 选项 |
|------|--------|------|
| 汇报主题是什么？ | 汇报主题 | 选项A / 选项B / 选项C |
```

**禁止的写法：**
```markdown
> "请确认：
> 1. 主题是什么？
> 2. 对象是谁？"
```

**2d. Spec 模式规范（必装）**

如果 skill 涉及执行动作（生成、修改、创建文件等），**必须**在正文中指示使用 Spec 模式。

**Spec 模式流程：**
1. 信息收集完成后，调用 `EnterSpecMode` 进入 spec 模式
2. 生成执行计划（Spec），包含：任务概览、关键决策、预期输出
3. 用户审核 Spec，确认后调用 `ExitSpecMode` 退出
4. 退出后才允许开始执行

**在 skill 正文中的写法：**

```markdown
### 阶段X：Spec 模式计划审核

信息收集完成后，必须调用 EnterSpecMode 进入 spec 模式。

Spec 内容必须包含：
1. {列出计划中必须包含的内容项}
2. {关键决策点}
3. {预期输出格式}

用户审核后调用 ExitSpecMode 确认，才能进入下一阶段。
```

**2e. 触发测试同步设计**

在写正文的同时逐步填充 eval_queries.json：
- **should-trigger（>= 8 条）**：覆盖不同措辞变体、含触发关键词的边界场景
- **should-not-trigger（>= 8 条，含 >= 4 条 near-miss）**：near-miss 必须共享关键词但不该触发
- 每条包含 query + should_trigger（bool）+ reason

**2f. Eval 用例同步设计**

在写正文的同时逐步填充 evals.json：
- **>= 5 条用例**：覆盖正常路径 + 异常路径 + 边界场景 + near-miss
- 每条包含 prompt + expected_output + assertions（>= 2 条）
- assertions 必须是可机械判定的

### 第三步：自检清单

所有产出完成后，逐项核对。**全部通过才能进入第四步。**

```
[ ] 1. SKILL.md 存在且 frontmatter 包含 name 和 description
[ ] 2. name 与父目录名一致，仅含小写字母/数字/连字符
[ ] 3. description 使用了命令式，含触发关键词和不应触发的边界说明
[ ] 4. 正文包含具体的操作步骤（非泛泛的"适当处理"）
[ ] 5. 包含 >= 5 条 Gotchas（基于真实经验）
[ ] 6. evals/evals.json 存在且含 >= 3 条用例
[ ] 7. 每条用例有 prompt + expected_output + assertions（>= 2 条/用例）
[ ] 8. evals/eval_queries.json 存在且含 >= 16 条（含 >= 4 条 near-miss）
[ ] 9. SKILL.md 正文 <= 500 行（超出部分已拆分到 references/）
[ ] 10. 不含硬编码密钥/密码/Token 或内网 IP
[ ] 11. 正文末尾包含「执行后复盘（自迭代钩子）」章节
[ ] 12. 如 skill 涉及向用户提问，正文中明确指示使用 AskUserQuestion 工具
[ ] 13. 如 skill 涉及执行动作，正文中明确指示使用 EnterSpecMode/ExitSpecMode
```

### 第四步：格式预检

在提交前运行本地预检：
- frontmatter 字段完整性
- description 长度 <= 1024
- name 命名规范
- scripts/ 目录含环境预检（如适用）
- references/ 有条件加载指令（如适用）

### 第五步：产出报告与发布

输出创建完成报告，包含：
- skill 名称、域、预期版本号（v0.1.0）
- 自检清单结果（13/13）
- eval 用例数 + 触发测试数
- 下一步行动：提交到 skill registry -> CI 自动运行门禁 2-4 -> 人工审核

**发布到 Skill Hub（Tag + Release）：**

自检和格式预检通过后，使用 AskUserQuestion 工具确认提交方式：

调用 AskUserQuestion（2 个问题）：

| 问题 | header | 选项 |
|------|--------|------|
| 你的 GitLab 角色是？ | 角色确认 | Maintainer（可直接 push）/ Developer（需走 PR）/ 不确定 |
| 提交方式？ | 提交方式 | 创建 PR（推荐）/ 直接 push 到 main |

**路径 A：PR 流程（Developer 或选择 PR 的 Maintainer）**

```bash
# 1. 创建 feature 分支
git -C "<repo_path>" checkout -b "feature/<skill-name>-v<version>"

# 2. 提交代码
git -C "<repo_path>" add .
git -C "<repo_path>" commit -m "Add <skill-name> skill"

# 3. 推送分支
git -C "<repo_path>" push origin "feature/<skill-name>-v<version>"

# 4. 创建 Merge Request（GitLab API）
curl -s -X POST "https://<host>/api/v4/projects/<project_id>/merge_requests" \
  -H "PRIVATE-TOKEN: <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "source_branch": "feature/<skill-name>-v<version>",
    "target_branch": "main",
    "title": "Add <skill-name> skill v<version>",
    "description": "## 自检清单结果\n\n- [x] 1. SKILL.md frontmatter\n- [x] 2. name 与目录名一致\n...\n- [x] 13. EnterSpecMode/ExitSpecMode\n\n## 质量指标\n\n- Gotchas: X 条\n- Eval 用例: X 条\n- 触发测试: X 条"
  }'
```

等待 CI 门禁 2-4 自动运行。CI 通过后通知审核人进行门禁 5（人工审核）。Maintainer 审核通过并合并 MR 后，切回 main 创建 Tag：

```bash
# 5. 切回 main 并拉取最新代码
git -C "<repo_path>" checkout main
git -C "<repo_path>" pull origin main

# 6. 创建版本 Tag
git -C "<repo_path>" tag "<skill-name>/v<version>"
git -C "<repo_path>" push origin "<skill-name>/v<version>"
```

**路径 B：直接 push（仅 Maintainer）**

```bash
# 1. 提交并推送
git -C "<repo_path>" add .
git -C "<repo_path>" commit -m "Add <skill-name> skill"
git -C "<repo_path>" push origin main

# 2. 创建版本 Tag
git -C "<repo_path>" tag "<skill-name>/v<version>"
git -C "<repo_path>" push origin "<skill-name>/v<version>"
```

> **注意**：路径 B 仅限 Maintainer 角色。main 分支已设为受保护，Developer 直接 push 会被 403 拒绝。选择"不确定"角色的用户默认走路径 A。

**以下步骤两条路径都执行：**

```bash
# 创建 Release（GitLab API）
curl -s -X POST "https://<host>/api/v4/projects/<project_id>/releases" \
  -H "PRIVATE-TOKEN: <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "tag_name": "<skill-name>/v<version>",
    "name": "<skill-name> v<version>",
    "description": "<release_description>"
  }'
```

```bash
# 6. 上传 Skill Zip 附件到 Release（GitLab API）
# 先上传文件
curl -s --header "PRIVATE-TOKEN: <token>" \
  --form "file=@<skill-name>-v<version>.zip" \
  "https://<host>/api/v4/projects/<project_id>/uploads" | python -c "import sys,json; print(json.load(sys.stdin)['url'])"
# 返回值如 /uploads/xxxx/<skill-name>-v<version>.zip，拼接到 https://<host> 得到完整 URL

# 再链接到 Release
curl -s -X POST "https://<host>/api/v4/projects/<project_id>/releases/<skill-name>%2Fv<version>/assets/links" \
  -H "PRIVATE-TOKEN: <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "<skill-name>-v<version>.zip",
    "url": "https://<host><upload_url>",
    "link_type": "other"
  }'
```

> Zip 文件需预先打包：将 `skills/<domain>/<skill-name>/` 目录下的所有文件打成 `<skill-name>-v<version>.zip`。用户可通过 Release 页面直接下载 zip，无需 git。

**参数说明：**

| 参数 | 说明 | 示例 |
|------|------|------|
| `<repo_path>` | skill-hub 仓库本地路径 | `D:\qoder-skills` |
| `<skill-name>` | skill 名称（与目录名一致） | `skill-bootstrap` |
| `<version>` | 语义化版本号 | `0.1.0` |
| `<host>` | GitLab 域名 | `epfa-gitlab.csvw.com` |
| `<project_id>` | 项目 ID（数字） | `289` |
| `<token>` | GitLab 个人访问令牌 | `glpat-xxx` |

**版本号判定规则：**
- v0.1.0：首次创建
- patch（0.1.1）：仅修改 evals/、gotchas 措辞、references/
- minor（0.2.0）：修改 description、新增 gotchas、新增 eval 用例
- major（1.0.0）：修改 name、修改核心流程结构

**Release 描述规范：**

创建 Release 时，`description` 字段不能只写 "Initial release"，必须包含技能的完整描述，供用户在 Release 页面了解技能功能。

description 必须包含以下章节：

| 章节 | 内容 |
|------|------|
| 技能描述 | 从 SKILL.md frontmatter 的 description 字段提取 |
| 核心功能 | 列出技能的主要功能点（3-8 条） |
| 质量指标 | Gotchas 数量、Eval 用例数、触发测试数（含 near-miss 数） |
| 关键 Gotchas | 列出所有 Gotchas 条目标题 |
| 拉取方式 | Zip 下载链接 + `git clone --filter=blob:none --sparse --branch <skill-name>/v<version> <repo-url>` |
| 技能路径 | `skills/<domain>/<skill-name>/` |

**示例：**

```json
{
  "tag_name": "ask-before-act/v0.1.0",
  "name": "ask-before-act v0.1.0",
  "description": "## ask-before-act v0.1.0\n\n### 技能描述\n\n当Agent不确定用户诉求...\n\n### 核心功能\n\n- 意图确定性评估...\n\n### 质量指标\n\n| 指标 | 数量 |\n| Gotchas | 5 条 |\n| Eval 用例 | 7 条 |\n\n### 关键 Gotchas\n\n1. 使用纯文本提问而非 AskUserQuestion 工具\n2. ...\n\n### 拉取方式\n\n```bash\ngit clone --branch ask-before-act/v0.1.0 https://epfa-gitlab.csvw.com/ecc-2/qoder-skills.git\n```\n\n### 技能路径\n\n```\nskills/platform-engineering/ask-before-act/\n```"
}
```

**更新已有 Release 描述（PUT API）：**

如果 Release 已创建但描述需要更新（如补充完整描述），使用 PUT 方法：

```bash
curl -s -X PUT "https://<host>/api/v4/projects/<project_id>/releases/<skill-name>%2Fv<version>" \
  -H "PRIVATE-TOKEN: <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "description": "<new_release_description>"
  }'
```

> **注意**：此 GitLab 版本的 Release 更新使用 **PUT** 方法，不是 PATCH（PATCH 返回 404）。tag_name 中的 `/` 需 URL 编码为 `%2F`。

**删除历史版本 Release：**

发布新版本 Release 后，必须删除同一技能的历史版本 Release，保持 Release 页面只展示每个技能的最新版本。

```bash
curl -s -X DELETE "https://<host>/api/v4/projects/<project_id>/releases/<skill-name>%2Fv<old_version>" \
  -H "PRIVATE-TOKEN: <token>"
```

例如，发布 `ask-before-act/v0.2.0` 后，删除 `ask-before-act/v0.1.0` 的 Release：

```bash
curl -s -X DELETE "https://epfa-gitlab.csvw.com/api/v4/projects/289/releases/ask-before-act%2Fv0.1.0" \
  -H "PRIVATE-TOKEN: <token>"
```

> **注意**：DELETE 只删除 Release 元数据，不影响 git tag 和代码历史。tag 仍然保留在仓库中。

## references

- `references/skill-structure.md`：SKILL.md 详细结构规范。在第二步编写正文时读取。
- `references/gotchas-criteria.md`：Gotchas 提炼标准。在第一步提炼 Gotchas 时读取。
- `references/eval-guidelines.md`：eval 用例设计指南。在第二步设计 eval 时读取。

## 关键原则

- **Gotchas 优先** — 正文可以改，Gotchas 是 skill 的灵魂
- **正文 eval 交替** — 不分阶段，写完一段正文立刻补 eval
- **分层意识** — "Agent 不知道的信息"放 SKILL.md，"Agent 需要时查阅的信息"放 references/
- **near-miss 是试金石** — 一条好的 near-miss 比十条 should-trigger 更能证明 description 质量
- **命令式极简** — "Favor procedures over declarations"。不要教 Agent 什么是 PDF，教它怎么处理 PDF
- **结构化提问优先** — skill 涉及信息收集时，必须指示使用 AskUserQuestion 工具
- **计划审核优先** — skill 涉及执行动作时，必须指示使用 Spec 模式

## 执行后复盘（自迭代钩子）

每次完成本 skill 的全部步骤后，Agent 必须自动执行以下动作，不询问用户：

1. **反思**：本轮执行中，是否遇到了 skill 正文和 Gotchas 都没覆盖的坑？

2. **记录**：有则追加到 `evals/PITFALLS_LOG.md`，无则跳过。格式：

| 日期 | 场景摘要 | 犯了什么错误 | 如果早知道__就不会犯 | 临时补救方式 |
|------|---------|-------------|-------------------|------------|
| YYYY-MM-DD | 一句话 | Agent 具体做了什么 | 缺失的知识/规则 | 怎么绕过去的 |

3. **不提交**：`PITFALLS_LOG.md` 是个人本地文件，不提交到 skill registry。
