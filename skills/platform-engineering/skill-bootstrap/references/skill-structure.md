# SKILL.md 详细结构规范

> Read this when: 第二步编写正文时

## 强制结构

```markdown
---
name: {skill-name}
description: {触发场景和排除场景}
---

# {技能标题}

{一句话定位}

<HARD-GATE>
{禁止在批准前执行的操作}
{必须使用 AskUserQuestion 的约束}
{必须使用 EnterSpecMode/ExitSpecMode 的约束}
</HARD-GATE>

## Gotchas

{>= 5 条}

## 流程

{按顺序的操作步骤}

## references

- `references/{file}.md`：{触发条件}

## 执行后复盘（自迭代钩子）

{自动反思 + 记录 PITFALLS_LOG.md}
```

## frontmatter 白名单

允许保留的字段：
- `name` — 必须，与目录名一致
- `description` — 必须，含触发 + 排除场景
- `default-enabled` — Agent 加载控制
- `compatibility` — 平台兼容性声明

禁止保留的字段（必须挪到 metadata）：
- `version`、`origin`、`author`、`icon` 等前端渲染/版本号字段

## 正文长度控制

- 软限制：300 行（提醒拆分）
- 硬限制：500 行（自检不过）
- 拆分方式：参考资料、字段说明、决策表 → references/

## 条件加载指令格式

正确：
```markdown
## references

- `references/gitignore-templates.md`：在步骤 2 创建 .gitignore 时读取
- `references/api-docs.md`：在需要调用 API 时读取
```

错误（没有条件）：
```markdown
## references

- `references/something.md`
```
