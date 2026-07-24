from __future__ import annotations

from typing import Any, TYPE_CHECKING

from .._http import camel_to_snake, format_path, split_request_args

from ..poll_executed_tool import poll_executed_tool
from ..async_poll_executed_tool import async_poll_executed_tool

if TYPE_CHECKING:
    from ..client import AsyncVideoGen, VideoGen


class ToolsResource:
    def __init__(self, client: VideoGen) -> None:
        self._root = client
        self._client = client._http

    # @sdk-operation generateImage
    def generate_image(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'generate_image() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/generate-image', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation generateVideoClip
    def generate_video_clip(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'generate_video_clip() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/generate-video-clip', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation generateMotionGraphic
    def generate_motion_graphic(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'generate_motion_graphic() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/generate-motion-graphic', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation textToSpeech
    def text_to_speech(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'text_to_speech() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/text-to-speech', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation generateSoundEffect
    def generate_sound_effect(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'generate_sound_effect() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/generate-sound-effect', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation generateMusic
    def generate_music(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'generate_music() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/generate-music', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation generateAvatar
    def generate_avatar(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'generate_avatar() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/generate-avatar', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation vectorizeImage
    def vectorize_image(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'vectorize_image() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/vectorize-image', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation removeImageBackground
    def remove_image_background(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'remove_image_background() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/remove-image-background', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation removeVideoBackground
    def remove_video_background(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'remove_video_background() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/remove-video-background', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation upscaleImage
    def upscale_image(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'upscale_image() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/upscale-image', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation upscaleVideo
    def upscale_video(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'upscale_video() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/upscale-video', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation image3dEffect
    def image3d_effect(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'image3d_effect() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/image-3d-effect', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation listToolExecutions
    def list_tool_executions(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'list_tool_executions() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=['limit', 'cursor', 'selfOnly'],
        )
        path = format_path('/v1/tools/executions', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation getToolExecutionInfo
    def get_tool_execution_info(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['tool_execution_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'get_tool_execution_info() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['toolExecutionId'],
            query_params=[],
        )
        for required in ['toolExecutionId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/tools/executions/{toolExecutionId}', path_values)
        return self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation cancelToolExecution
    def cancel_tool_execution(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['tool_execution_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'cancel_tool_execution() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['toolExecutionId'],
            query_params=[],
        )
        for required in ['toolExecutionId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/tools/executions/{toolExecutionId}/cancel', path_values)
        return self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    def generate_image_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.generate_image(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    def generate_video_clip_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.generate_video_clip(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    def generate_motion_graphic_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.generate_motion_graphic(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    def text_to_speech_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.text_to_speech(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    def generate_sound_effect_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.generate_sound_effect(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    def generate_music_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.generate_music(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    def generate_avatar_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.generate_avatar(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    def vectorize_image_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.vectorize_image(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    def remove_image_background_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.remove_image_background(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    def remove_video_background_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.remove_video_background(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    def upscale_image_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.upscale_image(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    def upscale_video_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.upscale_video(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    def image3d_effect_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = self.image3d_effect(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )


class AsyncToolsResource:
    def __init__(self, client: AsyncVideoGen) -> None:
        self._root = client
        self._client = client._http

    # @sdk-operation generateImage
    async def generate_image(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'generate_image() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/generate-image', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation generateVideoClip
    async def generate_video_clip(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'generate_video_clip() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/generate-video-clip', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation generateMotionGraphic
    async def generate_motion_graphic(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'generate_motion_graphic() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/generate-motion-graphic', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation textToSpeech
    async def text_to_speech(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'text_to_speech() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/text-to-speech', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation generateSoundEffect
    async def generate_sound_effect(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'generate_sound_effect() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/generate-sound-effect', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation generateMusic
    async def generate_music(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'generate_music() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/generate-music', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation generateAvatar
    async def generate_avatar(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'generate_avatar() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/generate-avatar', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation vectorizeImage
    async def vectorize_image(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'vectorize_image() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/vectorize-image', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation removeImageBackground
    async def remove_image_background(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'remove_image_background() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/remove-image-background', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation removeVideoBackground
    async def remove_video_background(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'remove_video_background() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/remove-video-background', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation upscaleImage
    async def upscale_image(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'upscale_image() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/upscale-image', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation upscaleVideo
    async def upscale_video(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'upscale_video() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/upscale-video', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation image3dEffect
    async def image3d_effect(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'image3d_effect() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=[],
        )
        path = format_path('/v1/tools/image-3d-effect', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body if body is not None else {},
            cancel_event=cancel_event,
        )

    # @sdk-operation listToolExecutions
    async def list_tool_executions(self, *args: Any, **kwargs: Any) -> Any:
        if args:
            raise TypeError(f'list_tool_executions() does not take positional arguments')
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=[],
            query_params=['limit', 'cursor', 'selfOnly'],
        )
        path = format_path('/v1/tools/executions', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation getToolExecutionInfo
    async def get_tool_execution_info(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['tool_execution_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'get_tool_execution_info() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['toolExecutionId'],
            query_params=[],
        )
        for required in ['toolExecutionId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/tools/executions/{toolExecutionId}', path_values)
        return await self._client.request(
            method='GET',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    # @sdk-operation cancelToolExecution
    async def cancel_tool_execution(self, *args: Any, **kwargs: Any) -> Any:
        path_param_names = ['tool_execution_id']
        if args:
            if len(args) > len(path_param_names):
                raise TypeError(f'cancel_tool_execution() takes at most {len(path_param_names)} positional argument(s)')
            for name, value in zip(path_param_names, args):
                if name in kwargs:
                    raise TypeError(f"{name} specified twice")
                kwargs[name] = value
        path_values, query_values, body, cancel_event = split_request_args(
            kwargs,
            path_params=['toolExecutionId'],
            query_params=[],
        )
        for required in ['toolExecutionId']:
            if required not in path_values:
                raise TypeError(f"missing required argument: {camel_to_snake(required)}")
        path = format_path('/v1/tools/executions/{toolExecutionId}/cancel', path_values)
        return await self._client.request(
            method='POST',
            path=path,
            query=query_values or None,
            body=body,
            cancel_event=cancel_event,
        )

    async def generate_image_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.generate_image(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return await async_poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    async def generate_video_clip_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.generate_video_clip(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return await async_poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    async def generate_motion_graphic_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.generate_motion_graphic(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return await async_poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    async def text_to_speech_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.text_to_speech(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return await async_poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    async def generate_sound_effect_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.generate_sound_effect(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return await async_poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    async def generate_music_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.generate_music(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return await async_poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    async def generate_avatar_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.generate_avatar(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return await async_poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    async def vectorize_image_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.vectorize_image(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return await async_poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    async def remove_image_background_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.remove_image_background(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return await async_poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    async def remove_video_background_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.remove_video_background(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return await async_poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    async def upscale_image_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.upscale_image(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return await async_poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    async def upscale_video_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.upscale_video(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return await async_poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )

    async def image3d_effect_and_wait(self, *args: Any, **kwargs: Any) -> Any:
        poll_interval_ms = kwargs.pop('poll_interval_ms', 1500)
        timeout_ms = kwargs.pop('timeout_ms', 3_600_000)
        throw_on_failure = kwargs.pop('throw_on_failure', True)
        cancel_event = kwargs.get('cancel_event')
        started = await self.image3d_effect(*args, **kwargs)
        tool_execution_id = started['tool_execution_id']
        return await async_poll_executed_tool(
            self._root,
            tool_execution_id,
            poll_interval_ms=poll_interval_ms,
            timeout_ms=timeout_ms,
            throw_on_failure=throw_on_failure,
            cancel_event=cancel_event,
        )
