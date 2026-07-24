from __future__ import annotations

import time
from typing import Any, Callable, Optional

from .poll_helpers import (
    TERMINAL_STATUSES,
    async_poll_sleep,
    ensure_within_timeout,
    poll_raise_if_cancelled,
    raise_if_failed,
)


async def async_poll_workflow_run(
    client: Any,
    workflow_run_id: str,
    *,
    poll_interval_ms: int = 1500,
    timeout_ms: Optional[int] = 3_600_000,
    throw_on_failure: bool = True,
    on_progress: Optional[Callable[[float], None]] = None,
    cancel_event: Any = None,
) -> dict:
    """Async twin of `poll_workflow_run`."""
    started_at = time.monotonic()
    while True:
        poll_raise_if_cancelled(cancel_event)
        ensure_within_timeout(started_at=started_at, timeout_ms=timeout_ms)
        run = await client.workflows.get_workflow_run(
            workflow_run_id=workflow_run_id,
            cancel_event=cancel_event,
        )
        if isinstance(run, dict):
            progress = run.get("progress_percentage")
            if on_progress is not None and isinstance(progress, (int, float)):
                on_progress(float(progress))
            if run.get("status") in TERMINAL_STATUSES:
                raise_if_failed(run, throw_on_failure=throw_on_failure, kind="Workflow run")
                return run
        await async_poll_sleep(poll_interval_ms, cancel_event)
