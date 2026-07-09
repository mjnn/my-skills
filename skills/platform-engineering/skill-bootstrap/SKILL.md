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
4. **未创建 tag 和 release 的技能视为未发布** — 禁止将没有对应 Git tag 和 GitLab Release 的 skill 标记为"已发布"或写入 skill-browser.md。
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

### 本技能负责
- 从零创建新 skill 的完整流程（领域确认 → Gotchas 提炼 → 正文+eval 编写 → 自检 → 发布）
- 指导作者按 7 门禁质量标准完成 skill 创建
- skill 的结构规范、格式预检、版本管理和发布

### 本技能不负责
- 更新/修改已有 skill → 使用 **skill-update**
- 评估已有 skill 质量 → 手动走 **skill-audit** 流程
- skill 归档管理 → 手动标记 DEPRECATED 并移至 archive/ 域
- 具体的代码实现（被创建 skill 的业务逻辑由作者自行实现）

## Gotchas

1. **跳过 Gotchas 直接写正文** — Agent 不知道自己的盲区，Gotchas 是 skill 最有价值的部分。没有 Gotchas 的 skill 等同于没有安全网。**纠正：创建时先让作者列出 3 条曾踩过的坑，再从坑中提炼 Gotchas。正文可以改，Gotchas 是灵魂。**

2. **eval 用例和正文脱节** — 写完正文再补 eval 时，eval 测的是理想路径，和正文实际覆盖的场景不一致。**纠正：正文和 eval 交替推进。写完一段正文立刻出一两条 eval。一次性口述完所有正文但不提供 eval——明确拒绝进入第三步。**

3. **所有内容堆在 SKILL.md** — 正文超过 300 行时提醒拆分，超过 500 行自检不过。**纠正：参考资料、字段说明、决策表拆到 references/。不是"超过才拆"，创建时就有意识分层。**

4. **description 太泛导致误触发** — "Use when user asks about data" 会和几十个 skill 重叠。**纠正：description 必须包含明确的触发场景关键词、不应触发的边界说明、按实际复杂度判断。**

5. **near-miss 触发测试缺失** — 只测 should-trigger 不测 should-not-trigger，或者 should-not-trigger 里没有 near-miss。**纠正：near-miss（共享关键词但不该触发的查询）>= 4 条，这才是考验 description 质量的试金石。**

6. **忘记写"不适用场景"** — description 只有触发条件没有排除条件。**纠正：description 必须包含"不适用于"段落，列出至少 3 个不应触发的场景。**

7. **正文中用纯文本提问而非 AskUserQuestion** — 写 `> "请确认：1.xxx 2.xxx"` 导致用户需要手动输入。**纠正：所有面向用户的提问，必须明确指示使用 AskUserQuestion 工具，提供 2-4 个选项。**

8. **假设系统已装 Python/pip 并在线装库** — 内网零预装环境会整体失败。**纠正：Read references/portable-tools.md；共享 Python 用 skill-kit；专属库放 vendor/python-packages/；流程第一步 init_skill_python.ps1。**

## 流程



### 运行时说明（无脚本）

