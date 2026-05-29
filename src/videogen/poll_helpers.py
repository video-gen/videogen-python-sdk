import asyncio
import time
from threading import Event
from typing import Optional


class PollCancelledError(Exception):
    """Raised when polling is cancelled via ``cancel_event``."""


def _poll_raise_if_cancelled(cancel_event: Optional[Event]) -> None:
    if cancel_event is not None and cancel_event.is_set():
        raise PollCancelledError("Polling was cancelled.")


def _poll_sleep(poll_interval_ms: int, cancel_event: Optional[Event]) -> None:
    if cancel_event is None:
        time.sleep(poll_interval_ms / 1000)
        return

    deadline = time.monotonic() + poll_interval_ms / 1000
    while time.monotonic() < deadline:
        _poll_raise_if_cancelled(cancel_event)
        remaining = deadline - time.monotonic()
        time.sleep(min(0.1, remaining))


async def _async_poll_raise_if_cancelled(
    cancel_event: Optional[asyncio.Event],
) -> None:
    if cancel_event is not None and cancel_event.is_set():
        raise PollCancelledError("Polling was cancelled.")


async def _async_poll_sleep(
    poll_interval_ms: int,
    cancel_event: Optional[asyncio.Event],
) -> None:
    if cancel_event is None:
        await asyncio.sleep(poll_interval_ms / 1000)
        return

    loop = asyncio.get_running_loop()
    deadline = loop.time() + poll_interval_ms / 1000
    while loop.time() < deadline:
        await _async_poll_raise_if_cancelled(cancel_event)
        remaining = deadline - loop.time()
        await asyncio.sleep(min(0.1, remaining))
