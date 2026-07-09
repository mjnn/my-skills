---
name: skill-hub-management
description: >-
  管理 Qoder Skills Hub 仓库本身：一致性检查、新技能注册、多文档同步、本地安装。
  Use when the user mentions 技能仓库管理、一致性检查、注册新技能、同步文档、skills 目录和 README 不一致、
  技能浏览器和 CATALOG 不一致、注册 skill、skill hub 管理、仓库一致性、同步 skill-browser、同步 CATALOG。
  不适用于：创建新 skill 的具体内容编写（走 skill-bootstrap）、更新已有 skill 的具体内容（走 skill-update）、
  Git 仓库上传（走 gitlab-repo-upload）、纯 Git 操作（commit/push/tag/release）。
---

# Skill Hub 管理

管理 `qoder-skills` 仓库的元数据一致性、技能注册流程和文档同步。

## 能力边界

| 负责 | 不负责 |
|------|--------|
  一致性检查（README/技能浏览器/CATALOG/assets/skills） | 编写 Skill 的具体业务逻辑 |
  新技能注册到多份文档 | 单个 Skill 的 eval 编写 |
  文档描述同步（多文档间描述对齐） | Git 仓库上传（gitlab-repo-upload） |
  技能安装到本地 `~/.qoder-cn/skills/` | Release 创建后的 zip 内容审核 |

## Gotchas

1. **只改目录树不改描述表** — 更新了 README.md 目录结构，但 CATALOG.md 描述未同步，导致用户看到「有这个技能但描述是旧的」。**纠正：任何涉及技能增删改的修改，必须同时更新 README.md 目录树、CATALOG.md 目录表、skill-browser.md 总览表和详细描述。**

2. **skill-browser.md 中只更新总览表忘记详细描述** — 顶部表格改了，但下方折叠详情区的描述还是旧的。**纠正：skill-browser.md 中有两处描述（总览表 + 详细区），修改时两处必须同步。**

3. **README 目录树和实际 skills/ 目录不一致** — 文档中的目录结构落后于实际文件系统，用户按文档拉取命令找不到 skill。**纠正：每次修改前先 `ls skills/` 核对实际目录，再写入文档。**

4. **Release 描述和 SKILL.md description 不一致** — Release 页面的描述是手动写的，技能更新后忘记同步。**纠正：技能注册或修改后，通过 GitLab API PUT `/releases/:tag_name` 更新 Release 描述。**

5. **本地安装只复制 SKILL.md 忘记 references/scripts** — 用户把 zip 解压到 `~/.qoder-cn/skills/`，但只有 SKILL.md 没有 references/，运行时找不到参考文件。**纠正：本地安装时必须完整复制整个 skill 目录（含 references、scripts、evals）。**

6. **一致性检查只读不写** — 检查出 10 处不一致但只修了一半，剩余未修导致下次检查时又报同样的错。**纠正：一致性检查报告必须列出「已发现的不一致 → 修正措施 → 验证结果」三步闭环。**

## 流程



### 步骤 0：skill-kit 就绪检查

Read skill-kit `references/preflight.md`。

```powershell
powershell -ExecutionPolicy Bypass -File "$env:USERPROFILE\.qoder-cn\tools\skill-kit\scripts\check_skill_kit_ready.ps1" -SkillDir "$env:USERPROFILE\.qoder-cn\skills\skill-hub-management"
```

- 退出码 **0** → 继续
- **非 0** → 调用 AskUserQuestion（见 preflight.md）：引导用户**重新运行 skill-env-setup** 完成环境初始化，或重新检测；**禁止**使用裸 `python`/`git`/`pip`

### 阶段 1：确认任务类型

调用 AskUserQuestion（1 个问题）：

| 问题 | header | 选项 |
|------|--------|------|
| 本次 Skill Hub 管理任务？ | 任务类型 | 一致性检查 / 注册新技能 / 同步文档描述 / 安装技能到本地 |

### 阶段 2：一致性检查

**触发条件**：用户要求"检查一致性"、"skills 和 README 不一致"、"仓库有没有问题"。

步骤：

