import time
from threading import Event
from typing import Optional

from .client import VideoGenApi
from .poll_helpers import _poll_raise_if_cancelled, _poll_sleep
from .types.project_export import ProjectExport

_TERMINAL_STATUSES = frozenset({"succeeded", "failed"})


def poll_project_export(
    client: VideoGenApi,
    project_id: str,
    export_id: str,
    *,
    poll_interval_ms: int = 1500,
    timeout_ms: int = 3_600_000,
    cancel_event: Optional[Event] = None,
) -> ProjectExport:
    """Polls ``get_project_export`` until status is ``succeeded`` or ``failed``.

    Args:
        timeout_ms: Maximum time in ms to wait for a terminal state. Defaults to
            3_600_000 (1 hour).
        cancel_event: When set, polling stops early with ``PollCancelledError``.
    """
    deadline = time.monotonic() + timeout_ms / 1000

    while time.monotonic() < deadline:
        _poll_raise_if_cancelled(cancel_event)

        project_export = client.projects.get_project_export(
            project_id=project_id,
            export_id=export_id,
        )

        if project_export.status in _TERMINAL_STATUSES:
            return project_export

        _poll_sleep(poll_interval_ms, cancel_event)

    raise TimeoutError(
        f"Project export {export_id} for project {project_id} did not reach a terminal state within {timeout_ms}ms."
    )
