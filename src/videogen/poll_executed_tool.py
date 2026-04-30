import time
from typing import Optional

from .client import VideoGenApi
from .types.executed_tool import ExecutedTool

_TERMINAL_STATUSES = frozenset({"succeeded", "failed", "cancelled"})


def poll_executed_tool(
    client: VideoGenApi,
    tool_execution_id: str,
    *,
    poll_interval_ms: int = 1500,
    timeout_ms: int = 3_600_000,
) -> ExecutedTool:
    """Polls ``get_tool_execution_info`` until status is ``succeeded``, ``failed``, or ``cancelled``.

    Args:
        timeout_ms: Maximum time in ms to wait for a terminal state. Defaults to
            3_600_000 (1 hour).
    """
    deadline = time.monotonic() + timeout_ms / 1000

    while time.monotonic() < deadline:
        executed = client.tools.get_tool_execution_info(
            tool_execution_id=tool_execution_id,
        )

        if executed.status in _TERMINAL_STATUSES:
            return executed

        time.sleep(poll_interval_ms / 1000)

    raise TimeoutError(
        f"Tool execution {tool_execution_id} did not reach a terminal state within {timeout_ms}ms."
    )
