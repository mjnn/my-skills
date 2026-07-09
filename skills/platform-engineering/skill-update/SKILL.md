---
name: skill-update
description: 当用户要求更新、修改、迭代或升级已有 Agent Skill 时触发。引导按门禁流程完成变更分析、版本判定、正文+eval 同步更新、自检、发布全链路。不适用于：从零创建新 skill（走 skill-bootstrap）、仅讨论 skill 设计不修改、评估第三方 skill（走 skill-audit）、skill 归档管理。
---

# Skill 更新引导

引导作者按门禁流程更新一个已有 Agent Skill。更新不是"改完就推"，而是"分析变更 → 同步更新 → 门禁检查 → 版本管理 → 发布"。

<HARD-GATE>
1. 在用户审核 Spec 并调用 ExitSpecMode 确认前，禁止修改任何 skill 文件。
2. 涉及信息收集时，必须使用 AskUserQuestion 工具提供结构化选项，禁止纯文本提问。
3. 发布前必须完成 18 项自检清单，禁止跳过自检直接 commit + push。
4. **未创建 tag 和 release 的技能视为未发布** — 禁止将没有对应 Git tag 和 GitLab Release 的技能标记为"已发布"或写入 skill-browser.md。
</HARD-GATE>

## 能力边界与引导

本技能专注于**更新已有 skill**。如果目标 skill 是全新的（仓库中不存在），请引导用户使用 skill-bootstrap。

| 场景 | 使用技能 | 说明 |
|------|---------|------|
| 从零创建新 skill | **skill-bootstrap** | 全新技能，从领域确认到发布全流程 |
| 更新/修改/迭代/升级已有 skill | **skill-update**（本技能） | 已有技能的版本升级、内容修改、eval 迭代、旧 Release 清理 |
| 评估 skill 质量 | skill-audit | 对已有 skill 的独立质量审计 |
| skill 归档管理 | 手动归档 | 标记 DEPRECATED，移至 archive/ 域 |

> **关键判别**：如果目标 skill 已存在于仓库中（有 SKILL.md 文件），使用 **skill-update**（本技能）；如果是全新的（从零开始），引导用户使用 **skill-bootstrap**。

### 本技能负责
- 已有 skill 的版本升级、内容修改、eval 迭代、旧 Release 清理
- 变更分析、版本判定、正文+eval 同步更新、自检、发布全链路
- 确保更新后的 skill 仍满足 18 项自检标准

### 本技能不负责
- 从零创建新 skill → 使用 **skill-bootstrap**
- 评估已有 skill 质量 → 手动走 **skill-audit** 流程
- skill 归档管理 → 手动标记 DEPRECATED 并移至 archive/ 域

## Gotchas

1. **直接修改 SKILL.md 不走 Spec 模式** — Agent 拿到更新需求后直接改文件，用户无法在执行前审核变更范围。**纠正：必须调用 EnterSpecMode 生成变更计划，列出每个文件的修改内容、版本号判定、eval 更新需求，用户审核 ExitSpecMode 确认后才能修改。**

2. **改了正文不更新 eval** — 修改了 SKILL.md 的流程步骤但忘了同步更新 evals.json 和 eval_queries.json，导致 eval 与正文脱节。**纠正：每次修改正文模块后必须检查对应 eval 是否需要更新。修改了流程 → 更新 evals.json；修改了 description → 更新 eval_queries.json。**

3. **版本号判定错误** — 修改了 description 或新增了 Gotchas 应该是 minor，但只升了 patch。或者修改了核心流程结构应该是 major 但只升了 minor。**纠正：严格按照版本号判定规则对照变更内容确定版本类型，在 Spec 中明确标注版本号及判定依据。**

4. **发布新 Release 不删旧 Release** — 创建了新版本 Release 但历史版本 Release 仍然保留在 Release 页面。**纠正：发布新 Release 后必须通过 DELETE API 删除旧版本 Release，保持 Release 页面只展示最新版本。**

5. **README、CATALOG 和 skill-browser 版本不同步** — 升级了 skill 版本但 README.md 的版本号、Release 链接、git clone 命令三者没有同步更新，docs/skill-browser.md 中的版本号和下载链接也未更新。**纠正：每次版本变更后必须同步更新 README.md 已上架 Skill 表格、CATALOG.md 注册表和 docs/skill-browser.md 技能浏览器文档，确保版本号、Release 链接、Zip 下载链接三者一致。**

