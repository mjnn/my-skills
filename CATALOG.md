# Skill Catalog

> mjnn/my-skills 注册表（对齐 Qoder Skills Hub 域分类）
> 最后更新：2026-07-09

## 目录

| Skill 名称 | 域 | 版本 | 平台 | 路径 | 状态 |
|-----------|-----|------|------|------|------|
| separate-employee-extraction | development-testing | v0.0.0 | universal | `skills/development-testing/separate-employee-extraction` | 已发布 |
| subagent-driven-development | development-testing | v0.0.0 | universal | `skills/development-testing/subagent-driven-development` | 已发布 |
| vehicle-tracking-design | development-testing | v0.0.0 | cursor | `skills/development-testing/vehicle-tracking-design` | 已发布 |
| verification-before-completion | development-testing | v0.0.0 | universal | `skills/development-testing/verification-before-completion` | 已发布 |
| xuehaiqiang-perspective | development-testing | v0.0.0 | universal | `skills/development-testing/xuehaiqiang-perspective` | 已发布 |
| feishu-bitable-ops | general-office | v0.0.0 | cursor | `skills/general-office/feishu-bitable-ops` | 已发布 |
| svw-ppt-generator | general-office | v0.0.0 | universal | `skills/general-office/svw-ppt-generator` | 已发布 |
| ask-before-act | platform-engineering | v0.0.0 | universal | `skills/platform-engineering/ask-before-act` | 已发布 |
| ecs-connect | platform-engineering | v0.0.0 | cursor | `skills/platform-engineering/ecs-connect` | 已发布 |
| ecs-github-delivery-ops | platform-engineering | v0.0.0 | cursor | `skills/platform-engineering/ecs-github-delivery-ops` | 已发布 |
| github-connect | platform-engineering | v0.0.0 | cursor | `skills/platform-engineering/github-connect` | 已发布 |
| gitlab-repo-upload | platform-engineering | v0.3.0 | universal | `skills/platform-engineering/gitlab-repo-upload` | 已发布 |
| local-skill-runtime | platform-engineering | v0.1.0 | universal | `skills/platform-engineering/local-skill-runtime` | 已发布 |
| session-to-rules | platform-engineering | v0.0.0 | cursor | `skills/platform-engineering/session-to-rules` | 已发布 |
| skill-bootstrap | platform-engineering | v0.2.0 | universal | `skills/platform-engineering/skill-bootstrap` | 已发布 |
| skill-discipline | platform-engineering | v0.0.0 | universal | `skills/platform-engineering/skill-discipline` | 已发布 |
| skill-env-setup | platform-engineering | v0.5.0 | universal | `skills/platform-engineering/skill-env-setup` | 已发布 |
| skill-hub-management | platform-engineering | v0.0.0 | universal | `skills/platform-engineering/skill-hub-management` | 已发布 |
| skill-kit | platform-engineering | v0.0.0 | universal | `skills/platform-engineering/skill-kit` | 已发布 |
| skill-publish | platform-engineering | v0.0.0 | universal | `skills/platform-engineering/skill-publish` | 已发布 |
| skill-update | platform-engineering | v0.0.0 | universal | `skills/platform-engineering/skill-update` | 已发布 |
| requirement-briefing | project-management | v0.0.0 | universal | `skills/project-management/requirement-briefing` | 已发布 |
| writing-plans | project-management | v0.0.0 | universal | `skills/project-management/writing-plans` | 已发布 |

## 域分类

### development-testing

