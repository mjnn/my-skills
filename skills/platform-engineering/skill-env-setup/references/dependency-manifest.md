# 系统工具依赖清单（零预装假设）

> Read this when: 节点 0「系统依赖检测」阶段

## 设计原则

目标环境：**企业内网、无外网、无管理员权限、无预装 Python/Git/tar/curl/pip**。

除 Qoder CN 客户端与 Windows PowerShell 外，**一切工具由 skill-kit 便携包提供**，在节点 4.0 解压到 `%USERPROFILE%\.qoder-cn\tools\skill-kit\`。

## 硬依赖（节点 0 必须全部通过）

| ID | 依赖 | 用途 | 检测 | 通过条件 |
|----|------|------|------|---------|
| D1 | Qoder CN 客户端 | 加载 skill | `qoder-cn --version` | 输出版本号 |
| D2 | PowerShell | 执行安装脚本 | `$PSVersionTable.PSVersion.Major` ≥ 5 | 5.1+ |
| D3 | skill-kit 便携包 | 内含 7za、python.7z、MinGit | 检查 `assets/skill-kit/` 或 `skill-kit/assets/` | 三件套齐全 |

**不再**将 curl、tar、unzip、系统 Python、系统 git 列为硬依赖。

### D3 必备文件

| 文件 | 说明 |
|------|------|
| `7za.exe` | 解压 python.7z（PowerShell Expand-Archive 无法处理 7z） |
| `python.7z` | 便携 Python 3.12，解压后 `python/python.exe` |
| `git/MinGit-*-64-bit.zip` | 可与 `assets/git/` 共用 |

Read skill-kit `references/maintainer-bundle.md`。

## 流程内安装（节点 4，非节点 0 前置）

| 步骤 | 安装内容 | 目标路径 |
|------|---------|---------|
| 4.0 | skill-kit（Python + Git + 7za） | `%USERPROFILE%\.qoder-cn\tools\skill-kit\` |
| 4.1 | 初始化技能包全部 skill | `%USERPROFILE%\.qoder-cn\skills\` |
| 4.2 | 各 skill 的 vendor/python-packages 链接 | 便携 Python site-packages（.pth） |

安装后环境变量（用户级）：
- `QODER_TOOLS_ROOT`
- `QODER_PYTHON`
- `QODER_GIT`

## 自动化检测（节点 0）

```powershell
powershell -ExecutionPolicy Bypass -File scripts/check_system_deps.ps1 -ReportAuto
```

**禁止**在节点 0 使用 `python scripts/check_system_deps.py`（此时系统可能无 Python）。

## 安装后复检（节点 4.0 之后，可选）

```powershell
powershell -ExecutionPolicy Bypass -File scripts/run_with_kit.ps1 -ScriptPath scripts/check_system_deps.py -ScriptArgs "--report-auto","--post-kit"
```

`check_system_deps.py --post-kit` 验证 `QODER_PYTHON`、`QODER_GIT` 可用。

## 节点 0 报告模板

```
系统依赖检测报告（零预装）
════════════════════════════════════════
操作系统：     {OS}
硬依赖：
  [OK/FAIL] D1 Qoder CN
  [OK/FAIL] D2 PowerShell 5.x+
  [OK/FAIL] D3 skill-kit 便携包（7za + python.7z + MinGit）
════════════════════════════════════════
说明：Python/Git 将在节点 4.0 由 skill-kit 安装，非本阶段要求。
```

**门禁**：D1–D3 全部为 pass → 才允许进入节点 1。