6. **跳过自检直接发布** — 修改完 SKILL.md 就直接 commit + push + tag，没有跑 18 项自检清单。**纠正：发布前必须完成自检清单全部 18 项通过，包括正文行数 ≤ 500、Gotchas ≥ 5 条、eval ≥ 3 条、触发测试 ≥ 16 条等硬性指标。**

7. **修改 description 不检查触发测试覆盖** — 更新了 description 的触发条件但没检查 eval_queries.json 中的测试用例是否仍然匹配。**纠正：修改 description 后必须重新审视所有触发测试用例，确保 should-trigger 和 should-not-trigger 的 reason 仍然成立，必要时补充新的 near-miss。**

## 流程



### 步骤 0：skill-kit 就绪检查

Read skill-kit `references/preflight.md`。

```powershell
powershell -ExecutionPolicy Bypass -File "$env:USERPROFILE\.qoder-cn\tools\skill-kit\scripts\check_skill_kit_ready.ps1" -SkillDir "$env:USERPROFILE\.qoder-cn\skills\skill-update"
```

- 退出码 **0** → 继续
- **非 0** → 调用 AskUserQuestion（见 preflight.md）：引导用户**重新运行 skill-env-setup** 完成环境初始化，或重新检测；**禁止**使用裸 `python`/`git`/`pip`

### 阶段一：信息收集

使用 AskUserQuestion 工具收集以下信息（单次调用，4 个问题）：

| 问题 | header | 选项 |
|------|--------|------|
| 要更新哪个 skill？ | 技能名称 | 列出仓库中已有 skill / 其他 |
| 变更类型是什么？ | 变更类型 | 修改正文流程 / 新增 Gotchas / 修改 description / 修改 eval / 修复 bug / 其他 |
| 是否需要更新 eval？ | eval 同步 | 是-同步更新（推荐） / 否-仅改正文 |
| 预期版本号？ | 版本号 | patch / minor / major / 不确定 |

用户通过 "Other" 可自由输入任意回答。

> **可用域分类**：`platform-engineering`（平台工程与 DevOps）、`general-office`（通用办公与文件管理）、`development-testing`（功能开发与测试）、`project-management`（项目与功能管理）、`data-analysis`（数据分析与处理）、`archive`（已废弃 skill）。更新 skill 时无需变更域分类，但如需迁移域，在 Spec 中说明。

### 阶段二：变更分析

读取目标 skill 的当前文件：

1. 读取 `SKILL.md`，分析当前结构（行数、Gotchas 数、eval 数）
2. 读取 `evals/evals.json`，统计当前 eval 用例数
3. 读取 `evals/eval_queries.json`，统计当前触发测试数
4. 根据变更类型，确定需要修改的文件清单

**版本号判定规则：**

| 变更内容 | 版本类型 | 示例 |
|---------|---------|------|
| 仅修改 evals/、gotchas 措辞、references/ | patch（0.x.Y） | 修正 eval 断言、补充 gotcha 描述 |
| 修改 description、新增 gotchas、新增 eval 用例 | minor（0.X.0） | 新增 Gotcha、修改触发条件 |
| 修改 name、修改核心流程结构 | major（X.0.0） | 重构流程、重命名 skill |

### 阶段三：Spec 模式计划审核

信息收集和变更分析完成后，必须调用 EnterSpecMode 进入 spec 模式。

Spec 内容必须包含：
1. **变更清单**：每个文件的具体修改内容（SKILL.md / evals.json / eval_queries.json / references/）
2. **版本号判定**：新版本号 + 判定依据（对照版本号判定规则）
3. **eval 同步计划**：哪些 eval 用例需要新增/修改/删除
4. **触发测试同步计划**：哪些触发测试需要新增/修改/删除
5. **自检预估**：预估变更后 Gotchas 数、eval 数、触发测试数、正文行数
6. **发布计划**：tag 名称、Release 描述大纲、Zip 附件上传、需删除的旧 Release

用户审核后调用 ExitSpecMode 确认，才能进入下一阶段。

### 阶段四：执行变更

按 Spec 计划逐个文件修改：

**步骤 1：修改 SKILL.md**
- 按 Spec 中的变更清单修改对应章节
- 修改后检查正文行数 ≤ 500
- 确保「能力边界」和「依赖清单」章节存在且内容准确：
  - 能力边界：明确本 skill 「负责什么」和「不负责什么」
  - 依赖清单：列出依赖的技能/工具及拉取方式
  - 如果依赖清单包含其他 Agent Skill，确保正文中流程第一步包含前置依赖检查（检查可用性 + AskUserQuestion 降级方案）
  - 如果变更涉及能力扩展或收缩，同步更新「能力边界」章节
  - **便携运行时**：Read skill-bootstrap `references/portable-tools.md`；确保含步骤 0 skill-kit 检查、无裸 python/git/pip、vendor 包齐全

