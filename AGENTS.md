# Agent 指南

## 项目概述

本仓库是 **mjnn/my-skills** — 马捷个人 Agent Skill 的 GitHub 归档库。管理个人 skill 的创建、更新、发布与分发。

**与企业 Qoder Skills Hub（GitLab 内网）无关**：企业 skill 不在此仓库维护；发布或修改本仓库 skill 时不要引用企业 Hub 的 skill 清单。

## 关键约定

- 目录布局：`skills/<domain>/<skill-name>/`，域与 `registry.json`、`CATALOG.md` 保持一致
- 发布 skill 后同步更新：`registry.json`、`CATALOG.md`、`README.md`（技能表）、`docs/skill-browser.md`
- 报告任务完成前必须实际 Read 文件验证，禁止仅凭印象报告「已完成」
- 大体积二进制（>1MB）默认不进 `skills/` 源码树，放 `assets/` zip

## 域分类

| 域 | 用途 |
|----|------|
| `platform-engineering` | 连通性、交付运维、Skill 工程化 |
| `general-office` | 办公与协作工具 |
| `development-testing` | 领域专项开发与方案生成 |
