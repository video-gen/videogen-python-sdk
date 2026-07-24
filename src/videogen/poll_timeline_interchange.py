from __future__ import annotations

import time
from typing import Any, Optional

from .poll_helpers import (
    TERMINAL_STATUSES,
    ensure_within_timeout,
    poll_raise_if_cancelled,
    poll_sleep,
    raise_if_failed,
)


def poll_timeline_interchange(
    client: Any,
    interchange_job_id: str,
    *,
    poll_interval_ms: int = 1500,
    timeout_ms: Optional[int] = 3_600_000,
    throw_on_failure: bool = True,
    cancel_event: Any = None,
) -> dict:
    """Poll `get_timeline_interchange` until succeeded / failed / cancelled."""
    started_at = time.monotonic()
    while True:
        poll_raise_if_cancelled(cancel_event)
        ensure_within_timeout(started_at=started_at, timeout_ms=timeout_ms)
        interchange = client.projects.get_timeline_interchange(
            interchange_job_id=interchange_job_id,
            cancel_event=cancel_event,
        )
        if isinstance(interchange, dict) and interchange.get("status") in TERMINAL_STATUSES:
            raise_if_failed(
                interchange, throw_on_failure=throw_on_failure, kind="Timeline interchange"
            )
            return interchange
        poll_sleep(poll_interval_ms, cancel_event)
