"""飞书多维表格 (Bitable) CRUD CLI。

凭证从 工具/feishu_bitable/.env 或环境变量读取：
  FEISHU_APP_ID, FEISHU_APP_SECRET
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import uuid
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

BASE_URL = "https://open.feishu.cn/open-apis"
ENV_PATH = Path(__file__).resolve().parent / ".env"
UPLOAD_ALL_MAX_BYTES = 20 * 1024 * 1024


def load_dotenv(path: Path = ENV_PATH) -> None:
    if not path.is_file():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


class FeishuBitableClient:
    def __init__(self, app_id: str, app_secret: str) -> None:
        self.app_id = app_id
        self.app_secret = app_secret
        self._token = ""
        self._token_expire_at = 0.0

    def _ensure_token(self) -> str:
        if self._token and time.time() < self._token_expire_at - 60:
            return self._token
        payload = {"app_id": self.app_id, "app_secret": self.app_secret}
        data = self._request(
            "POST",
            "/auth/v3/tenant_access_token/internal",
            json_body=payload,
            auth=False,
        )
        self._token = data["tenant_access_token"]
        self._token_expire_at = time.time() + float(data.get("expire", 7200))
        return self._token

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_body: dict[str, Any] | None = None,
        auth: bool = True,
    ) -> dict[str, Any]:
        url = BASE_URL + path
        if params:
            query = urllib.parse.urlencode(
                {k: v for k, v in params.items() if v is not None},
                doseq=True,
            )
            url = f"{url}?{query}"

        headers = {"Content-Type": "application/json; charset=utf-8"}
        if auth:
            headers["Authorization"] = f"Bearer {self._ensure_token()}"

        body = None
        if json_body is not None:
            body = json.dumps(json_body, ensure_ascii=False).encode("utf-8")

        req = urllib.request.Request(url, data=body, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            raw = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"HTTP {exc.code}: {raw}") from exc

        result = json.loads(raw)
        if result.get("code") != 0:
            raise RuntimeError(f"Feishu API error: {result}")
        return result.get("data", result)

    def download_file(self, url: str, *, timeout: int = 300, retries: int = 3) -> bytes:
        headers = {"Authorization": f"Bearer {self._ensure_token()}"}
        last_exc: Exception | None = None
        for attempt in range(retries):
            try:
                req = urllib.request.Request(url, headers=headers, method="GET")
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    return resp.read()
            except Exception as exc:  # noqa: BLE001
                last_exc = exc
                if attempt + 1 < retries:
                    time.sleep(2 * (attempt + 1))
        raise RuntimeError(f"Download failed after {retries} attempts: {last_exc}") from last_exc

    def _multipart_upload_part(
        self, upload_id: str, seq: int, chunk: bytes, *, timeout: int = 120
    ) -> None:
        boundary = f"----FeishuFormBoundary{uuid.uuid4().hex}"
        parts: list[bytes] = []

        def add_field(name: str, value: str) -> None:
            parts.append(
                (
                    f"--{boundary}\r\n"
                    f'Content-Disposition: form-data; name="{name}"\r\n\r\n'
                    f"{value}\r\n"
                ).encode("utf-8")
            )

        add_field("upload_id", upload_id)
        add_field("seq", str(seq))
        add_field("size", str(len(chunk)))
        parts.append(
            (
                f"--{boundary}\r\n"
                'Content-Disposition: form-data; name="file"; filename="part.bin"\r\n'
                f"Content-Type: application/octet-stream\r\n\r\n"
            ).encode("utf-8")
        )
        body = b"".join(parts) + chunk + f"\r\n--{boundary}--\r\n".encode("utf-8")
        headers = {
            "Authorization": f"Bearer {self._ensure_token()}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        }
        req = urllib.request.Request(
            f"{BASE_URL}/drive/v1/medias/upload_part",
            data=body,
            headers=headers,
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            raw = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Upload part failed HTTP {exc.code}: {raw}") from exc

        result = json.loads(raw)
        if result.get("code") != 0:
            raise RuntimeError(f"Feishu upload_part error: {result}")

    def _upload_multipart_bitable_file(
        self, app_token: str, file_name: str, content: bytes, *, timeout: int = 120
    ) -> str:
        prep = self._request(
            "POST",
            "/drive/v1/medias/upload_prepare",
            json_body={
                "file_name": file_name,
                "parent_type": "bitable_file",
                "parent_node": app_token,
                "size": len(content),
            },
        )
        upload_id = prep["upload_id"]
        block_size = int(prep["block_size"])
        block_num = int(prep["block_num"])
        for seq in range(block_num):
            start = seq * block_size
            chunk = content[start : start + block_size]
            self._multipart_upload_part(upload_id, seq, chunk, timeout=timeout)
            time.sleep(0.25)
        finish = self._request(
            "POST",
            "/drive/v1/medias/upload_finish",
            json_body={"upload_id": upload_id, "block_num": block_num},
        )
        file_token = finish.get("file_token")
        if not file_token:
            raise RuntimeError(f"Upload finish missing file_token: {finish}")
        return file_token

    def upload_bitable_file(
        self, app_token: str, file_name: str, content: bytes, *, timeout: int = 120
    ) -> str:
        if len(content) > UPLOAD_ALL_MAX_BYTES:
            return self._upload_multipart_bitable_file(
                app_token, file_name, content, timeout=timeout
            )
        boundary = f"----FeishuFormBoundary{uuid.uuid4().hex}"
        parts: list[bytes] = []

        def add_field(name: str, value: str) -> None:
            parts.append(
                (
                    f"--{boundary}\r\n"
                    f'Content-Disposition: form-data; name="{name}"\r\n\r\n'
                    f"{value}\r\n"
                ).encode("utf-8")
            )

        add_field("file_name", file_name)
        add_field("parent_type", "bitable_file")
        add_field("parent_node", app_token)
        add_field("size", str(len(content)))
        parts.append(
            (
                f"--{boundary}\r\n"
                f'Content-Disposition: form-data; name="file"; filename="{file_name}"\r\n'
                f"Content-Type: application/octet-stream\r\n\r\n"
            ).encode("utf-8")
        )
        body = b"".join(parts) + content + f"\r\n--{boundary}--\r\n".encode("utf-8")

        headers = {
            "Authorization": f"Bearer {self._ensure_token()}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        }
        req = urllib.request.Request(
            f"{BASE_URL}/drive/v1/medias/upload_all",
            data=body,
            headers=headers,
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            raw = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Upload failed HTTP {exc.code}: {raw}") from exc

        result = json.loads(raw)
        if result.get("code") != 0:
            raise RuntimeError(f"Feishu upload error: {result}")
        file_token = (result.get("data") or {}).get("file_token")
        if not file_token:
            raise RuntimeError(f"Upload missing file_token: {result}")
        return file_token

    # --- meta ---
    def get_app(self, app_token: str) -> dict[str, Any]:
        return self._request("GET", f"/bitable/v1/apps/{app_token}")

    def list_tables(self, app_token: str, *, page_size: int = 100) -> list[dict[str, Any]]:
        items: list[dict[str, Any]] = []
        page_token = None
        while True:
            data = self._request(
                "GET",
                f"/bitable/v1/apps/{app_token}/tables",
                params={"page_size": page_size, "page_token": page_token},
            )
            items.extend(data.get("items") or [])
            if not data.get("has_more"):
                break
            page_token = data.get("page_token")
            if not page_token:
                break
        return items

    def list_fields(
        self, app_token: str, table_id: str, *, page_size: int = 100
    ) -> list[dict[str, Any]]:
        items: list[dict[str, Any]] = []
        page_token = None
        while True:
            data = self._request(
                "GET",
                f"/bitable/v1/apps/{app_token}/tables/{table_id}/fields",
                params={"page_size": page_size, "page_token": page_token},
            )
            items.extend(data.get("items") or [])
            if not data.get("has_more"):
                break
            page_token = data.get("page_token")
            if not page_token:
                break
        return items

    # --- records ---
    def list_records(
        self,
        app_token: str,
        table_id: str,
        *,
        page_size: int = 100,
        view_id: str | None = None,
        filter_expr: str | None = None,
        sort: list[str] | None = None,
    ) -> list[dict[str, Any]]:
        items: list[dict[str, Any]] = []
        page_token = None
        while True:
            params: dict[str, Any] = {"page_size": page_size, "page_token": page_token}
            if view_id:
                params["view_id"] = view_id
            if filter_expr:
                params["filter"] = filter_expr
            if sort:
                params["sort"] = json.dumps(sort, ensure_ascii=False)
            data = self._request(
                "GET",
                f"/bitable/v1/apps/{app_token}/tables/{table_id}/records",
                params=params,
            )
            items.extend(data.get("items") or [])
            if not data.get("has_more"):
                break
            page_token = data.get("page_token")
            if not page_token:
                break
        return items

    def get_record(self, app_token: str, table_id: str, record_id: str) -> dict[str, Any]:
        data = self._request(
            "GET",
            f"/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}",
        )
        return data.get("record") or data

    def create_record(
        self, app_token: str, table_id: str, fields: dict[str, Any]
    ) -> dict[str, Any]:
        data = self._request(
            "POST",
            f"/bitable/v1/apps/{app_token}/tables/{table_id}/records",
            json_body={"fields": fields},
        )
        return data.get("record") or data

    def batch_create_records(
        self, app_token: str, table_id: str, records: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        data = self._request(
            "POST",
            f"/bitable/v1/apps/{app_token}/tables/{table_id}/records/batch_create",
            json_body={"records": [{"fields": r} for r in records]},
        )
        return data.get("records") or []

    def update_record(
        self,
        app_token: str,
        table_id: str,
        record_id: str,
        fields: dict[str, Any],
    ) -> dict[str, Any]:
        data = self._request(
            "PUT",
            f"/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}",
            json_body={"fields": fields},
        )
        return data.get("record") or data

    def batch_update_records(
        self,
        app_token: str,
        table_id: str,
        records: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        data = self._request(
            "POST",
            f"/bitable/v1/apps/{app_token}/tables/{table_id}/records/batch_update",
            json_body={"records": records},
        )
        return data.get("records") or []

    def delete_record(self, app_token: str, table_id: str, record_id: str) -> None:
        self._request(
            "DELETE",
            f"/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}",
        )

    def batch_delete_records(
        self, app_token: str, table_id: str, record_ids: list[str]
    ) -> None:
        self._request(
            "POST",
            f"/bitable/v1/apps/{app_token}/tables/{table_id}/records/batch_delete",
            json_body={"records": record_ids},
        )

    # --- tables ---
    def create_table(
        self, app_token: str, name: str, *, default_view_name: str = "默认视图"
    ) -> dict[str, Any]:
        data = self._request(
            "POST",
            f"/bitable/v1/apps/{app_token}/tables",
            json_body={"table": {"name": name, "default_view_name": default_view_name}},
        )
        return data.get("table") or data

    def update_table(self, app_token: str, table_id: str, name: str) -> dict[str, Any]:
        data = self._request(
            "PATCH",
            f"/bitable/v1/apps/{app_token}/tables/{table_id}",
            json_body={"name": name},
        )
        return data.get("table") or data

    def delete_table(self, app_token: str, table_id: str) -> None:
        self._request("DELETE", f"/bitable/v1/apps/{app_token}/tables/{table_id}")

    # --- fields ---
    def create_field(
        self, app_token: str, table_id: str, field_name: str, field_type: int, **extra: Any
    ) -> dict[str, Any]:
        field_body: dict[str, Any] = {"field_name": field_name, "type": field_type}
        field_body.update(extra)
        data = self._request(
            "POST",
            f"/bitable/v1/apps/{app_token}/tables/{table_id}/fields",
            json_body=field_body,
        )
        return data.get("field") or data

    def update_field(
        self,
        app_token: str,
        table_id: str,
        field_id: str,
        *,
        field_name: str | None = None,
        **extra: Any,
    ) -> dict[str, Any]:
        field_body: dict[str, Any] = {}
        if field_name is not None:
            field_body["field_name"] = field_name
        field_body.update(extra)
        data = self._request(
            "PUT",
            f"/bitable/v1/apps/{app_token}/tables/{table_id}/fields/{field_id}",
            json_body={"field": field_body},
        )
        return data.get("field") or data

    def delete_field(self, app_token: str, table_id: str, field_id: str) -> None:
        self._request(
            "DELETE",
            f"/bitable/v1/apps/{app_token}/tables/{table_id}/fields/{field_id}",
        )

    # --- app / permissions ---
    def create_app(self, name: str, *, folder_token: str | None = None) -> dict[str, Any]:
        body: dict[str, Any] = {"name": name}
        if folder_token:
            body["folder_token"] = folder_token
        data = self._request("POST", "/bitable/v1/apps", json_body=body)
        return data.get("app") or data

    def list_permission_members(
        self, app_token: str, *, doc_type: str = "bitable"
    ) -> list[dict[str, Any]]:
        data = self._request(
            "GET",
            f"/drive/v1/permissions/{app_token}/members",
            params={"type": doc_type},
        )
        return data.get("items") or []

    def add_permission_member(
        self,
        app_token: str,
        member_id: str,
        *,
        member_type: str = "openid",
        perm: str = "full_access",
        doc_type: str = "bitable",
    ) -> dict[str, Any]:
        data = self._request(
            "POST",
            f"/drive/v1/permissions/{app_token}/members",
            params={"type": doc_type},
            json_body={
                "member_type": member_type,
                "member_id": member_id,
                "perm": perm,
            },
        )
        return data.get("member") or data

    def transfer_owner(
        self,
        app_token: str,
        member_id: str,
        *,
        member_type: str = "openid",
        doc_type: str = "bitable",
        remove_old_owner: bool = False,
        old_owner_perm: str = "edit",
    ) -> None:
        self._request(
            "POST",
            f"/drive/v1/permissions/{app_token}/members/transfer_owner",
            params={
                "type": doc_type,
                "remove_old_owner": str(remove_old_owner).lower(),
                "old_owner_perm": old_owner_perm,
            },
            json_body={"member_type": member_type, "member_id": member_id},
        )

    def grant_user_full_access(
        self,
        app_token: str,
        open_id: str,
        *,
        doc_type: str = "bitable",
    ) -> dict[str, Any]:
        """为用户开通可管理权限并转移文档所有权（应用保留可编辑）。"""
        try:
            self.add_permission_member(
                app_token, open_id, member_type="openid", perm="full_access", doc_type=doc_type
            )
        except RuntimeError as exc:
            if "1063003" not in str(exc) and "already" not in str(exc).lower():
                # 已存在协作者时继续尝试转移所有权
                members = self.list_permission_members(app_token, doc_type=doc_type)
                if not any(m.get("member_id") == open_id for m in members):
                    raise
        try:
            self.transfer_owner(
                app_token,
                open_id,
                member_type="openid",
                doc_type=doc_type,
                remove_old_owner=False,
                old_owner_perm="edit",
            )
        except RuntimeError as exc:
            # 已是所有者时忽略
            if "1063003" not in str(exc):
                raise
        return {"open_id": open_id, "perm": "full_access", "owner_transferred": True}


def parse_bitable_url(url: str) -> dict[str, str]:
    """从多维表格 URL 解析 app_token / table_id / view_id。"""
    app_match = re.search(r"/base/([A-Za-z0-9]+)", url)
    table_match = re.search(r"[?&]table=([A-Za-z0-9]+)", url)
    view_match = re.search(r"[?&]view=([A-Za-z0-9]+)", url)
    result: dict[str, str] = {}
    if app_match:
        result["app_token"] = app_match.group(1)
    if table_match:
        result["table_id"] = table_match.group(1)
    if view_match:
        result["view_id"] = view_match.group(1)
    return result


def load_json_arg(value: str) -> Any:
    path = Path(value)
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    return json.loads(value)


def default_app_token() -> str | None:
    return os.environ.get("FEISHU_BITABLE_APP_TOKEN")


def build_client() -> FeishuBitableClient:
    load_dotenv()
    app_id = os.environ.get("FEISHU_APP_ID")
    app_secret = os.environ.get("FEISHU_APP_SECRET")
    if not app_id or not app_secret:
        raise SystemExit(
            "缺少 FEISHU_APP_ID / FEISHU_APP_SECRET。"
            "请复制 .env.example 为 .env 并填写凭证。"
        )
    return FeishuBitableClient(app_id, app_secret)


def resolve_owner_open_id(client: FeishuBitableClient) -> str:
    """解析应获得全量权限的用户 open_id。"""
    open_id = os.environ.get("FEISHU_OWNER_OPEN_ID", "").strip()
    if open_id:
        return open_id

    email = os.environ.get("FEISHU_OWNER_EMAIL", "").strip()
    if email:
        data = client._request(
            "POST",
            "/contact/v3/users/batch_get_id",
            params={"user_id_type": "open_id"},
            json_body={"emails": [email]},
        )
        user_list = data.get("user_list") or []
        if user_list and user_list[0].get("user_id"):
            return str(user_list[0]["user_id"])
        raise RuntimeError(f"无法通过 FEISHU_OWNER_EMAIL 解析 open_id: {email}")

    data = client._request("GET", "/contact/v3/users", params={"page_size": 50})
    users = data.get("items") or []
    if len(users) == 1 and users[0].get("open_id"):
        return str(users[0]["open_id"])
    if len(users) > 1:
        raise RuntimeError(
            "通讯录有多人可见，请在 .env 设置 FEISHU_OWNER_OPEN_ID 或 FEISHU_OWNER_EMAIL"
        )
    raise RuntimeError(
        "无法解析文档所有者，请在 .env 设置 FEISHU_OWNER_OPEN_ID 或 FEISHU_OWNER_EMAIL"
    )


def ensure_user_full_access(
    client: FeishuBitableClient,
    app_token: str,
    *,
    doc_type: str = "bitable",
    open_id: str | None = None,
) -> dict[str, Any]:
    """创建多维表格后必须调用：为用户开通可管理权限并转移所有权，并校验结果。"""
    owner_open_id = open_id or resolve_owner_open_id(client)
    result = client.grant_user_full_access(app_token, owner_open_id, doc_type=doc_type)
    members = client.list_permission_members(app_token, doc_type=doc_type)
    matched = next((m for m in members if m.get("member_id") == owner_open_id), None)
    if not matched or matched.get("perm") != "full_access":
        raise RuntimeError(
            f"授权校验失败：用户 {owner_open_id} 未获得 full_access，当前成员: {members}"
        )
    result["verified"] = True
    return result


def cmd_auth(_: argparse.Namespace) -> None:
    client = build_client()
    token = client._ensure_token()
    print(json.dumps({"ok": True, "token_prefix": token[:12] + "..."}, ensure_ascii=False))


def cmd_parse_url(args: argparse.Namespace) -> None:
    print(json.dumps(parse_bitable_url(args.url), ensure_ascii=False, indent=2))


def cmd_app_info(args: argparse.Namespace) -> None:
    client = build_client()
    print(json.dumps(client.get_app(args.app_token), ensure_ascii=False, indent=2))


def cmd_create_app(args: argparse.Namespace) -> None:
    client = build_client()
    app = client.create_app(args.name, folder_token=args.folder_token)
    app_token = app["app_token"]
    permission = None
    if not args.skip_grant:
        permission = ensure_user_full_access(client, app_token)
    out = {
        "app": app,
        "url": app.get("url") or f"https://my.feishu.cn/base/{app_token}",
        "permission": permission,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_grant_access(args: argparse.Namespace) -> None:
    client = build_client()
    open_id = args.open_id or None
    if not open_id and args.email:
        data = client._request(
            "POST",
            "/contact/v3/users/batch_get_id",
            params={"user_id_type": "open_id"},
            json_body={"emails": [args.email]},
        )
        user_list = data.get("user_list") or []
        if not user_list or not user_list[0].get("user_id"):
            raise RuntimeError(f"无法通过邮箱解析 open_id: {args.email}")
        open_id = str(user_list[0]["user_id"])
    result = ensure_user_full_access(client, args.app_token, open_id=open_id)
    print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_list_permissions(args: argparse.Namespace) -> None:
    client = build_client()
    print(
        json.dumps(
            client.list_permission_members(args.app_token, doc_type=args.doc_type),
            ensure_ascii=False,
            indent=2,
        )
    )


def cmd_list_tables(args: argparse.Namespace) -> None:
    client = build_client()
    print(json.dumps(client.list_tables(args.app_token), ensure_ascii=False, indent=2))


def cmd_list_fields(args: argparse.Namespace) -> None:
    client = build_client()
    print(json.dumps(client.list_fields(args.app_token, args.table_id), ensure_ascii=False, indent=2))


def cmd_list_records(args: argparse.Namespace) -> None:
    client = build_client()
    records = client.list_records(
        args.app_token,
        args.table_id,
        view_id=args.view_id,
        filter_expr=args.filter,
    )
    print(json.dumps(records, ensure_ascii=False, indent=2))


def cmd_get_record(args: argparse.Namespace) -> None:
    client = build_client()
    print(
        json.dumps(
            client.get_record(args.app_token, args.table_id, args.record_id),
            ensure_ascii=False,
            indent=2,
        )
    )


def cmd_create_record(args: argparse.Namespace) -> None:
    client = build_client()
    fields = load_json_arg(args.fields)
    print(
        json.dumps(
            client.create_record(args.app_token, args.table_id, fields),
            ensure_ascii=False,
            indent=2,
        )
    )


def cmd_batch_create(args: argparse.Namespace) -> None:
    client = build_client()
    records = load_json_arg(args.file)
    if not isinstance(records, list):
        raise SystemExit("batch-create 需要 JSON 数组，每项为 fields 对象")
    print(
        json.dumps(
            client.batch_create_records(args.app_token, args.table_id, records),
            ensure_ascii=False,
            indent=2,
        )
    )


def cmd_update_record(args: argparse.Namespace) -> None:
    client = build_client()
    fields = load_json_arg(args.fields)
    print(
        json.dumps(
            client.update_record(args.app_token, args.table_id, args.record_id, fields),
            ensure_ascii=False,
            indent=2,
        )
    )


def cmd_batch_update(args: argparse.Namespace) -> None:
    client = build_client()
    records = load_json_arg(args.file)
    if not isinstance(records, list):
        raise SystemExit("batch-update 需要 JSON 数组，每项含 record_id 与 fields")
    print(
        json.dumps(
            client.batch_update_records(args.app_token, args.table_id, records),
            ensure_ascii=False,
            indent=2,
        )
    )


def cmd_delete_record(args: argparse.Namespace) -> None:
    client = build_client()
    client.delete_record(args.app_token, args.table_id, args.record_id)
    print(json.dumps({"deleted": args.record_id}, ensure_ascii=False))


def cmd_batch_delete(args: argparse.Namespace) -> None:
    client = build_client()
    ids = load_json_arg(args.ids)
    if not isinstance(ids, list):
        raise SystemExit("batch-delete 需要 JSON 字符串数组")
    client.batch_delete_records(args.app_token, args.table_id, ids)
    print(json.dumps({"deleted_count": len(ids)}, ensure_ascii=False))


def cmd_create_table(args: argparse.Namespace) -> None:
    client = build_client()
    print(
        json.dumps(
            client.create_table(args.app_token, args.name),
            ensure_ascii=False,
            indent=2,
        )
    )


def cmd_update_table(args: argparse.Namespace) -> None:
    client = build_client()
    print(
        json.dumps(
            client.update_table(args.app_token, args.table_id, args.name),
            ensure_ascii=False,
            indent=2,
        )
    )


def cmd_delete_table(args: argparse.Namespace) -> None:
    client = build_client()
    client.delete_table(args.app_token, args.table_id)
    print(json.dumps({"deleted_table": args.table_id}, ensure_ascii=False))


def cmd_create_field(args: argparse.Namespace) -> None:
    client = build_client()
    extra = load_json_arg(args.extra) if args.extra else {}
    if not isinstance(extra, dict):
        raise SystemExit("--extra 必须是 JSON 对象")
    print(
        json.dumps(
            client.create_field(args.app_token, args.table_id, args.name, args.type, **extra),
            ensure_ascii=False,
            indent=2,
        )
    )


def cmd_delete_field(args: argparse.Namespace) -> None:
    client = build_client()
    client.delete_field(args.app_token, args.table_id, args.field_id)
    print(json.dumps({"deleted_field": args.field_id}, ensure_ascii=False))


def add_common_bitable_args(parser: argparse.ArgumentParser, *, require_table: bool = False) -> None:
    parser.add_argument(
        "--app-token",
        default=default_app_token(),
        help="多维表格 app_token（URL /base/ 后那段；可用 FEISHU_BITABLE_APP_TOKEN）",
    )
    if require_table:
        parser.add_argument("--table-id", required=True, help="数据表 table_id（URL 参数 table=）")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="飞书多维表格 CRUD")
    sub = parser.add_subparsers(dest="command", required=True)

    p_auth = sub.add_parser("auth", help="验证 App 凭证并获取 token")
    p_auth.set_defaults(func=cmd_auth)

    p_parse = sub.add_parser("parse-url", help="从浏览器 URL 解析 token")
    p_parse.add_argument("url", help="多维表格完整 URL")
    p_parse.set_defaults(func=cmd_parse_url)

    p_app = sub.add_parser("app-info", help="读取多维表格元信息")
    add_common_bitable_args(p_app)
    p_app.set_defaults(func=cmd_app_info)

    p_create_app = sub.add_parser("create-app", help="新建多维表格（默认自动授予用户全量权限）")
    p_create_app.add_argument("--name", required=True, help="多维表格名称")
    p_create_app.add_argument("--folder-token", help="归属文件夹 token")
    p_create_app.add_argument(
        "--skip-grant",
        action="store_true",
        help="跳过创建后授权（仅调试；正常流程禁止）",
    )
    p_create_app.set_defaults(func=cmd_create_app)

    p_grant = sub.add_parser("grant-access", help="为指定用户开通可管理权限并转移所有权")
    add_common_bitable_args(p_grant)
    p_grant.add_argument("--open-id", help="用户 open_id（优先于邮箱）")
    p_grant.add_argument("--email", help="用户飞书邮箱")
    p_grant.set_defaults(func=cmd_grant_access)

    p_perms = sub.add_parser("list-permissions", help="列出云文档协作者")
    add_common_bitable_args(p_perms)
    p_perms.add_argument("--doc-type", default="bitable", help="云文档类型，默认 bitable")
    p_perms.set_defaults(func=cmd_list_permissions)

    p_tables = sub.add_parser("list-tables", help="列出所有数据表")
    add_common_bitable_args(p_tables)
    p_tables.set_defaults(func=cmd_list_tables)

    p_fields = sub.add_parser("list-fields", help="列出字段")
    add_common_bitable_args(p_fields, require_table=True)
    p_fields.set_defaults(func=cmd_list_fields)

    p_records = sub.add_parser("list-records", help="列出记录（Read）")
    add_common_bitable_args(p_records, require_table=True)
    p_records.add_argument("--view-id", help="可选视图 ID")
    p_records.add_argument("--filter", help="筛选表达式")
    p_records.set_defaults(func=cmd_list_records)

    p_get = sub.add_parser("get-record", help="读取单条记录")
    add_common_bitable_args(p_get, require_table=True)
    p_get.add_argument("--record-id", required=True)
    p_get.set_defaults(func=cmd_get_record)

    p_create = sub.add_parser("create-record", help="新增记录（Create）")
    add_common_bitable_args(p_create, require_table=True)
    p_create.add_argument(
        "--fields",
        required=True,
        help='字段 JSON，如 \'{"名称":"测试"}\' 或 records.json',
    )
    p_create.set_defaults(func=cmd_create_record)

    p_batch_create = sub.add_parser("batch-create", help="批量新增记录")
    add_common_bitable_args(p_batch_create, require_table=True)
    p_batch_create.add_argument("--file", required=True, help="JSON 数组文件")
    p_batch_create.set_defaults(func=cmd_batch_create)

    p_update = sub.add_parser("update-record", help="更新记录（Update）")
    add_common_bitable_args(p_update, require_table=True)
    p_update.add_argument("--record-id", required=True)
    p_update.add_argument("--fields", required=True, help="要更新的字段 JSON")
    p_update.set_defaults(func=cmd_update_record)

    p_batch_update = sub.add_parser("batch-update", help="批量更新记录")
    add_common_bitable_args(p_batch_update, require_table=True)
    p_batch_update.add_argument("--file", required=True)
    p_batch_update.set_defaults(func=cmd_batch_update)

    p_delete = sub.add_parser("delete-record", help="删除记录（Delete）")
    add_common_bitable_args(p_delete, require_table=True)
    p_delete.add_argument("--record-id", required=True)
    p_delete.set_defaults(func=cmd_delete_record)

    p_batch_delete = sub.add_parser("batch-delete", help="批量删除记录")
    add_common_bitable_args(p_batch_delete, require_table=True)
    p_batch_delete.add_argument("--ids", required=True, help='JSON 数组，如 \'["recXXX"]\'')
    p_batch_delete.set_defaults(func=cmd_batch_delete)

    p_create_table = sub.add_parser("create-table", help="新建数据表")
    add_common_bitable_args(p_create_table)
    p_create_table.add_argument("--name", required=True)
    p_create_table.set_defaults(func=cmd_create_table)

    p_update_table = sub.add_parser("update-table", help="重命名数据表")
    add_common_bitable_args(p_update_table, require_table=True)
    p_update_table.add_argument("--name", required=True)
    p_update_table.set_defaults(func=cmd_update_table)

    p_delete_table = sub.add_parser("delete-table", help="删除数据表")
    add_common_bitable_args(p_delete_table, require_table=True)
    p_delete_table.set_defaults(func=cmd_delete_table)

    p_create_field = sub.add_parser("create-field", help="新建字段")
    add_common_bitable_args(p_create_field, require_table=True)
    p_create_field.add_argument("--name", required=True)
    p_create_field.add_argument(
        "--type",
        type=int,
        required=True,
        help="字段类型编号，1=文本 2=数字 3=单选 5=日期 7=复选框 等",
    )
    p_create_field.add_argument("--extra", help="额外 field 属性 JSON")
    p_create_field.set_defaults(func=cmd_create_field)

    p_delete_field = sub.add_parser("delete-field", help="删除字段")
    add_common_bitable_args(p_delete_field, require_table=True)
    p_delete_field.add_argument("--field-id", required=True)
    p_delete_field.set_defaults(func=cmd_delete_field)

    args = parser.parse_args(argv)
    load_dotenv()
    no_app_token_cmds = {"auth", "parse-url", "create-app"}
    if getattr(args, "app_token", None) is None and args.command not in no_app_token_cmds:
        parser.error("缺少 --app-token（或设置 FEISHU_BITABLE_APP_TOKEN）")
    if args.command == "grant-access" and not args.open_id and not args.email:
        if not os.environ.get("FEISHU_OWNER_OPEN_ID") and not os.environ.get("FEISHU_OWNER_EMAIL"):
            parser.error("grant-access 需要 --open-id / --email，或在 .env 配置 FEISHU_OWNER_*")

    try:
        args.func(args)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
