import asyncio

from .client import AsyncVideoGenApi
from .types.executed_tool import ExecutedTool

_TERMINAL_STATUSES = frozenset({"succeeded", "failed", "cancelled"})


async def async_poll_executed_tool(
    client: AsyncVideoGenApi,
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
    deadline = asyncio.get_event_loop().time() + timeout_ms / 1000

    while asyncio.get_event_loop().time() < deadline:
        executed = await client.tools.get_tool_execution_info(
            tool_execution_id=tool_execution_id,
        )

        if executed.status in _TERMINAL_STATUSES:
            return executed

        await asyncio.sleep(poll_interval_ms / 1000)

    raise TimeoutError(
        f"Tool execution {tool_execution_id} did not reach a terminal state within {timeout_ms}ms."
    )