**步骤 2：同步更新 evals.json**
- 新增/修改/删除 eval 用例，与正文变更同步
- 确保每条用例有 prompt + expected_output + assertions（≥ 2 条）

**步骤 3：同步更新 eval_queries.json**
- 如果 description 变更：重新审视所有触发测试的 reason
- 新增/修改/删除触发测试用例
- 确保 should-trigger ≥ 8 条，should-not-trigger ≥ 8 条（含 ≥ 4 near-miss）

**步骤 4：更新 references/（如适用）**
- 如果变更涉及参考资料，同步更新 references/ 中的文件

### 阶段五：自检清单

所有变更完成后，逐项核对：

```
[ ] 1. SKILL.md 存在且 frontmatter 包含 name 和 description
[ ] 2. name 与父目录名一致，仅含小写字母/数字/连字符
[ ] 3. description 使用了命令式，含触发关键词和不应触发的边界说明
[ ] 4. 正文包含具体的操作步骤（非泛泛的"适当处理"）
[ ] 5. 包含 ≥ 5 条 Gotchas（基于真实经验）
[ ] 6. evals/evals.json 存在且含 ≥ 3 条用例
[ ] 7. 每条用例有 prompt + expected_output + assertions（≥ 2 条/用例）
[ ] 8. evals/eval_queries.json 存在且含 ≥ 16 条（含 ≥ 4 条 near-miss）
[ ] 9. SKILL.md 正文 ≤ 500 行（超出部分已拆分到 references/）
[ ] 10. 不含硬编码密钥/密码/Token 或内网 IP
[ ] 11. 正文末尾包含「执行后复盘（自迭代钩子）」章节
[ ] 12. 如 skill 涉及向用户提问，正文中明确指示使用 AskUserQuestion 工具
[ ] 13. 如 skill 涉及执行动作，正文中明确指示使用 EnterSpecMode/ExitSpecMode
[ ] 14. 正文中包含「能力边界」章节，明确本技能负责和不负责的范围
[ ] 15. 正文中包含「依赖清单」章节，列出依赖的技能/工具及拉取方式
[ ] 16. 如依赖清单包含其他 Agent Skill，流程第一步包含前置依赖检查（检查可用性 + AskUserQuestion 降级方案）
[ ] 17. 含 scripts/ 或 Py 库：符合 portable-tools.md（vendor、QODER_PYTHON、无 pip install）
[ ] 18. 含「步骤 0：skill-kit 就绪检查」；未就绪引导 skill-env-setup
[ ] 19. 已创建/更新 `<skill-name>/v<version>` tag 并推送到远程
[ ] 20. 已通过 GitLab API 创建/更新对应 Release（含完整描述）
```

**全部通过才能进入下一阶段。**

### 阶段六：格式预检

- frontmatter 字段完整性（name + description）
- description 长度 ≤ 1024
- name 命名规范（小写字母+数字+连字符）
- 正文行数 ≤ 500

### 阶段七：版本管理与发布

> **HARD-GATE：未创建/更新 tag 和 release 的版本视为未发布。自检清单第 19-20 项未通过前，禁止向用户报告"发布完成"。**

> **便携 Git**：发布命令中 `git` → `& $env:QODER_GIT`；须先通过步骤 0 skill-kit 检查。

**步骤 5：确认提交方式**

使用 AskUserQuestion 工具确认用户的 GitLab 角色和提交方式：

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
git -C "<repo_path>" add skills/<domain>/<skill-name>/
git -C "<repo_path>" commit -m "Update <skill-name> to v<version>: <change_summary>"

# 3. 推送分支
git -C "<repo_path>" push origin "feature/<skill-name>-v<version>"

