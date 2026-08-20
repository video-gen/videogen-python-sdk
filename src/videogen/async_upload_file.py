from __future__ import annotations

import time
from typing import Any, BinaryIO, Optional, Union

import httpx

from .poll_helpers import async_poll_sleep, ensure_within_timeout, poll_raise_if_cancelled
from .upload_file import _file_has_failed_source, _file_has_ready_source, _read_bytes


async def async_upload_file(
    client: Any,
    data: Union[bytes, bytearray, BinaryIO],
    *,
    type: Optional[str] = None,
    display_name: Optional[str] = None,
    temporary: Optional[bool] = None,
    is_temporary: Optional[bool] = None,
    hide_from_ui: Optional[bool] = None,
    content_type: Optional[str] = None,
    poll_interval_ms: int = 1500,
    timeout_ms: Optional[int] = 3_600_000,
    cancel_event: Any = None,
) -> dict:
    """Async twin of `upload_file`.

    Args:
        type: Optional file type (IMAGE, VIDEO, AUDIO, PDF, SLIDESHOW, LOTTIE).
            If omitted, auto-detected. Lottie animations (Bodymovin JSON) must
            set LOTTIE explicitly.
        hide_from_ui: When true, hide the file from the VideoGen Media page.
            Defaults to false.
        timeout_ms: Maximum time in ms to wait for processing. Defaults to
            3_600_000 (1 hour).
    """
    if display_name is None:
        display_name = "upload"
    body: dict[str, Any] = {
        "display_name": display_name,
        "hide_from_ui": False if hide_from_ui is None else hide_from_ui,
    }
    if type is not None:
        body["type"] = type
    temp = is_temporary if is_temporary is not None else temporary
    if temp is not None:
        body["is_temporary"] = temp
    else:
        body["is_temporary"] = False

    created = await client.files.create_file_upload(**body, cancel_event=cancel_event)
    file_id = created["file_id"]
    upload_url = created["upload_url"]
    payload = _read_bytes(data)

    headers = {}
    if content_type:
        headers["Content-Type"] = content_type
    async with httpx.AsyncClient(timeout=120.0) as http:
        put_response = await http.put(upload_url, content=payload, headers=headers)
    if put_response.status_code >= 400:
        raise RuntimeError(
            f"Upload PUT failed with status {put_response.status_code}: {put_response.text}"
        )

    started_at = time.monotonic()
    while True:
        poll_raise_if_cancelled(cancel_event)
        ensure_within_timeout(started_at=started_at, timeout_ms=timeout_ms)
        # hydrate_file (not get_file): GET omits signed sources, so readiness
        # never flips if we poll get_file alone.
        file_obj = await client.files.hydrate_file(file_id=file_id, cancel_event=cancel_event)
        if isinstance(file_obj, dict) and _file_has_ready_source(file_obj):
            return file_obj
        if isinstance(file_obj, dict) and _file_has_failed_source(file_obj):
            raise RuntimeError("Uploaded file processing failed")
        await async_poll_sleep(poll_interval_ms, cancel_event)
