# my-skills

> 马捷个人 Agent Skill 统一云端仓库
> 一套技能、一种目录结构，任意 Agent 环境按需安装

## 仓库定位

本仓库是个人 AI Agent Skill 的**唯一**归档与分发节点：所有 skill 共用同一套域分类、注册表与发布 zip，不按编辑器或运行时拆分。

| 安装方式 | 说明 |
|----------|------|
| **源码目录** | 克隆或 sparse-checkout `skills/<域>/<skill-name>/` 到本机 skill 目录 |
| **离线 zip** | 下载 `assets/<skill>-vX.Y.Z.zip` 解压到 skill 安装根目录 |
| **整库引用** | Agent 配置中引用 `github.com/mjnn/my-skills` 子路径 |

常见 skill 安装根目录（按环境自动识别，无需在仓库内区分）：

- 项目级：`<项目>/.cursor/skills/` 或 `<项目>/.qoder/skills/`
- 用户级：`~/.cursor/skills/`、`~/.qoder-cn/skills/` 等

## 目录结构

```
my-skills/
├── README.md
├── CATALOG.md
├── registry.json
├── AGENTS.md
├── CONTRIBUTING.md
├── assets/
├── docs/
├── skills/
│   ├── platform-engineering/
│   ├── general-office/
│   ├── development-testing/
│   └── project-management/
└── templates/
```

## 已收录 Skill

<!-- SKILLS_TABLE_START -->
| Skill | 域 | 说明 |
|-------|-----|------|
| [ask-before-act](skills/platform-engineering/ask-before-act) | platform-engineering | 当Agent不确定用户诉求、任务细节或执行方向时触发。使用AskUserQuestion工具向用户提出结构化问题，明确用户意图后再继续执行。适用于：任务目标模糊、需求描述不完整、存在多种理解可能、需要… |
| [ecs-connect](skills/platform-engineering/ecs-connect) | platform-engineering | Connects to the user's Alibaba Cloud ECS via SSH (alias ecs-main, KeyForAgent key pair), verifies co… |
| [ecs-github-delivery-ops](skills/platform-engineering/ecs-github-delivery-ops) | platform-engineering | Connects to the user's ECS via SSH, deploys services with Docker Compose, configures Nginx reverse-p… |
| [feishu-bitable-ops](skills/general-office/feishu-bitable-ops) | general-office | 飞书开放平台多维表格 (Bitable) API 操作：首次初始化引导配置开放平台 App ID/Secret、 新建 Base 后自动授予用户可管理权限、操作他人表格的协作者配置、用户车 VIN 过… |
| [github-connect](skills/platform-engineering/github-connect) | platform-engineering | Verifies GitHub connectivity on Windows: Git CLI install, HTTPS/SSH network checks, SSH key setup (i… |
| [session-to-rules](skills/platform-engineering/session-to-rules) | platform-engineering | Extracts durable knowledge from the current workspace project only into that project's .cursor/rules… |
| [skill-bootstrap](skills/platform-engineering/skill-bootstrap) | platform-engineering | 当用户要求新建、创建、编写或做一个 Agent Skill 时触发。引导作者按 7 门禁质量标准从零创建高质量 Agent Skill，覆盖领域确认、Gotchas 提炼、正文+eval 交替编写、自… |
| [skill-publish](skills/platform-engineering/skill-publish) | platform-engineering | 将本地高可用 Skill 发布到 mjnn/my-skills 云端仓库。当用户说「发布这个skill」「上传到my-skills」「入库」「推送到skill仓库」「把这个skill传到云端」时触发。… |
| [vehicle-tracking-design](skills/development-testing/vehicle-tracking-design) | development-testing | 为车端应用生成完整埋点设计方案。基于功能 SPEC（DOCX/PDF/Markdown）和可选 UE 设计 PDF，输出含四大 Sheet 的标准化 Excel（事件、用户路径、转化漏斗、关联埋点）。… |

<!-- SKILLS_TABLE_END -->

## 文档

- [技能浏览器](docs/skill-browser.md)
- [生命周期规范](docs/lifecycle-spec.md)
- [目录注册表](CATALOG.md)

---

*维护者：马捷（mjnn）*
