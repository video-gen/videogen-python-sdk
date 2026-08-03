# VideoGen Python SDK

Official Python client for the [VideoGen API](https://docs.videogen.io).

Package: `videogen` (PyPI). Generate full videos from scripts, voiceovers, or slideshows, run media tools, manage files and projects, chat with the AI assistant, and verify webhooks.

## Install

```bash
pip install videogen
```

Default base URL: `https://api.videogen.io`.

## Quick start

```python
import os
from videogen import VideoGen

vg = VideoGen(api_key=os.environ["VIDEOGEN_API_KEY"])

me = vg.account.get_me()
print(me["email"])

run = vg.workflows.script_to_video_and_wait(
    script="Stay hydrated for better focus and energy.",
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

Omit `api_key` to read `VIDEOGEN_API_KEY` from the environment.

### Async client

```python
import os
from videogen import AsyncVideoGen

vg = AsyncVideoGen(api_key=os.environ["VIDEOGEN_API_KEY"])

run = await vg.workflows.script_to_video_and_wait(
    script="Stay hydrated for better focus and energy.",
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

## What you can do

| Area | Client surface | Typical entry points |
| --- | --- | --- |
| Account | `vg.account` | `get_me` |
| Workflows | `vg.workflows` | `script_to_video_and_wait`, `prompt_to_video_clip_and_wait`, `voiceover_to_video_and_wait`, `slideshow_to_video_and_wait` |
| Tools | `vg.tools` | `generate_image_and_wait`, `generate_video_clip_and_wait`, `text_to_speech_and_wait`, … |
| Files | helpers on `vg` | `upload_file`, `download_file`, `create_public_preview` |
| Projects | `vg.projects` | `export_and_wait`, `remix_and_wait`, `create_timeline_interchange_and_wait` |
| Assistant | `vg.assistant` | `start_assistant_chat_and_wait`, `send_assistant_message_and_wait` |
| Entities | `vg.entities` | `create_entity`, `list_entities`, `add_entity_reference` |
| Text | `vg.text` | `generate_text` |
| Catalog | `vg.resources` | `list_tts_voices`, `list_avatar_presenters`, `list_languages` |
| Webhooks | `vg.webhooks` + helper | `create_webhook_endpoint`, `verify_webhook_signature` |

Prefer `*_and_wait` (or the matching `poll_*` / `async_poll_*` helper) for anything asynchronous. Thin REST methods match OpenAPI `operationId`s (snake_case).

## Naming and JSON

- **Methods:** snake_case (`script_to_video`, `get_tool_execution_info`).
- **Requests:** pass snake_case kwargs (and nested dict keys). The client serializes body/query keys to camelCase for the wire.
- **Responses:** JSON objects are converted recursively to snake_case keys (`tool_execution_id`, `workflow_run_id`, `has_more`).

## Workflows

Script to video (above) is the usual path. Prompt to video clip builds a single clip from a prompt:

```python
import os
from videogen import VideoGen

vg = VideoGen(api_key=os.environ["VIDEOGEN_API_KEY"])

run = vg.workflows.prompt_to_video_clip_and_wait(
    prompt="A glass of water catching morning light on a kitchen counter, slow push-in",
    quality="HIGH",
)
print(run["status"], run.get("project_id"))
```

Other workflow starters: `voiceover_to_video_and_wait` (uploaded audio `file_id`), `slideshow_to_video_and_wait` (deck `file_id`).

## Tools

```python
import os
from videogen import VideoGen

vg = VideoGen(api_key=os.environ["VIDEOGEN_API_KEY"])

execution = vg.tools.generate_image_and_wait(
    prompt="A sunset over a calm ocean, cinematic lighting",
    quality="HIGH",
)

results = execution.get("results") or []
file_id = results[0]["file_id"] if results else None
if file_id is None:
    raise RuntimeError("Expected a generated file id")

preview = vg.create_public_preview(file_id)
print(execution["status"], preview)
```

The same `*_and_wait` pattern exists for video clips, motion graphics, TTS, music, sound effects, avatar, upscale, background removal, and more under `vg.tools`.

## Files

```python
import os
from videogen import VideoGen

vg = VideoGen(api_key=os.environ["VIDEOGEN_API_KEY"])

with open("input.mp4", "rb") as f:
    uploaded = vg.upload_file(f, display_name="input.mp4", type="VIDEO")

print(uploaded["file_id"])

vg.download_file(uploaded["file_id"], output_path="output.mp4")
```

## Projects

Export a finished workflow project, or apply remix actions later:

```python
import os
from videogen import VideoGen

vg = VideoGen(api_key=os.environ["VIDEOGEN_API_KEY"])

project_id = "vg_proj_..."

exported = vg.projects.export_and_wait(project_id=project_id, quality="HIGH")
print(exported["status"], exported.get("export_file_id"))

remix = vg.projects.remix_and_wait(
    project_id=project_id,
    remix_actions=[
        {"type": "ENABLE_CAPTIONS"},
        {"type": "ADD_TRANSITIONS"},
    ],
)
print(remix)
```

## Assistant

```python
import os
from videogen import VideoGen

vg = VideoGen(api_key=os.environ["VIDEOGEN_API_KEY"])

started = vg.assistant.start_assistant_chat(
    message="Draft a 20-second script about morning hydration.",
)
message = vg.poll_assistant_message(started["message_id"])

print(message["status"], started.get("assistant_id"), started.get("project_id"))
```

Or use `start_assistant_chat_and_wait` when you only need the terminal message. Continue with `send_assistant_message_and_wait` / `act_on_assistant_action_and_wait` on the same `assistant_id`.

## Entities

Reusable actors, products, and visual styles for consistent generation:

```python
import os
from videogen import VideoGen

vg = VideoGen(api_key=os.environ["VIDEOGEN_API_KEY"])

entity = vg.entities.create_entity(
    entity_type="ACTOR",
    name="Alex",
    description="Friendly narrator in casual clothes",
)
print(entity["entity_id"])
```

Attach reference images with `add_entity_reference`, then pass entity ids into workflows.

## Text

```python
import os
from videogen import VideoGen

vg = VideoGen(api_key=os.environ["VIDEOGEN_API_KEY"])

result = vg.text.generate_text(
    prompt="Write a one-sentence hook for a hydration tip video.",
)
print(result["text"])
```

## Webhooks

```python
import os
from videogen import verify_webhook_signature

event = verify_webhook_signature(
    raw_body="...",  # raw request body string
    headers={
        "webhook-id": "...",
        "webhook-timestamp": "...",
        "webhook-signature": "...",
    },
    secret=os.environ.get("VIDEOGEN_WEBHOOK_SECRET", ""),
)
print(event)
```

Register endpoints with `vg.webhooks.create_webhook_endpoint`. Signatures follow the Standard Webhooks scheme.

## Helpers

Exported as module functions and bound on the client:

| Helper | Purpose |
| --- | --- |
| `poll_assistant_message` / `async_poll_assistant_message` | Poll an assistant message to a terminal status |
| `poll_executed_tool` / `async_poll_executed_tool` | Poll a tool execution to a terminal status |
| `poll_workflow_run` / `async_poll_workflow_run` | Poll a workflow run |
| `poll_project_export` / `async_poll_project_export` | Poll a project export |
| `poll_timeline_interchange` / `async_poll_timeline_interchange` | Poll a timeline interchange job |
| `poll_remix_actions` / `async_poll_remix_actions` | Poll remix actions until all are terminal |
| `poll_public_preview` / `async_poll_public_preview` | Poll until a public preview URL is ready |
| `upload_file` / `async_upload_file` | Presign, PUT bytes, poll until the file is ready |
| `get_hydrated_file` / `async_get_hydrated_file` | Hydrate signed source URLs |
| `download_file` / `async_download_file` | Hydrate then download bytes (optional path) |
| `create_public_preview` / `async_create_public_preview` | Enable + poll public preview |
| `verify_webhook_signature` | Verify Standard Webhooks and return the event dict |

Cancellation: pass `cancel_event=threading.Event()` (sync) or `asyncio.Event()` (async) to poll helpers and thin request methods. Setting the event raises `PollCancelledError`.

## Errors

`VideoGenError` exposes `status`, `body`, and `request_id` (from `x-request-id` when present).

## Docs

- [API documentation](https://docs.videogen.io)
- [PyPI: videogen](https://pypi.org/project/videogen/)
- [GitHub](https://github.com/video-gen/videogen-python-sdk)
