# Reference
## Workflows
<details><summary><code>client.workflows.<a href="src/videogen/workflows/client.py">add_visuals_narrations_and_captions_to_script</a>(...) -> StartWorkflowRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a project and generates a narrated video from a prompt or script. Returns immediately with a workflow run id; poll or subscribe to webhooks for completion.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.workflows.add_visuals_narrations_and_captions_to_script(
    script="script",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**script:** `str` — The narration script, used verbatim. This exact text is narrated and turned into a video — it is not rewritten or expanded.
    
</dd>
</dl>

<dl>
<dd>

**aspect_ratio:** `typing.Optional[AspectRatio]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workflows.<a href="src/videogen/workflows/client.py">add_visuals_and_captions_to_voiceover</a>(...) -> StartWorkflowRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a project from an uploaded voiceover file and generates a video with matching b-roll. Upload the voiceover via the files API first.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.workflows.add_visuals_and_captions_to_voiceover(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — Opaque file id of an uploaded voiceover audio file (e.g. `vg_file_...`). Upload the file first via `POST /v1/files/upload`.
    
</dd>
</dl>

<dl>
<dd>

**aspect_ratio:** `typing.Optional[AspectRatio]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workflows.<a href="src/videogen/workflows/client.py">add_narration_transitions_and_captions_to_slideshow</a>(...) -> StartWorkflowRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a project from an uploaded PDF or PowerPoint file and generates an AI-narrated video walking through each slide. Upload the file via `POST /v1/files/upload` first.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.workflows.add_narration_transitions_and_captions_to_slideshow(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — Opaque file id of an uploaded PDF or PowerPoint file (e.g. `vg_file_...`). Upload the file first via `POST /v1/files/upload`.
    
</dd>
</dl>

<dl>
<dd>

**aspect_ratio:** `typing.Optional[AspectRatio]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workflows.<a href="src/videogen/workflows/client.py">get_workflow_run</a>(...) -> WorkflowRun</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.workflows.get_workflow_run(
    workflow_run_id="workflowRunId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_run_id:** `str` — The workflow run id returned when the workflow was started.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workflows.<a href="src/videogen/workflows/client.py">cancel_workflow_run</a>(...) -> StartWorkflowRunResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.workflows.cancel_workflow_run(
    workflow_run_id="workflowRunId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_run_id:** `str` — The workflow run id returned when the workflow was started.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Projects
<details><summary><code>client.projects.<a href="src/videogen/projects/client.py">list_projects</a>(...) -> ListProjectsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns API-created projects, most recently updated first. Dashboard projects are excluded. Use `selfOnly=true` to restrict results to the calling API key's user; otherwise all API-created projects for the team are returned. Paginated; pass `nextCursor` from the previous response as `cursor` to fetch the next page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.projects.list_projects()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return in the page. Defaults to 50; capped at 200.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque pagination cursor returned as `nextCursor` by the previous page. Omit on the first request. Cursors are tied to the endpoint that produced them and must be passed unmodified.
    
</dd>
</dl>

<dl>
<dd>

**self_only:** `typing.Optional[bool]` — When true, returns only projects created by the API key's owner workspace. When false (default), returns all projects accessible to the team.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/videogen/projects/client.py">get_project</a>(...) -> ProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a simplified view of a project including its title, aspect ratio, status, and URL.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.projects.get_project(
    project_id="projectId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` — The project id (e.g. `vg_proj_...`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/videogen/projects/client.py">export_project</a>(...) -> ExportProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts an export of a project to MP4. Returns immediately with an export id; the file becomes available when the export task completes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.projects.export_project(
    project_id="projectId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` — The project id (e.g. `vg_proj_...`).
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[ExportProjectQuality]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/videogen/projects/client.py">get_project_export</a>(...) -> ProjectExport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current status of a project export started via `POST /v1/projects/{projectId}/export`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.projects.get_project_export(
    project_id="projectId",
    export_id="exportId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` — The project id (e.g. `vg_proj_...`).
    
</dd>
</dl>

<dl>
<dd>

**export_id:** `str` — The export id returned by `POST /v1/projects/{projectId}/export`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tools
<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">generate_image</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate an image from a text prompt, optionally guided by one or more reference images. When reference images are provided, the prompt describes the desired transformation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.generate_image(
    prompt="A serene Japanese garden with cherry blossoms at golden hour",
    quality="LOW",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt:** `str` — Text prompt describing the image to generate. When reference images are provided, the prompt describes the desired transformation.
    
</dd>
</dl>

<dl>
<dd>

**quality:** `GenerateImageRequestQuality` — Image generation quality tier. LOW is fastest; HIGH is slowest and highest quality.
    
</dd>
</dl>

<dl>
<dd>

**image_file_ids:** `typing.Optional[typing.List[str]]` — Optional file ids of reference images (e.g. `["vg_file_..."]`). Upload files first via `POST /v1/files/upload`, then pass the returned ids here. Maximum 4 images. When provided, the model uses these as guidance for generation.
    
</dd>
</dl>

<dl>
<dd>

**aspect_ratio:** `typing.Optional[AspectRatio]` — Aspect ratio for the generated image. Defaults to 16:9 when omitted.
    
</dd>
</dl>

<dl>
<dd>

**watermark_mode:** `typing.Optional[WatermarkMode]` 
    
</dd>
</dl>

<dl>
<dd>

**num_results:** `typing.Optional[int]` — Number of output results to generate. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**is_output_temporary:** `typing.Optional[bool]` — When true, generated files are temporary. Temporary files are guaranteed to be available for 24 hours, after which they may be archived at any time. Temporary files are not analyzed (no description, transcript, or embedding will be generated), so they will not appear in search results. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">generate_video_clip</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a video clip from a text prompt, optionally guided by reference images or an input video. At least one of `prompt`, `imageFileIds`, or `videoFileId` must be provided.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.generate_video_clip(
    quality="STANDARD",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**quality:** `GenerateVideoClipRequestQuality` — Video generation quality tier. STANDARD is fastest; HIGH is slowest and highest quality.
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` — Text prompt describing the video to generate. Optional when reference images or a video are provided.
    
</dd>
</dl>

<dl>
<dd>

**image_file_ids:** `typing.Optional[typing.List[str]]` — Optional file ids of reference images (e.g. `["vg_file_..."]`). Upload files first via `POST /v1/files/upload`, then pass the returned ids here. When provided, the model animates or uses these images as guidance.
    
</dd>
</dl>

<dl>
<dd>

**video_file_id:** `typing.Optional[str]` — Optional file id of a source video (e.g. `vg_file_...`). Upload a file first via `POST /v1/files/upload`, then pass the returned id here. When provided, the model restyles or transforms the input video.
    
</dd>
</dl>

<dl>
<dd>

**generate_audio:** `typing.Optional[bool]` — When true, the generated video is guaranteed to include audio. When false, audio may still be present. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**aspect_ratio:** `typing.Optional[AspectRatio]` — Aspect ratio for the generated video. Defaults to 16:9 when omitted.
    
</dd>
</dl>

<dl>
<dd>

**watermark_mode:** `typing.Optional[WatermarkMode]` 
    
</dd>
</dl>

<dl>
<dd>

**num_results:** `typing.Optional[int]` — Number of output results to generate. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**is_output_temporary:** `typing.Optional[bool]` — When true, generated files are temporary. Temporary files are guaranteed to be available for 24 hours, after which they may be archived at any time. Temporary files are not analyzed (no description, transcript, or embedding will be generated), so they will not appear in search results. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">text_to_speech</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Convert text into a spoken audio file. Only voices with `supportsDirectToolExecution` set to true can be used. Optionally choose a voice, language, speed, and pronunciation overrides.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.text_to_speech(
    tts_text="ttsText",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tts_text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**voice_id:** `typing.Optional[str]` — Voice id from `GET /v1/resources/tts-voices`. A default voice is used when null. Only voices with `supportsDirectToolExecution` set to true are accepted.
    
</dd>
</dl>

<dl>
<dd>

**speech_language_code:** `typing.Optional[str]` — ISO-639-1 language hint for pronunciation (e.g. `en`, `es`, `zh`).
    
</dd>
</dl>

<dl>
<dd>

**pronunciation_replacements:** `typing.Optional[typing.List[PronunciationReplacement]]` 
    
</dd>
</dl>

<dl>
<dd>

**auto_expand_pronunciation_replacements:** `typing.Optional[bool]` — When true, automatically expands numbers, symbols, acronyms, and other non-word tokens into their spoken forms before synthesis so the voice pronounces them correctly (e.g. `$100` → `one hundred dollars`, `NASA` → `nasa`, `3rd` → `third`). Defaults to false when omitted.
    
</dd>
</dl>

<dl>
<dd>

**voice_speed:** `typing.Optional[float]` — Speech rate multiplier. Defaults to the voice's default speed.
    
</dd>
</dl>

<dl>
<dd>

**num_results:** `typing.Optional[int]` — Number of output results to generate. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**is_output_temporary:** `typing.Optional[bool]` — When true, generated files are temporary. Temporary files are guaranteed to be available for 24 hours, after which they may be archived at any time. Temporary files are not analyzed (no description, transcript, or embedding will be generated), so they will not appear in search results. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">generate_sound_effect</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a sound effect from a text description. Optionally control the duration and prompt influence.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.generate_sound_effect(
    prompt="prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**duration_seconds:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt_influence:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**num_results:** `typing.Optional[int]` — Number of output results to generate. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**is_output_temporary:** `typing.Optional[bool]` — When true, generated files are temporary. Temporary files are guaranteed to be available for 24 hours, after which they may be archived at any time. Temporary files are not analyzed (no description, transcript, or embedding will be generated), so they will not appear in search results. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">generate_music</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate an instrumental music track from a text description. The returned track is approximately 30 seconds long.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.generate_music(
    prompt="prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt:** `str` — A text description of the music to generate. Include genre, mood, instrumentation, and tempo for best results.
    
</dd>
</dl>

<dl>
<dd>

**duration_seconds:** `typing.Optional[float]` — Desired track length in seconds. Currently informational — output tracks are approximately 30 seconds regardless of this value.
    
</dd>
</dl>

<dl>
<dd>

**num_results:** `typing.Optional[int]` — Number of output results to generate. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**is_output_temporary:** `typing.Optional[bool]` — When true, generated files are temporary. Temporary files are guaranteed to be available for 24 hours, after which they may be archived at any time. Temporary files are not analyzed (no description, transcript, or embedding will be generated), so they will not appear in search results. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">generate_avatar</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a talking-head avatar video by pairing a presenter with an audio file, typically from a prior text-to-speech result.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.generate_avatar(
    avatar_presenter_id="avatarPresenterId",
    audio_storage_file_id="audioStorageFileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**avatar_presenter_id:** `str` — Presenter id from `GET /v1/resources/avatar-presenters`.
    
</dd>
</dl>

<dl>
<dd>

**audio_storage_file_id:** `str` — File id of an AUDIO file (e.g. `vg_file_...`), typically from a prior text-to-speech result. Upload a file first via `POST /v1/files/upload` or generate one with `POST /v1/tools/text-to-speech`, then pass the returned id here.
    
</dd>
</dl>

<dl>
<dd>

**watermark_mode:** `typing.Optional[WatermarkMode]` 
    
</dd>
</dl>

<dl>
<dd>

**num_results:** `typing.Optional[int]` — Number of output results to generate. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**is_output_temporary:** `typing.Optional[bool]` — When true, generated files are temporary. Temporary files are guaranteed to be available for 24 hours, after which they may be archived at any time. Temporary files are not analyzed (no description, transcript, or embedding will be generated), so they will not appear in search results. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">vectorize_image</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Convert any raster image into a scalable vector graphic (SVG). The output traces the shapes and colors of the input image.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.vectorize_image(
    image_storage_file_id="imageStorageFileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ImageAssetRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">remove_image_background</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove the background from an image, returning a transparent-background PNG of the foreground subject.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.remove_image_background(
    image_storage_file_id="imageStorageFileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ImageAssetRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">remove_video_background</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove the background from a video, producing a transparent-background video of the foreground subject.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.remove_video_background(
    video_storage_file_id="videoStorageFileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `VideoAssetRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">upscale_image</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Increase the resolution of an image while preserving detail and sharpness.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.upscale_image(
    image_storage_file_id="imageStorageFileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ImageAssetRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">upscale_video</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Increase the resolution of a video while preserving detail and sharpness.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.upscale_video(
    video_storage_file_id="videoStorageFileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `VideoAssetRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">image3d_effect</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Turn a still image into a short video clip with a 3D parallax motion effect, simulating camera movement through the scene.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.image3d_effect(
    image_storage_file_id="imageStorageFileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ImageAssetRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">cancel_tool_execution</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Request cancellation of a running tool execution. The execution transitions to `cancelled` if it has not already completed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.cancel_tool_execution(
    tool_execution_id="toolExecutionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tool_execution_id:** `str` — The tool execution id returned when the tool was started.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">get_tool_execution_info</a>(...) -> ExecutedTool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the current status and result of a tool execution. Poll this endpoint until `status` is `succeeded`, `failed`, or `cancelled`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.get_tool_execution_info(
    tool_execution_id="toolExecutionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tool_execution_id:** `str` — The tool execution id returned when the tool was started.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Files
<details><summary><code>client.files.<a href="src/videogen/files/client.py">get_files</a>(...) -> GetFilesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List files in your account, including generated assets and uploads. Files are returned most recently updated first. Paginated; pass `nextCursor` from the previous response as `cursor` to fetch the next page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.files.get_files()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return in the page. Defaults to 50; capped at 200.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque pagination cursor returned as `nextCursor` by the previous page. Omit on the first request. Cursors are tied to the endpoint that produced them and must be passed unmodified.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/videogen/files/client.py">search_files</a>(...) -> SearchFilesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Semantic vector search over your files. Embeds the query text and returns the closest matching files ranked by cosine similarity. Only files with indexed descriptions are searchable.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.files.search_files(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — Natural-language search query. The text is embedded and compared against file description vectors using cosine similarity.
    
</dd>
</dl>

<dl>
<dd>

**num_results:** `typing.Optional[int]` — Number of results to return (1-100). Defaults to 10.
    
</dd>
</dl>

<dl>
<dd>

**self_only:** `typing.Optional[bool]` — When true, only files created by the calling API key's user are returned. When false (default), all files accessible to the team are included.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/videogen/files/client.py">get_file</a>(...) -> StorageFile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve metadata for a single file by its id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.files.get_file(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — The file id (e.g. `vg_file_...`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/videogen/files/client.py">create_file_upload</a>(...) -> FileUploadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new file and receive a pre-signed upload URL. PUT the file bytes to the returned URL, then poll `GET /v1/files/{fileId}` until the file is ready.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.files.create_file_upload(
    display_name="displayName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**display_name:** `str` — Display name for the uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[CreateFileUploadRequestType]` — The type of file to upload. Optional; when omitted, the type is inferred after upload processing completes.
    
</dd>
</dl>

<dl>
<dd>

**is_temporary:** `typing.Optional[bool]` — When true, the file is temporary. Temporary files are guaranteed to be available for 24 hours, after which they may be archived at any time. Temporary files are not analyzed (no description, transcript, or embedding will be generated), so they will not appear in search results. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/videogen/files/client.py">hydrate_file</a>(...) -> StorageFile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate fresh signed URLs for all available renditions of a file. Call this when source URLs are missing or expired. Returns the full file object with populated `thumbnailSource`, `previewSource`, and `downloadSource`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.files.hydrate_file(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — The file id (e.g. `vg_file_...`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/videogen/files/client.py">archive_file</a>(...) -> StorageFile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Archive a file by setting its archived timestamp. Archived files are excluded from list results. Returns the updated file object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.files.archive_file(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — The file id (e.g. `vg_file_...`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/videogen/files/client.py">enable_public_preview</a>(...) -> StorageFile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enable public preview for a file. Works for any file type. Copies the file to a permanent public URL (`staticPublicPreviewSource`) and, for video and audio, registers a public embed playback id (`publicPlaybackId`) for use with `@videogen/player`. If the file is not yet on the streaming provider, the endpoint starts the upload and polls briefly; otherwise the Mux asset-ready webhook finishes creating the embed playback id. Returns the updated file.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.files.enable_public_preview(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — The file id (e.g. `vg_file_...`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/videogen/files/client.py">disable_public_preview</a>(...) -> StorageFile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disable public preview for a file. Removes the permanent public URL copy and revokes unauthenticated embed streaming access. Authenticated signed URLs remain functional. Returns the updated file.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.files.disable_public_preview(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — The file id (e.g. `vg_file_...`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Text
<details><summary><code>client.text.<a href="src/videogen/text/client.py">generate_text</a>(...) -> GenerateTextResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate text from a prompt using a fast, general-purpose language model. Synchronous — the response includes the generated text. Useful for drafting scripts, titles, descriptions, and other short copy before generating a video.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.text.generate_text(
    prompt="Write a 30-second upbeat video script about why the sky is blue.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt:** `str` — The instruction or content to generate text from.
    
</dd>
</dl>

<dl>
<dd>

**system:** `typing.Optional[str]` — Optional system instructions that steer the model's role, tone, and constraints.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[GenerateTextRequestModel]` — Model tier. `fast` is quickest and cheapest; `smart` is higher quality. Defaults to `fast`.
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` — Sampling temperature. Higher values produce more varied output. Defaults to the model's default.
    
</dd>
</dl>

<dl>
<dd>

**max_output_tokens:** `typing.Optional[int]` — Maximum number of tokens to generate. Defaults to 512.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Resources
<details><summary><code>client.resources.<a href="src/videogen/resources/client.py">list_avatar_presenters</a>(...) -> AvatarPresenterListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List available avatar presenters. Pass an `avatarPresenterId` from the response to the avatar video endpoint. Paginated; pass `nextCursor` from the previous response as `cursor` to fetch the next page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.resources.list_avatar_presenters()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return in the page. Defaults to 50; capped at 200.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque pagination cursor returned as `nextCursor` by the previous page. Omit on the first request. Cursors are tied to the endpoint that produced them and must be passed unmodified.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.resources.<a href="src/videogen/resources/client.py">list_tts_voices</a>(...) -> TtsVoiceListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List available text-to-speech voices. Pass a `voiceId` from the response to the text-to-speech endpoint. Paginated; pass `nextCursor` from the previous response as `cursor` to fetch the next page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.resources.list_tts_voices()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return in the page. Defaults to 50; capped at 200.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque pagination cursor returned as `nextCursor` by the previous page. Omit on the first request. Cursors are tied to the endpoint that produced them and must be passed unmodified.
    
</dd>
</dl>

<dl>
<dd>

**include_deprecated_voices:** `typing.Optional[bool]` — When true, includes voices that are deprecated but still callable. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks
<details><summary><code>client.webhooks.<a href="src/videogen/webhooks/client.py">list_webhook_endpoints</a>(...) -> WebhookEndpointListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List configured webhook endpoints for your account. Paginated; pass `nextCursor` from the previous response as `cursor` to fetch the next page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.webhooks.list_webhook_endpoints()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return in the page. Defaults to 50; capped at 200.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque pagination cursor returned as `nextCursor` by the previous page. Omit on the first request. Cursors are tied to the endpoint that produced them and must be passed unmodified.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/videogen/webhooks/client.py">create_webhook_endpoint</a>(...) -> WebhookEndpoint</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register a new webhook endpoint to receive `tool_execution.*` and `file.*` events. The signing secret is only returned in this response. Store it securely.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.webhooks.create_webhook_endpoint(
    url="url",
    events=[
        "tool_execution.succeeded"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url:** `str` — HTTPS URL that will receive webhook POST requests.
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.List[WebhookEventName]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/videogen/webhooks/client.py">delete_webhook_endpoint</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a webhook endpoint. It will stop receiving events immediately.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.webhooks.delete_webhook_endpoint(
    endpoint_id="endpointId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**endpoint_id:** `str` — The webhook endpoint id returned by `POST /v1/webhooks/endpoints`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