# 4. 创建 Merge Request（GitLab API）
curl -s -X POST "https://<host>/api/v4/projects/<project_id>/merge_requests" \
  -H "PRIVATE-TOKEN: <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "source_branch": "feature/<skill-name>-v<version>",
    "target_branch": "main",
    "title": "Update <skill-name> to v<version>",
    "description": "## 变更概要\n\n- 变更类型: <change_summary>\n- 新版本: v<version>\n\n## 自检清单结果\n\n- [x] 1. SKILL.md frontmatter\n- [x] 2. name 与目录名一致\n...\n- [x] 13. EnterSpecMode/ExitSpecMode\n- [x] 14. 能力边界章节\n- [x] 15. 依赖清单章节\n- [x] 16. 前置依赖检查（如适用）\n- [x] 17. tag 已创建/更新\n- [x] 18. Release 已创建/更新\n\n## 质量指标\n\n- Gotchas: X 条\n- Eval 用例: X 条\n- 触发测试: X 条"
  }'
```

等待 CI 门禁自动运行。CI 通过后通知审核人进行人工审核。Maintainer 审核通过并合并 MR 后，切回 main 创建 Tag：

```bash
# 5. 切回 main 并拉取最新代码
git -C "<repo_path>" checkout main
git -C "<repo_path>" pull origin main
```

**路径 B：直接 push（仅 Maintainer）**

```bash
# 1. 提交并推送
git -C "<repo_path>" add skills/<domain>/<skill-name>/
git -C "<repo_path>" commit -m "Update <skill-name> to v<version>: <change_summary>"
git -C "<repo_path>" push origin main
```

> **注意**：路径 B 仅限 Maintainer 角色。main 分支已设为受保护，Developer 直接 push 会被 403 拒绝。选择"不确定"角色的用户默认走路径 A。

**步骤 6：创建 Tag（两条路径都执行）**

```bash
git -C "<repo_path>" tag "<skill-name>/v<version>"
git -C "<repo_path>" push origin "<skill-name>/v<version>"
```

**步骤 7：创建 Release（GitLab API）**

Release 描述**必须使用中文**，禁止使用 "Initial release" 等英文简单描述。description 必须包含：技能描述、核心功能、质量指标（Gotchas/Eval/触发测试数量）、关键 Gotchas、拉取方式（Zip 下载链接 + Sparse Checkout 命令）、技能路径。

```bash
curl -s -X POST "https://<host>/api/v4/projects/<project_id>/releases" \
  -H "PRIVATE-TOKEN: <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "tag_name": "<skill-name>/v<version>",
    "name": "<skill-name> v<version>",
    "description": "<release_description>"
  }'
```

**步骤 8：上传 Zip 附件到 Release**

将 skill 目录打包为 zip 并上传到 Release Assets，供用户直接下载（无需 git）。

```bash
# 1. 打包 skill 目录
cd "<repo_path>" && zip -r "<skill-name>-v<version>.zip" "skills/<domain>/<skill-name>/"

# 2. 上传 zip 到 GitLab（响应中的 url 字段用于下一步）
curl -s -X POST "https://<host>/api/v4/projects/<project_id>/uploads" \
  -H "PRIVATE-TOKEN: <token>" \
  -F "file=@<skill-name>-v<version>.zip"

# 3. 链接到 Release（upload_url 从上一步响应获取）
curl -s -X POST "https://<host>/api/v4/projects/<project_id>/releases/<skill-name>%2Fv<version>/assets/links" \
  -H "PRIVATE-TOKEN: <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "<skill-name>-v<version>.zip",
    "url": "https://<host><upload_url>",
    "link_type": "other"
  }'

# 4. 清理临时 zip
rm -f "<skill-name>-v<version>.zip"
```

**步骤 9：删除旧版本 Release**

发布新版本 Release 后，必须删除旧版本的 Release，确保 Release 页面只展示最新版本。

```bash
curl -s -X DELETE "https://<host>/api/v4/projects/<project_id>/releases/<skill-name>%2Fv<old_version>" \
  -H "PRIVATE-TOKEN: <token>"
```

> **注意**：此操作仅删除 Release 元数据，不会删除 git tag。tag 保留在仓库中作为历史记录。

**步骤 10：更新 README.md、CATALOG.md 和 docs/skill-browser.md**

同步更新仓库中的管理文档，确保版本号、Release 链接、Zip 下载链接三者一致：

| 文档 | 更新内容 |
|------|---------|
| README.md | 已上架 Skill 表格：版本号、Release 链接、Zip 下载链接 |
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

**步骤 11：发布后汇报**

完成所有发布步骤后，必须向用户汇报以下信息：

| 汇报项 | 内容 |
|--------|------|
| 新版本号 | `<skill-name> v<version>` |
| Release 链接 | `https://<host>/<project_path>/-/releases/<skill-name>%2Fv<version>` |
| Zip 附件上传结果 | 上传成功/失败，附件下载链接 |
| 旧 Release 删除结果 | 列出已删除的旧版本，标注成功/失败 |
| README.md 同步状态 | 已更新 / 未更新 |
| CATALOG.md 同步状态 | 已更新 / 未更新 |
| docs/skill-browser.md 同步状态 | 已更新 / 未更新 |
| 自检清单 | 18/18 通过 |

