# my-skills

> 马捷（mjnn）个人 Agent Skill 云端仓库  
> 质量门控 · 域分类 · 宁缺毋滥

## 这是什么

本仓库收录**个人维护**的高可用 Agent Skill，作为统一归档与分发节点。所有 skill 共用一套目录结构与注册表，**不按编辑器或运行时拆分**，克隆到任意 Agent 的 skill 目录即可使用。

**不包含**企业内网 Qoder Skills Hub 中的 skill（如 skill-env-setup、skill-kit、svw-ppt-generator 等）。那些 skill 由企业 GitLab 仓库单独分发；本仓库仅存放个人场景下验证过的 skill。

## 收录范围（9 个）

| 域 | 数量 | 侧重 |
|----|------|------|
| [platform-engineering](skills/platform-engineering/) | 7 | 基础设施连通、Skill 工程化、会话沉淀 |
| [general-office](skills/general-office/) | 1 | 飞书多维表格办公自动化 |
| [development-testing](skills/development-testing/) | 1 | 车端埋点方案设计 |

**平台工程** — 不确定先问（ask-before-act）、阿里云 ECS / GitHub 连通与交付（ecs-connect、github-connect、ecs-github-delivery-ops）、Skill 创建与发布（skill-bootstrap、skill-publish）、项目规则沉淀（session-to-rules）

**通用办公** — 飞书 Bitable API 全流程（feishu-bitable-ops）

**开发测试** — 基于 SPEC/UE 生成车端埋点 Excel 与校验报告（vehicle-tracking-design）

## 如何安装

任选一种方式，将 skill 放到本机 **skill 安装根目录**（由 Agent 环境决定，例如项目 `.cursor/skills/` 或用户 `~/.cursor/skills/`）：

**方式一：拷贝源码目录（推荐）**

```bash
git clone https://github.com/mjnn/my-skills.git
cp -r my-skills/skills/<域>/<skill-name>/ <skill-root>/
```

**方式二：Sparse Checkout（只拉一个 skill）**

```bash
git clone --filter=blob:none --sparse https://github.com/mjnn/my-skills.git
cd my-skills
git sparse-checkout set skills/platform-engineering/github-connect
cp -r skills/platform-engineering/github-connect <skill-root>/
```

**方式三：离线 zip**

从 [assets/](assets/) 下载 `<skill-name>-vX.Y.Z.zip`，解压到 `<skill-root>/`。

## 收录标准

| 维度 | 要求 |
|------|------|
| 命名 | 小写 + 连字符，目录名与 `SKILL.md` 的 `name` 一致 |
| 质量 | `SKILL.md` 完整 + `evals/` 覆盖 + 至少一次实战验证 |
| 安全 | 无硬编码密钥、无任意命令注入 |
| 边界 | 单一职责，不与已有 skill 高度重叠 |
| 原则 | **宁缺毋滥** — 未达质量门控的不入库 |

## 目录结构

```
my-skills/
├── README.md           # 本文件
├── CATALOG.md          # 人类可读注册表
├── registry.json       # 机器可读注册表
├── assets/             # 单 skill 发布 zip
├── docs/               # 技能浏览器、生命周期规范
├── skills/
│   ├── platform-engineering/
│   ├── general-office/
│   └── development-testing/
└── templates/          # 新建 skill 模板
```

## 已收录 Skill

<!-- SKILLS_TABLE_START -->
| Skill | 域 | 说明 |
|-------|-----|------|
| [ask-before-act](skills/platform-engineering/ask-before-act) | platform-engineering | 意图不确定时，用 AskUserQuestion 结构化澄清后再执行。 |
| [ecs-connect](skills/platform-engineering/ecs-connect) | platform-engineering | 阿里云 ECS SSH 连通、密钥配置与只读巡检。 |
| [ecs-github-delivery-ops](skills/platform-engineering/ecs-github-delivery-ops) | platform-engineering | ECS 上 Docker Compose 部署、Nginx 反代、ACR 与 GitHub 交付。 |
| [github-connect](skills/platform-engineering/github-connect) | platform-engineering | Windows 下 GitHub 连通性验证与 SSH/HTTPS 认证配置。 |
| [session-to-rules](skills/platform-engineering/session-to-rules) | platform-engineering | 将当前项目会话沉淀为 `.cursor/rules` 并清理临时产物。 |
| [skill-bootstrap](skills/platform-engineering/skill-bootstrap) | platform-engineering | 按 7 门禁从零创建高质量 Agent Skill。 |
| [skill-publish](skills/platform-engineering/skill-publish) | platform-engineering | 将本地 skill 发布回本仓库并更新 registry。 |
| [feishu-bitable-ops](skills/general-office/feishu-bitable-ops) | general-office | 飞书多维表格 API：配置、CRUD、授权与协作者管理。 |
| [vehicle-tracking-design](skills/development-testing/vehicle-tracking-design) | development-testing | 基于 SPEC/UE 生成车端埋点 Excel 与 UE 校验报告。 |

<!-- SKILLS_TABLE_END -->

## 文档

- [技能浏览器](docs/skill-browser.md) — 分域浏览与安装示例
- [目录注册表](CATALOG.md) — 版本与路径一览
- [贡献指南](CONTRIBUTING.md) — 新增 / 更新 skill 流程
- [生命周期规范](docs/lifecycle-spec.md) — 版本与门禁说明

## 贡献

欢迎 PR。新增 skill 请附功能说明、eval 用例，以及与已有 skill 的差异说明。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

*维护者：马捷（mjnn）*
