# 自检清单

> 提交前，作者逐条自查。全部勾选才能提交。

- [ ] 1. SKILL.md 存在且 frontmatter 包含 name 和 description
- [ ] 2. name 与父目录名一致，仅含小写字母/数字/连字符
- [ ] 3. description 使用了命令式，含触发关键词和不应触发的边界说明
- [ ] 4. 正文包含具体的操作步骤（非泛泛的"适当处理"）
- [ ] 5. 包含 >= 5 条 Gotchas（基于真实经验，不编造）
- [ ] 6. evals/evals.json 存在且含 >= 3 条用例
- [ ] 7. 每条用例有 prompt + expected_output + assertions（>= 2 条/用例）
- [ ] 8. evals/eval_queries.json 存在且含 >= 16 条（含 >= 4 条 near-miss）
- [ ] 9. SKILL.md 正文 <= 500 行（超出部分已拆分到 references/）
- [ ] 10. 不含硬编码密钥/密码/Token 或内网 IP

## 附加检查项

- [ ] references/ 有条件加载指令（"Read references/xxx.md if ..."）
- [ ] 正文末尾包含「执行后复盘（自迭代钩子）」章节
- [ ] 涉及提问时使用 AskUserQuestion 工具
- [ ] 涉及执行动作时走 EnterSpecMode/ExitSpecMode

## 提交信息

- 作者：
- 日期：
- skill 名称：
- 所属域：
