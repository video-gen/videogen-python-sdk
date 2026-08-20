from __future__ import annotations

import time
from typing import Any, BinaryIO, Optional, Union

import httpx

from .poll_helpers import ensure_within_timeout, poll_raise_if_cancelled, poll_sleep


def _read_bytes(data: Union[bytes, bytearray, BinaryIO]) -> bytes:
    if isinstance(data, (bytes, bytearray)):
        return bytes(data)
    return data.read()


_SOURCE_KEYS = (
    "download_source",
    "preview_source",
    "thumbnail_source",
    "hls_source",
)


def _file_has_ready_source(file_obj: dict) -> bool:
    for key in _SOURCE_KEYS:
        source = file_obj.get(key)
        if isinstance(source, dict) and source.get("status") == "ready":
            return True
    return False


def _file_has_failed_source(file_obj: dict) -> bool:
    for key in _SOURCE_KEYS:
        source = file_obj.get(key)
        if isinstance(source, dict) and source.get("status") == "failed":
            return True
    return False


def upload_file(
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
    """Create an upload URL, PUT bytes, and poll until a source is ready.

    Args:
        type: Optional file type (IMAGE, VIDEO, AUDIO, PDF, SLIDESHOW, LOTTIE).
            If omitted, auto-detected. Lottie animations (Bodymovin JSON) must
            set LOTTIE explicitly.
        hide_from_ui: When true, hide the file from the VideoGen Media page.
            Defaults to false.
        timeout_ms: Maximum time in ms to wait for processing. Defaults to
            3_600_000 (1 hour).

    Note:
        Polls ``hydrate_file`` (not ``get_file``). ``get_file`` omits signed
        source URLs, so readiness is only visible after hydration.

        A secondary source (hls / thumbnail) can be ``failed`` after a probe
        error while ``download_source`` is already ``ready`` from R2. Any ready
        source means the upload is usable; only fail when something failed and
        nothing is ready.
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

    created = client.files.create_file_upload(**body, cancel_event=cancel_event)
    file_id = created["file_id"]
    upload_url = created["upload_url"]
    payload = _read_bytes(data)

    headers = {}
    if content_type:
        headers["Content-Type"] = content_type
    put_response = httpx.put(upload_url, content=payload, headers=headers, timeout=120.0)
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
        file_obj = client.files.hydrate_file(file_id=file_id, cancel_event=cancel_event)
        if isinstance(file_obj, dict) and _file_has_ready_source(file_obj):
            return file_obj
        if isinstance(file_obj, dict) and _file_has_failed_source(file_obj):
            raise RuntimeError("Uploaded file processing failed")
        poll_sleep(poll_interval_ms, cancel_event)
