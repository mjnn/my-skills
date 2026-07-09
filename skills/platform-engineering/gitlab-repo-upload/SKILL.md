---
name: gitlab-repo-upload
description: 当用户要求将本地项目、代码或文件夹上传/推送到 GitLab 仓库时触发。涵盖 git init、.gitignore 配置、remote add、commit、push 全流程，处理企业内网自签名 SSL 证书和 token 认证等常见障碍。push 成功后支持创建 Tag、Release、上传 zip 附件和同步仓库文档。不适用于：仅克隆仓库（git clone）、仅查看仓库信息、GitHub 仓库管理、已有 git 仓库的日常 push/pull 操作、仅修改 .gitignore。
---

# GitLab 仓库上传

将本地项目首次上传到 GitLab 仓库的标准化流程，覆盖从 git init 到 push 成功的全链路。

<HARD-GATE>
1. 在用户审核 Spec 并调用 ExitSpecMode 确认前，禁止执行任何 git 写操作（init、add、commit、push）。
2. 涉及向用户收集信息（认证方式、分支名等）时，必须使用 AskUserQuestion 工具提供结构化选项，禁止纯文本提问。
3. 禁止将 .env、密钥文件、token 等敏感信息硬编码到 remote URL 后提交到仓库。remote URL 中的 token 仅用于推送，不写入任何被跟踪的文件。
</HARD-GATE>

## 能力边界

### 本技能负责
- 将本地项目首次上传到 GitLab 仓库（git init → .gitignore → remote → commit → push）
- 处理企业内网自签名 SSL 证书和 token 认证
- 创建 Tag 和 Release
- 上传 zip 附件到 Release assets（如目标为托管型仓库）
- 同步 README/CATALOG 等仓库文档（如目标为托管型仓库）

### 本技能不负责
- 已有 git 仓库的日常 push/pull → 直接使用 git 命令
- GitHub / Bitbucket 仓库管理 → 其他平台有各自的 API
- 仅克隆仓库 → 直接使用 `git clone`
- 仅查看仓库信息 → 使用 GitLab Web 界面或 API
- 项目代码开发 → 由开发型 skill 负责

## 依赖清单

