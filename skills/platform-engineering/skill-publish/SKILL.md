---
name: skill-publish
description: 将本地高可用 Skill 发布到 mjnn/my-skills 云端仓库。当用户说「发布这个skill」「上传到my-skills」「入库」「推送到skill仓库」「把这个skill传到云端」时触发。不适用于：创建新 skill（走 skill-bootstrap）、修改已有 skill 内容、纯本地 skill 质量审计。
default-enabled: false
---

# Skill 云端发布

> 将经过质量门控验证的高可用 Skill 归档到 mjnn/my-skills 云端仓库，同步更新 registry。

<HARD-GATE>
禁止在完成全部质量验证（第三步）之前执行任何 GitHub 上传操作。禁止上传未通过安全审查的 skill。
</HARD-GATE>

## Gotchas

Agent 在执行 skill 发布时会反复犯以下错误：

1. **跳过质量门禁直接上传** — Agent 拿到 skill 路径后直接调 GitHub API 上传，没有先跑质量检查。纠正：必须先完成第三步全部验证，任一不通过则中止。
2. **上传后忘记更新 registry.json** — 文件传上去了但 registry 里没有登记，导致 skill 在索引中不可见。纠正：上传完成后必须更新 registry.json 并提交。
3. **目录名与 SKILL.md 的 name 字段不一致** — 本地改过目录名但没同步改 name，上传后产生歧义。纠正：上传前校验 `dirname === name`。
4. **上传了不该上传的文件** — 把 `PITFALLS_LOG.md`、`_cleanup/`、临时文件一起推到云端。纠正：只上传 `SKILL.md`、`evals/`、`references/`、`scripts/`、`assets/`，过滤 `PITFALLS_LOG.md`、`.` 开头的隐藏文件、`_` 开头的本地目录。
5. **覆盖已有 skill 不警告** — 目标路径已存在时直接覆盖，不告知用户。纠正：上传前检查目标路径是否存在，存在则询问用户是覆盖还是跳过。
6. **commit message 太随意** — 写 "update" "fix" 这种无意义信息。纠正：commit message 必须包含 skill 名称、版本号、变更摘要。
7. **不验证 GitHub 仓库可访问性** — 直接调 API 假设仓库存在且可写入。纠正：上传前先验证 `mjnn/my-skills` 仓库存在且可访问。
8. **本机用 HTTPS push 超时** — 443 可能不通。**纠正：remote 设为 `git@github.com:mjnn/my-skills.git`；推送前走 **github-connect** 验收 `ssh -T`（账号 mjnn，指纹见 reference）。**

## 本机 GitHub 连接（已配置）

| 项 | 值 |
|----|-----|
| 仓库 | `git@github.com:mjnn/my-skills.git` |
| SSH 密钥 | `~/.ssh/id_ed25519_github` |
| 账号 | `mjnn` |
| 指纹 | `SHA256:NtjZ5te0PJybwqFJdXpSLjEaVki+FAWOIf5//tbXOOA` |

推送前：`ssh -T git@github.com` 含 `Hi mjnn`；`git remote -v` 为 SSH URL。详见 **github-connect** `reference.md`。

## 流程

### 第一步：确认发布目标

Agent 向用户确认：
1. **Skill 本地路径**：位于 `~/.hanako/skills/<skill-name>/` 或用户指定的路径
2. **版本号**：语义化版本（如 `v1.0.0`），如果 SKILL.md 未标注则询问用户

如果用户只说"发布这个 skill"但没给路径，Agent 应根据当前上下文推断（如刚创建的 skill、刚修改的 skill），推断不出则询问。

### 第二步：读取并校验本地 Skill

读取本地 skill 目录下的 `SKILL.md`，逐项验证：

```
[ ] frontmatter 包含 name 和 description
[ ] name 字段与父目录名完全一致
[ ] 正文末尾包含「执行后复盘（自迭代钩子）」章节
[ ] 无硬编码密钥/密码/Token（搜索 common patterns：api_key=、token:、secret=、Bearer、Authorization:）
[ ] 正文 ≤ 500 行（超出部分已拆分到 references/）
```

任意一项不通过 → 报告不通过项，中止发布。

### 第三步：收集待上传文件

遍历本地 skill 目录，收集以下文件：

| 包含 | 排除 |
|------|------|
| `SKILL.md` | `PITFALLS_LOG.md` |
| `evals/` 目录下所有文件 | `_` 开头的目录（如 `_cleanup/`、`_snapshots/`） |
| `references/` 目录下所有文件 | `.` 开头的隐藏文件 |
| `scripts/` 目录下所有文件 | `node_modules/` |
| `assets/` 目录下所有文件 | 任何大于 1MB 的二进制文件（提醒用户确认） |

### 第四步：检查远程冲突

通过 GitHub API 检查 `mjnn/my-skills` 仓库中 `skills/<skill-name>/` 是否已存在：

- **不存在** → 继续
- **已存在** → 列出已有文件列表，使用 AskUserQuestion 询问用户：覆盖 / 跳过 / 取消

### 第五步：上传到 GitHub

**本机优先 git push**（SSH remote，见上文「本机 GitHub 连接」）；API/MCP 为备选。

使用 GitHub MCP 工具 `push_files` 或 `git push` 到 `mjnn/my-skills`：

```
owner: mjnn
repo: my-skills
branch: main
路径前缀: skills/<skill-name>/
```

commit message 格式：
```
publish: <skill-name> v<version> — <一句话摘要>
```

示例：
```
publish: feishu-bitable-setup v1.0.0 — 飞书多维表格快速搭建
```

### 第六步：更新 registry.json

1. 获取当前 `registry.json`（路径：仓库根目录 `registry.json`）
2. 检查该 skill 是否已在 registry 中：
   - **已在** → 更新 version、updated 字段
   - **不在** → 追加新条目
3. 条目格式：

```json
{
  "name": "<skill-name>",
  "platform": "<hana | cursor | universal>",
  "description": "<从 SKILL.md description 提取>",
  "version": "<version>",
  "path": "skills/<skill-name>",
  "quality": {
    "gated": true,
    "evalCoverage": "<eval 用例数 + 触发测试数>",
    "securityReviewed": true
  }
}
```

4. 单独提交 registry.json，commit message：
```
registry: add/update <skill-name> v<version>
```

### 第七步：输出发布报告

```
✅ 发布完成：<skill-name> v<version>

平台：<hana | cursor | universal>
上传文件：N 个
Registry：已更新
GitHub：https://github.com/mjnn/my-skills/tree/main/skills/<skill-name>
```

## 异常处理

| 场景 | 处理方式 |
|------|---------|
| SKILL.md 不存在 | 报告路径错误，中止 |
| 质量验证不通过 | 列出不通过项，中止，建议修复后重试 |
| GitHub API 不可用 | 报告网络错误，建议稍后重试 |
| 仓库不存在 | 报告仓库可能已被删除或重命名，建议检查 https://github.com/mjnn/my-skills |
| 文件上传部分失败 | 报告已成功和失败的文件，不更新 registry，建议修复后重试 |
| 用户中断 | 已上传的文件不回滚（Git 历史可追溯），做清理提示 |

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

3. **不提交**：`PITFALLS_LOG.md` 是个人本地文件，不提交到 skill registry。积累 ≥ 3 条同类型坑后，由维护者提炼为正式 Gotchas，更新 SKILL.md 并走迭代管线。

> 这个复盘步骤不打断用户工作流。Agent 在后台完成，用户无感知。
