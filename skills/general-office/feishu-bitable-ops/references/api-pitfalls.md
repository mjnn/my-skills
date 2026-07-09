# 飞书 Bitable API 踩坑

## 分页：必须用 has_more

飞书 `list_fields` / `list_tables` / `list_records` 在 **`has_more=false` 时仍可能返回非空 `page_token`**（例如字段列表最后一项的 field_id）。

错误写法（会死循环）：

```python
page_token = data.get("page_token")
if not page_token:
    break
```

正确写法（`工具/feishu_bitable/feishu_bitable.py` 已采用）：

```python
if not data.get("has_more"):
    break
page_token = data.get("page_token")
if not page_token:
    break
```

## tenant_access_token

- 端点：`POST /open-apis/auth/v3/tenant_access_token/internal`
- Body：`{"app_id","app_secret"}`
- 有效期约 2h；client 内缓存并在过期前 60s 刷新

## 记录 fields 值形态

| 字段类型 | API 返回值 |
|----------|------------|
| 文本 | 字符串 |
| 单选 | 选项名称字符串 |
| 日期 | 毫秒时间戳整数 |
| 附件 | `[{file_token, name, url, size, type, ...}]` |
| 关联 | 含 `record_ids` / `link_record_ids` 等结构 |

写记录时用**列名字符串**作 key；单选写选项名；日期写毫秒时间戳。

## 权限常见错误

| code / 现象 | 原因 |
|-------------|------|
| 99991663 | 应用未开通 bitable 相关权限或未安装 |
| 1254031 | 无该多维表格访问权（需把表授权给应用或开文档权限） |
| HTTP 400 WrongRequestBody | GET 请求误带 body，或参数格式错误 |

## 附件下载 / 上传（`FeishuBitableClient`）

- `download_file(url)`：Bearer GET，大文件 300s 超时 + 3 次重试
- `upload_bitable_file(app_token, file_name, content)`：
  - ≤ 20MB：`POST /drive/v1/medias/upload_all`（`parent_type=bitable_file`）
  - \> 20MB：`upload_prepare` → `upload_part`（4MB）→ `upload_finish`

写附件字段：`update_record(..., {"过筛用户车6.16VIN后的数据": [{"file_token": "..."}]})`

## Windows 终端编码

PowerShell 默认可能把 UTF-8 JSON 显示为乱码；数据本身正确。  
优先：`PYTHONIOENCODING=utf-8`，或 `write_text(..., encoding="utf-8")` 落盘后用 Read 工具查看。
