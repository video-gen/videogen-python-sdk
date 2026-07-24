from __future__ import annotations

from typing import Any, Mapping, Optional

import httpx

from ._http import DEFAULT_CLIENT_ID, AsyncHttpClient, SyncHttpClient
from .async_create_public_preview import async_create_public_preview
from .async_download_file import async_download_file
from .async_get_hydrated_file import async_get_hydrated_file
from .async_poll_executed_tool import async_poll_executed_tool
from .async_poll_project_export import async_poll_project_export
from .async_poll_public_preview import async_poll_public_preview
from .async_poll_remix_actions import async_poll_remix_actions
from .async_poll_timeline_interchange import async_poll_timeline_interchange
from .async_poll_workflow_run import async_poll_workflow_run
from .async_upload_file import async_upload_file
from .create_public_preview import create_public_preview
from .download_file import download_file
from .get_hydrated_file import get_hydrated_file
from .poll_executed_tool import poll_executed_tool
from .poll_project_export import poll_project_export
from .poll_public_preview import poll_public_preview
from .poll_remix_actions import poll_remix_actions
from .poll_timeline_interchange import poll_timeline_interchange
from .poll_workflow_run import poll_workflow_run
from .resources.account import AccountResource, AsyncAccountResource
from .resources.assistant import AssistantResource, AsyncAssistantResource
from .resources.files import AsyncFilesResource, FilesResource
from .resources.projects import AsyncProjectsResource, ProjectsResource
from .resources.resources import AsyncResourcesResource, ResourcesResource
from .resources.text import AsyncTextResource, TextResource
from .resources.tools import AsyncToolsResource, ToolsResource
from .resources.webhooks import AsyncWebhooksResource, WebhooksResource
from .resources.workflows import AsyncWorkflowsResource, WorkflowsResource
from .upload_file import upload_file
from .verify_webhook_signature import verify_webhook_signature


class VideoGen:
    """Synchronous VideoGen API client."""

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        http_client: Optional[httpx.Client] = None,
        timeout: float = 60.0,
        client_id: str = DEFAULT_CLIENT_ID,
    ) -> None:
        self._http = SyncHttpClient(
            api_key=api_key,
            base_url=base_url,
            http_client=http_client,
            timeout=timeout,
            client_id=client_id,
        )
        self.account = AccountResource(self)
        self.workflows = WorkflowsResource(self)
        self.projects = ProjectsResource(self)
        self.tools = ToolsResource(self)
        self.files = FilesResource(self)
        self.assistant = AssistantResource(self)
        self.text = TextResource(self)
        self.resources = ResourcesResource(self)
        self.webhooks = WebhooksResource(self)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> "VideoGen":
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    def request(
        self,
        *,
        method: str,
        path: str,
        query: Optional[Mapping[str, Any]] = None,
        body: Any = None,
        cancel_event: Any = None,
    ) -> Any:
        """Escape hatch for arbitrary REST calls."""
        return self._http.request(
            method=method,
            path=path,
            query=query,
            body=body,
            cancel_event=cancel_event,
        )

    def poll_executed_tool(self, tool_execution_id: str, **kwargs: Any) -> dict:
        return poll_executed_tool(self, tool_execution_id, **kwargs)

    def poll_workflow_run(self, workflow_run_id: str, **kwargs: Any) -> dict:
        return poll_workflow_run(self, workflow_run_id, **kwargs)

    def poll_project_export(self, project_id: str, export_id: str, **kwargs: Any) -> dict:
        return poll_project_export(self, project_id, export_id, **kwargs)

    def poll_timeline_interchange(self, interchange_job_id: str, **kwargs: Any) -> dict:
        return poll_timeline_interchange(self, interchange_job_id, **kwargs)

    def poll_remix_actions(self, project_id: str, **kwargs: Any) -> dict:
        return poll_remix_actions(self, project_id, **kwargs)

    def poll_public_preview(self, file_id: str, **kwargs: Any) -> dict:
        return poll_public_preview(self, file_id, **kwargs)

    def upload_file(self, data: Any, **kwargs: Any) -> dict:
        return upload_file(self, data, **kwargs)

    def get_hydrated_file(self, file_id: str, **kwargs: Any) -> dict:
        return get_hydrated_file(self, file_id, **kwargs)

    def download_file(self, file_id: str, **kwargs: Any) -> bytes:
        return download_file(self, file_id, **kwargs)

    def create_public_preview(self, file_id: str, **kwargs: Any) -> dict:
        return create_public_preview(self, file_id, **kwargs)

    def verify_webhook_signature(self, *args: Any, **kwargs: Any) -> dict:
        return verify_webhook_signature(*args, **kwargs)


