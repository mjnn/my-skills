---
name: skill-kit
description: 当 skill 需要 Python/Git/解压等系统工具、或需初始化某 skill 的 vendor/python-packages 到便携 Python 时触发。提供企业内网无管理员、无预装工具场景下的共享便携工具链（python.7z、MinGit、7za），安装到 %USERPROFILE%\.qoder-cn\tools\skill-kit\。不适用于：用户机器已全局安装且明确只用系统 Python/Git；非 Windows 环境（当前仅支持 Windows 便携包）；仅需修改单个 skill 业务逻辑、不涉及工具链的场景。
---

# Skill Kit — 共享便携工具链

为企业内网 Qoder CN 场景提供**零预装假设**的共享运行时：不依赖系统 Python、Git、tar、curl 或管理员权限。

<HARD-GATE>
1. **禁止**在 skill 正文或脚本中假设 `python`、`git`、`pip`、`tar`、`curl` 已在 PATH 中可用。
2. **禁止**引导用户 winget、外网下载、联系 IT 安装全局工具作为默认路径。
3. 需要 Python 时**必须**通过本 kit 的 `resolve_tools.ps1` 取得便携 `python.exe` 路径。
4. skill 专属 Python 库**必须**放在该 skill 的 `vendor/python-packages/`，由 `init_skill_python.ps1` 链接到便携 site-packages，**禁止**在线 `pip install`。
</HARD-GATE>

## 能力边界

### 本技能负责
- 将 `assets/` 内便携包解压到 `%USERPROFILE%\.qoder-cn\tools\skill-kit\`
- 暴露 `resolve_tools.ps1`：返回 `PYTHON_EXE`、`GIT_EXE`、`SEVENZIP_EXE` 路径
- 将单个 skill 的 `vendor/python-packages/` 链接进便携 Python（`.pth` 文件）
- 维护 skill-kit 目录结构与打包规范

### 本技能不负责
- 首次环境初始化全流程 → **skill-env-setup**（节点 4 会调用本 kit 安装）
- 创建新 skill 的目录骨架与打包规范 → **skill-bootstrap**
- 业务脚本逻辑 → 各业务 skill 自行实现

## 目录结构（安装后）

```
%USERPROFILE%\.qoder-cn\tools\skill-kit\
├── python\python.exe          # 自 python.7z 解压
├── git\cmd\git.exe            # 自 MinGit zip 解压
├── 7za.exe                    # 解压 python.7z 用
└── state\                     # 已链接 skill 清单
```

## 便携包源文件（skill 包内）

```
skill-kit/assets/
├── 7za.exe                    # 7-Zip 命令行（x64），维护者离线放入
├── python.7z                  # 便携 Python 3.12（结构见 references/python-bundle.md）
└── git/
    └── MinGit-*-64-bit.zip
```

> skill-env-setup 的 `assets/skill-kit/` 与上表**同结构**（发布时可复制或硬链接），节点 4 优先从 skill-env-setup 安装。

## Gotchas

**1. 直接调用 `python scripts/foo.py`** — 内网机可能没有 Python。**纠正：先 `.\scripts\resolve_tools.ps1`，用返回的 `$env:QODER_PYTHON` 执行。**

**2. 在 skill 里写 `pip install requests`** — 无外网、无 pip 全局环境。**纠正：开发机离线 `pip download -d vendor/wheels requests`，解压 wheel 到 `vendor/python-packages/`，运行前调用 `init_skill_python.ps1`。**

**3. python.7z 只有 Expand-Archive 解不了** — PowerShell 不能解 7z。**纠正：assets 必须含 `7za.exe`；安装脚本先用 7za 解 python.7z。**

**4. 每个 skill 各带一份 Python** — 体积爆炸。**纠正：仅 skill-kit 放一份 python.7z；各 skill 只放自己需要的 `vendor/python-packages/`。**

**5. 链接 vendor 包后 import 仍失败** — 未执行 init 或路径错误。**纠正：skill 流程第一步调用 `init_skill_python.ps1 -SkillDir <本 skill 根目录>`，并验证 `import` 关键模块。**

## 流程

### 安装 skill-kit（通常由 skill-env-setup 节点 4.0 调用）

```powershell
powershell -ExecutionPolicy Bypass -File scripts/install_skill_kit.ps1
```

Read references/python-bundle.md。

### 解析工具路径（任意 skill 脚本开头）

```powershell
. "$env:USERPROFILE\.qoder-cn\tools\skill-kit\scripts\resolve_tools.ps1"
# 或 skill 包内相对路径：
. "..\..\skill-kit\scripts\resolve_tools.ps1"  # 仅当 skill-kit 与当前 skill 同处 skills 目录
```

安装后环境变量：
- `QODER_TOOLS_ROOT` — kit 根目录
- `QODER_PYTHON` — 便携 python.exe
- `QODER_GIT` — 便携 git.exe

### 初始化某 skill 的 Python 依赖

```powershell
powershell -ExecutionPolicy Bypass -File scripts/init_skill_python.ps1 -SkillDir "$env:USERPROFILE\.qoder-cn\skills\skill-kit"
```

将 `{SkillDir}/vendor/python-packages/` 下每个包目录写入 `python/Lib/site-packages/qoder-skill-{skillname}.pth`。

### 用便携 Python 运行脚本

```powershell
& $env:QODER_PYTHON scripts\check_env.py
```

## 依赖清单

| 依赖 | 类型 | 说明 |
|------|------|------|
| PowerShell 5.1+ | 系统 | 唯一假设的系统能力（与 Qoder CN 同机） |
| skill-kit/assets/* | 便携包 | 维护者打包时离线放入，见 references/maintainer-bundle.md |

## references

- `references/python-bundle.md`：python.7z 目录结构与版本约定
- `references/maintainer-bundle.md`：维护者如何准备 7za、python.7z、离线 wheel
- `references/vendor-layout.md`：各 skill 的 vendor/python-packages 规范

## 执行后复盘（自迭代钩子）

完成后反思并记录 `evals/PITFALLS_LOG.md`（不提交 registry）。
