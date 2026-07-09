# 自检清单

> gitlab-repo-upload | platform-engineering

- [x] 1. SKILL.md 存在且 frontmatter 包含 name 和 description
- [x] 2. name (gitlab-repo-upload) 与目录名一致，仅含小写字母/连字符
- [x] 3. description 命令式 + 触发关键词 + 排除场景
- [x] 4. 正文含具体操作步骤（bash 命令级）
- [x] 5. Gotchas 10 条（基于会话真实经验）
- [x] 6. evals.json 8 条用例
- [x] 7. 每条用例有 prompt + expected_output + assertions（>= 2 条/用例）
- [x] 8. eval_queries.json 20 条（10 trigger + 10 not-trigger，含 8 条 near-miss）
- [x] 9. SKILL.md 正文 <= 500 行（441 行，无需拆分）
- [x] 10. 无硬编码密钥/密码/Token/内网 IP
- [x] 11. 包含创建 Tag 和 Release 的完整流程（git tag + push + GitLab API）
- [x] 12. 包含 zip 附件上传流程（POST /uploads + POST /assets/links）
- [x] 13. 下载链接使用 uploads 格式（禁止 archive 格式）

## 附加检查项

- [x] references/ 有条件加载指令
- [x] 正文末尾包含「执行后复盘（自迭代钩子）」章节
- [x] 涉及提问时使用 AskUserQuestion 工具
- [x] 涉及执行动作时走 EnterSpecMode/ExitSpecMode
- [x] 包含可选的 Tag/Release 创建流程（阶段五）
- [x] 包含文档同步流程（阶段六：README/CATALOG/skill-browser）
- [x] 包含下载链接验证步骤（步骤 12）

## 提交信息

- 作者：MaJienuona
- 日期：2026-07-06
- skill 名称：gitlab-repo-upload
- 版本：v0.3.0
- 所属域：platform-engineering
