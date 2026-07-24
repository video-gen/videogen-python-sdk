from __future__ import annotations

from typing import Any, TYPE_CHECKING

from .._http import camel_to_snake, format_path, split_request_args

from ..async_poll_assistant_message import async_poll_assistant_message
from ..poll_assistant_message import poll_assistant_message

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
        path = format_path('/v1/assistants', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    def start_assistant_chat_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.start_assistant_chat(*args, **kwargs)
        message_id = started['message_id']
        return poll_assistant_message(
            self._root,
            message_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    # @sdk-operation getAssistant
    def get_assistant(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['assistant_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'get_assistant() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['assistantId'],
            query_params=[],
        )
        for required in ['assistantId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/assistants/{assistantId}', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=None,
            cancel_event=cancel_event,
        )

    # @sdk-operation sendAssistantMessage
    def send_assistant_message(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['assistant_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'send_assistant_message() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['assistantId'],
            query_params=[],
        )
        for required in ['assistantId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/assistants/{assistantId}/messages', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    def send_assistant_message_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.send_assistant_message(*args, **kwargs)
        message_id = started['message_id']
        return poll_assistant_message(
            self._root,
            message_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    # @sdk-operation actOnAssistantAction
    def act_on_assistant_action(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['assistant_id', 'action_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'act_on_assistant_action() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['assistantId', 'actionId'],
            query_params=[],
        )
        for required in ['assistantId', 'actionId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/assistants/{assistantId}/actions/{actionId}', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    def act_on_assistant_action_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.act_on_assistant_action(*args, **kwargs)
        message_id = started['message_id']
        return poll_assistant_message(
            self._root,
            message_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    # @sdk-operation getAssistantMessage
    def get_assistant_message(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['message_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'get_assistant_message() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['messageId'],
            query_params=[],
        )
        for required in ['messageId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/assistant-messages/{messageId}', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=None,
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
        path = format_path('/v1/assistants', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    async def start_assistant_chat_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.start_assistant_chat(*args, **kwargs)
        message_id = started['message_id']
        return await async_poll_assistant_message(
            self._root,
            message_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    # @sdk-operation getAssistant
    async def get_assistant(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['assistant_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'get_assistant() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['assistantId'],
            query_params=[],
        )
        for required in ['assistantId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/assistants/{assistantId}', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=None,
            cancel_event=cancel_event,
        )

    # @sdk-operation sendAssistantMessage
    async def send_assistant_message(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['assistant_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'send_assistant_message() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['assistantId'],
            query_params=[],
        )
        for required in ['assistantId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/assistants/{assistantId}/messages', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    async def send_assistant_message_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.send_assistant_message(*args, **kwargs)
        message_id = started['message_id']
        return await async_poll_assistant_message(
            self._root,
            message_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    # @sdk-operation actOnAssistantAction
    async def act_on_assistant_action(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['assistant_id', 'action_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'act_on_assistant_action() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['assistantId', 'actionId'],
            query_params=[],
        )
        for required in ['assistantId', 'actionId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/assistants/{assistantId}/actions/{actionId}', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    async def act_on_assistant_action_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.act_on_assistant_action(*args, **kwargs)
        message_id = started['message_id']
        return await async_poll_assistant_message(
            self._root,
            message_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    # @sdk-operation getAssistantMessage
    async def get_assistant_message(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['message_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'get_assistant_message() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['messageId'],
            query_params=[],
        )
        for required in ['messageId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/assistant-messages/{messageId}', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=None,
            cancel_event=cancel_event,
        )
