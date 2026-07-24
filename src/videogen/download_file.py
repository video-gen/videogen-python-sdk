from __future__ import annotations

from pathlib import Path
from typing import Any, Optional, Union

import httpx

from .get_hydrated_file import get_hydrated_file


def _pick_download_url(file_obj: dict) -> str:
    for key in ("download_source", "preview_source", "static_public_preview_source"):
        source = file_obj.get(key)
        if isinstance(source, dict) and isinstance(source.get("url"), str) and source["url"]:
            return source["url"]
    raise RuntimeError("No downloadable URL found on hydrated file.")


def download_file(
    client: Any,
    file_id: str,
    *,
    output_path: Optional[Union[str, Path]] = None,
    cancel_event: Any = None,
) -> bytes:
    """Hydrate a file and download its bytes. Optionally write to `output_path`."""
    file_obj = get_hydrated_file(client, file_id, cancel_event=cancel_event)
    url = _pick_download_url(file_obj)
    response = httpx.get(url, timeout=120.0, follow_redirects=True)
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
