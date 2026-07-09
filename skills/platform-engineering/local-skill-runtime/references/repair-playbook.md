# 修复剧本（Repair Playbook）

> Read this when: 节点 3 EnterSpecMode 或节点 4 执行 repair

## 剧本 A：skill-kit 未安装（diagnose exit 1）

**症状**：`reason = skill-kit not installed` 或 `QODER_PYTHON not functional`

**Spec 内容**：
1. 说明需完整 onboarding，非本 skill 可独立修复
2. 引导用户在新对话触发 **skill-env-setup**

**AskUserQuestion**：

| 问题 | header | 选项 |
|------|--------|------|
| skill-kit 未安装，无法做本地运行时修复。如何处理？ | Kit 缺失 | 运行 skill-env-setup 完整初始化（推荐）/ 取消 |

**禁止**：winget install python/git、使用系统 python、仅 mkdir 不装 kit

---

## 剧本 B：vendor 未链接（diagnose exit 2，vendor_unlinked）

**症状**：`scan.vendor_unlinked` 非空；业务 skill 步骤 0 退出码 **2**

**Spec 内容**：
1. 列出未链接 skill 名称
2. 计划：`repair_local_runtime.ps1 -RelinkSkills @(...)` 或 `-RelinkAll`
3. 修复后节点 5 复检 diagnose

**命令示例**：

```powershell
powershell -ExecutionPolicy Bypass -File scripts/repair_local_runtime.ps1 -RelinkAll
```

或指定 skill：

```powershell
powershell -ExecutionPolicy Bypass -File scripts/repair_local_runtime.ps1 -RelinkSkills @("feishu-bitable-ops","svw-ppt-generator")
```

**AskUserQuestion**（节点 2）：

| 问题 | header | 选项 |
|------|--------|------|
| 发现 N 个 skill 的 Python vendor 未链接到便携环境。如何修复？ | Vendor 修复 | 全部重新链接（推荐）/ 仅修复我指定的 skill / 暂不修复 |

---

## 剧本 C：Hub 版本落后（-CompareHub，outdated）

**症状**：`hub_compare.outdated` 非空

**Spec 内容**：
1. 展示 Hub vs 本地对比表
2. 区分「内容升级」（skill-update / zip）与「运行时修复」（vendor relink）
3. 用户确认后 `-UpgradeSkills` 或引导 skill-update

**AskUserQuestion**：

| 问题 | header | 选项 |
|------|--------|------|
| 发现 N 个 skill 版本落后于 Hub。如何处理？ | 版本同步 | 从 Hub zip 升级选中的 skill（推荐）/ 使用 skill-update 流程 / 暂不升级 |

**升级命令**：

```powershell
powershell -ExecutionPolicy Bypass -File scripts/repair_local_runtime.ps1 -UpgradeSkills @("skill-bootstrap","local-skill-runtime")
```

升级后若 skill 含 vendor，追加 `-RelinkSkills` 同名列表。

---

## 剧本 D：skill 依赖缺失

**症状**：业务 skill 依赖清单中的 Agent Skill 在本地 skills 目录不存在

**Spec 内容**：
1. 列出 `{skill} → 缺失 {dep}`
2. 若 Hub 有 release → `-UpgradeSkills dep`；否则引导 skill-env-setup 全量包

---

## 剧本 E：GITLAB_TOKEN 缺失（Hub 对比失败）

**症状**：`hub_compare.error` 含 TOKEN

**处理**：
1. 仍执行 vendor/kit 本地诊断
2. AskUserQuestion 是否跳过 Hub 对比或配置 Token（参考 skill-env-setup 节点 2）
3. **不**因 Hub 失败阻止 vendor relink

---

## 复检清单（节点 5）

```
本地 Skill 运行时修复报告
════════════════════════════════════════
修复前：kit={}/vendor 未链={}/outdated={}
修复动作：{actions}
修复后：diagnose exit_code={}
════════════════════════════════════════
仍异常项：...
建议下一步：...
```

若修复后仍为 exit 2，返回节点 2 换剧本，**禁止**未复检即声称成功。
