# 自检清单

> skill-bootstrap | platform-engineering

- [x] 1. SKILL.md 存在且 frontmatter 包含 name 和 description
- [x] 2. name (skill-bootstrap) 与目录名一致，仅含小写字母/连字符
- [x] 3. description 命令式 + 触发关键词 + 排除场景（修改已有 skill、评估第三方 skill、归档管理）
- [x] 4. 正文含具体操作步骤（6 步流程：确认领域→提炼 Gotchas→编写正文→自检→格式预检→发布）
- [x] 5. Gotchas 7 条（基于会话真实经验：跳过 Gotchas、eval 脱节、内容堆在 SKILL.md、description 太泛、near-miss 缺失、不适用场景缺失、纯文本提问）
- [x] 6. evals.json 5 条用例
- [x] 7. 每条用例有 prompt + expected_output + assertions（>= 2 条/用例）
- [x] 8. eval_queries.json 16 条（8 trigger + 8 not-trigger，含 4 条 near-miss）
- [x] 9. SKILL.md 正文 <= 500 行，详细规范拆到 references/
- [x] 10. 无硬编码密钥/密码/Token/内网 IP
- [x] 11. 包含 Tag/Release 发布流程（第五步：git tag + push + GitLab API）

## 附加检查项

- [x] references/ 有条件加载指令（gotchas-criteria.md、skill-structure.md、eval-guidelines.md）
- [x] 正文末尾包含「执行后复盘（自迭代钩子）」章节
- [x] 涉及提问时指示使用 AskUserQuestion 工具（阶段二、2c）
- [x] 涉及执行动作时指示使用 EnterSpecMode/ExitSpecMode（2d、阶段三 Spec 模式）
- [x] 包含可选的 Tag/Release 发布流程（第五步）

## 提交信息

- 作者：MaJienuona
- 日期：2026-07-03
- skill 名称：skill-bootstrap
- 版本：v0.3.0
- 所属域：platform-engineering
