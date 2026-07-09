# 自检清单

> svw-ppt-generator | general-office

- [x] 1. SKILL.md 存在且 frontmatter 包含 name 和 description
- [x] 2. name (svw-ppt-generator) 与目录名一致，仅含小写字母/连字符
- [x] 3. description 命令式 + 触发关键词 + 排除场景（修改现有PPT、非结构化叙事、艺术创作）
- [x] 4. 正文含具体操作步骤（5阶段：信息收集→Spec模式→图表绘制→生成PPT→结果交付）
- [x] 5. Gotchas 12 条（基于真实PPT生成踩坑经验）
- [x] 6. evals.json 11 条用例
- [x] 7. 每条用例有 prompt + expected_output + assertions（>= 2 条/用例）
- [x] 8. eval_queries.json 20 条（10 trigger + 10 not-trigger，含 4 条 near-miss）
- [x] 9. SKILL.md 正文 437 行（<= 500）
- [x] 10. 无硬编码密钥/密码/Token/内网 IP

## 附加检查项

- [x] references/ 目录存在（条件加载指令在正文中）
- [x] 正文末尾包含「执行后复盘（自迭代钩子）」章节
- [x] 涉及提问时指示使用 AskUserQuestion 工具（阶段1 第1-3轮）
- [x] 涉及执行动作时指示使用 EnterSpecMode/ExitSpecMode（阶段2）

## 提交信息

- 作者：MaJienuona
- 日期：2026-07-03
- skill 名称：svw-ppt-generator
- 所属域：general-office
