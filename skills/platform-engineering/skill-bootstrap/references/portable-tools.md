# 便携工具与 vendor 规范

> Read this when: 第二步编写正文、设计 scripts/ 或打包发布前

## 环境假设（Qoder CN 企业内网）

- **无**外网、**无**管理员权限、**无**预装 Python/Git/pip/tar/curl
- 共享运行时由 **skill-kit** 提供（`%USERPROFILE%\.qoder-cn\tools\skill-kit\`）
- 各 skill **不得**默认 `pip install` 或 `winget install`

## 目录骨架（创建时即包含）

```
{skill-name}/
├── SKILL.md
├── scripts/
├── references/
├── evals/
├── vendor/
│   └── python-packages/     # 本 skill 专属 Py 库（解压后的 wheel 内容）
└── tools/                   # 可选：本 skill 独占的非 Python 便携工具
    └── manifest.json
```

Read skill-kit `references/vendor-layout.md`。

## 脚本写法

**禁止：**
```bash
python scripts/foo.py
pip install requests
```

**必须：**
```powershell
# 流程第一步（若依赖 Py 库）
powershell -ExecutionPolicy Bypass -File "$env:USERPROFILE\.qoder-cn\tools\skill-kit\scripts\init_skill_python.ps1" -SkillDir "<本 skill 根目录>"

& $env:QODER_PYTHON scripts/foo.py
```

或在 skill-env-setup 完成后的会话中，Agent 先确认 `QODER_PYTHON` 已设置。

## 维护者准备 vendor 包（开发机，可有外网）

```bash
mkdir -p vendor/wheels vendor/python-packages
pip download -d vendor/wheels -r requirements.txt --only-binary=:all: --python-version 312 --platform win_amd64
# 将每个 .whl 解压到 vendor/python-packages/<包名>/
```

Release zip **包含** `vendor/python-packages/`，**不包含** `vendor/wheels/`（可选）。

## SKILL.md 必装章节

1. **依赖清单**：skill-kit、skill-env-setup（环境未就绪时）、本 skill vendor 包名
2. **步骤 0：skill-kit 就绪检查**（skill-kit `references/preflight.md`）— 含 scripts/ 的 skill **强制**；纯对话 skill 用轻量「运行时说明」
3. 检查失败 → AskUserQuestion 引导 **skill-env-setup**（exit **1**，kit 未安装）或 **local-skill-runtime**（exit **2**，vendor 未链接）；禁止裸 `python`/`git`/`pip`
4. **能力边界**：Python/Git 安装属 skill-kit / skill-env-setup；vendor 重链属 local-skill-runtime

## tools/ 与 skill-kit 分工

| 工具类型 | 位置 |
|---------|------|
| Python 3.12 | skill-kit `python.7z` |
| Git | skill-kit MinGit |
| 7za | skill-kit `7za.exe` |
| skill 专用 CLI | 本 skill `tools/` |

## 自检补充项

- [ ] 流程含步骤 0 skill-kit 检查（或纯对话 skill 的运行时说明）
- [ ] scripts/ 无裸 `python`/`pip` 命令（用 `$env:QODER_PYTHON`）
- [ ] 若用第三方 Py 库，`vendor/python-packages/` 已提交且 init 步骤已写入流程
- [ ] 未要求用户安装系统级工具
