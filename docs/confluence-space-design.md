# Confluence 空间目录架构设计

> 设计文档 | 2026-07-08 | 马捷
> 状态：待实施

## 一、角色与权限矩阵

| | 技能域 Owner | 技能 User |
|---|---|---|
| **Confluence 权限** | 空间管理员（全页面读写、模板管理、权限管理） | 空间只读 + 评论 + 基于模板创建页面 |
| **GitLab 权限** | Maintainer（push、tag、release、CI/CD 配置） | 无 |
| **本地环境** | Git + Qoder CN 企业版 | Qoder CN 企业版 |
| **核心职责** | 审核需求、创建/更新技能、提交 GitLab、维护 CI/CD | 浏览技能、下载安装、提交需求 |

## 二、空间目录树

> 活跃域 4 个 + 归档域 1 个。`data-analysis` 和 `vehicle-connectivity` 已移除，后续有技能落域时再新建。

```
Skill Hub（Confluence Space）
│
├── 📄 空间首页（Home）
│   ├── 空间简介 & 角色入口（按角色跳转）
│   ├── 最新动态公告（CI/CD 同步时自动追加）
│   └── 快速搜索（按域、按关键词）
│
├── 📂 技能目录（Skill Catalog）           ← User 主要交互区
│   │
│   ├── 📄 技能总览
│   │   └── Page Properties Report 宏，自动汇总所有技能页面的属性表格
│   │       （名称 | 域 | 版本 | 一句话描述 | 下载链接 | 状态）
│   │
│   ├── 📂 平台工程（platform-engineering）    7 个技能
│   │   ├── 📄 skill-env-setup          v0.4.1
│   │   ├── 📄 skill-hub-management     v0.1.0
│   │   ├── 📄 gitlab-repo-upload       v0.3.0
│   │   ├── 📄 skill-bootstrap          v0.2.1
│   │   ├── 📄 skill-update             v0.1.0
│   │   ├── 📄 skill-discipline         v0.1.0
│   │   └── 📄 ask-before-act           v0.1.0
│   │
│   ├── 📂 通用办公（general-office）         2 个技能
│   │   ├── 📄 svw-ppt-generator        v0.1.0
│   │   └── 📄 feishu-bitable-ops       v0.1.0
│   │
│   ├── 📂 开发测试（development-testing）     4 个技能
│   │   ├── 📄 verification-before-completion  v0.1.0
│   │   ├── 📄 subagent-driven-development     v0.1.0
│   │   ├── 📄 separate-employee-extraction    v1.0.0
│   │   └── 📄 xuehaiqiang-perspective         v0.2.0
│   │
│   ├── 📂 项目管理（project-management）     2 个技能
│   │   ├── 📄 requirement-briefing     v0.1.0
│   │   └── 📄 writing-plans            v0.1.0
│   │
│   └── 📂 已归档（archive）                 历史记录，保留页面但标记 DEPRECATED
│
├── 📂 需求工坊（Requirement Workshop）       ← User 提交入口
│   ├── 📄 提交指南（如何写好技能需求）
│   ├── 📄 【模板】新增技能需求
│   │     字段：技能名称 | 建议归属域 | 需求描述 | 期望效果 | 优先级 | 提交人
│   ├── 📄 【模板】技能更新需求
│   │     字段：技能名称 | 当前版本 | 更新内容 | 更新原因 | 提交人
│   ├── 📄 需求看板
│   │   └── Confluence 表格管理状态流转：
│   │       待评审 → 设计中 → 开发中 → 已交付 / 已拒绝
│   └── 📄 需求归档（已关闭的需求）
│
├── 📂 审核专区（Review Zone）               ← Owner 专用
│   ├── 📄 审核门禁标准（7 道门禁清单）
│   ├── 📄 审核 SOP（标准操作流程）
│   │     1. 接收需求 → 2. 评估可行性 → 3. 创建/更新技能
│   │     → 4. 过门禁自检 → 5. GitLab 提交+Release
│   │     → 6. CI/CD 自动同步 Confluence → 7. 通知提交人
│   ├── 📄 待审核清单
│   └── 📄 审核记录（每次审核的决策日志）
│
├── 📂 使用指南（User Guide）
│   ├── 📄 角色与权限说明
│   ├── 📄 技能 User 快速上手（浏览→下载→安装，3 步完事）
│   ├── 📄 技能域 Owner 操作指南
│   │     前置条件、全流程操作步骤、GitLab Release 参考
│   └── 📄 FAQ
│
└── 📂 空间管理（Space Admin）               ← Owner 专用
    ├── 📄 权限矩阵
    ├── 📄 同步状态监控（CI/CD 日志链接、上次同步时间）
    └── 📄 空间公告
```

## 三、自动化同步机制

### 3.1 同步架构总览

```
┌─────────────────────── GitLab ───────────────────────┐
│                                                       │
│  Owner 操作:                                           │
│  git push + git tag skill-name/vX.X.X                 │
│  git push origin --tags                               │
│  → GitLab Release 创建（含 zip 附件）                   │
│                                                       │
│  ┌─────────────────────────────────────────┐          │
│  │  GitLab CI/CD Pipeline                  │          │
│  │  触发条件: tag push (pattern: */v*)      │          │
│  │                                         │          │
│  │  Job: sync-to-confluence                │          │
│  │  ┌───────────────────────────────────┐  │          │
│  │  │ 1. 解析 tag → skill_name, version  │  │          │
│  │  │ 2. 读取 SKILL.md（tagged commit）  │  │          │
│  │  │ 3. 解析 frontmatter + 正文         │  │          │
│  │  │ 4. 确定域（从目录路径）             │  │          │
│  │  │ 5. 获取 GitLab Release zip URL     │  │          │
│  │  │ 6. 构建 Confluence 页面内容        │  │          │
│  │  │ 7. 调用 Confluence REST API        │  │          │
│  │  │    - 查找/创建页面                  │  │          │
│  │  │    - 更新内容 + 属性 + 标签         │  │          │
│  │  │    - 发公告到空间首页               │  │          │
│  │  └───────────────────────────────────┘  │          │
│  └─────────────────────────────────────────┘          │
│                       │                               │
└───────────────────────┼───────────────────────────────┘
                        │ HTTPS (Confluence REST API)
                        ▼
┌─────────────────── Confluence ────────────────────────┐
│                                                        │
│  Space: SKILLHUB                                       │
│  ├── 技能目录/                                          │
│  │   ├── 平台工程/                                      │
│  │   │   └── skill-env-setup  ← 自动创建/更新           │
│  │   │       ├── 页面内容（来自 SKILL.md）              │
│  │   │       ├── Page Properties（版本/下载链接/状态）   │
│  │   │       └── Labels（domain:platform-engineering）  │
│  │   └── ...                                            │
│  └── 空间首页                                           │
│      └── 最新动态  ← 自动追加公告                       │
│                                                        │
└────────────────────────────────────────────────────────┘
```

### 3.2 GitLab CI/CD 配置

在仓库根目录新增 `.gitlab-ci.yml`：

```yaml
stages:
  - sync

sync-to-confluence:
  stage: sync
  image: python:3.11-slim
  rules:
    - if: $CI_COMMIT_TAG =~ /\//
  script:
    - pip install requests pyyaml markdown --quiet
    - python scripts/sync-confluence.py
  variables:
    CONFLUENCE_BASE_URL: $CONFLUENCE_BASE_URL
    CONFLUENCE_API_TOKEN: $CONFLUENCE_API_TOKEN
    CONFLUENCE_SPACE_KEY: $CONFLUENCE_SPACE_KEY
    CONFLUENCE_DOMAIN_PAGE_MAP: $CONFLUENCE_DOMAIN_PAGE_MAP
    CONFLUENCE_HOME_PAGE_ID: $CONFLUENCE_HOME_PAGE_ID
    GITLAB_API_TOKEN: $GITLAB_API_TOKEN
    GITLAB_PROJECT_ID: $GITLAB_PROJECT_ID
```

### 3.3 需要配置的 GitLab CI/CD 变量

| 变量名 | 说明 | 示例值 |
|--------|------|--------|
| `CONFLUENCE_BASE_URL` | Confluence 基础 URL | `https://confluence.csvw.com` |
| `CONFLUENCE_API_TOKEN` | Confluence PAT（Masked） | `ATATT3xFfGF0...` |
| `CONFLUENCE_SPACE_KEY` | 空间 Key | `SKILLHUB` |
| `CONFLUENCE_DOMAIN_PAGE_MAP` | 域名→父页面 ID 映射 JSON | `{"platform-engineering":"123456","general-office":"123457","development-testing":"123458","project-management":"123459","archive":"123460"}` |
| `CONFLUENCE_HOME_PAGE_ID` | 空间首页页面 ID（用于发公告） | `123450` |
| `GITLAB_API_TOKEN` | GitLab API Token（用于查 Release） | `glpat-xxxxx` |
| `GITLAB_PROJECT_ID` | 项目 ID | `ecc-2%2Fqoder-skills` 或数字 ID |

### 3.4 同步脚本设计

仓库新增 `scripts/sync-confluence.py`，结构如下：

```
scripts/sync-confluence.py
│
├── main()
│   ├── 1. 解析 tag
│   │     CI_COMMIT_TAG = "skill-env-setup/v0.4.1"
│   │     → skill_name = "skill-env-setup", version = "v0.4.1"
│   │
│   ├── 2. 定位 SKILL.md
│   │     遍历 skills/*/skill-env-setup/SKILL.md 找到文件
│   │     从路径提取 domain = "platform-engineering"
│   │
│   ├── 3. 解析 SKILL.md
│   │     用 PyYAML 解析 frontmatter → {name, description}
│   │     用 markdown 库将正文转为 HTML
│   │
│   ├── 4. 获取 GitLab Release 信息
│   │     GET /api/v4/projects/:id/releases/:tag
│   │     → 提取 zip asset 下载链接
│   │     → 提取 Release description（作为 changelog）
│   │
│   ├── 5. 构建 Confluence 页面内容
│   │     组装 Storage Format XHTML:
│   │     - 属性表格（域/版本/状态/下载链接）
│   │     - Page Properties 宏（供总览页自动汇总）
│   │     - 技能描述（frontmatter description）
│   │     - 触发场景 + 不适用场景
│   │     - 变更日志（Release description）
│   │     - 安装方式说明
│   │
│   ├── 6. 调用 Confluence API
│   │     a. GET /rest/api/content?title={skill_name}&spaceKey=SKILLHUB
│   │        → 页面已存在? 获取 page_id + current_version
│   │     b. 不存在 → POST /rest/api/content（在域父页面下创建）
│   │        存在 → PUT /rest/api/content/{page_id}（更新内容，version+1）
│   │     c. POST /rest/api/content/{page_id}/label
│   │        标签: domain:{domain}, status:published
│   │     d. PUT /rest/api/content/{page_id}/property/{key}
│   │        属性: version, download_url, release_url, last_synced
│   │
│   └── 7. 发公告
│         POST 评论到空间首页
│         内容: "📌 [{skill_name}] {version} 已同步 — {一句话描述}"
│         幂等检查: 搜索已有评论，避免重复发
│
├── 错误处理
│   ├── Confluence API 5xx → 重试 3 次，指数退避
│   ├── SKILL.md 未找到 → pipeline fail，Owner 收到 GitLab 通知
│   └── 域父页面 ID 未配置 → pipeline fail，提示补充 CI/CD 变量
│
└── 幂等性保证
    同一个 tag 重复触发 pipeline，结果一致：
    - 页面已存在则更新（不重复创建）
    - 公告评论检查是否已存在相同内容（避免重复发）
```

### 3.5 Confluence API 调用清单

