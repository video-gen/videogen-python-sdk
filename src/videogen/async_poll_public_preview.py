from __future__ import annotations

import time
from typing import Any, Optional

from .poll_helpers import async_poll_sleep, ensure_within_timeout, poll_raise_if_cancelled
from .poll_public_preview import _preview_ready


async def async_poll_public_preview(
    client: Any,
    file_id: str,
    *,
    poll_interval_ms: int = 1500,
    timeout_ms: Optional[int] = 3_600_000,
    wait_for_embed_playback_id: bool = False,
    cancel_event: Any = None,
) -> dict:
    """Async twin of `poll_public_preview`."""
    started_at = time.monotonic()
    while True:
        poll_raise_if_cancelled(cancel_event)
        ensure_within_timeout(started_at=started_at, timeout_ms=timeout_ms)
        file_obj = await client.files.get_file(file_id=file_id, cancel_event=cancel_event)
        if isinstance(file_obj, dict) and _preview_ready(
            file_obj, wait_for_embed_playback_id=wait_for_embed_playback_id
        ):
            return file_obj
        await async_poll_sleep(poll_interval_ms, cancel_event)