class AsyncVideoGen:
    """Asynchronous VideoGen API client with the same public surface as `VideoGen`."""

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        http_client: Optional[httpx.AsyncClient] = None,
        timeout: float = 60.0,
        client_id: str = DEFAULT_CLIENT_ID,
    ) -> None:
        self._http = AsyncHttpClient(
            api_key=api_key,
            base_url=base_url,
            http_client=http_client,
            timeout=timeout,
            client_id=client_id,
        )
        self.account = AsyncAccountResource(self)
        self.workflows = AsyncWorkflowsResource(self)
        self.projects = AsyncProjectsResource(self)
        self.tools = AsyncToolsResource(self)
        self.files = AsyncFilesResource(self)
        self.assistant = AsyncAssistantResource(self)
        self.text = AsyncTextResource(self)
        self.resources = AsyncResourcesResource(self)
        self.webhooks = AsyncWebhooksResource(self)

    async def aclose(self) -> None:
        await self._http.aclose()

    async def __aenter__(self) -> "AsyncVideoGen":
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.aclose()

    async def request(
        self,
        *,
        method: str,
        path: str,
        query: Optional[Mapping[str, Any]] = None,
        body: Any = None,
        cancel_event: Any = None,
    ) -> Any:
        """Escape hatch for arbitrary REST calls."""
        return await self._http.request(
            method=method,
            path=path,
            query=query,
            body=body,
            cancel_event=cancel_event,
        )

    async def poll_executed_tool(self, tool_execution_id: str, **kwargs: Any) -> dict:
        return await async_poll_executed_tool(self, tool_execution_id, **kwargs)

    async def poll_workflow_run(self, workflow_run_id: str, **kwargs: Any) -> dict:
        return await async_poll_workflow_run(self, workflow_run_id, **kwargs)

    async def poll_project_export(
        self, project_id: str, export_id: str, **kwargs: Any
    ) -> dict:
        return await async_poll_project_export(self, project_id, export_id, **kwargs)

    async def poll_timeline_interchange(
        self, interchange_job_id: str, **kwargs: Any
    ) -> dict:
        return await async_poll_timeline_interchange(self, interchange_job_id, **kwargs)

    async def poll_remix_actions(self, project_id: str, **kwargs: Any) -> dict:
        return await async_poll_remix_actions(self, project_id, **kwargs)

    async def poll_public_preview(self, file_id: str, **kwargs: Any) -> dict:
        return await async_poll_public_preview(self, file_id, **kwargs)

    async def upload_file(self, data: Any, **kwargs: Any) -> dict:
        return await async_upload_file(self, data, **kwargs)

    async def get_hydrated_file(self, file_id: str, **kwargs: Any) -> dict:
        return await async_get_hydrated_file(self, file_id, **kwargs)

    async def download_file(self, file_id: str, **kwargs: Any) -> bytes:
        return await async_download_file(self, file_id, **kwargs)

    async def create_public_preview(self, file_id: str, **kwargs: Any) -> dict:
        return await async_create_public_preview(self, file_id, **kwargs)

    def verify_webhook_signature(self, *args: Any, **kwargs: Any) -> dict:
        return verify_webhook_signature(*args, **kwargs)
