# Self Check — skill-env-setup v0.5.0

## v0.5.0 变更（零预装 + skill-kit）

- [x] 35. 节点 0 改为 `check_system_deps.ps1`（D1–D3，不假设系统 Python/Git/curl）
- [x] 36. 节点 4.0 安装 skill-kit（python.7z + MinGit + 7za）到 `%USERPROFILE%\.qoder-cn\tools\skill-kit\`
- [x] 37. 节点 4.5–4.6 使用 `run_with_kit.ps1` + `init_all_skill_runtimes.ps1`
- [x] 38. `assets/skill-kit/` 便携资源目录与 README
- [x] 39. `check_system_deps.py --post-kit` 安装后复检

## v0.4.1 变更

- [x] 34. 初始化技能包新增 skill-hub-management（v0.1.0）

## v0.4.0 变更

- [x] 28. 默认全量安装 assets/init-skills/初始化技能包.zip → %USERPROFILE%\.qoder-cn\skills\
- [x] 29. 禁止 AskUserQuestion 安装范围 / Git 外网 vs 便携
- [x] 30. 无 git 自动 MinGit，不询问
- [x] 31. 节点 5 GitLab G1–G8 全权限 checklist + check_gitlab_access.py
- [x] 32. 节点 6 compare_skill_inventory.py + 版本不一致时 AskUserQuestion 升级
- [x] 33. scripts: install_init_skills.py, check_gitlab_access.py, compare_skill_inventory.py, build_init_skills_bundle.py

## 质量指标

| 指标 | 数值 |
|------|------|
| 流程节点 | 7（0–6） |
| Eval 用例 | 10 |
| Gotchas | 8 |
