# skill-kit 就绪检查（所有业务 skill 流程第 0 步）

> Read this when: 任意 skill 在执行脚本或依赖 Python/Git 之前

## 检查什么

skill-kit 已由 **skill-env-setup** 节点 4.0 安装到：

```
%USERPROFILE%\.qoder-cn\tools\skill-kit\
├── python\python.exe     → 环境变量 QODER_PYTHON
├── git\cmd\git.exe       → 环境变量 QODER_GIT
└── 7za.exe
```

**就绪条件**（全部满足）：
1. `Test-Path $env:QODER_PYTHON` 或 `Test-Path "$env:USERPROFILE\.qoder-cn\tools\skill-kit\python\python.exe"`
2. 执行 `& $env:QODER_PYTHON -c "import sys; print(sys.executable)"` 成功
3. 若本 skill 有 `vendor/python-packages/`，已执行过 `init_skill_python.ps1 -SkillDir <本 skill 根>`

## 标准检查命令

```powershell
powershell -ExecutionPolicy Bypass -File "$env:USERPROFILE\.qoder-cn\tools\skill-kit\scripts\check_skill_kit_ready.ps1" -SkillDir "<本-skill-根目录>"
```

退出码 `0` = 就绪；`1` = 未安装 skill-kit；`2` = skill-kit 在但本 skill vendor 未链接。

- **exit 1** → 引导 **skill-env-setup**
- **exit 2** → 引导 **local-skill-runtime**（vendor 重链，无需完整 env-setup）

## 未就绪时（必须用 AskUserQuestion）

| 问题 | header | 选项 |
|------|--------|------|
| skill-kit 未安装或未初始化，无法运行本技能脚本。如何处理？ | 环境未就绪 | 重新运行 skill-env-setup 初始化环境（推荐）/ 我已手动修复，重新检测 / 取消任务 |
| vendor 未链接（退出码 2），如何修复？ | Vendor 未链 | 运行 local-skill-runtime 修复 vendor 链接（推荐）/ 重新运行 skill-env-setup 节点 4.6 / 取消任务 |

- **重新运行 skill-env-setup**：引导用户在新对话中说「配置 Qoder Skills 环境」或「运行 skill-env-setup」，完成节点 4 后再回到本 skill。
- **重新检测**：再次运行 `check_skill_kit_ready.ps1`，通过则继续。
- **取消任务**：终止，不假装环境可用。

## SKILL.md 正文模板（复制到各 skill「流程」第一步）

```markdown
### 步骤 0：skill-kit 就绪检查

Read skill-kit `references/preflight.md`。

```powershell
powershell -ExecutionPolicy Bypass -File "$env:USERPROFILE\.qoder-cn\tools\skill-kit\scripts\check_skill_kit_ready.ps1" -SkillDir "<SKILL_ROOT>"
```

- 退出码 **0** → 继续下一步
- 退出码 **非 0** → 调用 AskUserQuestion（见 preflight.md），**禁止**继续执行脚本或使用裸 `python`/`git`
```

## 无 scripts/ 的 skill

仍须在依赖清单中声明：**若同会话后续 skill 需要脚本**，须先确认 skill-kit 就绪；纯对话类 skill 可写「本 skill 不执行脚本，跳过 kit 检查，但若用户要求运行关联脚本则先检查 kit」。
