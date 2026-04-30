from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import httpx

if TYPE_CHECKING:
    from .client import AsyncVideoGenApi

from .async_get_hydrated_file import async_get_hydrated_file


async def async_download_file(
    client: AsyncVideoGenApi,
    file_id: str,
    output_path: Optional[str] = None,
) -> Optional[httpx.Response]:
    """Download a file by first hydrating it to get a fresh download URL.

    If *output_path* is provided the file is streamed to disk and ``None``
    is returned.  If *output_path* is omitted the raw ``httpx.Response``
    is returned so the caller can process it:

    .. code-block:: python

        response = await async_download_file(client, file_id)
        data = response.content
    """
    file = await async_get_hydrated_file(client, file_id)

    download = getattr(file, "download_source", None)
    url = getattr(download, "url", None) if download is not None else None

    if url is None:
        status = getattr(download, "status", "unknown") if download is not None else "unknown"
        raise RuntimeError(
            f"File {file_id} has no download URL available (status: {status})."
        )

    async with httpx.AsyncClient() as http:
        if output_path is not None:
            async with http.stream("GET", url) as response:
                response.raise_for_status()
                with open(output_path, "wb") as f:
                    async for chunk in response.aiter_bytes():
                        f.write(chunk)
            return None

        response = await http.get(url)
        response.raise_for_status()
        return response
