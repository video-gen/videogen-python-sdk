from __future__ import annotations

from typing import Any, TYPE_CHECKING

from .._http import camel_to_snake, format_path, split_request_args

if TYPE_CHECKING:
    from ..client import AsyncVideoGen, VideoGen


class FilesResource:
    def __init__(self, client: VideoGen) -> None:
        self._root = client
        self._client = client._http

    # @sdk-operation getFiles
    def get_files(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'get_files() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=['limit', 'cursor', 'includeExportFiles', 'includeProjectFiles'],
        )
        path = format_path('/v1/files', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation searchFiles
    def search_files(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'search_files() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/files/search', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation getFile
    def get_file(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['file_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'get_file() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['fileId'],
            query_params=[],
        )
        for required in ['fileId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/files/{fileId}', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation createFileUpload
    def create_file_upload(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'create_file_upload() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/files/upload', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation hydrateFile
    def hydrate_file(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['file_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'hydrate_file() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['fileId'],
            query_params=[],
        )
        for required in ['fileId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/files/{fileId}/hydrate', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation archiveFile
    def archive_file(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['file_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'archive_file() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['fileId'],
            query_params=[],
        )
        for required in ['fileId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/files/{fileId}/archive', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation enablePublicPreview
    def enable_public_preview(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['file_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'enable_public_preview() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['fileId'],
            query_params=[],
        )
        for required in ['fileId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/files/{fileId}/enable-public-preview', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation disablePublicPreview
    def disable_public_preview(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['file_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'disable_public_preview() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['fileId'],
            query_params=[],
        )
        for required in ['fileId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/files/{fileId}/disable-public-preview', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )


class AsyncFilesResource:
    def __init__(self, client: AsyncVideoGen) -> None:
        self._root = client
        self._client = client._http

    # @sdk-operation getFiles
    async def get_files(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'get_files() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=['limit', 'cursor', 'includeExportFiles', 'includeProjectFiles'],
        )
        path = format_path('/v1/files', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation searchFiles
    async def search_files(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'search_files() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/files/search', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation getFile
    async def get_file(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['file_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'get_file() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['fileId'],
            query_params=[],
        )
        for required in ['fileId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/files/{fileId}', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation createFileUpload
    async def create_file_upload(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'create_file_upload() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/files/upload', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation hydrateFile
    async def hydrate_file(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['file_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'hydrate_file() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['fileId'],
            query_params=[],
        )
        for required in ['fileId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/files/{fileId}/hydrate', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation archiveFile
    async def archive_file(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['file_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'archive_file() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['fileId'],
            query_params=[],
        )
        for required in ['fileId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/files/{fileId}/archive', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation enablePublicPreview
    async def enable_public_preview(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['file_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'enable_public_preview() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['fileId'],
            query_params=[],
        )
        for required in ['fileId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/files/{fileId}/enable-public-preview', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation disablePublicPreview
    async def disable_public_preview(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['file_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'disable_public_preview() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['fileId'],
            query_params=[],
        )
        for required in ['fileId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/files/{fileId}/disable-public-preview', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )
