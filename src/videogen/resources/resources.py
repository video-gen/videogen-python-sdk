from __future__ import annotations

from typing import Any, TYPE_CHECKING

from .._http import format_path, split_request_args

if TYPE_CHECKING:
    from ..client import AsyncVideoGen, VideoGen


class ResourcesResource:
    def __init__(self, client: VideoGen) -> None:
        self._root = client
        self._client = client._http

    # @sdk-operation listAvatarPresenters
    def list_avatar_presenters(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'list_avatar_presenters() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=['limit', 'cursor', 'voiceId'],
        )
        path = format_path('/v1/resources/avatar-presenters', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation listTtsVoices
    def list_tts_voices(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'list_tts_voices() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=['limit', 'cursor', 'includeDeprecatedVoices'],
        )
        path = format_path('/v1/resources/tts-voices', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation listLanguages
    def list_languages(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'list_languages() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/resources/languages', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )


class AsyncResourcesResource:
    def __init__(self, client: AsyncVideoGen) -> None:
        self._root = client
        self._client = client._http

    # @sdk-operation listAvatarPresenters
    async def list_avatar_presenters(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'list_avatar_presenters() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=['limit', 'cursor', 'voiceId'],
        )
        path = format_path('/v1/resources/avatar-presenters', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation listTtsVoices
    async def list_tts_voices(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'list_tts_voices() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=['limit', 'cursor', 'includeDeprecatedVoices'],
        )
        path = format_path('/v1/resources/tts-voices', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation listLanguages
    async def list_languages(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'list_languages() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/resources/languages', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )
