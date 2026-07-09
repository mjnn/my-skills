# .gitignore 模板

在 SKILL.md 步骤 2 创建 .gitignore 时读取此文件。根据项目类型选择对应模板，合并通用排除项。

## 通用排除项（所有项目类型必须包含）

```gitignore
# === 敏感文件 ===
.env
.env.*
!.env.example
*.key
*.pem
credentials*
secrets*

# === OS 元数据 ===
.DS_Store
._*
Thumbs.db
desktop.ini

# === IDE ===
.idea/
.vscode/
*.swp
*.swo
*~

# === 日志 ===
*.log
logs/
```

## Python 项目

```gitignore
# === Python ===
__pycache__/
*.py[cod]
*$py.class
*.so
*.egg
*.egg-info/
dist/
build/
eggs/
sdist/
wheels/

# === 虚拟环境 ===
venv/
.venv/
env/
ENV/

# === 测试 ===
.pytest_cache/
.coverage
htmlcov/
.tox/

# === Jupyter ===
.ipynb_checkpoints/
```

## Node.js 项目

```gitignore
# === 依赖 ===
node_modules/

# === 构建产物 ===
dist/
build/
.next/
.nuxt/
out/

# === 框架 ===
.npm
.yarn/cache
.pnpm-store/

# === 环境变量 ===
.env.local
.env.*.local

# === 调试 ===
npm-debug.log*
yarn-debug.log*
yarn-error.log*
```

## Java 项目

```gitignore
# === 编译产物 ===
*.class
target/
build/
out/

# === 包管理 ===
.gradle/
gradle-app.setting
!gradle-wrapper.jar

# === IDE ===
.idea/
*.iml
*.iws
*.ipr
.classpath
.project
.settings/

# === Spring Boot ===
*.original
```

## 通用补充规则

- 如果项目中有 `dist/` 目录是源码（非构建产物），在 .gitignore 中用 `!dist/` 反排除
- 如果项目需要提交 `.env.example`，确保通用排除项中的 `!.env.example` 生效
- 如果项目有大型二进制文件（模型、镜像等），考虑使用 Git LFS 或单独排除
