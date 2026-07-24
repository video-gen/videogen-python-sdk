from __future__ import annotations

import time
from typing import Any, Optional

from .poll_helpers import (
    TERMINAL_STATUSES,
    async_poll_sleep,
    ensure_within_timeout,
    poll_raise_if_cancelled,
    raise_if_failed,
)


async def async_poll_executed_tool(
    client: Any,
    tool_execution_id: str,
    *,
    poll_interval_ms: int = 1500,
    timeout_ms: Optional[int] = 3_600_000,
    throw_on_failure: bool = True,
    cancel_event: Any = None,
) -> dict:
    """Async twin of `poll_executed_tool`."""
    started_at = time.monotonic()
    while True:
        poll_raise_if_cancelled(cancel_event)
        ensure_within_timeout(started_at=started_at, timeout_ms=timeout_ms)
        executed = await client.tools.get_tool_execution_info(
            tool_execution_id=tool_execution_id,
            cancel_event=cancel_event,
        )
        if isinstance(executed, dict) and executed.get("status") in TERMINAL_STATUSES:
            raise_if_failed(executed, throw_on_failure=throw_on_failure, kind="Tool execution")
            return executed
        await async_poll_sleep(poll_interval_ms, cancel_event)
