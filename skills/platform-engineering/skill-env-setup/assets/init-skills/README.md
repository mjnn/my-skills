# 初始化技能包（初始化技能包.zip）

> Read this when: 节点 4 安装内置 skill 时

## 位置

```
assets/init-skills/init-skills-bundle.zip   # 主文件名（脚本优先）
assets/init-skills/初始化技能包.zip          # 中文别名（build 脚本自动复制）
```

本 skill 包**必须**内含此 zip。打包 skill-env-setup 发布前，将 Hub 已发布的全部 skill 目录打入该 zip。

## Zip 结构

```
初始化技能包.zip
├── manifest.json          # 推荐：skill 名称与版本清单
├── skill-bootstrap/
│   └── SKILL.md
├── skill-kit/             # 共享便携工具链（必须）
├── skill-update/
├── skill-discipline/
├── ask-before-act/
└── ...（Hub 已发布 skill 各一个顶层目录）
```

### manifest.json 格式

```json
{
  "bundle_version": "2026.07.07",
  "skills": [
    { "name": "skill-bootstrap", "version": "v0.2.1" },
    { "name": "skill-update", "version": "v0.1.0" }
  ]
}
```

安装脚本解压后，会在每个 skill 目录写入 `.installed-version`（内容为 version 字符串）。

## 安装目标（默认，无需询问用户）

**全部**解压到：

```
Windows:  %USERPROFILE%\.qoder-cn\skills\
Linux:    $HOME/.qoder-cn/skills/
```

示例：`C:\Users\zhangsan\.qoder-cn\skills\skill-bootstrap\`

## 安装命令

```bash
python scripts/install_init_skills.py
```

或 Windows：

```powershell
powershell -ExecutionPolicy Bypass -File scripts/install_init_skills.ps1
```

## 缺失处理

若 zip 不存在 → 节点 4 **on_fail**，报告「初始化技能包缺失」，禁止声称安装完成。不要用 curl 逐个从 Hub 下载替代（除非用户明确要求离线包不可用时的降级方案，且需 Spec 审核）。
