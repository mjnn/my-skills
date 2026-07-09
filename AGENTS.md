# Agent 指南

## 项目概述

本仓库是 mjnn/my-skills 云端 Skill 注册库，托管在 GitLab（github.com/mjnn，项目 ID 289）。管理 Agent Skills 的创建、更新、发布和分发。

## 会话启动规则

**每次会话开始时，必须先读取 `.qoder/rules/lessons-learned.md`**，加载历次会话沉淀的经验教训和踩坑记录，避免重复犯错。

读取命令：
```
Read: docs/lessons-learned.md（如存在）
```

## 关键约定

- 技能下载链接统一使用 API raw 端点格式：`https://<host>/api/v4/projects/<id>/repository/files/<url_encoded_path>/raw?ref=main`
- 发布技能时必须同步更新 README.md、CATALOG.md、docs/skill-browser.md 三个文档
- GitLab Markdown 锚点使用自动生成的 kebab-case 格式（版本号中的 `.` 移除）
- GitLab API 的 JSON payload 使用文件方式传递，避免 shell 编码问题
- 报告任务完成前必须实际 Read 文件验证，禁止仅凭印象或摘要报告"已完成"
