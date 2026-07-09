# Contributing to Skill Hub

> 上汽大众电子电器研发部 Skill 贡献指南

## 提交流程

```
[提案] → [起草] → [门禁1:自检] → [提交] → [门禁2:格式] → [门禁3:触发] → [门禁4:Eval] → [门禁5:人工审核] → [门禁6:安全] → [发布] → [运维]
```

## 目录结构规范

```
skills/{domain}/{skill-name}/
├── SKILL.md              # 技能正文（必须）
├── SELF_CHECK.md         # 自检清单（必须）
├── references/           # 参考资料（可选）
└── evals/
    ├── evals.json        # 行为 eval 用例（必须）
    ├── eval_queries.json # 触发测试用例（必须）
    ├── edge_cases.json   # 边界场景（可选）
    ├── grading.json      # 评分结果（CI 产出）
    └── workspace/        # CI 临时目录（.gitignore）
```

## 门禁说明

### 门禁 1：自检清单（提交前，作者自查）

见 [SELF_CHECK_TEMPLATE.md](templates/SELF_CHECK_TEMPLATE.md)。全部 10 条勾选后才能提交。

### 门禁 2：格式校验（CI 自动）

- frontmatter 字段完整性
- name 规范（小写+连字符，与目录名一致）
- description 长度 ≤ 1024
- 非标准字段清理
- scripts/ 目录含环境预检
- references/ 有条件加载指令

### 门禁 3：触发测试（CI 自动）

- should-trigger 触发率 ≥ 80%
- should-not-trigger 误触率 ≤ 20%
- near-miss 必须 0 误判

### 门禁 4：行为 Eval（CI 自动）

- pass@3 ≥ 90%
- delta（with − without）≥ 0.3

### 门禁 5：人工审核

- 至少 1 人审核（核心域 2 人）
- 5 维度评分（Gotchas 质量、指令清晰度、边界处理、内容纯度、可维护性）
- 总分 ≥ 7/10，单项无 0 分

### 门禁 6：安全审查

- P0 阻断：硬编码密钥/Token、内网地址、危险命令、明文密码
- P1 警告：外部网络请求、无 --dry-run 的写操作、未锁定依赖

## 版本号规则

CI 自动判定（人工确认）：
- **patch**：仅修改 evals/、gotchas 措辞、references/
- **minor**：修改 description、新增 gotchas、新增 eval 用例
- **major**：修改 name（及目录名）、修改核心流程

## 核心域与个人工具

| 类型 | 门禁要求 | 审核人 |
|------|---------|--------|
| 核心域 skill（≥ 3 项目引用） | 全部门禁 + 2 人审核 | 2 人 |
| 个人工具 skill | 全部门禁 + 1 人审核 | 1 人 |

## 提交 PR 前检查

1. 阅读 [SKILL_TEMPLATE.md](templates/SKILL_TEMPLATE.md)
2. 填写 [SELF_CHECK_TEMPLATE.md](templates/SELF_CHECK_TEMPLATE.md)
3. 运行本地预检：`./ci/format_check.sh skills/{domain}/{skill-name}`
4. 提交 PR，描述中附自检清单结果
