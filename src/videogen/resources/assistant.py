from __future__ import annotations

from typing import Any, TYPE_CHECKING

from .._http import camel_to_snake, format_path, split_request_args

if TYPE_CHECKING:
    from ..client import AsyncVideoGen, VideoGen


class AssistantResource:
    def __init__(self, client: VideoGen) -> None:
        self._root = client
        self._client = client._http

    # @sdk-operation startAssistantChat
    def start_assistant_chat(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'start_assistant_chat() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/assistant/chats', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation sendAssistantMessage
    def send_assistant_message(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['project_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'send_assistant_message() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['projectId'],
            query_params=[],
        )
        for required in ['projectId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/assistant/chats/{projectId}/messages', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation actOnAssistantAction
    def act_on_assistant_action(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['project_id', 'assistant_action_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'act_on_assistant_action() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['projectId', 'assistantActionId'],
            query_params=[],
        )
        for required in ['projectId', 'assistantActionId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/assistant/chats/{projectId}/actions/{assistantActionId}', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )


class AsyncAssistantResource:
    def __init__(self, client: AsyncVideoGen) -> None:
        self._root = client
        self._client = client._http

    # @sdk-operation startAssistantChat
    async def start_assistant_chat(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'start_assistant_chat() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/assistant/chats', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation sendAssistantMessage
    async def send_assistant_message(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['project_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'send_assistant_message() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['projectId'],
            query_params=[],
        )
        for required in ['projectId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/assistant/chats/{projectId}/messages', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation actOnAssistantAction
    async def act_on_assistant_action(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['project_id', 'assistant_action_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'act_on_assistant_action() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['projectId', 'assistantActionId'],
            query_params=[],
        )
        for required in ['projectId', 'assistantActionId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/assistant/chats/{projectId}/actions/{assistantActionId}', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )
