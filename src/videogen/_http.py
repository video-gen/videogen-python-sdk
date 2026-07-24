from __future__ import annotations

import json
import os
import re
from typing import Any, Mapping, Optional

import httpx

from .errors import PollCancelledError, VideoGenError


DEFAULT_BASE_URL = "https://api.videogen.io"

DEFAULT_CLIENT_ID = "sdk-python"


_CAMEL_BOUNDARY = re.compile(r"([a-z0-9])([A-Z])")
_SNAKE_SPLIT = re.compile(r"_+")


def snake_to_camel(key: str) -> str:
    if "_" not in key:
        return key
    parts = _SNAKE_SPLIT.split(key)
    if not parts:
        return key
    head = parts[0]
    return head + "".join(part[:1].upper() + part[1:] for part in parts[1:] if part)


def camel_to_snake(key: str) -> str:
    if "_" in key or key == "":
        return key
    # Preserve all-uppercase enum-like keys (e.g. ENABLE_CAPTIONS stays as-is when already snake)
    return _CAMEL_BOUNDARY.sub(r"\1_\2", key).lower()


def to_wire_keys(value: Any) -> Any:
    """Recursively convert snake_case dict keys to camelCase for JSON bodies/queries."""
    if isinstance(value, Mapping):
        return {snake_to_camel(str(k)): to_wire_keys(v) for k, v in value.items()}
    if isinstance(value, list):
        return [to_wire_keys(item) for item in value]
    if isinstance(value, tuple):
        return [to_wire_keys(item) for item in value]
    return value


def to_python_keys(value: Any) -> Any:
    """Recursively convert camelCase JSON keys to snake_case for Python callers."""
    if isinstance(value, Mapping):
        return {camel_to_snake(str(k)): to_python_keys(v) for k, v in value.items()}
    if isinstance(value, list):
        return [to_python_keys(item) for item in value]
    if isinstance(value, tuple):
        return [to_python_keys(item) for item in value]
    return value


def _raise_if_cancelled(cancel_event: Any) -> None:
    if cancel_event is not None and cancel_event.is_set():
        raise PollCancelledError()


def _parse_error_body(response: httpx.Response) -> Any:
    text = response.text
    if not text:
        return None
    try:
        return response.json()
    except Exception:
        return text


def _error_message(body: Any, status: int) -> str:
    if isinstance(body, Mapping):
        message = body.get("message")
        if isinstance(message, str) and message:
            return message
    return f"VideoGen API request failed with status {status}"


class SyncHttpClient:
    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        http_client: Optional[httpx.Client] = None,
        timeout: float = 60.0,
        client_id: str = DEFAULT_CLIENT_ID,
    ) -> None:
        resolved_key = api_key if api_key is not None else os.environ.get("VIDEOGEN_API_KEY")
        if resolved_key is None or resolved_key == "":
            raise ValueError(
                "api_key is required (pass api_key=... or set VIDEOGEN_API_KEY)."
            )
        self.api_key = resolved_key
        self.base_url = (base_url or DEFAULT_BASE_URL).rstrip("/")
        self.client_id = client_id
        self._owns_client = http_client is None
        self._client = http_client or httpx.Client(timeout=timeout)

    def close(self) -> None:
        if self._owns_client:
            self._client.close()

    def __enter__(self) -> "SyncHttpClient":
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    def request(
        self,
        *,
        method: str,
        path: str,
        query: Optional[Mapping[str, Any]] = None,
        body: Any = None,
        cancel_event: Any = None,
        raw_response: bool = False,
    ) -> Any:
        _raise_if_cancelled(cancel_event)

        url = path if path.startswith("http://") or path.startswith("https://") else f"{self.base_url}{path}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "X-VideoGen-Client": self.client_id,
        }
        params = to_wire_keys(dict(query)) if query else None
        if params is not None:
            params = {k: v for k, v in params.items() if v is not None}

        json_body = None
        content = None
        if body is not None:
            if isinstance(body, (bytes, bytearray)):
                content = bytes(body)
            else:
                json_body = to_wire_keys(body)
                headers["Content-Type"] = "application/json"

        response = self._client.request(
            method=method.upper(),
            url=url,
            params=params,
            json=json_body,
            content=content,
            headers=headers,
        )

        _raise_if_cancelled(cancel_event)

        request_id = response.headers.get("x-request-id")
        if response.status_code >= 400:
            err_body = _parse_error_body(response)
            raise VideoGenError(
                _error_message(err_body, response.status_code),
                status=response.status_code,
                body=to_python_keys(err_body) if isinstance(err_body, (dict, list)) else err_body,
                request_id=request_id,
            )

        if raw_response:
            return response

        if response.status_code == 204 or not response.content:
            return None

        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type or response.text[:1] in "{[":
            try:
                data = response.json()
            except json.JSONDecodeError:
                return response.text
            return to_python_keys(data)
        return response.content


class AsyncHttpClient:
    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        http_client: Optional[httpx.AsyncClient] = None,
        timeout: float = 60.0,
        client_id: str = DEFAULT_CLIENT_ID,
    ) -> None:
        resolved_key = api_key if api_key is not None else os.environ.get("VIDEOGEN_API_KEY")
        if resolved_key is None or resolved_key == "":
            raise ValueError(
                "api_key is required (pass api_key=... or set VIDEOGEN_API_KEY)."
            )
        self.api_key = resolved_key
        self.base_url = (base_url or DEFAULT_BASE_URL).rstrip("/")
        self.client_id = client_id
        self._owns_client = http_client is None
        self._client = http_client or httpx.AsyncClient(timeout=timeout)

    async def aclose(self) -> None:
        if self._owns_client:
            await self._client.aclose()

    async def __aenter__(self) -> "AsyncHttpClient":
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.aclose()

    async def request(
        self,
        *,
        method: str,
        path: str,
        query: Optional[Mapping[str, Any]] = None,
        body: Any = None,
        cancel_event: Any = None,
        raw_response: bool = False,
    ) -> Any:
        _raise_if_cancelled(cancel_event)

        url = path if path.startswith("http://") or path.startswith("https://") else f"{self.base_url}{path}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "X-VideoGen-Client": self.client_id,
        }
        params = to_wire_keys(dict(query)) if query else None
        if params is not None:
            params = {k: v for k, v in params.items() if v is not None}

        json_body = None
        content = None
        if body is not None:
            if isinstance(body, (bytes, bytearray)):
                content = bytes(body)
            else:
                json_body = to_wire_keys(body)
                headers["Content-Type"] = "application/json"

        response = await self._client.request(
            method=method.upper(),
            url=url,
            params=params,
            json=json_body,
            content=content,
            headers=headers,
        )

        _raise_if_cancelled(cancel_event)

        request_id = response.headers.get("x-request-id")
        if response.status_code >= 400:
            err_body = _parse_error_body(response)
            raise VideoGenError(
                _error_message(err_body, response.status_code),
                status=response.status_code,
                body=to_python_keys(err_body) if isinstance(err_body, (dict, list)) else err_body,
                request_id=request_id,
            )

        if raw_response:
            return response

        if response.status_code == 204 or not response.content:
            return None

        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type or response.text[:1] in "{[":
            try:
                data = response.json()
            except json.JSONDecodeError:
                return response.text
            return to_python_keys(data)
        return response.content


RequestOptions = Mapping[str, Any]


def split_request_args(
    kwargs: Mapping[str, Any],
    *,
    path_params: list[str],
    query_params: list[str],
) -> tuple[dict[str, Any], dict[str, Any], Optional[dict[str, Any]], Any]:
    """Split merged snake_case kwargs into path / query / body / cancel_event."""
    data = dict(kwargs)
    cancel_event = data.pop("cancel_event", None)
    options = data.pop("options", None)
    if isinstance(options, Mapping) and cancel_event is None:
        cancel_event = options.get("cancel_event")

    path_values: dict[str, Any] = {}
    for name in path_params:
        snake = camel_to_snake(name)
        if snake in data:
            path_values[name] = data.pop(snake)
        elif name in data:
            path_values[name] = data.pop(name)

    query_values: dict[str, Any] = {}
    for name in query_params:
        snake = camel_to_snake(name)
        if snake in data:
            query_values[name] = data.pop(snake)
        elif name in data:
            query_values[name] = data.pop(name)

    body: Optional[dict[str, Any]] = data if data else None
    return path_values, query_values, body, cancel_event


def format_path(path_template: str, path_values: Mapping[str, Any]) -> str:
    path = path_template
    for key, value in path_values.items():
        path = path.replace("{" + key + "}", str(value))
    return path
