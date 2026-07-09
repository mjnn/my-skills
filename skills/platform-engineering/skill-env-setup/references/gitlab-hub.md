# 内网 Skill Hub（GitLab）

> Read this when: 需要克隆仓库、拉取 skill、或向 Hub 贡献 skill 时

## 仓库地址

**内网 Skill Hub GitLab 根路径：**

```
https://epfa-gitlab.csvw.com/ecc-2
```

**主仓库（qoder-skills）：**

```
https://epfa-gitlab.csvw.com/ecc-2/qoder-skills.git
```

## 认证

- 克隆、拉取 Zip、贡献 MR 均需要 GitLab 凭据。
- 推荐在环境初始化阶段配置 **全量权限 Personal Access Token**，写入用户环境变量 `GITLAB_TOKEN`。
- Token 创建入口：GitLab → User Settings → Access Tokens → 勾选 `api`、`read_repository`、`write_repository`（或等效全量权限）。

## 内网 SSL

企业内网 GitLab 常使用自签名证书。克隆前可执行：

```bash
git config --global http.sslVerify false
```

并告知用户原因。
