from __future__ import annotations

from typing import Any, TYPE_CHECKING

from .._http import camel_to_snake, format_path, split_request_args

from ..poll_project_export import poll_project_export
from ..async_poll_project_export import async_poll_project_export
from ..poll_remix_actions import poll_remix_actions
from ..async_poll_remix_actions import async_poll_remix_actions
from ..poll_timeline_interchange import poll_timeline_interchange
from ..async_poll_timeline_interchange import async_poll_timeline_interchange

if TYPE_CHECKING:
    from ..client import AsyncVideoGen, VideoGen


class ProjectsResource:
    def __init__(self, client: VideoGen) -> None:
        self._root = client
        self._client = client._http

    # @sdk-operation listProjects
    def list_projects(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'list_projects() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=['limit', 'cursor', 'selfOnly', 'includeUiProjects'],
        )
        path = format_path('/v1/projects', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation getProject
    def get_project(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['project_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'get_project() takes at most {len(path_param_names)} positional argument(s)')
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
        path = format_path('/v1/projects/{projectId}', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation exportProject
    def export_project(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['project_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'export_project() takes at most {len(path_param_names)} positional argument(s)')
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
        path = format_path('/v1/projects/{projectId}/export', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation listProjectExports
    def list_project_exports(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['project_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'list_project_exports() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['projectId'],
            query_params=['limit', 'cursor'],
        )
        for required in ['projectId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/projects/{projectId}/exports', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation getProjectExport
    def get_project_export(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['project_id', 'export_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'get_project_export() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['projectId', 'exportId'],
            query_params=[],
        )
        for required in ['projectId', 'exportId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/projects/{projectId}/exports/{exportId}', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation createTimelineInterchange
    def create_timeline_interchange(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['project_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'create_timeline_interchange() takes at most {len(path_param_names)} positional argument(s)')
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
        path = format_path('/v1/projects/{projectId}/timeline-interchange', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation getTimelineInterchange
    def get_timeline_interchange(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['interchange_job_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'get_timeline_interchange() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['interchangeJobId'],
            query_params=[],
        )
        for required in ['interchangeJobId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/timeline-interchange/{interchangeJobId}', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation remixProject
    def remix_project(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['project_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'remix_project() takes at most {len(path_param_names)} positional argument(s)')
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
        path = format_path('/v1/projects/{projectId}/remix', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation listProjectRemixActions
    def list_project_remix_actions(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['project_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'list_project_remix_actions() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['projectId'],
            query_params=['limit', 'cursor'],
        )
        for required in ['projectId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/projects/{projectId}/remix-actions', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    def export_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.export_project(*args, **kwargs)
        project_id = kwargs.get('project_id')
        if project_id is None and args:
            project_id = args[0]
        if project_id is None:
            project_id = started.get('project_id')
        export_id = started['export_id']
        return poll_project_export(
            self._root,
            project_id,
            export_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    def create_timeline_interchange_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.create_timeline_interchange(*args, **kwargs)
        interchange_job_id = started['interchange_job_id']
        return poll_timeline_interchange(
            self._root,
            interchange_job_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    def remix_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.remix_project(*args, **kwargs)
        project_id = kwargs.get('project_id')
        if project_id is None and args:
            project_id = args[0]
        if project_id is None:
            project_id = started.get('project_id')
        target_project_id = started.get('project_id') or project_id
        return poll_remix_actions(
            self._root,
            target_project_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )


class AsyncProjectsResource:
    def __init__(self, client: AsyncVideoGen) -> None:
        self._root = client
        self._client = client._http

    # @sdk-operation listProjects
    async def list_projects(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'list_projects() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=['limit', 'cursor', 'selfOnly', 'includeUiProjects'],
        )
        path = format_path('/v1/projects', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation getProject
    async def get_project(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['project_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'get_project() takes at most {len(path_param_names)} positional argument(s)')
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
        path = format_path('/v1/projects/{projectId}', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation exportProject
    async def export_project(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['project_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'export_project() takes at most {len(path_param_names)} positional argument(s)')
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
        path = format_path('/v1/projects/{projectId}/export', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation listProjectExports
    async def list_project_exports(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['project_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'list_project_exports() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['projectId'],
            query_params=['limit', 'cursor'],
        )
        for required in ['projectId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/projects/{projectId}/exports', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation getProjectExport
    async def get_project_export(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['project_id', 'export_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'get_project_export() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['projectId', 'exportId'],
            query_params=[],
        )
        for required in ['projectId', 'exportId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/projects/{projectId}/exports/{exportId}', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation createTimelineInterchange
    async def create_timeline_interchange(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['project_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'create_timeline_interchange() takes at most {len(path_param_names)} positional argument(s)')
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
        path = format_path('/v1/projects/{projectId}/timeline-interchange', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation getTimelineInterchange
    async def get_timeline_interchange(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['interchange_job_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'get_timeline_interchange() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['interchangeJobId'],
            query_params=[],
        )
        for required in ['interchangeJobId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/timeline-interchange/{interchangeJobId}', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation remixProject
    async def remix_project(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['project_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'remix_project() takes at most {len(path_param_names)} positional argument(s)')
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
        path = format_path('/v1/projects/{projectId}/remix', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation listProjectRemixActions
    async def list_project_remix_actions(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['project_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'list_project_remix_actions() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['projectId'],
            query_params=['limit', 'cursor'],
        )
        for required in ['projectId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/projects/{projectId}/remix-actions', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    async def export_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.export_project(*args, **kwargs)
        project_id = kwargs.get('project_id')
        if project_id is None and args:
            project_id = args[0]
        if project_id is None:
            project_id = started.get('project_id')
        export_id = started['export_id']
        return await async_poll_project_export(
            self._root,
            project_id,
            export_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    async def create_timeline_interchange_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.create_timeline_interchange(*args, **kwargs)
        interchange_job_id = started['interchange_job_id']
        return await async_poll_timeline_interchange(
            self._root,
            interchange_job_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    async def remix_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.remix_project(*args, **kwargs)
        project_id = kwargs.get('project_id')
        if project_id is None and args:
            project_id = args[0]
        if project_id is None:
            project_id = started.get('project_id')
        target_project_id = started.get('project_id') or project_id
        return await async_poll_remix_actions(
            self._root,
            target_project_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )
