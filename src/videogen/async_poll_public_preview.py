import asyncio
from typing import Optional

from .async_client import AsyncVideoGenApi
from .poll_helpers import _async_poll_raise_if_cancelled, _async_poll_sleep
from .poll_public_preview import (
    PublicEmbedPlaybackPollResult,
    PublicPreviewPollResult,
    _assert_public_preview_enabled,
    _build_poll_result,
)


async def async_poll_public_preview_url(
    client: AsyncVideoGenApi,
    file_id: str,
    *,
    poll_interval_ms: int = 1500,
    timeout_ms: int = 120_000,
    cancel_event: Optional[asyncio.Event] = None,
) -> str:
    """Polls ``get_file`` until the permanent public preview URL is ready."""
    result = await async_poll_public_preview(
        client,
        file_id,
        poll_interval_ms=poll_interval_ms,
        timeout_ms=timeout_ms,
        cancel_event=cancel_event,
        wait_for_embed_playback_id=False,
    )
    return result["public_preview_url"]


async def async_poll_public_embed_playback_id(
    client: AsyncVideoGenApi,
    file_id: str,
    *,
    poll_interval_ms: int = 1500,
    timeout_ms: int = 120_000,
    cancel_event: Optional[asyncio.Event] = None,
) -> PublicEmbedPlaybackPollResult:
    """Polls ``get_file`` until the embed playback id is ready (video/audio only)."""
    loop = asyncio.get_running_loop()
    deadline = loop.time() + timeout_ms / 1000

    while loop.time() < deadline:
        await _async_poll_raise_if_cancelled(cancel_event)

        file = await client.files.get_file(file_id=file_id)
        _assert_public_preview_enabled(file)

        file_type = getattr(file, "type", None)
        if file_type not in ("VIDEO", "AUDIO"):
            raise ValueError(
                "Embed playback ids are only available for video and audio files."
            )

        public_playback_id = getattr(file, "public_playback_id", None)
        if public_playback_id is not None and len(public_playback_id) > 0:
            return PublicEmbedPlaybackPollResult(
                public_playback_id=public_playback_id,
                public_hls_url=getattr(file, "public_hls_url", None),
            )

        await _async_poll_sleep(poll_interval_ms, cancel_event)

    raise TimeoutError(
        f"Public embed playback id for file {file_id} was not ready within {timeout_ms}ms."
    )


async def async_poll_public_preview(
    client: AsyncVideoGenApi,
    file_id: str,
    *,
    poll_interval_ms: int = 1500,
    timeout_ms: int = 120_000,
    cancel_event: Optional[asyncio.Event] = None,
    wait_for_embed_playback_id: bool = True,
) -> PublicPreviewPollResult:
    """Polls ``get_file`` until public preview URLs are ready."""
    loop = asyncio.get_running_loop()
    deadline = loop.time() + timeout_ms / 1000

    while loop.time() < deadline:
        await _async_poll_raise_if_cancelled(cancel_event)

        file = await client.files.get_file(file_id=file_id)
        _assert_public_preview_enabled(file)

        result = _build_poll_result(
            file,
            wait_for_embed_playback_id=wait_for_embed_playback_id,
        )
        if result is not None:
            return result

        await _async_poll_sleep(poll_interval_ms, cancel_event)

    raise TimeoutError(
        f"Public preview for file {file_id} was not ready within {timeout_ms}ms."
    )