| 依赖项 | 类型 | 说明 | 拉取方式 |
|--------|------|------|---------|
| skill-kit | 共享运行时 | 便携 Python/Git；由 skill-env-setup 安装 | `%USERPROFILE%\.qoder-cn\tools\skill-kit\` |
| skill-env-setup | Agent Skill | 首次环境未就绪时安装 skill-kit | 对用户说「配置 Qoder Skills 环境」 |

| git | 系统工具 | 版本控制 | 随操作系统或 Git 安装包提供 |
| curl | 系统工具 | 调用 GitLab API | 随操作系统自带，Windows 可用 PowerShell 替代 |
| AskUserQuestion | 内置工具 | 收集认证方式等信息 | 内置，无需拉取 |

## Gotchas

1. **直接 `git add .` 不先建 .gitignore** — Agent 急于完成上传，跳过 .gitignore 直接 `git add .`，导致 venv/、node_modules/、.env、__pycache__/、.DS_Store、._*（macOS 元数据）等大量不该提交的文件进入仓库。一个 Python 项目的 venv 可能有数千个文件，仓库体积膨胀且无意义。**纠正：在 `git add` 之前，必须先检查项目类型并创建/补充 .gitignore，排除依赖目录、缓存目录、敏感文件、IDE 配置、OS 元数据。**

2. **推送时才发现 SSL 证书问题** — 企业内网 GitLab（如 `*.csvw.com`）常用自签名证书，Agent 没有提前处理，推送失败后才用 `git config http.sslVerify false` 补救。这个错误导致推送流程被打断，用户体验差。**纠正：在前置检查阶段检测 remote URL 是否为内网地址（非 github.com/gitlab.com），若是则提前配置 `http.sslVerify false` 并告知用户原因。**

3. **推送时才发现认证问题** — Agent 没有在流程开始时询问用户是否有 GitLab 访问凭据，推送失败后才要求提供 token。导致推送流程被打断两次（SSL + 认证）。**纠正：在信息收集阶段使用 AskUserQuestion 工具询问用户认证方式（个人访问令牌 / 用户名密码 / SSH 密钥），提前准备好凭据。**

4. **提交了 .env 敏感文件** — .env 文件可能包含数据库密码、API key、secret 等敏感信息，Agent 没有检查就直接提交，造成安全隐患。即使后续删除，git 历史中仍可追溯。**纠正：在 .gitignore 中必须包含 `.env`，在 `git add` 后 `git status` 检查中确认 .env 未被跟踪。若已被跟踪，用 `git rm --cached .env` 移除后再提交。**

5. **没确认远程仓库状态就直接 push** — 如果远程仓库已有提交（如初始化时生成了 README），直接 push 会被拒绝（non-fast-forward）。Agent 默认远程仓库是空的，不检查就推。**纠正：在 push 前先执行 `git ls-remote origin` 检查远程是否有已有提交。若远程非空，需要先 `git pull --rebase origin <branch>` 或 `git push -f`（需用户确认强推）。**

6. **分支名不匹配** — `git init` 默认创建的分支可能是 master（旧版 git）或 main（新版 git），但 GitLab 项目可能配置了不同的默认分支名。Agent 不确认就直接 push，可能推到错误的分支。**纠正：在信息收集阶段确认目标分支名，用 `git branch -M <branch>` 重命名本地分支使其与远程默认分支一致。**

7. **Windows 环境下 `cd` 后 git 命令丢失上下文** — 在 Windows 的 bash 环境中，`cd "D:\path" && git status` 可能因路径分隔符或 shell 会话问题失败。**纠正：使用 `git -C <path>` 语法替代 `cd && git`，确保路径用引号包裹。**

8. **Release 创建后未将 zip 放入仓库 assets 目录** — Agent 通过 API 创建了 Release 描述但 assets=0，用户无法直接下载 zip，只能通过 git clone 拉取。**纠正：创建 Release 后必须执行三步：打包 zip（git archive 或 zip -r）→ 放入仓库 `assets/` 目录并 commit + push → 通过 GitLab API 添加 raw 链接到 Release（`POST /releases/<tag>/assets/links`，url 使用 `/-/raw/main/assets/<filename>.zip` 格式）。**

9. **uploads 格式链接被清理导致 404** — 使用 GitLab uploads API（`POST /projects/:id/uploads`）上传的文件可能被服务器清理策略删除，导致 uploads 格式链接（`/uploads/<hash>/<filename>.zip`）返回 404。这种链接不稳定，不可长期依赖。**纠正：zip 文件应放在仓库 `assets/` 目录中，通过版本控制确保持久存在。Release link 使用 `/-/raw/main/assets/<filename>.zip` 格式（浏览器已登录时 cookie 认证可直接下载）。CLI 下载使用 API 端点 `https://<host>/api/v4/projects/<project_id>/repository/files/assets%2F<filename>.zip/raw?ref=main` + `PRIVATE-TOKEN` 头认证（`/-/raw/` 端点不支持 token 头认证）。**

10. **发布后未同步仓库文档** — Agent 完成 git push + Release 创建后直接报告完成，但目标仓库的 README.md（已上架表格）、CATALOG.md（注册表）、docs/skill-browser.md（技能浏览器）中的版本号、Release 链接、Zip 下载链接均未更新，导致用户看到的版本信息与实际不一致。**纠正：push + Release 后必须检查目标仓库是否为托管型仓库（根目录有 README.md/CATALOG.md 等管理文件），若是则同步更新所有文档引用，确保版本号、Release 链接、Zip 下载链接三者一致。**

## 流程



### 步骤 0：skill-kit 就绪检查

Read skill-kit `references/preflight.md`。

