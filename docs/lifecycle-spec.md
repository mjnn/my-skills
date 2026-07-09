# Skill Hub 生命周期管理方案

> 设计文档 | 2026-06-10 | 马捷

## 概述

在上汽大众电子电器研发部门内部搭建一个 Skill Hub（内部技能市场），核心定位是跨团队的 Skill 发现与复用，通过多门禁质量管线保证所有上架 Skill 的可靠性。

## 一、整体流程架构

```
[提案] → [起草] → [门禁1:自检] → [提交] → [门禁2:格式] → [门禁3:触发] → [门禁4:Eval] → [门禁5:人工审核] → [门禁6:安全] → [发布] → [运维]
```

7 道门禁，每道是阻断性的——不通过则打回，不存在"警告但放过"。

## 二、门禁详细标准

### 门禁 1：自检清单

- **时机**：提交前，作者自查
- **载体**：`SELF_CHECK.md`，10 条 checklist，全部勾选才能提交
- **内容**：
  1. SKILL.md 存在且 frontmatter 完整
  2. name 命名规范（小写字母+数字+连字符，与目录名一致）
  3. description 使用了命令式（"Use when..."），含触发关键词和不应触发边界
  4. 正文包含具体的操作步骤
  5. 包含至少 5 条 Gotchas（基于真实经验）
  6. evals/evals.json 存在且含 >= 3 条用例
  7. 每条用例有 prompt + expected_output + assertions（>= 2 条/用例）
  8. evals/eval_queries.json 存在且含 >= 16 条（含 >= 4 条 near-miss）
  9. SKILL.md 正文 <= 500 行（超出部分已拆分到 references/）
  10. 不含硬编码的密钥、密码、Token 或内网 IP

### 门禁 2：格式校验

- **时机**：提交后，CI 自动运行
- **引擎**：基于 skills-ref validate
- **检查项**：frontmatter 字段完整性、name 规范、description 长度 <= 1024、非标准字段清理、scripts/ 目录须含环境预检、references/ 须有触发条件指令
- **阻断**：任何一条失败即打回

### 门禁 3：触发测试

- **时机**：格式通过后，CI 自动运行
- **输入**：`evals/eval_queries.json`（>= 16 条，含 >= 4 条 near-miss）
- **方法**：每条 query 独立运行 3 轮（新上下文）
- **通过标准**：
  - should-trigger 触发率 >= 80%
  - should-not-trigger 误触率 <= 20%
  - near-miss 必须 0 误判
- **阻断**：不达标打回，附带失败 case 列表

### 门禁 4：行为 Eval

- **时机**：触发测试通过后，CI 自动运行
- **输入**：`evals/evals.json`（>= 3 条用例）
- **方法**：每条用例跑 with-skill + without-skill 双轨对比，各 3 轮
- **通过标准**：
  - pass@3 >= 90%
  - delta（with - without pass_rate）>= 0.3
- **软性警告**（不阻断）：delta < 0.3 但 >= 0、delta < 0
- **阻断**：不达标打回 + grading 报告

### 门禁 5：人工审核

- **时机**：自动门禁全部通过后
- **要求**：至少 1 人审核（核心域 2 人），审核人需是该域有经验者，不能是作者
- **评分**：5 维度各 0-2 分（Gotchas 质量、指令清晰度、边界处理、内容纯度、可维护性）
- **通过标准**：总分 >= 7/10，单项无 0 分
- **决策**：通过/要求修改/拒绝

### 门禁 6：安全审查

- **时机**：人工审核通过后
- **自动扫描**（CI 运行）：
  - P0 阻断：硬编码密钥/Token、内网地址、危险命令（rm -rf /、curl | bash 等）、明文密码
  - P1 警告：外部网络请求、无 --dry-run 的写操作、未锁定的依赖版本
- **人工复核**：P1 项逐一确认，P0 不允许豁免
- **阻断**：P0 命中直接打回

## 三、发布与运维

### 发布

- **触发**：7 道门禁全部通过
- **版本号**：`{major}.{minor}.{patch}`，语义化版本
- **动作**：Git tag -> 更新 CATALOG.md -> 生成 changelog -> 通知订阅者

### 运维

