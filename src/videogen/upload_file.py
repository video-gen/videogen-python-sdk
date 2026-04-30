from __future__ import annotations

import time
from typing import BinaryIO, Optional, TYPE_CHECKING

import httpx

if TYPE_CHECKING:
    from .client import VideoGenApi
    from .types.storage_file import StorageFile


def upload_file(
    client: VideoGenApi,
    file: BinaryIO,
    *,
    display_name: str,
    type: Optional[str] = None,
    temporary: bool = False,
    poll_interval_ms: int = 2000,
    timeout_ms: int = 3_600_000,
) -> StorageFile:
    """Upload a file to VideoGen.

    1. Creates a pending file via ``create_file_upload``
    2. PUTs the raw bytes to the returned presigned URL
    3. Polls until the file is processed, then returns the hydrated file

    Args:
        type: Optional file type (IMAGE, VIDEO, AUDIO). If omitted, auto-detected.
        timeout_ms: Maximum time in ms to wait for processing. Defaults to
            3_600_000 (1 hour).
    """
    upload_response = client.files.create_file_upload(
        display_name=display_name,
        is_temporary=temporary,
        **({"type": type} if type is not None else {}),
    )

    data = file.read()
    put_response = httpx.put(upload_response.upload_url, content=data)
    put_response.raise_for_status()

    deadline = time.monotonic() + timeout_ms / 1000

    while time.monotonic() < deadline:
        current = client.files.hydrate_file(file_id=upload_response.file_id)

        download = getattr(current, "download_source", None)
        preview = getattr(current, "preview_source", None)

        has_ready = (
            (download is not None and getattr(download, "status", None) == "ready")
            or (preview is not None and getattr(preview, "status", None) == "ready")
        )

        if has_ready:
            return current

        time.sleep(poll_interval_ms / 1000)

    raise TimeoutError(
        f"File {upload_response.file_id} was not processed within {timeout_ms}ms."
    )