**汇报格式示例：**

```
<skill-name> v<version> 发布完成

- Release: https://epfa-gitlab.csvw.com/ecc-2/qoder-skills/-/releases/<skill-name>%2Fv<version>
- Zip 附件: <skill-name>-v<version>.zip 已上传 ✓
- 旧 Release 删除:
  - <skill-name>/v<old_version> 已删除 ✓
  - （如无旧版本）首次发布，无旧 Release 需删除
- README.md 已同步 ✓
- CATALOG.md 已同步 ✓
- docs/skill-browser.md 已同步 ✓
- 自检清单: 18/18 通过
```

> **旧 Release 删除汇报是必选项**：无论旧 Release 是否成功删除，都必须在汇报中列出。删除失败时标注失败原因（如 403 权限错误），并提示用户检查 token 权限。

### 阶段八：异常处理

| 异常场景 | 处理方式 |
|---------|---------|
| 自检清单有项不通过 | 返回阶段四修正，禁止跳过 |
| 正文超过 500 行 | 拆分到 references/，重新自检 |
| 版本号判定不确定 | 按最保守规则处理（就高不就低） |
| 直接 push 被 403 拒绝 | main 分支受保护，引导用户走路径 A（PR 流程） |
| MR 创建失败（API 错误） | 检查 source_branch 是否已推送、token 权限，重试 |
| Release 创建失败 | 检查 tag 是否已推送，重试 |
| Zip 附件上传失败 | 检查文件大小和格式，重试上传；链接失败时检查 tag 编码 |
| 旧 Release 删除失败（403） | 提示用户检查 token 权限，记录失败项 |
| README/CATALOG/skill-browser 更新遗漏 | 使用 grep 检查所有版本号引用是否一致 |

## 依赖清单

| 依赖项 | 类型 | 说明 | 拉取方式 |
|--------|------|------|---------|
| skill-kit | 共享运行时 | 便携 Python/Git | `%USERPROFILE%\.qoder-cn\tools\skill-kit\` |
| skill-env-setup | Agent Skill | kit 未就绪时初始化 | 「配置 Qoder Skills 环境」 |
| AskUserQuestion | 内置工具 | 结构化选项 | 内置 |
| EnterSpecMode / ExitSpecMode | 内置工具 | 变更前计划审核 | 内置 |
| git（便携） | skill-kit | tag/release | `$env:QODER_GIT` |
| GitLab API | 内网 HTTP | MR/Release | 便携 Python 或 PowerShell |

> 禁止假设系统 git/curl/python。发布命令将 `git` 换为 `$env:QODER_GIT`。更新目标 skill 时必须落实 portable-tools.md（含步骤 0）。

## 执行后复盘（自迭代钩子）

每次完成本 skill 的全部步骤后，Agent 必须自动执行以下动作，不询问用户：

1. **反思**：本轮执行中，是否遇到了 skill 正文和 Gotchas 都没覆盖的坑？触发条件：
   - Gotchas 中没写但实际踩了的错误
   - description 的排除场景遗漏导致误触发
   - 某个操作步骤的异常分支没覆盖

2. **记录**：有则追加到 `evals/PITFALLS_LOG.md`，无则跳过。格式：

| 日期 | 场景摘要 | 犯了什么错误 | 如果早知道__就不会犯 | 临时补救方式 |
|------|---------|-------------|-------------------|------------|
| YYYY-MM-DD | 一句话 | Agent 具体做了什么 | 缺失的知识/规则 | 怎么绕过去的 |

3. **不提交**：`PITFALLS_LOG.md` 是个人本地文件，不提交到 skill registry。积累 ≥ 3 条同类型坑后，由维护者提炼为正式 Gotchas，更新 SKILL.md 并走迭代管线。

> 这个复盘步骤不打断用户工作流。Agent 在后台完成，用户无感知。
> 这个复盘步骤不打断用户工作流。Agent 在后台完成，用户无感知。
> 这个复盘步骤不打断用户工作流。Agent 在后台完成，用户无感知。