1. **读取多份文档**
   - `README.md` → 提取目录树结构
   - `CATALOG.md` → 提取目录表和域分类表
   - `docs/skill-browser.md` → 提取总览表和详细描述
   - `assets/` → 列出所有 zip 文件
   - `skills/` → 列出所有实际目录

2. **比对规则**
   - skills/ 下的每个目录 → 必须在 README.md 目录树中出现
   - skills/ 下的每个目录 → 必须在 CATALOG.md 目录表中出现
   - skills/ 下的每个目录 → 必须在 skill-browser.md 总览表中出现
   - assets/ 下的每个 zip → 必须在 skill-browser.md 中可下载
   - CATALOG.md 描述 ↔ skill-browser.md 描述 → 必须一致

3. **输出报告**
   - 不一致数量
   - 每项不一致的：位置、预期值、实际值
   - 修正建议

### 阶段 3：注册新技能

**触发条件**：用户提供了新 skill 的 zip 或目录，要求"注册到仓库"。

步骤：

1. 确认 skill 所在域（6 个域之一）
2. 将 skill 目录移动到 `skills/{domain}/{skill-name}/`
3. 将 zip 复制到 `assets/{skill-name}-v{version}.zip`
4. 更新 CATALOG.md
   - 目录表添加一行
   - 对应域分类表添加一行
   - 更新统计数据
5. 更新 README.md
   - 目录树中添加 skill 目录
6. 更新 skill-browser.md
   - 总览表添加一行
   - 对应域的详细描述区添加完整条目（含 zip 下载链接、单技能拉取命令）
7. 创建 Tag `skill-name/v{version}`
8. 创建 Release（含描述和 zip asset）
9. 提交并推送

### 阶段 4：同步文档描述

**触发条件**：用户说"描述不一致"、"同步一下文档"。

步骤：
1. 以 SKILL.md 中的 description 为基准
2. 检查 CATALOG.md 和 skill-browser.md 中的描述是否与之一致
3. 如果不一致，统一更新为 SKILL.md 中的描述
4. 提交并推送

### 阶段 5：安装技能到本地

**触发条件**：用户说"安装到本地"、"放到我电脑上"。

步骤：
1. 确认目标路径：`~/.qoder-cn/skills/{skill-name}/`
2. 从仓库复制完整目录（含 references、scripts、evals）
3. 验证 SKILL.md 存在且可读

## 代码内调用

```python
import os
from pathlib import Path

def check_consistency(repo_root: str) -> dict:
    """检查仓库一致性，返回不一致项列表。"""
    skills_dir = Path(repo_root) / "skills"
    readme = Path(repo_root) / "README.md"
    catalog = Path(repo_root) / "CATALOG.md"
    browser = Path(repo_root) / "docs" / "skill-browser.md"
    assets_dir = Path(repo_root) / "assets"
    
    issues = []
    # 读取 skills/ 实际目录
    actual_skills = {d.name for d in skills_dir.iterdir() if d.is_dir()}
    # 读取 README 目录树
    # 读取 CATALOG 目录表
    # 比对并收集 issues
    return {"issues": issues, "count": len(issues)}

def install_skill_local(skill_name: str, version: str, target_dir: str = "~/.qoder-cn/skills"):
    """将仓库中的 skill 安装到本地用户目录。"""
    # 从 skills/ 复制完整目录到 target_dir
    pass
```

## references

- `references/consistency-check.md`：一致性检查清单和比对脚本（详细规则）

## 执行后复盘（自迭代钩子）

每次完成 Skill Hub 管理任务后自动执行：

1. **反思**：是否遗漏了任何文档同步？是否有新的不一致未被检测到？
2. **记录**：有则追加 `evals/PITFALLS_LOG.md`
3. **不提交**：`PITFALLS_LOG.md` 仅本地，不上传 registry


## 依赖清单

| 依赖项 | 类型 | 说明 | 拉取方式 |
|--------|------|------|---------|
| skill-kit | 共享运行时 | 便携 Python/Git；由 skill-env-setup 安装 | `%USERPROFILE%\.qoder-cn\tools\skill-kit\` |
| skill-env-setup | Agent Skill | 首次环境未就绪时安装 skill-kit | 对用户说「配置 Qoder Skills 环境」 |
