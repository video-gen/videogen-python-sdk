from __future__ import annotations

from typing import Any, Optional

from .poll_public_preview import poll_public_preview


def create_public_preview(
    client: Any,
    file_id: str,
    *,
    poll_interval_ms: int = 1500,
    timeout_ms: Optional[int] = 3_600_000,
    wait_for_embed_playback_id: bool = False,
    cancel_event: Any = None,
) -> dict:
    """Enable public preview and poll until the public URL is ready."""
    client.files.enable_public_preview(file_id=file_id, cancel_event=cancel_event)
    return poll_public_preview(
        client,
        file_id,
        poll_interval_ms=poll_interval_ms,
        timeout_ms=timeout_ms,
        wait_for_embed_playback_id=wait_for_embed_playback_id,
        cancel_event=cancel_event,
    )
