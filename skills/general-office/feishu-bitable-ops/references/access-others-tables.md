# 操作他人创建的多维表格

## 核心结论

| 方式 | 能否让 Agent API 读写 |
|------|----------------------|
| 只发 Base 链接 | ❌ 不够 |
| 链接分享设为「互联网可编辑」 | ❌ 不够（仅网页端对人有效） |
| 链接 + **添加文档应用**为协作者 | ✅ 可以 |

Agent 使用 **开放平台应用身份**（`tenant_access_token`），不走用户浏览器登录态。

## 用户需完成的配置

1. 提供完整 URL：`https://my.feishu.cn/base/{app_token}?table={table_id}&view=...`
2. 表所有者或有管理权的人在多维表格：
   - **右上角「…」→「…更多」→「添加文档应用」**
   - 搜索并添加 `.env` 中 `FEISHU_APP_ID` 对应的应用
3. 按任务授予协作者权限：

| Agent 任务 | 应用所需权限 |
|-----------|-------------|
| 读记录、列字段、导出 | 可阅读 |
| 增删改记录、上传附件 | 可编辑 |
| 建表、建字段、改结构 | 可管理（`full_access`） |

4. 若启用 **高级权限**：在高级权限设置中单独给应用或含应用的群组授权。

## Agent 侧验证步骤

```powershell
$env:NO_PROXY='*'
python feishu_bitable.py parse-url "<用户链接>"
python feishu_bitable.py list-fields --app-token APP --table-id TBL
python feishu_bitable.py list-permissions --app-token APP
```

- `list-fields` 成功 → 至少有读权限
- `1063002` / `1254031` → 应用未加协作者或权限不足，**停止写操作**，提示用户添加文档应用

## 与「新建表」的区别

| 场景 | 谁建表 | Agent 还要做什么 |
|------|--------|------------------|
| Agent 新建 | 应用 | `ensure_user_full_access` 给用户 |
| 操作他人表 | 他人 | 用户给应用加协作者；Agent **不能**自行 grant（除非应用仍是所有者） |

## 常见误解

**Q：分享链接设成「互联网获得链接的人可编辑」，你是不是就能访问？**  
A：不能。那是网页分享策略，不等于开放平台 API 授权。

**Q：只给 app_token 行吗？**  
A：不够。token 只用于定位资源，鉴权仍靠应用协作者身份。
