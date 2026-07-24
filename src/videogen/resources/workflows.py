from __future__ import annotations

from typing import Any, TYPE_CHECKING

from .._http import camel_to_snake, format_path, split_request_args

from ..poll_workflow_run import poll_workflow_run
from ..async_poll_workflow_run import async_poll_workflow_run

if TYPE_CHECKING:
    from ..client import AsyncVideoGen, VideoGen


class WorkflowsResource:
    def __init__(self, client: VideoGen) -> None:
        self._root = client
        self._client = client._http

    # @sdk-operation scriptToVideo
    def script_to_video(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'script_to_video() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/workflows/script-to-video', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation voiceoverToVideo
    def voiceover_to_video(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'voiceover_to_video() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/workflows/voiceover-to-video', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation slideshowToVideo
    def slideshow_to_video(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'slideshow_to_video() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/workflows/slideshow-to-video', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation promptToVideoClip
    def prompt_to_video_clip(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'prompt_to_video_clip() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/workflows/prompt-to-video-clip', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation contentOutlineToVideo
    def content_outline_to_video(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'content_outline_to_video() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/workflows/content-outline-to-video', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation listWorkflowRuns
    def list_workflow_runs(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'list_workflow_runs() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=['limit', 'cursor', 'selfOnly'],
        )
        path = format_path('/v1/workflows/runs', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation getWorkflowRun
    def get_workflow_run(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['workflow_run_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'get_workflow_run() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['workflowRunId'],
            query_params=[],
        )
        for required in ['workflowRunId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/workflows/runs/{workflowRunId}', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation cancelWorkflowRun
    def cancel_workflow_run(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['workflow_run_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'cancel_workflow_run() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['workflowRunId'],
            query_params=[],
        )
        for required in ['workflowRunId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/workflows/runs/{workflowRunId}/cancel', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    def script_to_video_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        on_progress = kwargs.pop('on_progress', None)
        cancel_event = kwargs.get('cancel_event')
        started = self.script_to_video(*args, **kwargs)
        workflow_run_id = started['workflow_run_id']
        return poll_workflow_run(
            self._root,
            workflow_run_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            on_progress=on_progress,
            cancel_event=cancel_event,
        )

    def voiceover_to_video_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        on_progress = kwargs.pop('on_progress', None)
        cancel_event = kwargs.get('cancel_event')
        started = self.voiceover_to_video(*args, **kwargs)
        workflow_run_id = started['workflow_run_id']
        return poll_workflow_run(
            self._root,
            workflow_run_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            on_progress=on_progress,
            cancel_event=cancel_event,
        )

    def slideshow_to_video_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        on_progress = kwargs.pop('on_progress', None)
        cancel_event = kwargs.get('cancel_event')
        started = self.slideshow_to_video(*args, **kwargs)
        workflow_run_id = started['workflow_run_id']
        return poll_workflow_run(
            self._root,
            workflow_run_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            on_progress=on_progress,
            cancel_event=cancel_event,
        )

    def prompt_to_video_clip_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        on_progress = kwargs.pop('on_progress', None)
        cancel_event = kwargs.get('cancel_event')
        started = self.prompt_to_video_clip(*args, **kwargs)
        workflow_run_id = started['workflow_run_id']
        return poll_workflow_run(
            self._root,
            workflow_run_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            on_progress=on_progress,
            cancel_event=cancel_event,
        )

    def content_outline_to_video_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        on_progress = kwargs.pop('on_progress', None)
        cancel_event = kwargs.get('cancel_event')
        started = self.content_outline_to_video(*args, **kwargs)
        workflow_run_id = started['workflow_run_id']
        return poll_workflow_run(
            self._root,
            workflow_run_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            on_progress=on_progress,
            cancel_event=cancel_event,
        )


class AsyncWorkflowsResource:
    def __init__(self, client: AsyncVideoGen) -> None:
        self._root = client
        self._client = client._http

    # @sdk-operation scriptToVideo
    async def script_to_video(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'script_to_video() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/workflows/script-to-video', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation voiceoverToVideo
    async def voiceover_to_video(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'voiceover_to_video() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/workflows/voiceover-to-video', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation slideshowToVideo
    async def slideshow_to_video(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'slideshow_to_video() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/workflows/slideshow-to-video', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation promptToVideoClip
    async def prompt_to_video_clip(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'prompt_to_video_clip() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/workflows/prompt-to-video-clip', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation contentOutlineToVideo
    async def content_outline_to_video(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'content_outline_to_video() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/workflows/content-outline-to-video', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation listWorkflowRuns
    async def list_workflow_runs(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'list_workflow_runs() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=['limit', 'cursor', 'selfOnly'],
        )
        path = format_path('/v1/workflows/runs', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation getWorkflowRun
    async def get_workflow_run(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['workflow_run_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'get_workflow_run() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['workflowRunId'],
            query_params=[],
        )
        for required in ['workflowRunId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/workflows/runs/{workflowRunId}', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation cancelWorkflowRun
    async def cancel_workflow_run(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['workflow_run_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'cancel_workflow_run() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['workflowRunId'],
            query_params=[],
        )
        for required in ['workflowRunId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/workflows/runs/{workflowRunId}/cancel', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    async def script_to_video_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        on_progress = kwargs.pop('on_progress', None)
        cancel_event = kwargs.get('cancel_event')
        started = await self.script_to_video(*args, **kwargs)
        workflow_run_id = started['workflow_run_id']
        return await async_poll_workflow_run(
            self._root,
            workflow_run_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            on_progress=on_progress,
            cancel_event=cancel_event,
        )

    async def voiceover_to_video_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        on_progress = kwargs.pop('on_progress', None)
        cancel_event = kwargs.get('cancel_event')
        started = await self.voiceover_to_video(*args, **kwargs)
        workflow_run_id = started['workflow_run_id']
        return await async_poll_workflow_run(
            self._root,
            workflow_run_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            on_progress=on_progress,
            cancel_event=cancel_event,
        )

    async def slideshow_to_video_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        on_progress = kwargs.pop('on_progress', None)
        cancel_event = kwargs.get('cancel_event')
        started = await self.slideshow_to_video(*args, **kwargs)
        workflow_run_id = started['workflow_run_id']
        return await async_poll_workflow_run(
            self._root,
            workflow_run_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            on_progress=on_progress,
            cancel_event=cancel_event,
        )

    async def prompt_to_video_clip_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        on_progress = kwargs.pop('on_progress', None)
        cancel_event = kwargs.get('cancel_event')
        started = await self.prompt_to_video_clip(*args, **kwargs)
        workflow_run_id = started['workflow_run_id']
        return await async_poll_workflow_run(
            self._root,
            workflow_run_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            on_progress=on_progress,
            cancel_event=cancel_event,
        )

    async def content_outline_to_video_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        on_progress = kwargs.pop('on_progress', None)
        cancel_event = kwargs.get('cancel_event')
        started = await self.content_outline_to_video(*args, **kwargs)
        workflow_run_id = started['workflow_run_id']
        return await async_poll_workflow_run(
            self._root,
            workflow_run_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            on_progress=on_progress,
            cancel_event=cancel_event,
        )
