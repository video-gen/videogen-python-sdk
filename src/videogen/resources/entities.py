from __future__ import annotations

from typing import Any, TYPE_CHECKING

from .._http import camel_to_snake, format_path, split_request_args

if TYPE_CHECKING:
    from ..client import AsyncVideoGen, VideoGen


class EntitiesResource:
    def __init__(self, client: VideoGen) -> None:
        self._root = client
        self._client = client._http

    # @sdk-operation listEntities
    def list_entities(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'list_entities() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=['entityType', 'limit', 'cursor'],
        )
        path = format_path('/v1/entities', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation createEntity
    def create_entity(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'create_entity() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/entities', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation getEntity
    def get_entity(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['entity_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'get_entity() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['entityId'],
            query_params=[],
        )
        for required in ['entityId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/entities/{entityId}', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation updateEntity
    def update_entity(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['entity_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'update_entity() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['entityId'],
            query_params=[],
        )
        for required in ['entityId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/entities/{entityId}/update', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation archiveEntity
    def archive_entity(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['entity_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'archive_entity() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['entityId'],
            query_params=[],
        )
        for required in ['entityId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/entities/{entityId}/archive', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation addEntityReference
    def add_entity_reference(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['entity_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'add_entity_reference() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['entityId'],
            query_params=[],
        )
        for required in ['entityId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/entities/{entityId}/references', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation removeEntityReference
    def remove_entity_reference(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['entity_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'remove_entity_reference() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['entityId'],
            query_params=[],
        )
        for required in ['entityId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/entities/{entityId}/references/remove', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )


class AsyncEntitiesResource:
    def __init__(self, client: AsyncVideoGen) -> None:
        self._root = client
        self._client = client._http

    # @sdk-operation listEntities
    async def list_entities(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'list_entities() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=['entityType', 'limit', 'cursor'],
        )
        path = format_path('/v1/entities', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation createEntity
    async def create_entity(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'create_entity() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/entities', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation getEntity
    async def get_entity(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['entity_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'get_entity() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['entityId'],
            query_params=[],
        )
        for required in ['entityId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/entities/{entityId}', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation updateEntity
    async def update_entity(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['entity_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'update_entity() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['entityId'],
            query_params=[],
        )
        for required in ['entityId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/entities/{entityId}/update', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation archiveEntity
    async def archive_entity(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['entity_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'archive_entity() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['entityId'],
            query_params=[],
        )
        for required in ['entityId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/entities/{entityId}/archive', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation addEntityReference
    async def add_entity_reference(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['entity_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'add_entity_reference() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['entityId'],
            query_params=[],
        )
        for required in ['entityId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/entities/{entityId}/references', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation removeEntityReference
    async def remove_entity_reference(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['entity_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'remove_entity_reference() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['entityId'],
            query_params=[],
        )
        for required in ['entityId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/entities/{entityId}/references/remove', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )
