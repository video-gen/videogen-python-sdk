import asyncio
from typing import Optional

from .client import AsyncVideoGenApi
from .poll_helpers import _async_poll_raise_if_cancelled, _async_poll_sleep
from .types.workflow_run import WorkflowRun

_TERMINAL_STATUSES = frozenset({"succeeded", "failed", "cancelled"})


async def async_poll_workflow_run(
    client: AsyncVideoGenApi,
    workflow_run_id: str,
    *,
    poll_interval_ms: int = 1500,
    timeout_ms: int = 3_600_000,
    cancel_event: Optional[asyncio.Event] = None,
) -> WorkflowRun:
    """Polls ``get_workflow_run`` until status is ``succeeded``, ``failed``, or ``cancelled``.

    Args:
        timeout_ms: Maximum time in ms to wait for a terminal state. Defaults to
            3_600_000 (1 hour).
        cancel_event: When set, polling stops early with ``PollCancelledError``.
    """
    loop = asyncio.get_running_loop()
    deadline = loop.time() + timeout_ms / 1000

    while loop.time() < deadline:
        await _async_poll_raise_if_cancelled(cancel_event)

        workflow_run = await client.workflows.get_workflow_run(
            workflow_run_id=workflow_run_id,
        )

        if workflow_run.status in _TERMINAL_STATUSES:
            return workflow_run

        await _async_poll_sleep(poll_interval_ms, cancel_event)

    raise TimeoutError(
        f"Workflow run {workflow_run_id} did not reach a terminal state within {timeout_ms}ms."
    )
