import time
from threading import Event
from typing import Optional, TypedDict

from .client import VideoGenApi
from .poll_helpers import _poll_raise_if_cancelled, _poll_sleep
from .types.storage_file import StorageFile

PUBLIC_PREVIEW_NOT_ENABLED_ERROR_MESSAGE = (
    "Public preview is not enabled for this file. Call enable_public_preview before polling."
)


class PublicPreviewPollResult(TypedDict):
    public_preview_url: str
    public_playback_id: Optional[str]
    public_hls_url: Optional[str]


class PublicEmbedPlaybackPollResult(TypedDict):
    public_playback_id: str
    public_hls_url: Optional[str]


def _assert_public_preview_enabled(file: StorageFile) -> None:
    if not getattr(file, "is_public_preview_enabled", False):
        raise ValueError(PUBLIC_PREVIEW_NOT_ENABLED_ERROR_MESSAGE)


def _is_static_public_preview_ready(file: StorageFile) -> bool:
    source = getattr(file, "static_public_preview_source", None)
    if source is None:
        return False
    url = getattr(source, "url", None)
    return getattr(source, "status", None) == "ready" and url is not None and len(url) > 0


def _should_wait_for_embed_playback_id(
    file: StorageFile,
    *,
    wait_for_embed_playback_id: bool,
) -> bool:
    if not wait_for_embed_playback_id:
        return False
    file_type = getattr(file, "type", None)
    return file_type in ("VIDEO", "AUDIO")


def _is_embed_playback_ready(file: StorageFile) -> bool:
    public_playback_id = getattr(file, "public_playback_id", None)
    return public_playback_id is not None and len(public_playback_id) > 0


def _build_poll_result(
    file: StorageFile,
    *,
    wait_for_embed_playback_id: bool,
) -> Optional[PublicPreviewPollResult]:
    if not _is_static_public_preview_ready(file):
        return None

    source = getattr(file, "static_public_preview_source", None)
    public_preview_url = getattr(source, "url", None) if source is not None else None
    if public_preview_url is None or len(public_preview_url) == 0:
        return None

    if _should_wait_for_embed_playback_id(
        file,
        wait_for_embed_playback_id=wait_for_embed_playback_id,
    ) and not _is_embed_playback_ready(file):
        return None

    return PublicPreviewPollResult(
        public_preview_url=public_preview_url,
        public_playback_id=getattr(file, "public_playback_id", None),
        public_hls_url=getattr(file, "public_hls_url", None),
    )


def poll_public_preview_url(
    client: VideoGenApi,
    file_id: str,
    *,
    poll_interval_ms: int = 1500,
    timeout_ms: int = 120_000,
    cancel_event: Optional[Event] = None,
) -> str:
    """Polls ``get_file`` until the permanent public preview URL is ready."""
    result = poll_public_preview(
        client,
        file_id,
        poll_interval_ms=poll_interval_ms,
        timeout_ms=timeout_ms,
        cancel_event=cancel_event,
        wait_for_embed_playback_id=False,
    )
    return result["public_preview_url"]


def poll_public_embed_playback_id(
    client: VideoGenApi,
    file_id: str,
    *,
    poll_interval_ms: int = 1500,
    timeout_ms: int = 120_000,
    cancel_event: Optional[Event] = None,
) -> PublicEmbedPlaybackPollResult:
    """Polls ``get_file`` until the embed playback id is ready (video/audio only)."""
    deadline = time.monotonic() + timeout_ms / 1000

    while time.monotonic() < deadline:
        _poll_raise_if_cancelled(cancel_event)

        file = client.files.get_file(file_id=file_id)
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

        _poll_sleep(poll_interval_ms, cancel_event)

    raise TimeoutError(
        f"Public embed playback id for file {file_id} was not ready within {timeout_ms}ms."
    )


def poll_public_preview(
    client: VideoGenApi,
    file_id: str,
    *,
    poll_interval_ms: int = 1500,
    timeout_ms: int = 120_000,
    cancel_event: Optional[Event] = None,
    wait_for_embed_playback_id: bool = True,
) -> PublicPreviewPollResult:
    """Polls ``get_file`` until public preview URLs are ready."""
    deadline = time.monotonic() + timeout_ms / 1000

    while time.monotonic() < deadline:
        _poll_raise_if_cancelled(cancel_event)

        file = client.files.get_file(file_id=file_id)
        _assert_public_preview_enabled(file)

        result = _build_poll_result(
            file,
            wait_for_embed_playback_id=wait_for_embed_playback_id,
        )
        if result is not None:
            return result

        _poll_sleep(poll_interval_ms, cancel_event)

    raise TimeoutError(
        f"Public preview for file {file_id} was not ready within {timeout_ms}ms."
    )