```powershell
powershell -ExecutionPolicy Bypass -File "$env:USERPROFILE\.qoder-cn\tools\skill-kit\scripts\check_skill_kit_ready.ps1" -SkillDir "$env:USERPROFILE\.qoder-cn\skills\gitlab-repo-upload"
```

- 退出码 **0** → 继续
- **非 0** → 调用 AskUserQuestion（见 preflight.md）：引导用户**重新运行 skill-env-setup** 完成环境初始化，或重新检测；**禁止**使用裸 `python`/`git`/`pip`

> **便携 Git**：下文所有 `git` 命令均执行 `& $env:QODER_GIT`（或 `git -C` → `& $env:QODER_GIT -C`）。禁止假设系统 PATH 中有 git。

### 阶段一：前置检查

1. 确认项目目录存在且非空
   ```bash
   ls "<project_path>"
   ```

2. 检查是否已有 git 仓库
   ```bash
   git -C "<project_path>" status
   ```
   - 若已是 git 仓库 → 跳到阶段三（配置 remote）
   - 若不是 → 继续阶段二

3. 检测 remote URL 是否为内网地址（非 github.com / gitlab.com / bitbucket.org），若是内网则标记需要 SSL 处理

4. 检查远程仓库是否已有内容
   ```bash
   git -C "<project_path>" ls-remote "<remote_url>"
   ```
   - 若远程有提交 → 标记需要 pull/rebase 或强推
   - 若远程为空 → 正常推送

### 阶段二：信息收集

使用 AskUserQuestion 工具收集以下信息（单次调用，4 个问题）：

| 问题 | header | 选项 |
|------|--------|------|
| GitLab 认证方式是什么？ | 认证方式 | 个人访问令牌（推荐） / 用户名+密码 / SSH 密钥 |
| 目标分支名是什么？ | 分支名 | main（推荐） / master / 其他 |
| 是否需要生成 .gitignore？ | gitignore | 自动生成（推荐） / 使用项目已有的 / 不需要 |
| 项目类型是什么？ | 项目类型 | Python / Node.js / Java / 其他 |

用户通过 "Other" 可自由输入任意回答。

### 阶段三：Spec 模式计划审核

信息收集完成后，必须调用 EnterSpecMode 进入 spec 模式。

Spec 内容必须包含：
1. 项目路径、远程仓库 URL、目标分支名
2. .gitignore 策略（哪些目录/文件将被排除）
3. 认证方式与凭据处理方案（token 不写入被跟踪文件）
4. 远程仓库状态（空/非空）及对应策略
5. 预期操作步骤序列（init → gitignore → remote → add → commit → push）
6. SSL 证书处理方案（如适用）

用户审核后调用 ExitSpecMode 确认，才能进入下一阶段。

### 阶段四：执行上传

**步骤 1：初始化 git 仓库（如未初始化）**
```bash
git -C "<project_path>" init
git -C "<project_path>" branch -M "<branch_name>"
```

**步骤 2：创建/补充 .gitignore**

Read references/gitignore-templates.md 获取对应项目类型的 .gitignore 模板。

核心排除项（所有项目类型通用）：
```
# 敏感文件
.env
.env.*
*.key
*.pem
credentials*

# OS 元数据
.DS_Store
._*
Thumbs.db

# IDE
.idea/
.vscode/
*.swp

# Python
__pycache__/
*.pyc
venv/
.venv/

# Node.js
node_modules/

# 构建产物
dist/
build/
*.egg-info/
```

**步骤 3：配置 SSL（如远程为内网地址）**
```bash
git -C "<project_path>" config http.sslVerify false
```
告知用户：已禁用 SSL 证书验证，因为远程仓库使用自签名证书（企业内网常见）。

**步骤 4：添加远程仓库**
```bash
git -C "<project_path>" remote add origin "<remote_url>"
```

若使用 token 认证，remote URL 格式：
```
https://oauth2:<token>@<host>/<group>/<project>.git
```

