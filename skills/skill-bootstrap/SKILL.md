---
name: skill-bootstrap
description: 新建技能时的质量引导与门禁检查。当用户说「新建skill」「创建技能」「写个skill」「做一个技能」「skill模板」「技能引导」或需要按技能质量标准从零创建一个 Agent Skill 时激活。不适用于：修改已有 skill、单纯讨论 skill 设计而不创建、评估第三方 skill、对已有 skill 的独立质量审计（走 skill-audit 流程）、或已完成的 skill 归档管理。
default-enabled: false
---

# 技能引导与质量门禁

> 所属域：`platform-engineering` | 预期位置：`skills/platform-engineering/skill-bootstrap/`

引导作者按 7 门禁质量标准从零创建一个高质量 Agent Skill。走 5 步流程，每一步都是门禁——不通过不进入下一步。

<HARD-GATE>
在完成第三步（自检清单全部通过）之前，禁止将 skill 提交到 skill registry、禁止声称 skill 已就绪、禁止跳过任何门禁步骤。
</HARD-GATE>

## Gotchas

Agent 在引导创建 skill 时会反复犯以下错误：

- **跳过 Gotchas 直接写正文** — 最致命。Gotchas 是 skill 最有价值的部分——Agent 不知道自己的盲区，需要你去想。创建时先让作者列出 3 条曾踩过的坑，再从坑中提炼 Gotchas。
- **eval 用例和正文脱节** — 写完 skill 再补 eval 时，eval 测的往往是理想路径，和正文实际覆盖的场景不一致。创建时必须正文和 eval 交替推进：写完一段正文立刻出一两条 eval。
- **所有内容堆在 SKILL.md** — 正文超过 300 行时提醒拆分（超过 500 行自检查不过），必须把参考资料、字段说明、决策表拆到 references/。不是"超过才拆"，而是在创建时就有意识地分层。
- **description 太泛导致误触发** — "Use when user asks about data" 这种描述会和几十个 skill 重叠。description 必须包含：明确的触发场景关键词、不应触发的边界说明、按实际复杂度而非措辞判断。
- **near-miss 触发测试缺失** — 只测 should-trigger 不测 should-not-trigger，或者 should-not-trigger 里没有 near-miss。near-miss（共享关键词但不该触发的查询）才是考验 description 质量的真正试金石。
- **忘记写"不适用场景"** — description 只有触发条件没有排除条件，导致和其他 skill 冲突时无法裁决。
- **name 和目录名不一致** — SKILL.md 的 name 字段必须和父目录名完全相同。这是格式门禁的硬阻断项。
- **Gotchas 编造而非提炼** — 为了凑数写"记得检查输入""确保输出正确"这种废话 Gotchas。每一条 Gotchas 必须对应一个 Agent 实际会犯的具体错误，且有纠正方案。
- **明知交替推进却允许一次性完稿** — 最隐蔽的坑。即使作者是领域专家，一次性写完所有正文再回头补 eval，必然导致：① eval 覆盖缺口（某些模块根本没用例）、② 正文中"自认为清晰但 eval 揭露歧义"的部分不会被发现。Agent 不能因为"作者说很清楚了"就妥协。唯一的例外：作者单次回复中一次性给出了完整的正文+eval+触发测试（即交替已完成，只是压缩在同一轮对话里），这时走第三步验证即可。如果正文完整但 eval 缺失——必须要求补交后再进入第三步。"你很急""我经验丰富""这个很简单"都不是例外。
- **忘记在创建时预装自迭代钩子** — skill 的质量不是一次性的。如果创建时不在正文末尾加「执行后复盘」章节，这个 skill 的 Gotchas 会永远停留在创建那天的水平——之后的真实踩坑经验全部丢失。每一步都应该让作者的 skill 越用越强，而不是越用越破。第二步 2b 第 5 条是硬性要求。

## 流程

必须按顺序完成以下 5 步（第零至第二步产生产出，第三步汇总验证，第四步最终预检，第五步收官）：

### 第零步：确认领域

1. 确认 skill 所属功能域（从 skill registry 的域分类中选择，或新建一个域）
2. 确认 skill 名称（小写字母+数字+连字符，1-64 字符）
3. 在本地 skill 目录下创建目录结构骨架：
   ```
   {skill-name}/
   ├── SKILL.md          # 待填充
   ├── references/       # 可选
   ├── scripts/          # 可选
   └── evals/
       ├── evals.json          # 待填充
       └── eval_queries.json   # 待填充
   ```

### 第一步：提炼 Gotchas

先不做任何其他事，让作者回忆并写出 3-5 条"Agent 在没有这个 skill 时会犯的具体错误"。再从这些错误中提炼 Gotchas。

每一条 Gotchas 必须满足：
- 描述 Agent 具体会犯什么错误（不是泛泛的"注意质量"）
- 给出纠正方案（Agent 应该怎么做）
- 基于真实经验，不编造

### 第二步：编写正文 + 同步设计 eval 资产

**核心原则：正文、触发测试、eval 用例三者交替推进，不写完正文再补 eval。**

**2a. 交替节奏**

每完成 SKILL.md 的一个模块（frontmatter / HARD-GATE / Gotchas / 某个操作步骤 / 异常处理），立刻做两件事：
- 出 1-2 条 eval 用例草稿（追加到 evals.json）
- 出 2-3 条触发测试草稿（追加到 eval_queries.json）

