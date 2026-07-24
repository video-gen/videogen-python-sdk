from __future__ import annotations

from pathlib import Path
from typing import Any, Optional, Union

import httpx

from .async_get_hydrated_file import async_get_hydrated_file
from .download_file import _pick_download_url


async def async_download_file(
    client: Any,
    file_id: str,
    *,
    output_path: Optional[Union[str, Path]] = None,
    cancel_event: Any = None,
) -> bytes:
    """Async twin of `download_file`."""
    file_obj = await async_get_hydrated_file(client, file_id, cancel_event=cancel_event)
    url = _pick_download_url(file_obj)
    async with httpx.AsyncClient(timeout=120.0, follow_redirects=True) as http:
        response = await http.get(url)
    if response.status_code >= 400:
        raise RuntimeError(
            f"Download failed with status {response.status_code}: {response.text}"
        )
    content = response.content
    if output_path is not None:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    return content
