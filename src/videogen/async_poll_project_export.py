import asyncio
from typing import Optional

from .client import AsyncVideoGenApi
from .poll_helpers import _async_poll_raise_if_cancelled, _async_poll_sleep
from .types.project_export import ProjectExport

_TERMINAL_STATUSES = frozenset({"succeeded", "failed"})


async def async_poll_project_export(
    client: AsyncVideoGenApi,
    project_id: str,
    export_id: str,
    *,
    poll_interval_ms: int = 1500,
    timeout_ms: int = 3_600_000,
    cancel_event: Optional[asyncio.Event] = None,
) -> ProjectExport:
    """Polls ``get_project_export`` until status is ``succeeded`` or ``failed``.

    Args:
        timeout_ms: Maximum time in ms to wait for a terminal state. Defaults to
            3_600_000 (1 hour).
        cancel_event: When set, polling stops early with ``PollCancelledError``.
    """
    loop = asyncio.get_running_loop()
    deadline = loop.time() + timeout_ms / 1000

    while loop.time() < deadline:
        await _async_poll_raise_if_cancelled(cancel_event)

        project_export = await client.projects.get_project_export(
            project_id=project_id,
            export_id=export_id,
        )

        if project_export.status in _TERMINAL_STATUSES:
            return project_export

        await _async_poll_sleep(poll_interval_ms, cancel_event)

    raise TimeoutError(
        f"Project export {export_id} for project {project_id} did not reach a terminal state within {timeout_ms}ms."
    )
