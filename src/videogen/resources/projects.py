from __future__ import annotations

import warnings
from typing import Any, TYPE_CHECKING

from .._http import camel_to_snake, format_path, split_request_args

from ..poll_video_edits import poll_video_edits
from ..async_poll_video_edits import async_poll_video_edits
from ..poll_project_export import poll_project_export
from ..async_poll_project_export import async_poll_project_export
from ..poll_remix_actions import poll_remix_actions
from ..async_poll_remix_actions import async_poll_remix_actions
from ..poll_timeline_interchange import poll_timeline_interchange
from ..async_poll_timeline_interchange import async_poll_timeline_interchange

if TYPE_CHECKING:
    from ..client import AsyncVideoGen, VideoGen


def _pop_deprecated_include_ui_projects(kwargs: dict[str, Any]) -> None:
    # Unknown kwargs become the request body, so drop this before splitting.
    values = [kwargs.pop(key, None) for key in ('include_ui_projects', 'includeUiProjects')]
    if any(value is not None for value in values):
        warnings.warn(
            "list_projects(include_ui_projects=...) is deprecated and ignored. "
            "The list always includes projects created in the VideoGen app.",
            DeprecationWarning,
            stacklevel=3,
        )


def _split_undo_project_edit_args(kwargs: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], Any]:
    # The path mutationId names the edit to undo; the body mutationId is the new undo's id.
    path_values, query_values, fields, cancel_event = split_request_args(
        kwargs, path_params=['projectId', 'mutationId'], query_params=[],
    )
    for required in ['projectId', 'mutationId']:
        if required not in path_values:
            raise TypeError(f"missing required argument: {camel_to_snake(required)}")
    remaining = dict(fields or {})
    new_mutation_ids = [remaining.pop(key) for key in ('new_mutation_id', 'newMutationId') if key in remaining]
    if not new_mutation_ids:
        raise TypeError("missing required argument: new_mutation_id")
    if remaining:
        raise TypeError(f"unexpected argument(s): {', '.join(sorted(remaining))}")
    return path_values, query_values, {"mutationId": new_mutation_ids[0]}, cancel_event


