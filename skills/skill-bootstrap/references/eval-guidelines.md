# Eval 用例设计指南

> Read this when: 第二步设计 eval 资产时

## evals.json 设计原则

### 用例类型分布

| 类型 | 数量 | 说明 |
|------|------|------|
| 正常路径 | >= 2 | 最核心、最常见的使用场景 |
| 异常路径 | >= 1 | 常见错误输入或边界条件 |
| 边界场景 | >= 1 | 极限情况、特殊情况 |
| Near-miss | >= 1 | 共享关键词但不该触发 |

### assertions 设计

每条 assertion 必须是可机械判定的：

```json
// 好的 assertion（可机械判定）
"assertions": [
  "在 git add 之前创建了 .gitignore",
  ".gitignore 中包含 .env 和 venv/",
  "使用了 AskUserQuestion 工具收集认证方式"
]

// 坏的 assertion（主观不可判定）
"assertions": [
  "代码质量很好",
  "用户体验良好",
  "逻辑清晰"
]
```

### expected_output 写法

- 描述 Agent 应该**做什么**，而不是**不做什么**
- 包含关键动作和顺序
- 提及必须使用的工具（AskUserQuestion、EnterSpecMode 等）

## eval_queries.json 设计原则

### near-miss 设计方法

1. 找出 skill 的触发关键词（如"创建"、"skill"、"GitLab"）
2. 构造共享这些关键词但意图不同的查询
3. 确保 near-miss 查询在语义上接近但不相同

示例：
- 触发：`帮我创建一个处理 PDF 的 skill`
- near-miss：`帮我评估一个 PDF 处理 skill 的设计`
  - 共享关键词：PDF、skill
  - 不同意图：评估 vs 创建
  - should_trigger: false