**交替是不可能妥协的硬约束。** 如果作者试图一次性口述完所有正文但不提供对应 eval——明确拒绝进入第三步，指出具体缺失了哪些模块的 eval 覆盖。如果作者单轮回复中同时给出了完整的正文+eval+触发测试（交替已在同一轮中完成），正常进入第三步。除此之外没有例外。

**2b. SKILL.md 编写规范**

1. **frontmatter**：name（与目录名一致）、description（含触发关键词 + 排除场景）
 注意：目标 Agent 平台的特定 frontmatter 字段（如 `enabled`、`compatibility` 等）是平台必需字段而非非标准字段——它们的规则由目标平台定义，不属于格式门禁的清理范围。
2. **HARD-GATE**：如果 skill 涉及执行动作，必须有禁止在批准前执行的硬门禁
3. **正文**：按"触发条件 → 前置检查 → 操作步骤 → 输出格式 → 异常处理"的结构组织
   - 正文超过 **300 行**时提醒拆分到 references/，超过 **500 行**自检查不过
4. **references/**：条件加载指令（"Read references/xxx.md if ..." 放在正文中，不在 references/ 中藏指令）
5. **执行后自迭代钩子（必装）**：每个 skill 的流程末尾必须包含一个复盘步骤——Agent 每次执行完任务后，自动反思本轮是否遇到了 skill 没覆盖的坑，有则记录到 `evals/PITFALLS_LOG.md`。格式见下方「自迭代钩子规范」。用户零打扰——Agent 自己做，不询问用户。

#### 自迭代钩子规范

每个 skill 正文末尾必须包含以下内容（直接复制到 skill 的 SKILL.md 中）：

```markdown
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
```

**2c. 触发测试同步设计**

在写正文的同时逐步填充 eval_queries.json：
- **should-trigger（≥ 8 条）**：覆盖不同措辞变体、含触发关键词的边界场景
- **should-not-trigger（≥ 8 条，含 ≥ 4 条 near-miss）**：near-miss 必须共享关键词但不该触发
- 每条包含 query + should_trigger（bool）+ reason

**2d. Eval 用例同步设计**

在写正文的同时逐步填充 evals.json：
- **≥ 5 条用例**：覆盖正常路径 + 异常路径 + 边界场景 + near-miss
- 每条包含 prompt + expected_output + assertions（≥ 2 条）
- assertions 必须是可机械判定的（不是"质量很好"这种主观判断）

### 第三步：自检清单

所有产出完成后，逐项核对。**全部通过才能进入第四步。**

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
[ ] 11. 正文末尾包含「执行后复盘（自迭代钩子）」章节（Agent 后台自动记录 PITFALLS_LOG.md）
```

### 第四步：格式预检

在提交前运行本地预检（门禁 2 的离线版）：
- frontmatter 字段完整性（目标平台必需字段如 `enabled`/`compatibility` 等不受非标准字段规则限制，由平台自定义白名单）
- description 长度 ≤ 1024
- name 命名规范
- scripts/ 目录含环境预检（如适用）
- references/ 有触发条件指令（如适用）

### 第五步：产出报告

输出创建完成报告，包含：
- skill 名称、域、预期版本号（v0.1.0）
- 自检清单结果（11/11）
- eval 用例数 + 触发测试数
- 下一步行动：提交到 skill registry → CI 自动运行门禁 2-4 → 人工审核

## 关键原则

- **Gotchas 优先** — 正文可以改，Gotchas 是 skill 的灵魂。创建时先挖 Gotchas
- **正文 eval 交替** — 不分阶段。写完一段正文立刻补 eval，保证覆盖率
- **分层意识** — 创建时就区分"Agent 不知道的信息"（放 SKILL.md）和"Agent 需要时查阅的信息"（放 references/）
- **near-miss 是试金石** — 一条好的 near-miss 比十条 should-trigger 更能证明 description 的质量
- **命令式极简** — "Favor procedures over declarations"。不要教 Agent 什么是 PDF，教它怎么处理 PDF

## 产出规范

### SKILL.md 结构

```markdown
---
name: {skill-name}
description: {触发场景和排除场景}
---

# {技能标题}

{一句话定位}

<HARD-GATE>
{如果 skill 涉及执行动作，必须写禁止在批准前执行}
</HARD-GATE>

## Gotchas

{≥ 5 条，每条对应一个 Agents 会犯的具体错误}

## 流程

{按顺序的操作步骤，含触发条件、前置检查、异常处理}

{正文内容引用 references/ 时必须写条件加载指令}

## {其他必要章节}
```

### evals/evals.json 结构

```json
[
  {
    "id": 1,
    "name": "{用例名称}",
    "prompt": "{用户输入的完整 prompt}",
    "expected_output": "{期望的 Agent 行为描述}",
    "assertions": [
      "{可机械判定的断言 1}",
      "{可机械判定的断言 2}"
    ]
  }
]
```

### evals/eval_queries.json 结构

```json
[
  {
    "query": "{用户输入的查询}",
    "should_trigger": true,
    "reason": "{为什么该触发/不该触发}"
  }
]
```
