from __future__ import annotations

from typing import Any, TYPE_CHECKING

from .._http import format_path, split_request_args

if TYPE_CHECKING:
    from ..client import AsyncVideoGen, VideoGen


class AccountResource:
    def __init__(self, client: VideoGen) -> None:
        self._root = client
        self._client = client._http

    # @sdk-operation getMe
    def get_me(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'get_me() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/me', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )


class AsyncAccountResource:
    def __init__(self, client: AsyncVideoGen) -> None:
        self._root = client
        self._client = client._http

    # @sdk-operation getMe
    async def get_me(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'get_me() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/me', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )
