# Skill Hub 已发布清单

> Read this when: 节点 6 compare_skill_inventory.py API 失败时的降级对照；或升级时查 zip 链接

> **安装方式已变更**：首次初始化不再逐个从 Hub 下载，而是使用 `assets/init-skills/初始化技能包.zip` 全量安装。本表用于节点 6 版本对比与升级。

## 已发布 Skill

> **下载方式**：Zip 文件存放在仓库 `assets/` 目录，通过 GitLab API 端点下载：
> ```bash
> curl -s -k -L -H "PRIVATE-TOKEN: $GITLAB_TOKEN" -o <filename>.zip >   "https://epfa-gitlab.csvw.com/api/v4/projects/289/repository/files/assets%2F<filename>.zip/raw?ref=main"
> ```
> 内网 Skill Hub：`https://epfa-gitlab.csvw.com/ecc-2`

| 优先级 | Skill 名称 | 版本 | 描述 | Zip 下载链接 |
|--------|-----------|------|------|-------------|
| ★★★ 必装 | skill-bootstrap | v0.2.1 | 引导按 7 门禁质量标准从零创建 Agent Skill | https://epfa-gitlab.csvw.com/api/v4/projects/289/repository/files/assets%2Fskill-bootstrap-v0.2.1.zip/raw?ref=main |
| ★★☆ 推荐 | skill-update | v0.1.0 | 按门禁流程更新迭代已有 Agent Skill | https://epfa-gitlab.csvw.com/api/v4/projects/289/repository/files/assets%2Fskill-update-v0.1.0.zip/raw?ref=main |
| ★★☆ 推荐 | ask-before-act | v0.1.0 | 不确定用户意图时先问再做 | https://epfa-gitlab.csvw.com/api/v4/projects/289/repository/files/assets%2Fask-before-act-v0.1.0.zip/raw?ref=main |
| ★★☆ 推荐 | gitlab-repo-upload | v0.3.0 | 将本地项目上传到 GitLab 仓库（含 zip 附件上传和文档同步） | https://epfa-gitlab.csvw.com/api/v4/projects/289/repository/files/assets%2Fgitlab-repo-upload-v0.3.0.zip/raw?ref=main |
| ★☆☆ 按需 | svw-ppt-generator | v0.1.0 | 生成遵循总分总结构化叙事框架的 PPT | https://epfa-gitlab.csvw.com/api/v4/projects/289/repository/files/assets%2Fsvw-ppt-generator-v0.1.0.zip/raw?ref=main |
| ★★★ 必装 | skill-discipline | v0.1.0 | 流程守卫，确保 Agent 不绕过其他 Skill | https://epfa-gitlab.csvw.com/api/v4/projects/289/repository/files/assets%2Fskill-discipline-v0.1.0.zip/raw?ref=main |
| ★★☆ 推荐 | requirement-briefing | v0.1.0 | 复杂任务前梳理需求，再动手执行 | https://epfa-gitlab.csvw.com/api/v4/projects/289/repository/files/assets%2Frequirement-briefing-v0.1.0.zip/raw?ref=main |
| ★★☆ 推荐 | verification-before-completion | v0.1.0 | 任务完成前强制验证 | https://epfa-gitlab.csvw.com/api/v4/projects/289/repository/files/assets%2Fverification-before-completion-v0.1.0.zip/raw?ref=main |
| ★☆☆ 按需 | writing-plans | v0.1.0 | 将设计文档拆解为可执行任务 | https://epfa-gitlab.csvw.com/api/v4/projects/289/repository/files/assets%2Fwriting-plans-v0.1.0.zip/raw?ref=main |
| ★☆☆ 按需 | subagent-driven-development | v0.1.0 | 多个子 Agent 并行执行任务 | https://epfa-gitlab.csvw.com/api/v4/projects/289/repository/files/assets%2Fsubagent-driven-development-v0.1.0.zip/raw?ref=main |
| ★☆☆ 按需 | separate-employee-extraction | v1.0.0 | 离职员工思维框架蒸馏，生成人物 Skill | https://epfa-gitlab.csvw.com/api/v4/projects/289/repository/files/assets%2Fseparate-employee-extraction-v1.0.0.zip/raw?ref=main |
| ★★★ 必装 | skill-env-setup | v0.4.1 | 7 节点门禁环境初始化（MinGit + 初始化技能包，含 skill-hub-management） | https://epfa-gitlab.csvw.com/api/v4/projects/289/repository/files/assets%2Fskill-env-setup-v0.4.1.zip/raw?ref=main |

## 安装集定义（已废弃 — 仅作历史参考）

> v0.4.0 起：默认全量安装「初始化技能包.zip」，不再询问安装集。

## Git Sparse Checkout 命令

每个已发布 skill 均可通过 Git Sparse Checkout 拉取（推荐，无需额外认证，使用 git 凭据）：

```bash
# 通用格式
git clone --filter=blob:none --sparse --branch <skill-name>/v<version> https://epfa-gitlab.csvw.com/ecc-2/qoder-skills.git
cd qoder-skills
git sparse-checkout set skills/<domain>/<skill-name>
cp -r skills/<domain>/<skill-name> ~/.qoder-cn/skills/
```

| Skill | 分支 | 路径 |
|-------|------|------|
| skill-bootstrap | skill-bootstrap/v0.2.1 | skills/platform-engineering/skill-bootstrap |
| skill-update | skill-update/v0.1.0 | skills/platform-engineering/skill-update |
| ask-before-act | ask-before-act/v0.1.0 | skills/platform-engineering/ask-before-act |
| gitlab-repo-upload | gitlab-repo-upload/v0.3.0 | skills/platform-engineering/gitlab-repo-upload |
| skill-discipline | skill-discipline/v0.1.0 | skills/platform-engineering/skill-discipline |
| skill-env-setup | skill-env-setup/v0.4.0 | skills/platform-engineering/skill-env-setup |
| svw-ppt-generator | svw-ppt-generator/v0.1.0 | skills/general-office/svw-ppt-generator |
| requirement-briefing | requirement-briefing/v0.1.0 | skills/project-management/requirement-briefing |
| writing-plans | writing-plans/v0.1.0 | skills/project-management/writing-plans |
| verification-before-completion | verification-before-completion/v0.1.0 | skills/development-testing/verification-before-completion |
| subagent-driven-development | subagent-driven-development/v0.1.0 | skills/development-testing/subagent-driven-development |
| separate-employee-extraction | separate-employee-extraction/v1.0.0 | skills/development-testing/separate-employee-extraction |
