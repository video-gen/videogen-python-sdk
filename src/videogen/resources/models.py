from __future__ import annotations

from typing import TYPE_CHECKING, Any, Mapping, Optional
from urllib.parse import quote

if TYPE_CHECKING:
    from ..client import AsyncVideoGen, VideoGen


class ModelsResource:
    def __init__(self, client: VideoGen) -> None:
        self._client = client._http

    # @sdk-operation startModel1Generation
    def start_model1_generation(
        self, *, prompt: str, idempotency_key: str, seconds: int = 10,
        image_file_ids: Optional[list[str]] = None,
        options: Optional[Mapping[str, Any]] = None, cancel_event: Any = None,
    ) -> Any:
        """Submit once; reuse idempotency_key on an identical network retry."""
        return self._client.request(
            method="POST", path="/v1/models/model-1/generations",
            body={"prompt": prompt, "seconds": seconds, "image_file_ids": image_file_ids or []},
            idempotency_key=idempotency_key,
            cancel_event=cancel_event if cancel_event is not None else (options or {}).get("cancel_event"),
        )

    # @sdk-operation getModel1Generation
    def get_model1_generation(
        self, *, generation_id: str,
        options: Optional[Mapping[str, Any]] = None, cancel_event: Any = None,
    ) -> Any:
        """Read status and refresh the completed MP4 download URL. Timestamps are Unix seconds."""
        return self._client.request(
            method="GET", path="/v1/models/model-1/generations/" + quote(generation_id, safe=""),
            cancel_event=cancel_event if cancel_event is not None else (options or {}).get("cancel_event"),
        )

    # @sdk-operation getModel1Quota
    def get_model1_quota(
        self, *, options: Optional[Mapping[str, Any]] = None, cancel_event: Any = None,
    ) -> Any:
        """Read separate team quota; buying generation credits does not increase it."""
        return self._client.request(
            method="GET", path="/v1/models/model-1/quota",
            cancel_event=cancel_event if cancel_event is not None else (options or {}).get("cancel_event"),
        )


class AsyncModelsResource:
    def __init__(self, client: AsyncVideoGen) -> None:
        self._client = client._http

    # @sdk-operation startModel1Generation
    async def start_model1_generation(
        self, *, prompt: str, idempotency_key: str, seconds: int = 10,
        image_file_ids: Optional[list[str]] = None,
        options: Optional[Mapping[str, Any]] = None, cancel_event: Any = None,
    ) -> Any:
        """Submit once; reuse idempotency_key on an identical network retry."""
        return await self._client.request(
            method="POST", path="/v1/models/model-1/generations",
            body={"prompt": prompt, "seconds": seconds, "image_file_ids": image_file_ids or []},
            idempotency_key=idempotency_key,
            cancel_event=cancel_event if cancel_event is not None else (options or {}).get("cancel_event"),
        )

    # @sdk-operation getModel1Generation
    async def get_model1_generation(
        self, *, generation_id: str,
        options: Optional[Mapping[str, Any]] = None, cancel_event: Any = None,
    ) -> Any:
        """Read status and refresh the completed MP4 download URL. Timestamps are Unix seconds."""
        return await self._client.request(
            method="GET", path="/v1/models/model-1/generations/" + quote(generation_id, safe=""),
            cancel_event=cancel_event if cancel_event is not None else (options or {}).get("cancel_event"),
        )

    # @sdk-operation getModel1Quota
    async def get_model1_quota(
        self, *, options: Optional[Mapping[str, Any]] = None, cancel_event: Any = None,
    ) -> Any:
        """Read separate team quota; buying generation credits does not increase it."""
        return await self._client.request(
            method="GET", path="/v1/models/model-1/quota",
            cancel_event=cancel_event if cancel_event is not None else (options or {}).get("cancel_event"),
        )
