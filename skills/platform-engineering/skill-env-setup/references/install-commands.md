# 安装命令参考

> Read this when: 节点 4「自动安装」阶段

**前置条件**：节点 0 硬依赖 pass（Qoder CN + PowerShell + skill-kit 包内资源齐全）；节点 3 Spec 已确认。

**禁止**：winget、外网下载、假设系统已有 `python`/`git`/`pip`。

## 固定安装顺序

### 4.0 skill-kit 便携工具链（最先执行）

```powershell
# 优先使用已安装的 skill-kit skill；否则 skill-env-setup 内置 assets
$kitScript = "$env:USERPROFILE\.qoder-cn\skills\skill-kit\scripts\install_skill_kit.ps1"
if (-not (Test-Path $kitScript)) {
    $kitScript = Join-Path (Split-Path $PSScriptRoot -Parent) "..\skill-kit\scripts\install_skill_kit.ps1"
}
powershell -ExecutionPolicy Bypass -File $kitScript -AssetsRoot (Join-Path (Split-Path $PSScriptRoot -Parent) "assets\skill-kit")
```

验证：

```powershell
& $env:QODER_PYTHON -c "import sys; print(sys.executable)"
& $env:QODER_GIT --version
```

Read skill-kit `references/python-bundle.md`。

### 4.1 创建 skill 目录

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.qoder-cn\skills"
```

### 4.2 Git 全局身份

```powershell
& $env:QODER_GIT config --global user.name "<用户名>"
& $env:QODER_GIT config --global user.email "<邮箱>"
```

### 4.3 GITLAB_TOKEN

```powershell
powershell -ExecutionPolicy Bypass -File scripts/set_gitlab_token.ps1 -Token "<token>"
```

### 4.4 内网 SSL

```powershell
& $env:QODER_GIT config --global http.sslVerify false
```

### 4.5 初始化技能包 — 全量安装

```powershell
powershell -ExecutionPolicy Bypass -File scripts/run_with_kit.ps1 `
  -ScriptPath scripts/install_init_skills.py
```

- 源：`assets/init-skills/init-skills-bundle.zip`（或 `初始化技能包.zip`）
- 目标：`%USERPROFILE%\.qoder-cn\skills\{skill-name}\`

### 4.6 链接各 skill 的 Python vendor 包

```powershell
powershell -ExecutionPolicy Bypass -File scripts/init_all_skill_runtimes.ps1
```

对每个含 `vendor/python-packages/` 的 skill 写入便携 Python 的 `.pth` 文件。

### 4.7 本地 SKILL.md 验证

对每个 `{skill-name}` 检查 SKILL.md 含 `name` 与 `description`。

---

## 节点 5：GitLab 验证

```powershell
powershell -ExecutionPolicy Bypass -File scripts/run_with_kit.ps1 `
  -ScriptPath scripts/check_gitlab_access.py -ScriptArgs "--report-auto"
```

Read references/gitlab-permission-checklist.md。

---

## 节点 6：版本升级（用户确认后）

使用便携 Git + 内网 API；解压 skill zip 用 `Expand-Archive` 或 `$env:QODER_PYTHON -m zipfile`（**不用**系统 tar）。

```powershell
$token = [Environment]::GetEnvironmentVariable('GITLAB_TOKEN', 'User')
# API 下载可用 PowerShell Invoke-RestMethod 或便携 Python urllib（check_gitlab_access 同款）
Expand-Archive skill.zip -DestinationPath "$env:USERPROFILE\.qoder-cn\skills\<skill-name>" -Force
powershell -ExecutionPolicy Bypass -File scripts/init_all_skill_runtimes.ps1
```
