from __future__ import annotations

import time
from typing import Any


_SOURCE_KEYS = (
    "download_source",
    "preview_source",
    "thumbnail_source",
    "hls_source",
)


def _needs_hydration(file: dict) -> bool:
    now_seconds = int(time.time())
    for key in _SOURCE_KEYS:
        source = file.get(key)
        if source is None:
            continue
        if source.get("status") == "pending":
            return True
        if source.get("status") == "ready":
            if source.get("url") is None:
                return True
            expires_at = source.get("expires_at")
            if expires_at is not None and expires_at <= now_seconds + 60:
                return True

    has_any_ready_url = False
    for key in _SOURCE_KEYS:
        source = file.get(key)
        if source is not None and source.get("status") == "ready" and source.get("url") is not None:
            has_any_ready_url = True
            break
    return not has_any_ready_url


def get_hydrated_file(
    client: Any,
    file_id: str,
    *,
    cancel_event: Any = None,
) -> dict:
    file = client.files.get_file(file_id=file_id, cancel_event=cancel_event)
    if not _needs_hydration(file):
        return file
    return client.files.hydrate_file(file_id=file_id, cancel_event=cancel_event)
