import time

from .client import AsyncVideoGenApi
from .types.storage_file import StorageFile


async def async_get_hydrated_file(
    client: AsyncVideoGenApi,
    file_id: str,
) -> StorageFile:
    """Fetch a file, hydrating it if source URLs are missing or expired."""
    file = await client.files.get_file(file_id=file_id)

    download = getattr(file, "download_source", None)
    needs_hydration = (
        download is None
        or getattr(download, "status", None) == "pending"
        or (getattr(download, "status", None) == "ready" and getattr(download, "url", None) is None)
        or (
            getattr(download, "expires_at", None) is not None
            and download.expires_at < int(time.time())
        )
    )

    if not needs_hydration:
        return file

    return await client.files.hydrate_file(file_id=file_id)
