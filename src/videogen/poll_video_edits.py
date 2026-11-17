from __future__ import annotations

import time
from typing import Any, Optional, Sequence

from .errors import VideoGenError
from .poll_helpers import (
    TERMINAL_STATUSES,
    poll_sleep,
    ensure_within_timeout,
    poll_raise_if_cancelled,
)


def poll_video_edits(
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
            listing = client.projects.list_video_edits(
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
        poll_sleep(poll_interval_ms, cancel_event)


def _get_video_edit_poll_result(
    edits: list,
    video_edit_ids: Optional[Sequence[str]],
    throw_on_failure: bool,
) -> Optional[dict]:
    if video_edit_ids is not None:
        requested_ids = set(video_edit_ids)
        edits = [edit for edit in edits if edit.get("video_edit_id") in requested_ids]
        if {edit.get("video_edit_id") for edit in edits} != requested_ids:
            return None
    elif not edits:
        return None
    if not all(edit.get("status") in TERMINAL_STATUSES for edit in edits):
        return None
    result = {"video_edits": edits, "has_more": False, "next_cursor": None}
    if throw_on_failure and any(edit.get("status") in ("failed", "cancelled") for edit in edits):
        raise VideoGenError(
            "One or more video edits failed or were cancelled.", status=0, body=result,
        )
    return result
