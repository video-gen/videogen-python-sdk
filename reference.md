# Reference
## Tools
<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">prompt_to_image</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate an image from a text prompt. Optionally specify an aspect ratio and number of candidates.
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

client.tools.prompt_to_image(
    prompt="A serene Japanese garden with cherry blossoms at golden hour",
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

**aspect_ratio:** `typing.Optional[AspectRatio]` — Aspect ratio for the generated image. Defaults to 16:9 when omitted.
    
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

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">prompt_to_video_clip</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a video clip from a text prompt, with optional audio. Optionally specify an aspect ratio and number of candidates.
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

client.tools.prompt_to_video_clip(
    prompt="A golden retriever running through a sunlit meadow in slow motion, cinematic",
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

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">image_to_video_clip</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Animate a still image into a video clip using a text prompt. Optionally generate audio alongside the video.
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

client.tools.image_to_video_clip(
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

**image_storage_file_id:** `str` — File id of the source image (e.g. `vg_file_...`). Upload a file first via `POST /v1/files/upload`, then pass the returned id here.
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` — Optional text prompt to guide the animation. When omitted the model infers motion from the image.
    
</dd>
</dl>

<dl>
<dd>

**generate_audio:** `typing.Optional[bool]` — When true, the generated video is guaranteed to include audio. When false, audio may still be present. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**source_prompt_to_image_prompt:** `typing.Optional[str]` — Optional prompt used when the source image was generated.
    
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

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">image_to_image</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transform an existing image using a text prompt. The prompt describes the desired changes to apply.
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

client.tools.image_to_image(
    image_storage_file_ids=[
        "imageStorageFileIds"
    ],
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

**image_storage_file_ids:** `typing.List[str]` — File ids of the source images (e.g. `["vg_file_..."]`). Upload files first via `POST /v1/files/upload`, then pass the returned ids here. Maximum 4 images.
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `str` — Prompt describing how to transform the input image.
    
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

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">video_to_video_clip</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restyle an existing video using a text prompt. The prompt describes the visual transformation to apply.
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

client.tools.video_to_video_clip(
    video_storage_file_id="videoStorageFileId",
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

**video_storage_file_id:** `str` — File id of the source video (e.g. `vg_file_...`). Upload a file first via `POST /v1/files/upload`, then pass the returned id here.
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `str` — Prompt describing how to transform the input video.
    
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

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">prompt_to_sound_effect</a>(...) -> StartToolExecutionResponse</code></summary>
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

client.tools.prompt_to_sound_effect(
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

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">audio_to_avatar_clip</a>(...) -> StartToolExecutionResponse</code></summary>
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

client.tools.audio_to_avatar_clip(
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

**tool_execution_id:** `str` 
    
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

**tool_execution_id:** `str` 
    
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
<details><summary><code>client.files.<a href="src/videogen/files/client.py">get_files</a>() -> GetFilesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all files in your account, including generated assets and uploads.
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

**num_results:** `typing.Optional[int]` — Number of results to return (1–100). Defaults to 10.
    
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

**file_id:** `str` 
    
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

**file_id:** `str` 
    
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

Enable public preview for a file. Creates a public playback ID on the underlying Mux asset so the file can be streamed without authentication. Returns the updated file with `isPublicPreviewEnabled`, `publicHlsUrl`, and `publicPlaybackId` populated. Only works for video and audio files.
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

**file_id:** `str` 
    
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

Disable public preview for a file. Deletes the public playback ID from the underlying Mux asset. The file's signed URLs remain functional. Returns the updated file.
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

**file_id:** `str` 
    
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
<details><summary><code>client.resources.<a href="src/videogen/resources/client.py">list_avatar_presenters</a>() -> AvatarPresenterListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all available avatar presenters. Pass an `avatarPresenterId` from the response to the avatar video endpoint.
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

List all available text-to-speech voices. Pass a `voiceId` from the response to the text-to-speech endpoint.
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

**include_deprecated_voices:** `typing.Optional[bool]` — When true, includes deprecated voices in the response. Defaults to false.
    
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
<details><summary><code>client.webhooks.<a href="src/videogen/webhooks/client.py">list_webhook_endpoints</a>() -> WebhookEndpointListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all configured webhook endpoints for your account.
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

**endpoint_id:** `str` 
    
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

