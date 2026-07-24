from __future__ import annotations

import time
from typing import Any, Optional

from .errors import VideoGenError
from .poll_helpers import (
    TERMINAL_STATUSES,
    ensure_within_timeout,
    poll_raise_if_cancelled,
    poll_sleep,
)


def poll_remix_actions(
    client: Any,
    project_id: str,
    *,
    poll_interval_ms: int = 1500,
    timeout_ms: Optional[int] = 3_600_000,
    throw_on_failure: bool = True,
    cancel_event: Any = None,
) -> dict:
    started_at = time.monotonic()
    while True:
        poll_raise_if_cancelled(cancel_event)
        ensure_within_timeout(started_at=started_at, timeout_ms=timeout_ms)
        listing = client.projects.list_project_remix_actions(
            project_id=project_id,
            cancel_event=cancel_event,
        )
        actions = listing.get("remix_actions") or []
        if actions and all(a.get("status") in TERMINAL_STATUSES for a in actions):
            if throw_on_failure and any(
                a.get("status") in ("failed", "cancelled") for a in actions
            ):
                raise VideoGenError(
                    "One or more remix actions failed or were cancelled.",
                    status=0,
                    body=listing,
                )
            return listing
        poll_sleep(poll_interval_ms, cancel_event)
