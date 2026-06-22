# my-skills

> 马捷个人 Skill 云端仓库  
> 多平台兼容 · 质量门控 · 宁缺毋滥

## 仓库定位

本仓库是个人 AI 编码 Skill 的统一云端归档与分发节点，支持多平台：

| 平台 | 说明 |
|------|------|
| **HanaAgent** | 基于 OpenHanako 的个人 Agent 体系，通过 `install_skill` 安装 |
| **Cursor** | AI 编辑器，通过 `.cursor/rules/` 或项目级引入 |

收录的每一个 Skill 都经过：

- **质量门控**：SKILL.md 完整性 + evals 覆盖率 + 自检机制
- **可用性验证**：至少一次端到端实战验证
- **去重审查**：与已有 Skill 的功能重叠度低于阈值

## 目录结构

```
my-skills/
├── README.md              # 本文件
├── registry.json          # Skill 注册表（含 platform 元数据）
├── .github/workflows/     # CI 流水线
├── skills/                # Skill 归档目录（多平台共用）
│   └── <skill-name>/      # 单个 Skill 目录
│       ├── SKILL.md       # 核心 Skill 定义（必需）
│       ├── evals/         # 评估用例（推荐）
│       └── assets/        # 附属资源（可选）
└── templates/             # Skill 模板与创建指南
```

## Skill 收录标准

| 维度 | 要求 |
|------|------|
| 命名规范 | 小写 + 连字符，语义明确，如 `feishu-bitable-setup` |
| SKILL.md | 包含触发条件、使用说明、参数约定、依赖声明 |
| 自检机制 | 至少一个 smoke test 或 sanity check |
| 安全审查 | 无硬编码凭证、无任意命令注入风险 |
| 功能边界 | 单一职责，不与已有 Skill 高度重叠 |

## 已收录 Skill

<!-- SKILLS_TABLE_START -->

| Skill | 平台 | 说明 |
|-------|------|------|
| [skill-publish](skills/skill-publish) | HanaAgent | 将本地高可用 Skill 发布到 mjnn/my-skills 云端仓库。 |
| [skill-bootstrap](skills/skill-bootstrap) | HanaAgent | 新建技能时的质量引导与门禁检查。 |

<!-- SKILLS_TABLE_END -->

## 快速使用

**HanaAgent**

```
install_skill from github: mjnn/my-skills/skills/<skill-name>
```

**Cursor**

将 `SKILL.md` 内容复制到 `.cursor/rules/` 目录下，或直接引入仓库子目录。

## 贡献

欢迎提交 PR，需附上：
1. Skill 的功能说明与使用场景
2. 至少一条 eval 用例
3. 目标平台（HanaAgent / Cursor / 通用）
4. 与已有 Skill 的差异说明（如有重叠）

---

*维护者：马捷（mjnn）*  
*归档原则：宁缺毋滥，质量优先*