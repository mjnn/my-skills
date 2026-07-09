# Release assets

单 skill 离线包：`<skill-name>-v<semver>.zip`（或维护过程中生成的无版本后缀 zip）。

解压到本机 **skill 安装根目录**（如 `.cursor/skills/`、`~/.cursor/skills/`）：

```powershell
Expand-Archive assets\github-connect.zip -DestinationPath $env:USERPROFILE\.cursor\skills\
```

源码安装见 [README.md](../README.md)。
