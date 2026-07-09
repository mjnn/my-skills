# Release assets

单 skill 离线安装包，命名：`<skill-name>-v<semver>.zip`。

大体积运行时（`skill-kit` 的 Python/MinGit、`skill-env-setup` 初始化包）**仅**在此目录提供 zip，不进入 `skills/` 源码树，避免 Git 膨胀。

安装示例（Qoder CN）：

```powershell
Expand-Archive assets\skill-env-setup-v0.5.0.zip -DestinationPath $env:USERPROFILE\.qoder-cn\skills\
```

Cursor 用户推荐直接克隆或 sparse-checkout `skills/<域>/<skill-name>/`。
