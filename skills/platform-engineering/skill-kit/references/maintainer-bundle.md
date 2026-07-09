# 维护者打包清单

> Read this when: 发布 skill-kit 或 skill-env-setup 前

## assets 必备文件

| 文件 | 说明 | 获取方式（开发机，有外网） |
|------|------|---------------------------|
| `7za.exe` | 7-Zip 命令行 x64 (~858KB) | [7-Zip Extra](https://www.7-zip.org/download.html) 解压 `7z-extra.7z` |
| `python.7z` | 便携 Python 3.12 运行时 (~130MB) | 项目根 `python.7z` 或自建 |
| `python312.zip` | **标准库** (~3.8MB) | [Python 3.12 embed-amd64.zip](https://www.python.org/ftp/python/3.12.8/python-3.12.8-embed-amd64.zip) 内 `python312.zip` |
| `python312._pth` | 启用 DLLs + site-packages | 内容见 `assets/python312._pth`（须含 `DLLs` 与 `import site`） |
| `git/MinGit-*-64-bit.zip` | 便携 Git | 与 skill-env-setup `assets/git/` 相同 |

> **注意**：仅 `python.7z` 不含完整 stdlib 时，必须附带 `python312.zip`，否则 `urllib`/`xml` 等标准库导入失败。

## 为某 skill 准备 Python 库（开发机）

```bash
mkdir -p vendor/wheels vendor/python-packages
pip download -d vendor/wheels python-pptx matplotlib Pillow yt-dlp \
  --only-binary=:all: --python-version 312 --platform win_amd64
# 解压每个 .whl 到 vendor/python-packages/<wheel-stem>/
python scripts/bundle_vendor_packages.py   # 或手动解压
```

发布 zip 时**包含** `vendor/python-packages/`，**不包含** `vendor/wheels/`。

## 已打入 vendor 的 skill（2026-07-08）

| Skill | 包 |
|-------|-----|
| svw-ppt-generator | python-pptx, matplotlib, Pillow + 12 个依赖 wheel |
| separate-employee-extraction | yt-dlp |

## 体积建议

- skill-kit assets 合计：~135 MB（python.7z + python312.zip + 7za + MinGit）
- 单 skill vendor：通常 5–40 MB
