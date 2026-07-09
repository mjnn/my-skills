# 各 Skill 的 vendor 与 tools 目录

> Read this when: skill-bootstrap 创建新 skill 或审查依赖

## 标准结构

```
{skill-name}/
├── SKILL.md
├── scripts/
├── references/
├── evals/
├── vendor/
│   ├── python-packages/       # 必选（若依赖第三方 Py 库）；无则空目录或省略
│   │   ├── requests/
│   │   └── urllib3/
│   └── wheels/                # 可选，仅维护者保留 whl 源，可不打进 Release
└── tools/                     # 可选：本 skill 独占的便携工具（非 Python）
    ├── manifest.json
    └── some-portable-tool/
```

## tools/ 与 skill-kit 的分工

| 类型 | 放置位置 |
|------|----------|
| Python 解释器 | skill-kit `assets/python.7z` |
| Git | skill-kit / skill-env-setup `assets/git/` |
| 7za | skill-kit `assets/7za.exe` |
| 某 skill 专用 CLI（如定制转换器） | 该 skill 的 `tools/` |

## SKILL.md 必须声明

1. **依赖清单** 中列出：skill-kit（共享运行时）、本 skill `vendor/python-packages` 中的包名
2. **流程第一步**（若用 Python 脚本）：调用 `init_skill_python.ps1` + 验证 import
3. 脚本示例使用 `$env:QODER_PYTHON`，不写 `python` 裸命令

## manifest.json 示例（tools/）

```json
{
  "tools": [
    {
      "id": "custom-cli",
      "path": "tools/custom-cli/bin/cli.exe",
      "platform": "win-x64"
    }
  ]
}
```
