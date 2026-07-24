from __future__ import annotations

import time
from typing import Any, Optional

from .poll_helpers import ensure_within_timeout, poll_raise_if_cancelled, poll_sleep


def _preview_ready(file_obj: dict, *, wait_for_embed_playback_id: bool) -> bool:
    preview = file_obj.get("static_public_preview_source")
    url = None
    if isinstance(preview, dict):
        url = preview.get("url")
    if not isinstance(url, str) or not url:
        return False
    if wait_for_embed_playback_id:
        playback_id = file_obj.get("public_playback_id")
        return isinstance(playback_id, str) and bool(playback_id)
    return True


def poll_public_preview(
    client: Any,
    file_id: str,
    *,
    poll_interval_ms: int = 1500,
    timeout_ms: Optional[int] = 3_600_000,
    wait_for_embed_playback_id: bool = False,
    cancel_event: Any = None,
) -> dict:
    """Poll `get_file` until a public preview URL is ready."""
    started_at = time.monotonic()
    while True:
        poll_raise_if_cancelled(cancel_event)
        ensure_within_timeout(started_at=started_at, timeout_ms=timeout_ms)
        file_obj = client.files.get_file(file_id=file_id, cancel_event=cancel_event)
        if isinstance(file_obj, dict) and _preview_ready(
            file_obj, wait_for_embed_playback_id=wait_for_embed_playback_id
        ):
            return file_obj
        poll_sleep(poll_interval_ms, cancel_event)
