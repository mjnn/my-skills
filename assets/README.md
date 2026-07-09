# Release assets

单 skill 离线安装包：`<skill-name>-v<semver>.zip`

大体积运行时（便携 Python、MinGit 等）仅在此目录以 zip 分发，不进入 `skills/` 源码树。

解压到本机 **skill 安装根目录**（由 Agent 环境决定，例如项目 `.cursor/skills/` 或用户 `~/.qoder-cn/skills/`）：

```powershell
Expand-Archive assets\<skill>-vX.Y.Z.zip -DestinationPath <skill-root>\
```

或 sparse-checkout 源码：`skills/<域>/<skill-name>/`
