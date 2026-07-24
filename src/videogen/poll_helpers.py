from __future__ import annotations

import asyncio
import time
from typing import Any, Optional

from .errors import PollCancelledError, VideoGenError


TERMINAL_STATUSES = frozenset({"succeeded", "failed", "cancelled"})


def poll_raise_if_cancelled(cancel_event: Any) -> None:
    if cancel_event is not None and cancel_event.is_set():
        raise PollCancelledError()


def poll_sleep(poll_interval_ms: int, cancel_event: Any = None) -> None:
    deadline = time.monotonic() + (poll_interval_ms / 1000.0)
    while True:
        poll_raise_if_cancelled(cancel_event)
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return
        time.sleep(min(remaining, 0.05))


async def async_poll_sleep(poll_interval_ms: int, cancel_event: Any = None) -> None:
    deadline = time.monotonic() + (poll_interval_ms / 1000.0)
    while True:
        poll_raise_if_cancelled(cancel_event)
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return
        await asyncio.sleep(min(remaining, 0.05))


def ensure_within_timeout(*, started_at: float, timeout_ms: Optional[int]) -> None:
    if timeout_ms is None:
        return
    if (time.monotonic() - started_at) * 1000.0 >= timeout_ms:
        raise TimeoutError(f"Timed out after {timeout_ms}ms while polling.")


def raise_if_failed(
    result: dict,
    *,
    throw_on_failure: bool,
    kind: str,
) -> None:
    if not throw_on_failure:
        return
    status = result.get("status")
    if status in ("failed", "cancelled"):
        message = result.get("error") or result.get("message") or f"{kind} {status}"
        if not isinstance(message, str):
            message = f"{kind} {status}"
        raise VideoGenError(message, status=0, body=result)