**步骤 5：暂存文件并检查**
```bash
git -C "<project_path>" add .
git -C "<project_path>" status
```
检查 status 输出：
- 确认 .env 不在暂存区
- 确认 venv/、node_modules/、__pycache__/ 不在暂存区
- 确认无意外的大文件

若发现不该提交的文件已暂存：
```bash
git -C "<project_path>" rm --cached "<file>"
```
然后补充到 .gitignore。

**步骤 6：提交**
```bash
git -C "<project_path>" commit -m "Initial commit"
```

**步骤 7：推送**
```bash
git -C "<project_path>" push -u origin "<branch_name>"
```

### 阶段五：创建 Tag 和 Release（可选）

当用户需要为项目创建版本化 release 时（如 skill 发布到 skill-hub），执行以下步骤：

**步骤 8：创建 Tag**

```bash
git -C "<project_path>" tag "<skill-name>/v<version>"
```

- `skill-name`：skill 名称（小写，与目录名一致）
- `version`：语义化版本号（如 `0.1.0`、`1.2.3`）
- Tag 格式示例：`gitlab-repo-upload/v0.1.0`

**步骤 9：推送 Tag**

```bash
git -C "<project_path>" push origin --tags
```

**步骤 10：创建 Release（GitLab API）**

使用 GitLab API 创建 release：

```bash
curl -s -X POST "https://<host>/api/v4/projects/<project_id>/releases" \
  -H "PRIVATE-TOKEN: <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "tag_name": "<skill-name>/v<version>",
    "name": "<skill-name> v<version>",
    "description": "<release_description>"
  }'
```

**参数说明：**

| 参数 | 说明 | 示例 |
|------|------|------|
| `<host>` | GitLab 域名 | `gitlab.example.com` |
| `<project_id>` | 项目 ID（数字） | `123` |
| `<token>` | GitLab 个人访问令牌 | `glpat-xxx` |
| `<skill-name>/v<version>` | Tag 名称 | `gitlab-repo-upload/v0.1.0` |

**完整示例：**

```bash
# 创建 tag
git -C "<project_path>" tag "gitlab-repo-upload/v0.1.0"

# 推送 tag
git -C "<project_path>" push origin --tags

# 创建 release（通过 GitLab API）
curl -s -X POST "https://<host>/api/v4/projects/<project_id>/releases" \
  -H "PRIVATE-TOKEN: <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "tag_name": "gitlab-repo-upload/v0.1.0",
    "name": "gitlab-repo-upload v0.1.0",
    "description": "Initial release of gitlab-repo-upload skill"
  }'
```

**验证 Release 创建成功：**

```bash
curl -s "https://<host>/api/v4/projects/<project_id>/releases/<tag_name>" \
  -H "PRIVATE-TOKEN: <token>"
```

**Release 描述规范：**

创建 Release 时，`description` 字段不能只写 "Initial release"，必须包含技能的完整描述，供用户在 Release 页面了解技能功能。

description 必须包含以下章节：

| 章节 | 内容 |
|------|------|
| 技能描述 | 从 SKILL.md frontmatter 的 description 字段提取 |
| 核心功能 | 列出技能的主要功能点（3-8 条） |
| 质量指标 | Gotchas 数量、Eval 用例数、触发测试数（含 near-miss 数） |
| 关键 Gotchas | 列出所有 Gotchas 条目标题 |
| 拉取方式 | `git clone --branch <skill-name>/v<version> <repo-url>` |
| 技能路径 | `skills/<domain>/<skill-name>/` |

**完整示例（含描述）：**