class ProjectsResource:
    def __init__(self, client: VideoGen) -> None:
        self._root = client
        self._client = client._http

    # @sdk-operation getProjectArtifact
    def get_project_artifact(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = split_request_args(kwargs, path_params=['projectId', 'artifactId'], query_params=['textOffset', 'textLimit', 'itemOffset', 'itemLimit'])
        for required in ['projectId', 'artifactId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        return self._client.request(method="GET", path=format_path("/v1/projects/{projectId}/artifacts/{artifactId}", path_values), query=query_values or None, body=body, cancel_event=cancel_event)

    # @sdk-operation applyProjectEdits
    def apply_project_edits(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = split_request_args(kwargs, path_params=['projectId'], query_params=[])
        for required in ['projectId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        return self._client.request(method="POST", path=format_path("/v1/projects/{projectId}/mutations", path_values), query=query_values or None, body=body, cancel_event=cancel_event)

    # @sdk-operation listProjectArtifacts
    def list_project_artifacts(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs, path_params=['projectId'], query_params=['limit', 'cursor'],
        )
        for required in ['projectId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        return self._client.request(
            method="GET", path=format_path("/v1/projects/{projectId}/artifacts", path_values),
            query=query_values or None, body=body, cancel_event=cancel_event,
        )

    # @sdk-operation getProjectEditingCapabilities
    def get_project_editing_capabilities(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs, path_params=['projectId'], query_params=[],
        )
        for required in ['projectId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        return self._client.request(
            method="GET", path=format_path("/v1/projects/{projectId}/editing-capabilities", path_values),
            query=query_values or None, body=body, cancel_event=cancel_event,
        )

    # @sdk-operation inspectEditableVideo
    def inspect_editable_video(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs, path_params=['projectId', 'editableVideoId'], query_params=['limit', 'offset', 'sectionId', 'layerId', 'assetId', 'expectedRevision', 'textOffset'],
        )
        for required in ['projectId', 'editableVideoId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        return self._client.request(
            method="GET", path=format_path("/v1/projects/{projectId}/videos/{editableVideoId}/inspection", path_values),
            query=query_values or None, body=body, cancel_event=cancel_event,
        )

    # @sdk-operation editVideo
    def edit_video(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs, path_params=['projectId', 'editableVideoId'], query_params=[],
        )
        for required in ['projectId', 'editableVideoId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        return self._client.request(
            method="POST", path=format_path("/v1/projects/{projectId}/videos/{editableVideoId}/edits", path_values),
            query=query_values or None, body=body, cancel_event=cancel_event,
        )

    # @sdk-operation getProjectEdit
    def get_project_edit(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs, path_params=['projectId', 'mutationId'], query_params=[],
        )
        for required in ['projectId', 'mutationId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        return self._client.request(
            method="GET", path=format_path("/v1/projects/{projectId}/mutations/{mutationId}", path_values),
            query=query_values or None, body=body, cancel_event=cancel_event,
        )

    # @sdk-operation undoProjectEdit
    def undo_project_edit(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = _split_undo_project_edit_args(kwargs)
        return self._client.request(
            method="POST", path=format_path("/v1/projects/{projectId}/mutations/{mutationId}/undo", path_values),
            query=query_values or None, body=body, cancel_event=cancel_event,
        )

    # @sdk-operation listProjects
    def list_projects(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'list_projects() does not take positional arguments')
        _pop_deprecated_include_ui_projects(kwargs)
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=['limit', 'cursor', 'selfOnly'],
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

    # @sdk-operation startVideoEdits
    def start_video_edits(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs, path_params=['projectId'], query_params=[],
        )
        if 'projectId' not in path_values:
            raise TypeError("missing required argument: project_id")
        return self._client.request(
            method="POST", path=format_path("/v1/projects/{projectId}/video-edits", path_values),
            query=query_values or None, body=body, cancel_event=cancel_event,
        )

    # @sdk-operation listVideoEdits
    def list_video_edits(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs, path_params=['projectId'], query_params=['limit', 'cursor', 'editableVideoId'],
        )
        if 'projectId' not in path_values:
            raise TypeError("missing required argument: project_id")
        return self._client.request(
            method="GET", path=format_path("/v1/projects/{projectId}/video-edits", path_values),
            query=query_values or None, body=body, cancel_event=cancel_event,
        )

    def start_video_edits_and_wait(self, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.start_video_edits(**kwargs)
        return poll_video_edits(
            self._root,
            started['project_id'],
            video_edit_ids=started['video_edit_ids'],
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
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

    # @sdk-operation getProjectArtifact
    async def get_project_artifact(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = split_request_args(kwargs, path_params=['projectId', 'artifactId'], query_params=['textOffset', 'textLimit', 'itemOffset', 'itemLimit'])
        for required in ['projectId', 'artifactId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        return await self._client.request(method="GET", path=format_path("/v1/projects/{projectId}/artifacts/{artifactId}", path_values), query=query_values or None, body=body, cancel_event=cancel_event)

    # @sdk-operation applyProjectEdits
    async def apply_project_edits(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = split_request_args(kwargs, path_params=['projectId'], query_params=[])
        for required in ['projectId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        return await self._client.request(method="POST", path=format_path("/v1/projects/{projectId}/mutations", path_values), query=query_values or None, body=body, cancel_event=cancel_event)

    # @sdk-operation listProjectArtifacts
    async def list_project_artifacts(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs, path_params=['projectId'], query_params=['limit', 'cursor'],
        )
        for required in ['projectId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        return await self._client.request(
            method="GET", path=format_path("/v1/projects/{projectId}/artifacts", path_values),
            query=query_values or None, body=body, cancel_event=cancel_event,
        )

    # @sdk-operation getProjectEditingCapabilities
    async def get_project_editing_capabilities(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs, path_params=['projectId'], query_params=[],
        )
        for required in ['projectId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        return await self._client.request(
            method="GET", path=format_path("/v1/projects/{projectId}/editing-capabilities", path_values),
            query=query_values or None, body=body, cancel_event=cancel_event,
        )

    # @sdk-operation inspectEditableVideo
    async def inspect_editable_video(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs, path_params=['projectId', 'editableVideoId'], query_params=['limit', 'offset', 'sectionId', 'layerId', 'assetId', 'expectedRevision', 'textOffset'],
        )
        for required in ['projectId', 'editableVideoId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        return await self._client.request(
            method="GET", path=format_path("/v1/projects/{projectId}/videos/{editableVideoId}/inspection", path_values),
            query=query_values or None, body=body, cancel_event=cancel_event,
        )

    # @sdk-operation editVideo
    async def edit_video(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs, path_params=['projectId', 'editableVideoId'], query_params=[],
        )
        for required in ['projectId', 'editableVideoId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        return await self._client.request(
            method="POST", path=format_path("/v1/projects/{projectId}/videos/{editableVideoId}/edits", path_values),
            query=query_values or None, body=body, cancel_event=cancel_event,
        )

    # @sdk-operation getProjectEdit
    async def get_project_edit(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs, path_params=['projectId', 'mutationId'], query_params=[],
        )
        for required in ['projectId', 'mutationId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        return await self._client.request(
            method="GET", path=format_path("/v1/projects/{projectId}/mutations/{mutationId}", path_values),
            query=query_values or None, body=body, cancel_event=cancel_event,
        )

    # @sdk-operation undoProjectEdit
    async def undo_project_edit(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = _split_undo_project_edit_args(kwargs)
        return await self._client.request(
            method="POST", path=format_path("/v1/projects/{projectId}/mutations/{mutationId}/undo", path_values),
            query=query_values or None, body=body, cancel_event=cancel_event,
        )

    # @sdk-operation listProjects
    async def list_projects(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'list_projects() does not take positional arguments')
        _pop_deprecated_include_ui_projects(kwargs)
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=['limit', 'cursor', 'selfOnly'],
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

    # @sdk-operation startVideoEdits
    async def start_video_edits(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs, path_params=['projectId'], query_params=[],
        )
        if 'projectId' not in path_values:
            raise TypeError("missing required argument: project_id")
        return await self._client.request(
            method="POST", path=format_path("/v1/projects/{projectId}/video-edits", path_values),
            query=query_values or None, body=body, cancel_event=cancel_event,
        )

    # @sdk-operation listVideoEdits
    async def list_video_edits(self, **kwargs: Any) -> Any:
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs, path_params=['projectId'], query_params=['limit', 'cursor', 'editableVideoId'],
        )
        if 'projectId' not in path_values:
            raise TypeError("missing required argument: project_id")
        return await self._client.request(
            method="GET", path=format_path("/v1/projects/{projectId}/video-edits", path_values),
            query=query_values or None, body=body, cancel_event=cancel_event,
        )

    async def start_video_edits_and_wait(self, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.start_video_edits(**kwargs)
        return await async_poll_video_edits(
            self._root,
            started['project_id'],
            video_edit_ids=started['video_edit_ids'],
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
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