本 skill 以对话与流程引导为主，不直接执行脚本。若会话中需要运行**本 skill 或其他 skill 的 scripts/**，必须先确认 skill-kit 已就绪（Read skill-kit `references/preflight.md`）；未就绪则引导用户运行 **skill-env-setup**。

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
   ├── scripts/          # 可选；须用 $env:QODER_PYTHON，见 portable-tools.md
   ├── vendor/
   │   └── python-packages/   # 若需第三方 Py 库（离线 wheel 解压内容）
   ├── tools/            # 可选：本 skill 独占便携工具
   │   └── manifest.json
   └── evals/
       ├── evals.json
       └── eval_queries.json
   ```

Read references/portable-tools.md。

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

6. **能力边界与依赖清单（必装）**：每个 skill 必须包含独立的「能力边界」和「依赖清单」章节
   - **能力边界**：明确本技能「负责什么」和「不负责什么」
   - **依赖清单**：skill-kit（共享 Python/Git）、本 skill `vendor/python-packages`、其他 Agent Skill
   - **边界判定原则**：Python/Git 安装属 skill-kit + skill-env-setup，业务 skill 不得重复打包解释器

7. **便携工具规范（必装，若含 scripts/ 或 Py 依赖）**：Read references/portable-tools.md
   - scripts 使用 `$env:QODER_PYTHON`，禁止裸 `python`/`pip install`
   - 第三方库离线放入 `vendor/python-packages/`
   - 流程含 `init_skill_python.ps1 -SkillDir <本 skill 根>`

8. **前置依赖检查（必装）**：如果依赖清单中包含其他 Agent Skill（非内置工具），skill 流程的**第一步**必须是前置依赖检查
   - **检查方法**：查看当前会话的 `<available_skills>` 列表，或检查 `%USERPROFILE%\.qoder-cn\skills\`（Windows）/ `~/.qoder-cn/skills/`（Unix）目录下是否存在依赖的技能
   - **依赖可用** → 直接进入流程下一步
   - **依赖不可用** → 使用 AskUserQuestion 工具提示用户，选项包括：
     - "继续执行"（推荐）— 在没有依赖技能的情况下继续，手动完成对应步骤
     - "先安装依赖" — 暂停任务，提供依赖清单中的拉取命令
     - "取消任务" — 终止当前任务
   - **用户选择"继续执行"** → 记录限制，在流程中依赖技能的调用点提示用户手动完成
   - **用户选择"先安装依赖"** → 提供安装命令，等待用户确认安装完成后再继续
   - **用户选择"取消任务"** → 终止执行
   - **模板写法**：
     ```markdown
     0. **前置依赖检查** — 检查 `<dependency-skill-name>` 技能是否在当前环境中可用（查看 `<available_skills>` 列表或检查 skills 目录）。如果不可用，使用 AskUserQuestion 工具提示用户：
        - 问题："本技能需要 <dependency-skill-name> 技能，但当前环境未安装。是否继续？"
        - 选项 1（推荐）："继续执行" — 在没有依赖的情况下继续
        - 选项 2："先安装依赖" — 提供安装命令
        - 选项 3："取消任务" — 终止当前任务
     ```

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
[ ] 14. 正文中包含「能力边界」章节，明确本技能负责和不负责的范围
[ ] 15. 正文中包含「依赖清单」章节，列出依赖的技能/工具及拉取方式
[ ] 16. 如依赖清单包含其他 Agent Skill，流程第一步包含前置依赖检查（检查可用性 + AskUserQuestion 降级处理）
[ ] 17. 如含 scripts/ 或 Py 库：符合 portable-tools.md（vendor、QODER_PYTHON、无 pip install）
[ ] 18. 流程含「步骤 0：skill-kit 就绪检查」（见 skill-kit references/preflight.md）；未就绪时引导 skill-env-setup，禁止裸 python/git
[ ] 19. 已创建 `<skill-name>/v<version>` tag 并推送到远程
[ ] 20. 已通过 GitLab API 创建对应 Release（含完整描述）
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
- 自检清单结果（20/20）
- eval 用例数 + 触发测试数
- 下一步行动：提交到 skill registry -> CI 自动运行门禁 2-4 -> 人工审核

**发布到 Skill Hub（Tag + Release —— 强制步骤，不可跳过）：**

> **HARD-GATE：未创建 tag 和 release 的技能视为未发布。自检清单第 19-20 项未通过前，禁止向用户报告"发布完成"。**

自检和格式预检通过后，使用 AskUserQuestion 工具确认提交方式：

调用 AskUserQuestion（2 个问题）：

| 问题 | header | 选项 |
|------|--------|------|
| 你的 GitLab 角色是？ | 角色确认 | Maintainer（可直接 push）/ Developer（需走 PR）/ 不确定 |
| 提交方式？ | 提交方式 | 创建 PR（推荐）/ 直接 push 到 main |

> **便携 Git / Python**：发布阶段命令中的 `git` 替换为 `& $env:QODER_GIT`；`python -c` 替换为 `& $env:QODER_PYTHON -c`。须先通过步骤 0 skill-kit 检查。

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
    "description": "## 自检清单结果\n\n- [x] 1. SKILL.md frontmatter\n- [x] 2. name 与目录名一致\n...\n- [x] 13. EnterSpecMode/ExitSpecMode
- [x] 14. 能力边界章节
- [x] 15. 依赖清单章节
- [x] 16. 前置依赖检查（如适用）
- [x] 17. tag 已创建
- [x] 18. Release 已创建\n\n## 质量指标\n\n- Gotchas: X 条\n- Eval 用例: X 条\n- 触发测试: X 条"
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

**示例（中文 Release 描述）：**

```json
{
  "tag_name": "ask-before-act/v0.1.0",
  "name": "ask-before-act v0.1.0",
  "description": "## ask-before-act v0.1.0\n\n### 技能描述\n\n当Agent不确定用户诉求、任务细节或执行方向时，使用AskUserQuestion工具向用户提出结构化问题，明确用户意图后再继续执行。\n\n### 核心功能\n\n- 意图确定性评估（≥80%确定性阈值）\n- 使用AskUserQuestion工具进行结构化提问\n- 澄清后复述确认机制\n- 分轮次提问避免overwhelm用户\n\n### 质量指标\n\n| 指标 | 数量 |\n|------|------|\n| Gotchas | 5 条 |\n| Eval 用例 | 7 条 |\n| 触发测试 | 16 条 |\n\n### 关键 Gotchas\n\n1. 使用纯文本提问而非 AskUserQuestion 工具\n2. 用户说'随便'时自由发挥\n3. 澄清后未复述确认直接执行\n4. 一次抛出太多问题 overwhelm 用户\n5. 用户意图已明确仍反复确认\n\n### 拉取方式\n\n```bash\ngit clone --branch ask-before-act/v0.1.0 https://epfa-gitlab.csvw.com/ecc-2/qoder-skills.git\n```\n\n### 技能路径\n\n```\nskills/platform-engineering/ask-before-act/\n```"
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

**同步仓库文档（强制步骤，不可跳过）：**

Release 创建完成后，必须同步更新仓库中的管理文档，确保版本号、Release 链接、Zip 下载链接三者一致：

| 文档 | 更新内容 |
|------|---------|
| README.md | 已上架 Skill 表格：版本号、Release 链接、Zip 下载链接（三者必须一致） |
| CATALOG.md | 注册表条目：版本号、描述、最后更新日期 |
| docs/skill-browser.md | 技能总览 + 详细条目：版本号、Zip 下载链接、Release 链接、Sparse Checkout 命令 |

文档同步检查清单：

- [ ] README.md 版本号已更新
- [ ] README.md Release 链接已更新
- [ ] README.md Zip 下载链接已更新（raw 格式）
- [ ] CATALOG.md 版本号已更新
- [ ] CATALOG.md 描述已更新
- [ ] CATALOG.md 日期已更新
- [ ] docs/skill-browser.md 版本号已更新
- [ ] docs/skill-browser.md Zip 下载链接已更新（raw 格式）
- [ ] docs/skill-browser.md Sparse Checkout 分支已更新

> **版本信息同步规范**：README.md、CATALOG.md 和 docs/skill-browser.md 中的版本号、Release 链接和 Zip 下载链接三者必须保持一致。使用 `grep` 检查所有版本号引用是否一致后再提交。

## 依赖清单

| 依赖项 | 类型 | 说明 | 拉取方式 |
|--------|------|------|---------|
| AskUserQuestion | 内置工具 | 向用户收集信息时提供结构化选项 | 内置，无需拉取 |
| EnterSpecMode / ExitSpecMode | 内置工具 | 执行动作前的计划审核 | 内置，无需拉取 |
| skill-kit | Agent Skill | 共享便携 Python/Git/7za | skill-env-setup 节点 4.0 安装；或 Hub zip 中的 skill-kit |
| skill-env-setup | Agent Skill | 首次环境初始化（可选，作者本机若已配置可跳过） | 初始化技能包 |
| git（便携） | skill-kit 工具 | 版本控制、tag 和 release | `$env:QODER_GIT`，非系统 git |
| GitLab API | 内网 HTTP | 创建 MR/Release | 便携 Python `urllib` 或 PowerShell `Invoke-RestMethod` |

> **说明**：禁止假设系统 git/curl/python。发布阶段 git 操作引用 `gitlab-repo-upload` 命令范式，但须将 `git` 替换为 `$env:QODER_GIT`。

## references

- `references/skill-structure.md`：SKILL.md 详细结构规范。在第二步编写正文时读取。
- `references/portable-tools.md`：**便携工具与 vendor 规范**。编写 scripts/ 或打包 Py 依赖时读取。
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