```bash
# 创建 release（通过 GitLab API，description 包含完整技能描述）
curl -s -X POST "https://<host>/api/v4/projects/<project_id>/releases" \
  -H "PRIVATE-TOKEN: <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "tag_name": "gitlab-repo-upload/v0.2.0",
    "name": "gitlab-repo-upload v0.2.0",
    "description": "## gitlab-repo-upload v0.2.0\n\n### 技能描述\n\n将本地项目首次上传到 GitLab 仓库的标准化流程...\n\n### 核心功能\n\n- 全流程覆盖：git init -> .gitignore -> remote add -> commit -> push\n\n### 质量指标\n\n| 指标 | 数量 |\n| Gotchas | 7 条 |\n| Eval 用例 | 6 条 |\n\n### 关键 Gotchas\n\n1. 直接 git add 不先建 .gitignore 导致垃圾文件入库\n2. ...\n\n### 拉取方式\n\n```bash\ngit clone --branch gitlab-repo-upload/v0.2.0 https://<host>/ecc-2/qoder-skills.git\n```\n\n### 技能路径\n\n```\nskills/platform-engineering/gitlab-repo-upload/\n```"
  }'
```

**更新已有 Release 描述（PUT API）：**

如果 Release 已创建但描述需要更新（如补充完整描述），使用 PUT 方法：

```bash
curl -s -X PUT "https://<host>/api/v4/projects/<project_id>/releases/<skill-name>%2Fv<version>" \
  -H "PRIVATE-TOKEN: <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "description": "<new_release_description>"
  }'
```

> **注意**：此 GitLab 版本的 Release 更新使用 **PUT** 方法，不是 PATCH（PATCH 返回 404）。tag_name 中的 `/` 需 URL 编码为 `%2F`。

**删除历史版本 Release：**

发布新版本 Release 后，必须删除旧版本的 Release，确保 Release 页面只展示每个技能的最新版本。

```bash
curl -s -X DELETE "https://<host>/api/v4/projects/<project_id>/releases/<skill-name>%2Fv<old_version>" \
  -H "PRIVATE-TOKEN: <token>"
```

**示例：** 发布 `gitlab-repo-upload/v0.2.1` 后，删除 `gitlab-repo-upload/v0.2.0` 和 `gitlab-repo-upload/v0.1.0` 的 Release。

> **注意**：此操作仅删除 Release 元数据，不会删除 git tag。tag 保留在仓库中作为历史记录，但 Release 页面只展示最新版本。

**步骤 11：上传 zip 附件到 Release**

创建 Release 后必须将 zip 放入仓库 `assets/` 目录并关联到 Release，供用户直接下载（无需 git clone）。

```bash
# 1. 打包 skill 目录为 zip（从对应 tag 打包，确保版本一致）
cd "<repo_path>" && git archive --format=zip -o "assets/<skill-name>-v<version>.zip" "<skill-name>/v<version>" "skills/<domain>/<skill-name>/"

# 2. 提交并推送 zip 到仓库
git -C "<repo_path>" add "assets/<skill-name>-v<version>.zip"
git -C "<repo_path>" commit -m "Add <skill-name>-v<version>.zip to assets/"
git -C "<repo_path>" push origin main

# 3. 通过 GitLab API 添加 raw 链接到 Release
curl -s -X POST "https://<host>/api/v4/projects/<project_id>/releases/<skill-name>%2Fv<version>/assets/links" \
  -H "PRIVATE-TOKEN: <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "<skill-name>-v<version>.zip",
    "url": "https://<host>/<group>/<project>/-/raw/main/assets/<skill-name>-v<version>.zip",
    "link_type": "other"
  }'
```

> **关键**：zip 文件必须放在仓库 `assets/` 目录中，通过版本控制确保持久存在。**禁止使用** GitLab uploads API（`POST /projects/:id/uploads`），因为 uploads 目录的文件可能被服务器清理策略删除，导致链接 404。Release link 使用 `/-/raw/main/assets/<filename>.zip` 格式（浏览器已登录可访问）。CLI 下载需通过 API 端点 `https://<host>/api/v4/projects/<id>/repository/files/assets%2F<filename>.zip/raw?ref=main` + `PRIVATE-TOKEN` 头，因为 `/-/raw/` 端点不支持 header 认证。

**步骤 12：验证下载链接**

