# Contributing to my-skills

> 马捷个人 Agent Skill 贡献指南

## 提交流程

```
[起草] → [自检] → [PR] → [CI 格式/触发检查] → [合并] → [更新 registry + CATALOG]
```

## 目录结构

```
skills/{domain}/{skill-name}/
├── SKILL.md
├── evals/
│   ├── evals.json
│   └── eval_queries.json
├── references/     # 可选
├── scripts/        # 可选
└── SELF_CHECK.md   # 推荐
```

## 新增 skill 检查清单

1. 域分类正确（见 [CATALOG.md](CATALOG.md)）
2. `name` 与目录名一致
3. `description` 一句话说清触发场景与排除场景
4. 至少 5 条 eval + 16 条触发测试（含 near-miss）
5. 无硬编码密钥 / Token
6. 更新 `registry.json` 与 `CATALOG.md`

## 版本号

- **patch**：eval、措辞、references 微调
- **minor**：description、新增 gotchas / eval
- **major**：核心流程或 `name` 变更

## PR 说明

请写明：skill 用途、与已有 skill 的差异、自测结果。
