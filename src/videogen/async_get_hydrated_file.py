from __future__ import annotations

from typing import Any

from .get_hydrated_file import _needs_hydration


async def async_get_hydrated_file(
    client: Any,
    file_id: str,
    *,
    cancel_event: Any = None,
) -> dict:
    file = await client.files.get_file(file_id=file_id, cancel_event=cancel_event)
    if not _needs_hydration(file):
        return file
    return await client.files.hydrate_file(file_id=file_id, cancel_event=cancel_event)