| Skill | 版本 | 说明 |
|-------|------|------|
| separate-employee-extraction | v0.0.0 | | |
| subagent-driven-development | v0.0.0 | 拿到实施计划后，逐任务派出子 Agent 执行，每项完成后审查。适用于任务间相对独立的场景，可自动连续推进无需人工介入。不适用于：任务高度耦合（后面依赖前面的中… |
| vehicle-tracking-design | v0.0.0 | 为车端应用生成完整埋点设计方案。基于功能 SPEC（DOCX/PDF/Markdown）和可选 UE 设计 PDF，输出含四大 Sheet 的标准化 Excel… |
| verification-before-completion | v0.0.0 | 任何任务完成后、向用户报告"做完了"之前，必须用此 skill 做最终验证。防止"看起来好了"就交差的习惯。不适用于：纯聊天/寒暄、用户明确说"不用验证"、正在… |
| xuehaiqiang-perspective | v0.0.0 | | |

### general-office

| Skill | 版本 | 说明 |
|-------|------|------|
| feishu-bitable-ops | v0.0.0 | >- |
| svw-ppt-generator | v0.0.0 | 当用户需要生成遵循"总分总、由浅入深"结构化叙事框架的PPT时触发。适用于项目汇报、进度总结、方案评审等工作场景。基于内置标准模板，通过对话式引导完成信息收集、… |

### platform-engineering

| Skill | 版本 | 说明 |
|-------|------|------|
| ask-before-act | v0.0.0 | 当Agent不确定用户诉求、任务细节或执行方向时触发。使用AskUserQuestion工具向用户提出结构化问题，明确用户意图后再继续执行。适用于：任务目标模糊… |
| ecs-connect | v0.0.0 | >- |
| ecs-github-delivery-ops | v0.0.0 | >- |
| github-connect | v0.0.0 | >- |
| gitlab-repo-upload | v0.3.0 | 当用户要求将本地项目、代码或文件夹上传/推送到 GitLab 仓库时触发。涵盖 git init、.gitignore 配置、remote add、commit… |
| local-skill-runtime | v0.1.0 | 当用户要求检查、诊断、修复或调优本机已安装的 Qoder Skills 运行环境（skill-kit、vendor 链接、Hub 版本）时触发。适用于日常「把设… |
| session-to-rules | v0.0.0 | Extracts durable knowledge from the current workspace project only into that pro… |
| skill-bootstrap | v0.2.0 | 当用户要求新建、创建、编写或做一个 Agent Skill 时触发。引导作者按 7 门禁质量标准从零创建高质量 Agent Skill，覆盖领域确认、Gotch… |
| skill-discipline | v0.0.0 | 会话开始时、接到任何任务时、以及想跳过流程直接动手时，必须先过此 skill。它不干具体活，只确保你不会绕过其他 skill。不适用于：用户明确说"直接做""不… |
| skill-env-setup | v0.5.0 | 当用户首次配置 Qoder Skills 环境、初始化 skill 安装目录、检测内网零预装依赖与 GitLab 连通性时触发。默认先安装 skill-kit … |
| skill-hub-management | v0.0.0 | >- |
| skill-kit | v0.0.0 | 当 skill 需要 Python/Git/解压等系统工具、或需初始化某 skill 的 vendor/python-packages 到便携 Python 时… |
| skill-publish | v0.0.0 | 将本地高可用 Skill 发布到 mjnn/my-skills 云端仓库。当用户说「发布这个skill」「上传到my-skills」「入库」「推送到skill仓… |
| skill-update | v0.0.0 | 当用户要求更新、修改、迭代或升级已有 Agent Skill 时触发。引导按门禁流程完成变更分析、版本判定、正文+eval 同步更新、自检、发布全链路。不适用于… |

### project-management

| Skill | 版本 | 说明 |
|-------|------|------|
| requirement-briefing | v0.0.0 | 接到任何复杂任务（功能开发、系统搭建、文档撰写、方案设计等）时必须先用此 skill 梳理需求，再动手。禁止跳过设计直接执行。不适用于：已有明确设计文档且用户已… |
| writing-plans | v0.0.0 | 拿到已确认的设计文档或需求后，将其拆解为 bite-size 的可执行任务清单。每个任务 2-5 分钟，含明确文件路径、操作步骤和验证方式。不适用于：没有设计文… |