| 步骤 | HTTP | Endpoint | 用途 |
|------|------|----------|------|
| 查找页面 | GET | `/rest/api/content?title={name}&spaceKey={key}&expand=version,body.storage` | 判断技能页是否存在 |
| 创建页面 | POST | `/rest/api/content` | 在域父页面下新建技能详情页 |
| 更新页面 | PUT | `/rest/api/content/{id}` | 更新技能详情页内容（需带 version 号） |
| 添加标签 | POST | `/rest/api/content/{id}/label` | 打 domain 和 status 标签 |
| 设置属性 | PUT | `/rest/api/content/{id}/property/{key}` | 存 version/download_url 等元数据 |
| 发公告评论 | POST | `/rest/api/content/{home_page_id}/comment` | 在空间首页追加同步公告 |
| 查 Release | GET | `/api/v4/projects/{id}/releases/{tag}` | 从 GitLab 获取 zip 链接和 changelog |

### 3.6 SKILL.md → Confluence 页面内容映射

```
SKILL.md 结构                    →    Confluence Storage Format
─────────────────────────────────────────────────────────────
YAML frontmatter:
  name: skill-env-setup          →    页面标题
  description: "..."             →    「技能描述」段落

正文:
  ## 触发场景                     →    <h2>触发场景</h2>
  Use when the user mentions...  →    <p>...</p>

  ## 不适用场景                   →    <h2>不适用场景</h2>
  不适用于：...                   →    <p>...</p>

  ## Gotchas                     →    <h2>注意事项</h2>
  - 事项1                        →    <ul><li>事项1</li>...

  ## 工作流程                     →    <h2>工作流程</h2>
  ### Stage 1: ...               →    <h3>Stage 1: ...</h3>

  ```bash                        →    <ac:structured-macro ac:name="code">
  code block                        <ac:plain-text-body><![CDATA[...]]></...>
  ```                            </ac:structured-macro>

GitLab Release:
  zip asset URL                  →    Page Properties: download_url
  Release description            →    「变更日志」段落
  tag name (vX.X.X)             →    Page Properties: version
```

### 3.7 技能详情页模板（自动生成）

同步脚本生成的每个技能详情页统一结构：

```
┌─────────────────────────────────────────────┐
│  [skill-env-setup]                    标签:  │
│  domain:platform-engineering status:published│
├─────────────────────────────────────────────┤
│  Page Properties（供总览宏自动汇总）           │
│  ├── 域：        platform-engineering         │
│  ├── 版本：      v0.4.1                       │
│  ├── 一句话描述： 环境初始化+门禁+技能包        │
│  ├── 状态：      已发布                        │
│  └── 下载链接：   → GitLab Release zip         │
├─────────────────────────────────────────────┤
│  技能描述                                     │
│  7 节点门禁工作流环境初始化...                  │
├─────────────────────────────────────────────┤
│  触发场景                                     │
│  Use when the user mentions 环境初始化...      │
├─────────────────────────────────────────────┤
│  不适用场景                                   │
│  不适用于：已配置环境的日常单 skill 更新...     │
├─────────────────────────────────────────────┤
│  变更日志                                     │
│  v0.4.1 (2026-07-08) 新增 skill-hub-management │
│  v0.4.0 (2026-07-05) 初始化技能包重组           │
├─────────────────────────────────────────────┤
│  安装方式                                     │
│  1. 下载 zip → 解压到 ~/.qoder-cn/skills/      │
│  2. 或 git sparse checkout                    │
├─────────────────────────────────────────────┤
│  评论区（User 反馈、提问）                     │
└─────────────────────────────────────────────┘
```

## 四、端到端工作流（含自动化同步）

