# 内置 Git 便携包（企业内网、无需管理员权限）

本目录存放 **MinGit 便携版** zip，供企业内网用户在**无管理员权限**的情况下使用 Git。

## 为什么用便携版

标准 `Git-*-64-bit.exe` 安装程序会写入 `C:\Program Files\` 并修改系统 PATH，**需要管理员权限**。企业内网用户通常没有该权限。

MinGit 便携版解压到用户目录即可使用，**仅需用户级 PATH**，不涉及系统级安装。

## 内置文件

| 平台 | 文件名 | 说明 |
|------|--------|------|
| Windows x64 | `MinGit-2.47.1.2-64-bit.zip` | Git for Windows MinGit v2.47.1.2 |

## 安装位置

解压目标（由 `scripts/install_git_windows.ps1` 自动处理）：

```
%USERPROFILE%\.qoder-cn\tools\git\
```

并将 `%USERPROFILE%\.qoder-cn\tools\git\cmd` 加入**用户环境变量 PATH**。

## 使用方式

```powershell
powershell -ExecutionPolicy Bypass -File scripts/install_git_windows.ps1
git --version
```

> Agent 安装时优先使用此便携包，**禁止**使用 `winget`、标准 `.exe` 安装程序或访问外网下载。
