# 流程节点表

> Read this when: 核对节点门禁或调试跳步

## 节点总览

| node_id | name | purpose | outputs | gate | on_fail |
|---------|------|---------|---------|------|---------|
| 0 | 系统依赖检测 | D1–D3（零预装） | 检测报告 / dependency-fail | D1–D3 pass | 禁止节点 1–6 |
| 1 | 环境状态检查 | skill-kit 资源/目录/身份/Token | 环境状态报告 | 五项已检测 | 返回本节点 |
| 2 | 凭证收集 | 仅补 Git 身份 + Token | 凭证就绪 | 不询问安装范围 | 缺凭证则补收集 |
| 3 | Spec 审核 | 固定安装+验证计划 | 已确认 Spec | ExitSpecMode | 禁止节点 4 |
| 4 | 自动安装 | skill-kit + init skills + vendor 链接 | kit + 全部 skill | 4.0–4.7 成功 | 失败重试 |
| 5 | GitLab 验证 | G1–G8 全权限 | gitlab-access 报告 | G1–G8 pass | 禁止节点 6 |
| 6 | 清单对比升级 | Hub vs 本地版本 | 对比表+升级结果 | 对比完成+已询问 | — |

## 默认策略（禁止询问）

| 项 | 默认行为 |
|----|---------|
| skill-kit | `assets/skill-kit/` → `%USERPROFILE%\.qoder-cn\tools\skill-kit\` |
| Skill 安装范围 | 初始化技能包 **全部** → `%USERPROFILE%\.qoder-cn\skills\` |
| Python 库 | `init_all_skill_runtimes.ps1` 链接各 skill `vendor/python-packages/` |
| Git | skill-kit 内 MinGit，不询问系统 Git |

## 工具脚本

| 节点 | 脚本 |
|------|------|
| 0 | `check_system_deps.ps1 -ReportAuto`（**不用 python**） |
| 4.0 | `skill-kit/scripts/install_skill_kit.ps1` |
| 4.5 | `run_with_kit.ps1` → `install_init_skills.py` |
| 4.6 | `init_all_skill_runtimes.ps1` |
| 5 | `run_with_kit.ps1` → `check_gitlab_access.py --report-auto` |
| 6 | `run_with_kit.ps1` → `compare_skill_inventory.py` |
