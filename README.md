# VideoGen Python SDK

Official Python client for the [VideoGen API](https://docs.videogen.io).

Package: `videogen` (PyPI) · Import: `videogen` · Version: `2.0.0`

## Install

```bash
pip install videogen
```

For local development from this repo:

```bash
cd sdk-python
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Quick start

```python
import os
from videogen import VideoGen

vg = VideoGen(api_key=os.environ["VIDEOGEN_API_KEY"])

run = vg.workflows.script_to_video_and_wait(
    script="Staying hydrated keeps your body and mind running at their best.",
    visual_style={
        "type": "AI_IMAGE",
        "ai_style": "loose watercolor illustration with visible brushstrokes",
    },
    quality="HIGH",
    remix_actions=[
        {"type": "ENABLE_CAPTIONS"},
        {
            "type": "CONVERT_IMAGES_TO_VIDEOS",
            "motion_prompt": "slow cinematic push-in",
            "mute_output_videos": True,
            "quality": "HIGH",
        },
    ],
)
print(run["status"], run.get("project_id"))
```

Async twin:

```python
from videogen import AsyncVideoGen

vg = AsyncVideoGen(api_key=os.environ["VIDEOGEN_API_KEY"])
run = await vg.workflows.script_to_video_and_wait(script="...")
```

Default base URL: `https://api.videogen.io`. Omit `api_key` to read `VIDEOGEN_API_KEY` from the environment.

## Naming and JSON

- **Methods:** snake_case (`script_to_video`, `get_tool_execution_info`).
- **Requests:** pass snake_case kwargs (and nested dict keys). The client serializes body/query keys to camelCase for the wire.
- **Responses:** JSON objects are converted recursively to snake_case keys so Python callers use idiomatic names (`tool_execution_id`, `workflow_run_id`, `has_more`).

## Resources

`account` · `workflows` · `projects` · `tools` · `files` · `assistant` · `text` · `resources` · `webhooks`

Every public REST operation is a thin method (see `@sdk-operation` markers). Convenience helpers are exported as module functions and bound on the client:

| Helper | Purpose |
| --- | --- |
| `poll_executed_tool` / `async_poll_executed_tool` | Poll a tool execution to a terminal status |
| `poll_workflow_run` / `async_poll_workflow_run` | Poll a workflow run |
| `poll_project_export` / `async_poll_project_export` | Poll a project export |
| `poll_remix_actions` / `async_poll_remix_actions` | Poll remix actions until all are terminal |
| `poll_public_preview` / `async_poll_public_preview` | Poll until a public preview URL is ready |
| `upload_file` / `async_upload_file` | Presign, PUT bytes, poll until the file is ready |
| `get_hydrated_file` / `async_get_hydrated_file` | Hydrate signed source URLs |
| `download_file` / `async_download_file` | Hydrate then download bytes (optional path) |
| `create_public_preview` / `async_create_public_preview` | Enable + poll public preview |
| `verify_webhook_signature` | Verify Standard Webhooks and return the event dict |

`*AndWait` wrappers on `tools`, `workflows`, and `projects` start work and poll to completion.

## Cancellation

Pass `cancel_event=threading.Event()` (sync) or `asyncio.Event()` (async) to poll helpers or thin `request` / resource methods. Setting the event raises `PollCancelledError`.

## Errors

`VideoGenError` exposes `status`, `body`, and `request_id` (from `x-request-id` when present).
