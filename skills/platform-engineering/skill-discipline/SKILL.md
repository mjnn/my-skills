---
name: skill-discipline
description: 会话开始时、接到任何任务时、以及想跳过流程直接动手时，必须先过此 skill。它不干具体活，只确保你不会绕过其他 skill。不适用于：用户明确说"直接做""不用走流程"、纯聊天/寒暄、系统级查询（如查看当前时间/天气）。
---

<EXTREMELY-IMPORTANT>
如果你觉得某个 skill 有哪怕 1% 的可能性适用于当前要做的事，你必须调用那个 skill。

SKILL 适用就必须用。这不是建议，不是可选项。不存在"这次算了"。

这是不可协商的纪律。你没有选择权。别跟自己讲道理绕过去。
</EXTREMELY-IMPORTANT>

## 指令优先级

1. **用户的明确指令** — 最高优先级
2. **已安装的 skill** — 覆盖默认行为
3. **默认系统行为** — 最低优先级

如果用户说"别走流程直接做"，听用户的。用户掌控一切。

<HARD-GATE>
1. 在执行任何任务前，必须先检查已安装的 skill 列表中是否有适用的 skill。
2. 如果存在 1% 的可能性某个 skill 适用，必须调用该 skill。
3. 用户明确说"直接做""不用走流程"时，可以跳过检查。
4. 不确定某个 skill 是否适用时，使用 AskUserQuestion 工具向用户确认。
</HARD-GATE>

## 能力边界

### 本技能负责
- 在会话开始时、接到任何任务时检查是否有适用的 skill 需要触发
- 防止 Agent 跳过流程直接动手执行
- 引导 Agent 按正确的 skill 优先级顺序调用

### 本技能不负责
- 具体任务的执行 → 由对应的执行型 skill 负责（如 gitlab-repo-upload、svw-ppt-generator 等）
- 需求梳理 → 使用 **requirement-briefing**
- 任务规划 → 使用 **writing-plans**
- 最终验证 → 使用 **verification-before-completion**

## 依赖清单

| 依赖项 | 类型 | 说明 | 拉取方式 |
|--------|------|------|---------|
| skill-kit | 共享运行时 | 便携 Python/Git；由 skill-env-setup 安装 | `%USERPROFILE%\.qoder-cn\tools\skill-kit\` |
| skill-env-setup | Agent Skill | 环境未就绪时初始化 skill-kit | 对用户说「配置 Qoder Skills 环境」 |
| AskUserQuestion | 内置工具 | 不确定 skill 适用性时向用户确认 | 内置，无需拉取 |

## 核心规则

**在任何回应或行动之前，先过 skill 检查。** 哪怕你 1% 觉得可能适用，先调用那个 skill 看看。调用了发现不适用可以不用。

## 防自欺清单

以下想法出现时立刻停下来，去调用对应 skill：

| 想法 | 现实 | 该调用的 skill |
|------|------|---------------|
| "这个太简单了不需要设计" | 简单的任务最容易被未验证的假设坑 | requirement-briefing |
| "我先看看文件再说" | skill 告诉你该怎么看 | requirement-briefing |
| "我大概记得那个 skill 的内容" | skill 会更新，读最新版 | 对应的 skill |
| "先做一步再考虑流程" | 第一步就决定了方向 | requirement-briefing |
| "这不是正式任务，随便弄弄" | 随便弄弄的后果往往要花更多时间修 | 对应的 skill |
| "用户很急，直接出结果" | 做错比做慢更浪费时间 | requirement-briefing |
| "要跑脚本但 skill-kit 没装" | 内网零预装环境必须先初始化 | **skill-env-setup** |
| "这个任务我做过很多次了" | 每次都可能有细微差异 | 对应的 skill |
| "感觉用 skill 是大材小用" | 小事情用流程不会错，不用才会 | 对应的 skill |
| "我先收集信息再决定" | skill 告诉你该收集什么信息 | requirement-briefing |
| "这一步我确定没问题" | 确定的错觉是 bug 的温床 | verification-before-completion |

## Gotchas

1. **"这个 skill 我记得内容"** — skill 会更新，必须调用最新版。Agent 常犯的错误是凭记忆执行，导致遗漏新规则。
2. **多个 skill 适用时只挑一个** — 可能都适用，都要调用。Agent 常犯的错误是选一个最相关的，遗漏其他必要的 skill。
3. **"用户很急，直接出结果"** — 做错比做慢更浪费时间。Agent 常在用户催促下跳过流程，导致返工。
4. **任务中途才想起检查 skill** — 应该在任何行动之前就检查，不是做到一半才想起。Agent 常在执行一步后才想起来检查。
5. **"这不是正式任务，随便弄弄"** — 随便弄的后果往往要花更多时间修。Agent 常低估"小修小补"的复杂度。

## Skill 优先级

多个 skill 可能适用时，按这个顺序：

1. **流程型 skill 优先**（requirement-briefing, skill-discipline）— 决定怎么做
2. **规划型 skill 其次**（writing-plans）— 拆解怎么做
3. **执行型 skill 再次**（subagent-driven-development）— 具体做
4. **验证型 skill 最后**（verification-before-completion）— 确认做对了

## 执行后复盘（自迭代钩子）

每次完成本 skill 的全部步骤后，Agent 必须自动执行以下动作，不询问用户：

1. **反思**：本轮执行中，是否有应该触发的 skill 被遗漏？是否有不应该触发的 skill 被误触发？

2. **记录**：有则追加到 `evals/PITFALLS_LOG.md`，无则跳过。格式：

| 日期 | 场景摘要 | 犯了什么错误 | 如果早知道__就不会犯 | 临时补救方式 |
|------|---------|-------------|-------------------|------------|
| YYYY-MM-DD | 一句话 | Agent 具体做了什么 | 缺失的知识/规则 | 怎么绕过去的 |

3. **不提交**：`PITFALLS_LOG.md` 是个人本地文件，不提交到 skill registry。积累 >= 3 条同类型坑后，由维护者提炼为正式 Gotchas，更新 SKILL.md 并走迭代管线。
