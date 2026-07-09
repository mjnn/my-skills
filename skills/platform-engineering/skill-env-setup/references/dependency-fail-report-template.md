# 依赖不满足报告模板

> Read this when: 节点 0 硬依赖门禁 fail，需生成用户可保存/转发的报告时

## 生成规则

硬依赖（D1–D4）任一项 `fail` 时，Agent **必须**：

1. 运行 `python scripts/check_system_deps.py --report-auto` 写入报告文件
2. 在对话中**完整展示**报告正文（或摘要 + 文件路径）
3. **禁止**仅用一句「依赖不满足」带过而不出报告

## 报告输出路径

```
{用户主目录}/.qoder-cn/reports/dependency-fail-{YYYYMMDD-HHMMSS}.md
```

Windows 示例：`C:\Users\xxx\.qoder-cn\reports\dependency-fail-20260707-131500.md`

## 报告 Markdown 模板

脚本按此结构生成，Agent 手动检测时也须遵循：

```markdown
# Qoder Skills 环境依赖不满足报告

> 生成时间：{ISO8601 本地时间}
> 检测主机：{hostname}
> 操作系统：{OS} {release}
> **硬依赖门禁：未通过 — 配置流程已暂停**

## 摘要

| 指标 | 数值 |
|------|------|
| 硬依赖总数 | 4 |
| 已通过 | {n} |
| **未通过** | **{m}** |
| 条件依赖待关注 | {k} |

## 硬依赖检测结果

| ID | 依赖 | 状态 | 检测详情 | 修复指引 |
|----|------|------|---------|---------|
| D1 | Qoder CN | ❌ FAIL | command not found | 请先安装 Qoder CN 企业版客户端 |
| D2 | curl | ✅ PASS | curl 8.x ... | — |
| D3 | 解压工具 | ✅ PASS | Expand-Archive, tar | — |
| D4 | PowerShell | ✅ PASS | 5.1.x | — |

## 未通过项明细（需用户或 IT 处理）

### D1 — Qoder CN

- **当前状态**：未安装或未加入 PATH
- **影响**：无法加载 skill，配置流程无法继续
- **建议操作**：
  1. 联系 IT 安装 Qoder CN 企业版客户端
  2. 安装后重新打开终端，执行 `qoder-cn --version` 确认
  3. 对本 skill 说「重新检测依赖」

（每个 FAIL 项重复上述结构）

## 条件依赖（不阻断，供后续参考）

| ID | 依赖 | 状态 | 说明 |
|----|------|------|------|
| C1 | git | ⚠️ 未安装 | 节点 4 可用 MinGit；Zip 安装路径不受影响 |
| C2 | MinGit 内置包 | ✅ 存在 | — |
| C3 | GITLAB_TOKEN | ⏳ 待配置 | 节点 2 收集，非本次阻断 |

## 下一步

1. 按上表「未通过项明细」逐项修复
2. 修复后运行：`python scripts/check_system_deps.py --report-auto`
3. 硬依赖全部通过后，重新发起「配置 Qoder Skills 环境」

---
*本报告由 skill-env-setup 节点 0 自动生成，可转发给 IT 协助排查。*
```

## 通过时的报告（可选）

硬依赖全 pass 时，可输出简短「依赖满足确认」（不必写文件），进入节点 1：

```
系统依赖检测通过 ✅
D1–D4 全部满足，可进入环境配置流程。
```
