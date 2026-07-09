# 飞书开放平台应用初始化

首次使用本 skill 前，须在[飞书开放平台](https://open.feishu.cn/app)创建**企业自建应用**并完成安装。Agent 通过 `App ID` + `App Secret` 换取 `tenant_access_token` 调用 API。

## 一、创建应用（用户操作）

1. 打开 https://open.feishu.cn/app → **创建企业自建应用**
2. 填写应用名称（如「多维表格自动化」）与描述
3. 进入应用 → **凭证与基础信息**，记录：
   - **App ID**（形如 `cli_xxxxxxxx`）
   - **App Secret**（仅显示一次，务必当场复制保存）

> Secret 只写入本地 `scripts/.env`，勿提交 Git、勿在聊天中粘贴完整内容。

## 二、开通 API 权限

在应用 **权限管理** 中搜索并开通（满足其一组合即可，推荐全开下列项）：

| 权限 | 用途 |
|------|------|
| `bitable:app` | 多维表格读写、建表 |
| `docs:permission.member:create` | 添加协作者 |
| `docs:permission.member:transfer` | 转移文档所有权（新建表授权） |
| `drive:drive` | 云文档权限（可替代部分 permission 细项） |
| `contact:user.base:readonly` | 按邮箱解析 `open_id`（授权用，可选） |

如需 **VIN 过筛 / 附件**：还需 `drive:drive` 或文件相关读权限（下载/上传素材）。

## 三、发布并安装到企业

1. **版本管理与发布** → 创建版本 → 申请上线（企业内通常自动通过）
2. **应用发布** → 安装到本企业（管理员审批）
3. 未安装时 `auth` 可能成功但调业务 API 报 `99991663` 等无权限错误

## 四、配置本地凭证（Agent 协助）

1. 复制 `scripts/.env.example` → `scripts/.env`
2. 填入用户提供的 App ID / App Secret（由用户在飞书后台复制，Agent 引导粘贴到 `.env` 文件，**不要在对话里复述 Secret**）
3. 推荐同时配置（新建表自动授权对象，二选一）：
   - `FEISHU_OWNER_EMAIL`：用户飞书邮箱
   - `FEISHU_OWNER_OPEN_ID`：开放平台用户 ID

## 五、验证

```powershell
$env:NO_PROXY='*'
$env:PYTHONIOENCODING='utf-8'
python scripts/feishu_bitable.py auth
```

成功输出：`{"ok": true, "token_prefix": "t-g1..."}`

失败对照：

| 现象 | 处理 |
|------|------|
| 缺少 FEISHU_APP_ID | 检查 `.env` 路径与文件名 |
| code 10013 等鉴权失败 | App ID / Secret 错误 |
| 99991663 | 权限未开通或未发布安装 |
| ConnectionRefusedError | `$env:NO_PROXY='*'` |

## 六、用户需提供的信息清单

Agent 初始化时应向用户收集：

| 项 | 必填 | 说明 |
|----|------|------|
| App ID | 是 | `cli_` 开头 |
| App Secret | 是 | 仅写入 `.env` |
| 飞书邮箱 | 推荐 | 用于 `FEISHU_OWNER_EMAIL` |
| 是否已发布安装 | 是 | 未安装则先引导完成 |

**不要要求用户提供：** 个人飞书密码、`user_access_token`（本 skill 默认不用）。
