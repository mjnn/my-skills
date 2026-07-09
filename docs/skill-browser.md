# 技能浏览器

> mjnn/my-skills 个人 Agent Skill 索引（共 9 个）

## 技能总览

| 技能 | 域 | 版本 | 一句话 |
|------|-----|------|--------|
| [ask-before-act](skills/platform-engineering/ask-before-act) | platform-engineering | v0.1.0 | 意图不清时结构化提问，确认后再执行 |
| [ecs-connect](skills/platform-engineering/ecs-connect) | platform-engineering | v0.1.1 | 阿里云 ECS SSH 连通与巡检 |
| [ecs-github-delivery-ops](skills/platform-engineering/ecs-github-delivery-ops) | platform-engineering | v0.1.1 | ECS Docker 部署 + Nginx + GitHub 交付 |
| [github-connect](skills/platform-engineering/github-connect) | platform-engineering | v0.1.1 | Windows GitHub 连通与认证 |
| [session-to-rules](skills/platform-engineering/session-to-rules) | platform-engineering | v0.1.1 | 会话知识沉淀为项目 `.cursor/rules` |
| [skill-bootstrap](skills/platform-engineering/skill-bootstrap) | platform-engineering | v0.2.0 | 7 门禁引导创建新 Skill |
| [skill-publish](skills/platform-engineering/skill-publish) | platform-engineering | v0.2.0 | 发布 skill 到本仓库 |
| [feishu-bitable-ops](skills/general-office/feishu-bitable-ops) | general-office | v1.0.1 | 飞书多维表格 API 操作 |
| [vehicle-tracking-design](skills/development-testing/vehicle-tracking-design) | development-testing | v1.0.0 | 车端埋点方案 Excel + UE 校验 |

## 按域浏览

### platform-engineering

基础设施与 Skill 工程：连通性（ECS、GitHub）、交付运维、创建/发布 skill、项目规则沉淀。

```bash
git clone --filter=blob:none --sparse https://github.com/mjnn/my-skills.git
cd my-skills && git sparse-checkout set skills/platform-engineering
```

### general-office

办公自动化：飞书 Bitable。

```bash
git sparse-checkout set skills/general-office/feishu-bitable-ops
```

### development-testing

领域方案：车端埋点设计。

```bash
git sparse-checkout set skills/development-testing/vehicle-tracking-design
```

## 安装

将目标目录复制到本机 skill 根目录即可，例如：

```bash
cp -r my-skills/skills/platform-engineering/github-connect ~/.cursor/skills/
```

或解压 [assets/](assets/) 中的 zip。
