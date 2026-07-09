# 技能浏览器

> 上汽大众电子电器研发部 Agent Skill 内部技能市场

## 拉取全部技能

```bash
git clone https://github.com/mjnn/my-skills.git
```

## 技能总览

| 技能 | 域 | 版本 | 描述 |
|------|------|------|------|
| [gitlab-repo-upload](#gitlab-repo-upload-v030) | platform-engineering | v0.3.0 | 将本地项目上传到 GitLab 仓库（含 zip 附件上传和文档同步） |
| [skill-bootstrap](#skill-bootstrap-v021) | platform-engineering | v0.2.1 | 引导按 7 门禁质量标准从零创建 Agent Skill |
| [ask-before-act](#ask-before-act-v010) | platform-engineering | v0.1.0 | 不确定用户意图时先问再做 |
| [skill-update](#skill-update-v010) | platform-engineering | v0.1.0 | 按门禁流程更新迭代已有 Agent Skill |
| [skill-discipline](#skill-discipline-v010) | platform-engineering | v0.1.0 | 流程守卫，确保 Agent 不绕过其他 Skill |
| [skill-env-setup](#skill-env-setup-v040) | platform-engineering | v0.4.0 | 7 节点门禁环境初始化（MinGit + 初始化技能包） |
| [skill-hub-management](#skill-hub-management-v010) | platform-engineering | v0.1.0 | 管理 Qoder Skills Hub 仓库：一致性检查、新技能注册、多文档同步 |
| [skill-kit](#skill-kit-v010) | platform-engineering | v0.1.0 | 共享便携工具链（Python/Git/7za） |
| [local-skill-runtime](#local-skill-runtime-v010) | platform-engineering | v0.1.0 | 本地 Skill 运行时诊断与修复 |
| [svw-ppt-generator](#svw-ppt-generator-v010) | general-office | v0.1.0 | 生成遵循总分总结构化叙事框架的 PPT |
| [feishu-bitable-ops](#feishu-bitable-ops-v010) | general-office | v0.1.0 | 飞书多维表格 API 操作：初始化、授权、协作者配置 |
| [requirement-briefing](#requirement-briefing-v010) | project-management | v0.1.0 | 复杂任务前梳理需求 |
| [writing-plans](#writing-plans-v010) | project-management | v0.1.0 | 将设计文档拆解为可执行任务 |
| [verification-before-completion](#verification-before-completion-v010) | development-testing | v0.1.0 | 任务完成前强制验证 |
| [subagent-driven-development](#subagent-driven-development-v010) | development-testing | v0.1.0 | 多个子 Agent 并行执行任务 |
| [separate-employee-extraction](#separate-employee-extraction-v100) | development-testing | v1.0.0 | 离职员工思维框架蒸馏，生成人物 Skill |
| [xuehaiqiang-perspective](#xuehaiqiang-perspective-v020) | development-testing | v0.2.0 | 以薛海强视角做方案评审与决策参考 |

---

## platform-engineering（平台工程与 DevOps）

7 个技能

<details>
<summary><b>拉取本域全部技能</b></summary>

```bash
git clone --filter=blob:none --sparse https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/platform-engineering
```

</details>

### gitlab-repo-upload `v0.3.0`

将本地项目上传到 GitLab 仓库（含 Tag/Release 创建、zip 附件上传和文档同步）。涵盖 git init、.gitignore 配置、remote add、commit、push 全流程，处理企业内网自签名 SSL 证书和 token 认证等常见障碍。push 成功后支持创建 Tag、Release、上传 zip 附件和同步仓库文档。

| Zip 下载 | Release |
|---------|---------|
| [gitlab-repo-upload-v0.3.0.zip](https://github.com/mjnn/my-skills/-/raw/main/assets/gitlab-repo-upload-v0.3.0.zip) | [Release 页面](https://github.com/mjnn/my-skills/-/releases/gitlab-repo-upload%2Fv0.3.0) |

<details>
<summary>单技能拉取命令</summary>

```bash
git clone --filter=blob:none --sparse --branch gitlab-repo-upload/v0.3.0 https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/platform-engineering/gitlab-repo-upload
```

</details>

### skill-bootstrap `v0.2.1`

引导作者按 7 门禁质量标准从零创建高质量 Agent Skill。覆盖领域确认、Gotchas 提炼、正文+eval 交替编写、自检清单、格式预检、产出报告与发布全链路。

| Zip 下载 | Release |
|---------|---------|
| [skill-bootstrap-v0.2.1.zip](https://github.com/mjnn/my-skills/-/raw/main/assets/skill-bootstrap-v0.2.1.zip) | [Release 页面](https://github.com/mjnn/my-skills/-/releases/skill-bootstrap%2Fv0.2.1) |

<details>
<summary>单技能拉取命令</summary>

```bash
git clone --filter=blob:none --sparse --branch skill-bootstrap/v0.2.1 https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/platform-engineering/skill-bootstrap
```

</details>

### ask-before-act `v0.1.0`

当 Agent 不确定用户诉求、任务细节或执行方向时，使用 AskUserQuestion 工具向用户提出结构化问题，明确用户意图后再继续执行。

| Zip 下载 | Release |
|---------|---------|
| [ask-before-act-v0.1.0.zip](https://github.com/mjnn/my-skills/-/raw/main/assets/ask-before-act-v0.1.0.zip) | [Release 页面](https://github.com/mjnn/my-skills/-/releases/ask-before-act%2Fv0.1.0) |

<details>
<summary>单技能拉取命令</summary>

```bash
git clone --filter=blob:none --sparse --branch ask-before-act/v0.1.0 https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/platform-engineering/ask-before-act
```

</details>

### skill-update `v0.1.0`

引导按门禁流程更新迭代已有 Agent Skill。覆盖变更分析、版本判定、正文+eval 同步更新、自检、版本管理与发布（含 Zip 附件上传、旧 Release 清理、PR 流程）全链路。

| Zip 下载 | Release |
|---------|---------|
| [skill-update-v0.1.0.zip](https://github.com/mjnn/my-skills/-/raw/main/assets/skill-update-v0.1.0.zip) | [Release 页面](https://github.com/mjnn/my-skills/-/releases/skill-update%2Fv0.1.0) |

<details>
<summary>单技能拉取命令</summary>

```bash
git clone --filter=blob:none --sparse --branch skill-update/v0.1.0 https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/platform-engineering/skill-update
```

</details>

### skill-discipline `v0.1.0`

会话开始时、接到任何任务时、以及想跳过流程直接动手时，必须先过此 skill。它不干具体活，只确保你不会绕过其他 skill。

| Zip 下载 | Release |
|---------|---------|
| [skill-discipline-v0.1.0.zip](https://github.com/mjnn/my-skills/-/raw/main/assets/skill-discipline-v0.1.0.zip) | [Release 页面](https://github.com/mjnn/my-skills/-/releases/skill-discipline%2Fv0.1.0) |

<details>
<summary>单技能拉取命令</summary>

```bash
git clone --filter=blob:none --sparse --branch skill-discipline/v0.1.0 https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/platform-engineering/skill-discipline
```

</details>

### skill-env-setup `v0.4.1`

7 节点门禁工作流：系统依赖检测、环境状态、凭证收集、Spec 审核、自动安装、GitLab 全权限验证、版本对比与可选升级。内置 MinGit 便携版和初始化技能包，全量安装所有已发布 Skill。

| Zip 下载 | Release |
|---------|---------|
| [skill-env-setup-v0.4.1.zip](https://github.com/mjnn/my-skills/-/raw/main/assets/skill-env-setup-v0.4.1.zip) | [Release 页面](https://github.com/mjnn/my-skills/-/releases/skill-env-setup%2Fv0.4.1) |

<details>
<summary>单技能拉取命令</summary>

```bash
git clone --filter=blob:none --sparse --branch skill-env-setup/v0.4.1 https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/platform-engineering/skill-env-setup
```

</details>

### skill-hub-management `v0.1.0`

管理 Qoder Skills Hub 仓库本身：一致性检查（README/技能浏览器/CATALOG/assets/skills）、新技能注册、多文档描述同步、技能安装到本地用户目录。

| Zip 下载 | Release |
|---------|---------|
| [skill-hub-management-v0.1.0.zip](https://github.com/mjnn/my-skills/-/raw/main/assets/skill-hub-management-v0.1.0.zip) | [Release 页面](https://github.com/mjnn/my-skills/-/releases/skill-hub-management%2Fv0.1.0) |

<details>
<summary>单技能拉取命令</summary>

```bash
git clone --filter=blob:none --sparse --branch skill-hub-management/v0.1.0 https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/platform-engineering/skill-hub-management
```

</details>

---

### skill-kit `v0.1.0`

共享便携工具链（Python/Git/7za），供企业内网无管理员、无预装工具场景下的 skill 使用。安装到 `%USERPROFILE%\.qoder-cn\tools\skill-kit\`。

| Zip 下载 | Release |
|---------|---------|
| [skill-kit-v0.1.0.zip](https://github.com/mjnn/my-skills/-/raw/main/assets/skill-kit-v0.1.0.zip) | [Release 页面](https://github.com/mjnn/my-skills/-/releases/skill-kit%2Fv0.1.0) |

<details>
<summary>单技能拉取命令</summary>

```bash
git clone --filter=blob:none --sparse --branch skill-kit/v0.1.0 https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/platform-engineering/skill-kit
```

</details>

---

### local-skill-runtime `v0.1.0`

本地 Skill 运行时治理：诊断、修复、升级本地已安装的 skill 环境。适用于日常「把设备调到最佳状态」。

| Zip 下载 | Release |
|---------|---------|
| [local-skill-runtime-v0.1.0.zip](https://github.com/mjnn/my-skills/-/raw/main/assets/local-skill-runtime-v0.1.0.zip) | [Release 页面](https://github.com/mjnn/my-skills/-/releases/local-skill-runtime%2Fv0.1.0) |

<details>
<summary>单技能拉取命令</summary>

```bash
git clone --filter=blob:none --sparse --branch local-skill-runtime/v0.1.0 https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/platform-engineering/local-skill-runtime
```

</details>

---

## general-office（通用办公与文件管理）

2 个技能

<details>
<summary><b>拉取本域全部技能</b></summary>

```bash
git clone --filter=blob:none --sparse https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/general-office
```

</details>

### svw-ppt-generator `v0.1.0`

生成遵循"总分总、由浅入深"结构化叙事框架的 PPT。适用于项目汇报、进度总结、方案评审等工作场景。基于内置标准模板，通过对话式引导完成信息收集、文案确认、排版设计、图表绘制。

| Zip 下载 | Release |
|---------|---------|
| [svw-ppt-generator-v0.1.0.zip](https://github.com/mjnn/my-skills/-/raw/main/assets/svw-ppt-generator-v0.1.0.zip) | [Release 页面](https://github.com/mjnn/my-skills/-/releases/svw-ppt-generator%2Fv0.1.0) |

<details>
<summary>单技能拉取命令</summary>

```bash
git clone --filter=blob:none --sparse --branch svw-ppt-generator/v0.1.0 https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/general-office/svw-ppt-generator
```

</details>

### feishu-bitable-ops `v0.1.0`

飞书开放平台多维表格 (Bitable) API 操作：首次初始化引导配置开放平台 App ID/Secret、新建 Base 后自动授予用户可管理权限、操作他人表格的协作者配置。

| Zip 下载 | Release |
|---------|---------|
| [feishu-bitable-ops-v0.1.0.zip](https://github.com/mjnn/my-skills/-/raw/main/assets/feishu-bitable-ops-v0.1.0.zip) | [Release 页面](https://github.com/mjnn/my-skills/-/releases/feishu-bitable-ops%2Fv0.1.0) |

<details>
<summary>单技能拉取命令</summary>

```bash
git clone --filter=blob:none --sparse --branch feishu-bitable-ops/v0.1.0 https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/general-office/feishu-bitable-ops
```

</details>

---

## project-management（项目与功能管理）

2 个技能

<details>
<summary><b>拉取本域全部技能</b></summary>

```bash
git clone --filter=blob:none --sparse https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/project-management
```

</details>

### requirement-briefing `v0.1.0`

接到任何复杂任务（功能开发、系统搭建、文档撰写、方案设计等）时必须先用此 skill 梳理需求，再动手。禁止跳过设计直接执行。

| Zip 下载 | Release |
|---------|---------|
| [requirement-briefing-v0.1.0.zip](https://github.com/mjnn/my-skills/-/raw/main/assets/requirement-briefing-v0.1.0.zip) | [Release 页面](https://github.com/mjnn/my-skills/-/releases/requirement-briefing%2Fv0.1.0) |

<details>
<summary>单技能拉取命令</summary>

```bash
git clone --filter=blob:none --sparse --branch requirement-briefing/v0.1.0 https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/project-management/requirement-briefing
```

</details>

### writing-plans `v0.1.0`

拿到已确认的设计文档或需求后，将其拆解为 bite-size 的可执行任务清单。每个任务 2-5 分钟，含明确文件路径、操作步骤和验证方式。

| Zip 下载 | Release |
|---------|---------|
| [writing-plans-v0.1.0.zip](https://github.com/mjnn/my-skills/-/raw/main/assets/writing-plans-v0.1.0.zip) | [Release 页面](https://github.com/mjnn/my-skills/-/releases/writing-plans%2Fv0.1.0) |

<details>
<summary>单技能拉取命令</summary>

```bash
git clone --filter=blob:none --sparse --branch writing-plans/v0.1.0 https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/project-management/writing-plans
```

</details>

---

## development-testing（功能开发与测试）

4 个技能

<details>
<summary><b>拉取本域全部技能</b></summary>

```bash
git clone --filter=blob:none --sparse https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/development-testing
```

</details>

### verification-before-completion `v0.1.0`

任何任务完成后、向用户报告"做完了"之前，必须用此 skill 做最终验证。防止"看起来好了"就交差的习惯。

| Zip 下载 | Release |
|---------|---------|
| [verification-before-completion-v0.1.0.zip](https://github.com/mjnn/my-skills/-/raw/main/assets/verification-before-completion-v0.1.0.zip) | [Release 页面](https://github.com/mjnn/my-skills/-/releases/verification-before-completion%2Fv0.1.0) |

<details>
<summary>单技能拉取命令</summary>

```bash
git clone --filter=blob:none --sparse --branch verification-before-completion/v0.1.0 https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/development-testing/verification-before-completion
```

</details>

### subagent-driven-development `v0.1.0`

拿到实施计划后，逐任务派出子 Agent 执行，每项完成后审查。适用于任务间相对独立的场景，可自动连续推进无需人工介入。

| Zip 下载 | Release |
|---------|---------|
| [subagent-driven-development-v0.1.0.zip](https://github.com/mjnn/my-skills/-/raw/main/assets/subagent-driven-development-v0.1.0.zip) | [Release 页面](https://github.com/mjnn/my-skills/-/releases/subagent-driven-development%2Fv0.1.0) |

<details>
<summary>单技能拉取命令</summary>

```bash
git clone --filter=blob:none --sparse --branch subagent-driven-development/v0.1.0 https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/development-testing/subagent-driven-development
```

</details>

### separate-employee-extraction `v1.0.0`

离职员工思维框架蒸馏：输入人名/主题/甚至只是模糊需求，自动深度调研→思维框架提炼→生成可运行的人物 Skill。包含 6 Agent 并行调研、三重验证心智模型提取、Phase 检查点设计、质量自检脚本。

| Zip 下载 | Release |
|---------|---------|
| [separate-employee-extraction-v1.0.0.zip](https://github.com/mjnn/my-skills/-/raw/main/assets/separate-employee-extraction-v1.0.0.zip) | [Release 页面](https://github.com/mjnn/my-skills/-/releases/separate-employee-extraction%2Fv1.0.0) |

<details>
<summary>单技能拉取命令</summary>

```bash
git clone --filter=blob:none --sparse --branch separate-employee-extraction/v1.0.0 https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/development-testing/separate-employee-extraction
```

</details>

### xuehaiqiang-perspective `v0.2.0`

以薛海强（上汽大众车联网数据采集）视角做方案评审与决策参考。基于40+份SVW工作交接文档及1559封发送邮件提炼7个心智模型、10条决策启发式与表达风格。

| Zip 下载 | Release |
|---------|---------|
| [xuehaiqiang-perspective-v0.2.0.zip](https://github.com/mjnn/my-skills/-/raw/main/assets/xuehaiqiang-perspective-v0.2.0.zip) | [Release 页面](https://github.com/mjnn/my-skills/-/releases/xuehaiqiang-perspective%2Fv0.2.0) |

<details>
<summary>单技能拉取命令</summary>

```bash
git clone --filter=blob:none --sparse --branch xuehaiqiang-perspective/v0.2.0 https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/development-testing/xuehaiqiang-perspective
```

</details>

---

## data-analysis（数据分析与处理）

暂无技能

<details>
<summary><b>拉取本域全部技能</b></summary>

```bash
git clone --filter=blob:none --sparse https://github.com/mjnn/my-skills.git
cd qoder-skills
git sparse-checkout set skills/data-analysis
```

</details>

---

## archive（已废弃 skill）

暂无技能