发布后必须验证 zip 下载链接可用（通过 API 端点 + token）：

```bash
curl -s -o /dev/null -w "%{http_code}" -L -k \
  -H "PRIVATE-TOKEN: <token>" \
  "https://<host>/api/v4/projects/<project_id>/repository/files/assets%2F<filename>.zip/raw?ref=main"
# 应返回 200
```

### 阶段六：文档同步（如适用）

**适用条件**：目标仓库根目录有 README.md / CATALOG.md / docs/ 等管理文件（即托管型仓库，如 skill registry）。

发布新版本后，必须同步更新以下文档：

| 文档 | 同步内容 |
|------|---------|
| README.md | 已上架 Skill 表格：版本号、Release 链接、Zip 下载链接（三者必须一致） |
| CATALOG.md | 注册表条目：版本号、描述、最后更新日期 |
| docs/skill-browser.md | 技能总览 + 详细条目：版本号、Zip 下载链接、Release 链接、Sparse Checkout 命令 |

**验证清单：**
```
- [ ] README.md 版本号已更新
- [ ] README.md Release 链接已更新
- [ ] README.md Zip 下载链接已更新（raw 格式）
- [ ] CATALOG.md 版本号已更新
- [ ] CATALOG.md 描述已更新
- [ ] CATALOG.md 日期已更新
- [ ] docs/skill-browser.md 版本号已更新
- [ ] docs/skill-browser.md Zip 下载链接已更新（raw 格式）
- [ ] docs/skill-browser.md Sparse Checkout 分支已更新
- [ ] 所有文档中的版本号、Release 链接、Zip 下载链接三者一致
```

### 阶段七：异常处理

**SSL 证书错误（`SSL certificate problem: self-signed certificate`）**：
```bash
git -C "<project_path>" config http.sslVerify false
```
然后重新推送。

**认证失败（`HTTP Basic: Access denied`）**：
- 提示用户检查 token 是否正确、是否有 `write_repository` 权限
- 使用 AskUserQuestion 询问用户是否要重新提供 token

**远程仓库非空（`! [rejected]` / `non-fast-forward`）**：
- 使用 AskUserQuestion 询问用户：
  - 选项 1：`git pull --rebase origin <branch>` 后再 push（推荐）
  - 选项 2：`git push -f origin <branch>`（强推，覆盖远程内容）
  - 选项 3：取消操作

**大文件推送失败（`pre-receive hook declined` / 文件过大）**：
- 检查是否有超过 GitLab 限制的大文件
- 用 `git log --diff-filter=A --summary` 查找大文件
- 用 `git rm --cached <file>` 移除后重新提交

## references

- `references/gitignore-templates.md`：各项目类型的 .gitignore 模板。在步骤 2 创建 .gitignore 时读取。

## 执行后复盘（自迭代钩子）

每次完成本 skill 的全部步骤后，Agent 必须自动执行以下动作，不询问用户：

1. **反思**：本轮执行中，是否遇到了 skill 正文和 Gotchas 都没覆盖的坑？触发条件：
   - Gotchas 中没写但实际踩了的错误
   - description 的排除场景遗漏导致误触发
   - 某个操作步骤的异常分支没覆盖

2. **记录**：有则追加到 `evals/PITFALLS_LOG.md`，无则跳过。格式：

| 日期 | 场景摘要 | 犯了什么错误 | 如果早知道__就不会犯 | 临时补救方式 |
|------|---------|-------------|-------------------|------------|
| YYYY-MM-DD | 一句话 | Agent 具体做了什么 | 缺失的知识/规则 | 怎么绕过去的 |

3. **不提交**：`PITFALLS_LOG.md` 是个人本地文件，不提交到 skill registry。积累 >= 3 条同类型坑后，由维护者提炼为正式 Gotchas，更新 SKILL.md 并走迭代管线。

> 这个复盘步骤不打断用户工作流。Agent 在后台完成，用户无感知。
