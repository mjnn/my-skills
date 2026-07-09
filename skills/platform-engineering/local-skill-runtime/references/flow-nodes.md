# 流程节点表

> Read this when: 核对节点门禁或调试跳步

## 节点总览

| node_id | name | purpose | outputs | gate | on_fail |
|---------|------|---------|---------|------|---------|
| 0 | 运行时自检 | skill-kit 是否可用（不要求本 skill vendor） | kit 状态 JSON | python.exe 可执行 | 引导 skill-env-setup |
| 1 | 全量诊断 | kit + 已装 skill + vendor 链接 | diagnose JSON | 脚本已运行 | 按 exit_code 分支 |
| 2 | 问题解读 | 分类：kit 缺失 / vendor 未链 / 版本落后 | 问题摘要表 | AskUserQuestion 已调用 | — |
| 3 | 修复 Spec | EnterSpecMode 列出修复动作 | 已确认 Spec | ExitSpecMode | 禁止 repair |
| 4 | 执行修复 | relink / hub zip 升级 | repair JSON | 至少一项动作成功 | 返回节点 1 |
| 5 | 复检交付 | 再次 diagnose + 最终报告 | 前后对比 | 复检已运行 | — |

## 与 skill-env-setup 的分工

| 场景 | 使用技能 |
|------|---------|
| 首次零预装、无 kit、无 skill 目录 | **skill-env-setup**（7 节点） |
| kit 在、skill 已装、vendor 未链或 Hub 版本旧 | **local-skill-runtime**（本技能） |
| 修改 skill 正文/eval/发布 | **skill-update** |
| Hub 仓库文档一致性 | **skill-hub-management** |

## 工具脚本

| 节点 | 脚本 |
|------|------|
| 0 | `diagnose_local_runtime.ps1 -KitOnly` |
| 1 | `diagnose_local_runtime.ps1`（可选 `-CompareHub`） |
| 4 | `repair_local_runtime.ps1`（`-RelinkAll` / `-RelinkSkills` / `-UpgradeSkills`） |
| 5 | `diagnose_local_runtime.ps1 -CompareHub` |

## 退出码约定

| exit_code | 含义 | Agent 动作 |
|-----------|------|-----------|
| 0 | 运行时健康 | 交付报告，结束 |
| 1 | skill-kit 未安装或不可用 | AskUserQuestion → skill-env-setup |
| 2 | kit 在但有问题（vendor/版本/目录） | AskUserQuestion → 节点 3 修复 Spec |