- **使用统计**：安装次数、触发率、失败率（展示在 catalog 详情页）
- **问题反馈**：catalog 详情页提交 issue，同类型 >= 2 次触发迭代
- **迭代更新**：走简化管线（起草->自检->格式->触发->eval->审核），eval 必须与上一版本对比且 delta 为正
- **废弃标注**：6 月无更新+3 月无安装 / 被覆盖 / 依赖停维护 -> [DEPRECATED] -> 12 月后移入 archive/

## 四、目录结构

```
skill-hub/                          # Git 仓库根目录
├── CATALOG.md                      # 所有已发布 skill 的注册表
├── CONTRIBUTING.md                 # 贡献指南（含自检清单模板）
├── ci/
│   ├── format_check.sh             # 门禁 2
│   ├── trigger_test.sh             # 门禁 3
│   ├── behavior_eval.sh            # 门禁 4
│   └── security_scan.sh            # 门禁 6 自动部分
├── templates/
│   ├── SKILL_TEMPLATE.md
│   ├── SELF_CHECK_TEMPLATE.md
│   ├── EVALS_TEMPLATE.json
│   └── EVAL_QUERIES_TEMPLATE.json
├── skills/
│   ├── data-analysis/              # 按功能域分层
│   ├── platform-engineering/
│   └── archive/
└── docs/
    └── lifecycle-spec.md           # 本文件
```

## 五、关键设计决策

1. **CI 是前置基础设施**：门禁 2、3、4、6 全部依赖 CI 环境。CI 必须在第一批 skill 入库前搭建完成。
2. **基础设施无关**：方案不绑定特定 Web 框架或数据库。核心流程全部走 Git + CI。
3. **渐进式采用**：7 道门禁对简单 skill 有简化路径（门禁 1-2 不变，门禁 3-4 的阈值按 skill 复杂度分级可调）。
4. **eval 驱动**：门禁 3-4 直接复用触发测试和行为 eval 方法论，保证所有上架 skill 有量化质量指标。
5. **安全第一**：企业内网场景下，敏感信息泄漏是最高风险。安全门禁放在最后一道（所有质量问题排除后再审安全），但 P0 规则不可豁免。

## 六、补充规则

### 审核人指派

默认由该域 catalog 中最近 3 个月内有过 skill 贡献的人轮值。若该域无人，扩大到部门内任意有相关领域经验的人。审核人不能是作者本人。

### 版本号判定

CI 自动判定的默认规则（人工在 merge 时确认）：
- 仅修改 evals/、gotchas 措辞、references/ 内容 -> **patch**
- 修改 description、新增 gotchas 条目、新增 eval 用例 -> **minor**
- 修改 name（及目录名）、修改核心流程（SKILL.md 正文主体结构）-> **major**

### 触发测试通过标准（精确化）

- 单条 query 通过标准：3 轮平均触发率 >= 50%（即 3 轮中至少 2 轮触发）
- should-trigger 总体通过率：**10 条中 >= 8 条通过**（80% query 级通过率）
- should-not-trigger 总体通过率：**10 条中 <= 2 条误触**（20% query 级误触率）
- near-miss query：必须全部不触发（0 容忍）

### 核心域与个人工具划分（初步）

- **核心域 skill**：catalog 中被 >= 3 个不同项目引用的 skill，或涉及数据管线/安全/基础设施的 skill
- **个人工具 skill**：仅作者本人或单一项目使用的 skill
- 核心域 skill 必须走全部门禁 + 2 人审核；个人工具 skill 可走简化审核（1 人审核，安全门禁可仅自动扫描）

### 格式门禁 frontmatter 白名单

门禁 2 的"非标准字段"规则有一个白名单。以下 HanaAgent 平台必需字段允许留在 frontmatter：
- `default-enabled` -- Agent 加载控制
- `compatibility` -- 平台兼容性声明

被禁止的非标准字段仅限其他 Agent 框架的特有字段（如 `version`、`origin`、`author`、`icon` 等前端渲染/版本号字段），这些必须挪到 metadata 下。

## 七、后续工作（不在本次范围）

- Web 前端（catalog 浏览/搜索/安装/统计仪表盘/审核界面）
- 数据库选型（SQLite 起步，预留 PostgreSQL 接口）
- CI 环境搭建（实际运行门禁 2-6 的脚本和 Agent 实例）
- 域分类体系细化（电子电器研发部门的具体业务域划分）
- 分级策略（核心域 skill vs 个人工具 skill 的差异化门禁要求）
