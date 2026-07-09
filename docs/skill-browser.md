# 技能浏览器

> mjnn/my-skills 个人 Agent Skill 索引

## 技能总览

| 技能 | 域 | 版本 | 描述 |
|------|-----|------|------|
| [ask-before-act](skills/platform-engineering/ask-before-act) | platform-engineering | v0.0.0 | 当Agent不确定用户诉求、任务细节或执行方向时触发。使用AskUserQuestion工具向用户提出结构化问题，明确用户意图后再继续执行。适用于：任务目标模糊… |
| [ecs-connect](skills/platform-engineering/ecs-connect) | platform-engineering | v0.0.0 | Connects to the user's Alibaba Cloud ECS via SSH (alias ecs-main, KeyForAgent ke… |
| [ecs-github-delivery-ops](skills/platform-engineering/ecs-github-delivery-ops) | platform-engineering | v0.0.0 | Connects to the user's ECS via SSH, deploys services with Docker Compose, config… |
| [feishu-bitable-ops](skills/general-office/feishu-bitable-ops) | general-office | v0.0.0 | 飞书开放平台多维表格 (Bitable) API 操作：首次初始化引导配置开放平台 App ID/Secret、 新建 Base 后自动授予用户可管理权限、操作… |
| [github-connect](skills/platform-engineering/github-connect) | platform-engineering | v0.0.0 | Verifies GitHub connectivity on Windows: Git CLI install, HTTPS/SSH network chec… |
| [session-to-rules](skills/platform-engineering/session-to-rules) | platform-engineering | v0.0.0 | Extracts durable knowledge from the current workspace project only into that pro… |
| [skill-bootstrap](skills/platform-engineering/skill-bootstrap) | platform-engineering | v0.2.0 | 当用户要求新建、创建、编写或做一个 Agent Skill 时触发。引导作者按 7 门禁质量标准从零创建高质量 Agent Skill，覆盖领域确认、Gotch… |
| [skill-publish](skills/platform-engineering/skill-publish) | platform-engineering | v0.0.0 | 将本地高可用 Skill 发布到 mjnn/my-skills 云端仓库。当用户说「发布这个skill」「上传到my-skills」「入库」「推送到skill仓… |
| [vehicle-tracking-design](skills/development-testing/vehicle-tracking-design) | development-testing | v0.0.0 | 为车端应用生成完整埋点设计方案。基于功能 SPEC（DOCX/PDF/Markdown）和可选 UE 设计 PDF，输出含四大 Sheet 的标准化 Excel… |

## 安装

```bash
git clone https://github.com/mjnn/my-skills.git
cp -r my-skills/skills/<domain>/<skill-name> <你的-skill-目录>/
```
