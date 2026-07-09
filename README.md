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
| [separate-employee-extraction](skills/development-testing/separate-employee-extraction) | development-testing | 女娲造人：输入人名/主题/甚至只是模糊需求，自动深度调研→思维框架提炼→生成可运行的人物Skill。 两种入口：(1)明确人名→直接蒸馏 (2)模糊需求→诊断推荐→再蒸馏。 触发词：「造skill」「蒸馏XX」「女娲」「造人」「XX的思维方 |
| [subagent-driven-development](skills/development-testing/subagent-driven-development) | development-testing | 拿到实施计划后，逐任务派出子 Agent 执行，每项完成后审查。适用于任务间相对独立的场景，可自动连续推进无需人工介入。不适用于：任务高度耦合（后面依赖前面的中间产物）、单任务即可完成的简单工作、用户要求逐步确认每个任务结果、没有实施计划的 |
| [vehicle-tracking-design](skills/development-testing/vehicle-tracking-design) | development-testing | 为车端应用生成完整埋点设计方案。基于功能 SPEC（DOCX/PDF/Markdown）和可选 UE 设计 PDF，输出含四大 Sheet 的标准化 Excel（事件、用户路径、转化漏斗、关联埋点）。适用于中控、副驾屏、后排屏、SDS 语音 |
| [verification-before-completion](skills/development-testing/verification-before-completion) | development-testing | 任何任务完成后、向用户报告"做完了"之前，必须用此 skill 做最终验证。防止"看起来好了"就交差的习惯。不适用于：纯聊天/寒暄、用户明确说"不用验证"、正在进行中的中间步骤（应在最终完成后验证）、用户说"先这样"表示暂不需要完美交付的场 |
| [xuehaiqiang-perspective](skills/development-testing/xuehaiqiang-perspective) | development-testing | 以薛海强（上汽大众车联网数据采集）视角做方案评审与决策参考。基于40+份SVW工作交接文档及1559封发送邮件提炼7个心智模型、10条决策启发式与表达风格。 当用户提到「薛海强会怎么看」「动采/埋点/VDU」「车联网合规」「数据采集方案」「 |
| [feishu-bitable-ops](skills/general-office/feishu-bitable-ops) | general-office | 飞书开放平台多维表格 (Bitable) API 操作：首次初始化引导配置开放平台 App ID/Secret、 新建 Base 后自动授予用户可管理权限、操作他人表格的协作者配置、用户车 VIN 过筛。 Use when the user |
| [svw-ppt-generator](skills/general-office/svw-ppt-generator) | general-office | 当用户需要生成遵循"总分总、由浅入深"结构化叙事框架的PPT时触发。适用于项目汇报、进度总结、方案评审等工作场景。基于内置标准模板，通过对话式引导完成信息收集、文案确认、排版设计、图表绘制，最终生成统一布局的PPT。不适用于：仅需修改现有P |
| [ask-before-act](skills/platform-engineering/ask-before-act) | platform-engineering | 当Agent不确定用户诉求、任务细节或执行方向时触发。使用AskUserQuestion工具向用户提出结构化问题，明确用户意图后再继续执行。适用于：任务目标模糊、需求描述不完整、存在多种理解可能、需要确认优先级或偏好等场景。不适用于：用户意 |
| [ecs-connect](skills/platform-engineering/ecs-connect) | platform-engineering | Connects to the user's Alibaba Cloud ECS via SSH (alias ecs-main, KeyForAgent key pair), verifies connectivity, and runs |
| [ecs-github-delivery-ops](skills/platform-engineering/ecs-github-delivery-ops) | platform-engineering | Connects to the user's ECS via SSH, deploys services with Docker Compose, configures Nginx reverse-proxy URL paths, and  |
| [github-connect](skills/platform-engineering/github-connect) | platform-engineering | Verifies GitHub connectivity on Windows: Git CLI install, HTTPS/SSH network checks, SSH key setup (id_ed25519_github), s |
| [gitlab-repo-upload](skills/platform-engineering/gitlab-repo-upload) | platform-engineering | 当用户要求将本地项目、代码或文件夹上传/推送到 GitLab 仓库时触发。涵盖 git init、.gitignore 配置、remote add、commit、push 全流程，处理企业内网自签名 SSL 证书和 token 认证等常见障 |
| [local-skill-runtime](skills/platform-engineering/local-skill-runtime) | platform-engineering | 当用户要求检查、诊断、修复或调优本机已安装的 Qoder Skills 运行环境（skill-kit、vendor 链接、Hub 版本）时触发。适用于日常「把设备调到最佳状态」：复检便携 Python/Git、扫描 %USERPROFILE |
| [session-to-rules](skills/platform-engineering/session-to-rules) | platform-engineering | Extracts durable knowledge from the current workspace project only into that project's .cursor/rules/ as .mdc files (nev |
| [skill-bootstrap](skills/platform-engineering/skill-bootstrap) | platform-engineering | 当用户要求新建、创建、编写或做一个 Agent Skill 时触发。引导作者按 7 门禁质量标准从零创建高质量 Agent Skill，覆盖领域确认、Gotchas 提炼、正文+eval 交替编写、自检清单、格式预检、产出报告全链路。不适用 |
| [skill-discipline](skills/platform-engineering/skill-discipline) | platform-engineering | 会话开始时、接到任何任务时、以及想跳过流程直接动手时，必须先过此 skill。它不干具体活，只确保你不会绕过其他 skill。不适用于：用户明确说"直接做""不用走流程"、纯聊天/寒暄、系统级查询（如查看当前时间/天气）。 |
| [skill-env-setup](skills/platform-engineering/skill-env-setup) | platform-engineering | 当用户首次配置 Qoder Skills 环境、初始化 skill 安装目录、检测内网零预装依赖与 GitLab 连通性时触发。默认先安装 skill-kit 便携工具链（Python/Git/7za，不假设系统已装），再将初始化技能包全部 |
| [skill-hub-management](skills/platform-engineering/skill-hub-management) | platform-engineering | 管理 Qoder Skills Hub 仓库本身：一致性检查、新技能注册、多文档同步、本地安装。 Use when the user mentions 技能仓库管理、一致性检查、注册新技能、同步文档、skills 目录和 README 不一 |
| [skill-kit](skills/platform-engineering/skill-kit) | platform-engineering | 当 skill 需要 Python/Git/解压等系统工具、或需初始化某 skill 的 vendor/python-packages 到便携 Python 时触发。提供企业内网无管理员、无预装工具场景下的共享便携工具链（python.7z |
| [skill-publish](skills/platform-engineering/skill-publish) | platform-engineering | 将本地高可用 Skill 发布到 mjnn/my-skills 云端仓库。当用户说「发布这个skill」「上传到my-skills」「入库」「推送到skill仓库」「把这个skill传到云端」时触发。不适用于：创建新 skill（走 ski |
| [skill-update](skills/platform-engineering/skill-update) | platform-engineering | 当用户要求更新、修改、迭代或升级已有 Agent Skill 时触发。引导按门禁流程完成变更分析、版本判定、正文+eval 同步更新、自检、发布全链路。不适用于：从零创建新 skill（走 skill-bootstrap）、仅讨论 skil |
| [requirement-briefing](skills/project-management/requirement-briefing) | project-management | 接到任何复杂任务（功能开发、系统搭建、文档撰写、方案设计等）时必须先用此 skill 梳理需求，再动手。禁止跳过设计直接执行。不适用于：已有明确设计文档且用户已确认、仅修复单个小 bug、纯信息查询或讨论思路、已在其他 skill 中完成需 |
| [writing-plans](skills/project-management/writing-plans) | project-management | 拿到已确认的设计文档或需求后，将其拆解为 bite-size 的可执行任务清单。每个任务 2-5 分钟，含明确文件路径、操作步骤和验证方式。不适用于：没有设计文档或需求就拆任务、用户要求先出代码再补计划、纯探索性任务（需要边做边设计）、任务 |

<!-- SKILLS_TABLE_END -->

## 文档

- [技能浏览器](docs/skill-browser.md)
- [生命周期规范](docs/lifecycle-spec.md)
- [目录注册表](CATALOG.md)

---

*维护者：马捷（mjnn）*
