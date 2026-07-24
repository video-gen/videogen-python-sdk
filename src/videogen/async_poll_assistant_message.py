from __future__ import annotations

import time
from typing import Any, Optional

from .errors import VideoGenError
from .poll_helpers import (
    TERMINAL_STATUSES,
    async_poll_sleep,
    ensure_within_timeout,
    poll_raise_if_cancelled,
)


async def async_poll_assistant_message(
    client: Any,
    message_id: str,
    *,
    poll_interval_ms: int = 1500,
    timeout_ms: Optional[int] = 3_600_000,
    throw_on_failure: bool = True,
    cancel_event: Any = None,
) -> dict:
    """Async twin of `poll_assistant_message`."""
    started_at = time.monotonic()
    while True:
        poll_raise_if_cancelled(cancel_event)
        ensure_within_timeout(started_at=started_at, timeout_ms=timeout_ms)
        message = await client.assistant.get_assistant_message(
            message_id=message_id,
            cancel_event=cancel_event,
        )
        if isinstance(message, dict) and message.get("status") in TERMINAL_STATUSES:
            _raise_if_assistant_message_failed(
                message,
                throw_on_failure=throw_on_failure,
            )
            return message
        await async_poll_sleep(poll_interval_ms, cancel_event)


def _raise_if_assistant_message_failed(
    message: dict,
    *,
    throw_on_failure: bool,
) -> None:
    if not throw_on_failure:
        return
    status = message.get("status")
    if status not in ("failed", "cancelled"):
        return
    error = message.get("error")
    if isinstance(error, dict):
        error_message = error.get("message")
        if isinstance(error_message, str) and error_message:
            raise VideoGenError(error_message, status=0, body=message)
    raise VideoGenError(f"Assistant message {status}", status=0, body=message)
