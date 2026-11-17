from __future__ import annotations

import time
from typing import Any, Optional, Sequence

from .poll_helpers import (
    async_poll_sleep,
    ensure_within_timeout,
    poll_raise_if_cancelled,
)
from .poll_video_edits import _get_video_edit_poll_result


async def async_poll_video_edits(
    client: Any,
    project_id: str,
    *,
    editable_video_id: Optional[str] = None,
    video_edit_ids: Optional[Sequence[str]] = None,
    poll_interval_ms: int = 1500,
    timeout_ms: Optional[int] = 3_600_000,
    throw_on_failure: bool = True,
    cancel_event: Any = None,
) -> dict:
    """Poll video edits, optionally limited to the exact ids returned by a start."""
    started_at = time.monotonic()
    while True:
        poll_raise_if_cancelled(cancel_event)
        ensure_within_timeout(started_at=started_at, timeout_ms=timeout_ms)
        edits = []
        cursor = None
        while True:
            poll_raise_if_cancelled(cancel_event)
            ensure_within_timeout(started_at=started_at, timeout_ms=timeout_ms)
            listing = await client.projects.list_video_edits(
                project_id=project_id,
                editable_video_id=editable_video_id,
                limit=200,
                cursor=cursor,
                cancel_event=cancel_event,
            )
            edits.extend(listing.get("video_edits") or [])
            cursor = listing.get("next_cursor")
            if not listing.get("has_more") or cursor is None:
                break
        result = _get_video_edit_poll_result(edits, video_edit_ids, throw_on_failure)
        if result is not None:
            return result
        await async_poll_sleep(poll_interval_ms, cancel_event)
