# 便携 Python 包规范（python.7z）

> Read this when: 准备或验证 python.7z 内容

## 来源与版本

- 参考结构：`D:\cursor_project\skill_manager\python.7z`（维护者本地路径，不写入 skill 正文发布物）
- 解压后顶层目录名：**`python/`**
- 可执行文件：`python/python.exe`
- 版本：Python **3.12** x64（与参考包一致）

## 解压目标

```
%USERPROFILE%\.qoder-cn\tools\skill-kit\python\
├── python.exe
├── Lib\
│   └── site-packages\    # 共享 + 各 skill 的 .pth 链接
└── ...
```

## site-packages 扩展方式

**禁止**在目标机器上 `pip install`。

各 skill 在 `vendor/python-packages/<包名>/` 放置已解压的 wheel 内容，由 `init_skill_python.ps1` 写入：

```
Lib/site-packages/qoder-skill-{skill-name}.pth
```

`.pth` 文件内容为该 skill 的 `vendor/python-packages` 绝对路径（一行一路径）。

## 验证命令（安装后）

```powershell
& "$env:USERPROFILE\.qoder-cn\tools\skill-kit\python\python.exe" -c "import sys; print(sys.version); print(sys.executable)"
```
