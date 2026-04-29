from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import httpx

if TYPE_CHECKING:
    from .client import VideoGenApi

from .get_hydrated_file import get_hydrated_file


def download_file(
    client: VideoGenApi,
    file_id: str,
    output_path: Optional[str] = None,
) -> Optional[httpx.Response]:
    """Download a file by first hydrating it to get a fresh download URL.

    If *output_path* is provided the file is streamed to disk and ``None``
    is returned.  If *output_path* is omitted the raw ``httpx.Response``
    (with streaming enabled) is returned so the caller can process it:

    .. code-block:: python

        response = download_file(client, file_id)
        data = response.read()               # read all bytes
        # -- or --
        with open("out.mp4", "wb") as f:
            for chunk in response.iter_bytes():
                f.write(chunk)
        response.close()
    """
    file = get_hydrated_file(client, file_id)

    download = getattr(file, "download_source", None)
    url = getattr(download, "url", None) if download is not None else None

    if url is None:
        status = getattr(download, "status", "unknown") if download is not None else "unknown"
        raise RuntimeError(
            f"File {file_id} has no download URL available (status: {status})."
        )

    if output_path is not None:
        with httpx.stream("GET", url) as response:
            response.raise_for_status()
            with open(output_path, "wb") as f:
                for chunk in response.iter_bytes():
                    f.write(chunk)
        return None

    response = httpx.get(url)
    response.raise_for_status()
    return response