```
┌──────────┐                    ┌──────────────┐                 ┌─────────┐    ┌────────────┐
│ 技能 User │                    │ 技能域 Owner  │                 │ GitLab  │    │ Confluence │
└────┬─────┘                    └──────┬───────┘                 └────┬────┘    └─────┬──────┘
     │                                 │                              │              │
     │ 1. 需求工坊提交需求（填模板）     │                              │              │
     │────────────────────────────────►│                              │              │
     │                                 │                              │              │
     │                                 │ 2. 审核专区评审               │              │
     │                                 │ 3. 创建/更新技能（本地）       │              │
     │                                 │ 4. 过 7 道门禁自检            │              │
     │                                 │                              │              │
     │                                 │ 5. git push + tag + release   │              │
     │                                 │─────────────────────────────►│              │
     │                                 │                              │              │
     │                                 │                              │ 6. CI/CD 自动  │
     │                                 │                              │   触发同步     │
     │                                 │                              │──────────────►│
     │                                 │                              │              │
     │                                 │                              │              │ 7. 自动创建/
     │                                 │                              │              │    更新技能
     │                                 │                              │              │    详情页
     │                                 │                              │              │    + 总览表
     │                                 │                              │              │    + 首页公告
     │                                 │                              │              │
     │ 8. 收到公告通知，浏览技能目录      │                              │              │
     │ 9. 点击下载链接 → GitLab Release │                              │              │
     │◄─────────────────────────────────│──────────────────────────────│◄─────────────│
     │                                 │                              │              │
     │ 10. 安装到本地 ~/.qoder-cn/skills/                              │              │
     │ 11. 在技能详情页评论区反馈        │                              │              │
     │────────────────────────────────►│                              │              │
```

## 五、Confluence 特性利用

| 特性 | 用途 |
|------|------|
| **Page Properties + Report 宏** | 技能详情页填属性，总览页自动生成汇总表格，同步脚本自动写入属性，无需手工维护 |
| **页面模板** | 预置「新增技能需求」「技能更新需求」两个模板，User 一键创建。技能详情页不需要模板——由同步脚本自动生成 |
| **标签** | 同步脚本自动打标签：`domain:{域名}`、`status:published`，支持按域快速筛选 |
| **空间权限** | Owner 组 = 管理员；User 组 = 只读+评论+基于模板创建 |
| **页面评论** | User 在技能详情页底部评论区反馈，Owner 收到通知后处理 |

## 六、设计要点总结

1. **GitLab 是唯一数据源** — SKILL.md 和 Release zip 都在 GitLab，Confluence 只做展示镜像
2. **Tag 驱动同步** — Owner 只需 `git push --tags`，CI/CD 自动完成 Confluence 同步，零额外操作
3. **幂等安全** — 同一个 tag 重复推送不会产生重复页面或重复公告
4. **User 零门槛** — 全程不需要 GitLab 账号和 Git，浏览/下载/提需求全在 Confluence 完成
5. **Page Properties 自动汇总** — 总览表格随技能页面同步自动更新，Owner 无需手工维护目录

## 七、GitLab 仓库待清理项

两个空域在仓库中也有残留引用，实施时需要清理：

| 文件 | 引用内容 | 清理动作 |
|------|---------|---------|
| `skills/data-analysis/` | 空目录 | 删除目录 |
| `skills/vehicle-connectivity/` | 空目录 | 删除目录 |
| `CATALOG.md` L63 | `### data-analysis` | 删除该节 |
| `README.md` L245, L290 | 目录树 + 域统计表 | 删除相关行 |
| `docs/skill-browser.md` L386-399 | data-analysis 章节 | 删除该节 |
| `docs/lifecycle-spec.md` L113 | 目录结构示例 | 删除该行 |
| `skill-bootstrap/SKILL.md` L66 | 可用域分类列表 | 删除 `data-analysis` 条目 |
| `skill-update/SKILL.md` L71 | 可用域分类列表 | 删除 `data-analysis` 条目 |

## 八、实施计划

1. **清理仓库** — 删除 `data-analysis` 和 `vehicle-connectivity` 空域目录及所有文档引用
2. **编写同步脚本** — 在 `scripts/sync-confluence.py` 实现上述设计
3. **配置 CI/CD** — 在仓库根目录添加 `.gitlab-ci.yml`，在 GitLab Settings → CI/CD → Variables 中配置 7 个变量
4. **创建 Confluence 空间** — 按目录树创建空间结构，获取各域父页面 ID 填入 CI/CD 变量
5. **验证** — 推送一个测试 tag，确认 Confluence 页面自动创建/更新、公告自动发布
