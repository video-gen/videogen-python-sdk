# Reference
## tools
<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">prompt_to_image</a>(...) -> StartToolExecutionResponse</code></summary>
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

client.tools.prompt_to_image(
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

**aspect_ratio:** `typing.Optional[AspectRatio]` — Aspect ratio for the generated image. Defaults to 16:9 when omitted.
    
</dd>
</dl>

<dl>
<dd>

**num_candidates:** `typing.Optional[int]` — Number of output candidates to generate. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**is_output_file_temporary:** `typing.Optional[bool]` — When true, generated files are scoped as temporary. Defaults to false.
    
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
    prompt="prompt",
    generate_audio=True,
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

**generate_audio:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**aspect_ratio:** `typing.Optional[AspectRatio]` — Aspect ratio for the generated video. Defaults to 16:9 when omitted.
    
</dd>
</dl>

<dl>
<dd>

**num_candidates:** `typing.Optional[int]` — Number of output candidates to generate. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**is_output_file_temporary:** `typing.Optional[bool]` — When true, generated files are scoped as temporary. Defaults to false.
    
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

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">image_to_video</a>(...) -> StartToolExecutionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi, StorageFileRef
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.image_to_video(
    prompt="prompt",
    generate_audio=True,
    image=StorageFileRef(
        storage_file_id="storageFileId",
        type="IMAGE",
    ),
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

**generate_audio:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**image:** `StorageFileRef` 
    
</dd>
</dl>

<dl>
<dd>

**source_prompt_to_image_prompt:** `typing.Optional[str]` — Optional prompt used when the source image was generated.
    
</dd>
</dl>

<dl>
<dd>

**num_candidates:** `typing.Optional[int]` — Number of output candidates to generate. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**is_output_file_temporary:** `typing.Optional[bool]` — When true, generated files are scoped as temporary. Defaults to false.
    
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

**voice_id:** `typing.Optional[str]` — Opaque voice id from `GET /v1/resources/tts-voices`. Server defaults apply when null.
    
</dd>
</dl>

<dl>
<dd>

**previous_tts_text:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**next_tts_text:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**speech_language_code:** `typing.Optional[str]` — Optional ISO-639-1 language hint for pronunciation (e.g. `en`, `es`, `zh`). The server validates the value at runtime against the supported set.
    
</dd>
</dl>

<dl>
<dd>

**hide_captions:** `typing.Optional[bool]` — Defaults to false when omitted.
    
</dd>
</dl>

<dl>
<dd>

**pronunciation_replacements:** `typing.Optional[typing.List[PronunciationReplacement]]` 
    
</dd>
</dl>

<dl>
<dd>

**auto_expand_pronunciation_replacements:** `typing.Optional[bool]` — Defaults to false when omitted.
    
</dd>
</dl>

<dl>
<dd>

**voice_speed:** `typing.Optional[float]` — Defaults to server voice default when omitted.
    
</dd>
</dl>

<dl>
<dd>

**num_candidates:** `typing.Optional[int]` — Number of output candidates to generate. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**is_output_file_temporary:** `typing.Optional[bool]` — When true, generated files are scoped as temporary. Defaults to false.
    
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

**num_candidates:** `typing.Optional[int]` — Number of output candidates to generate. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**is_output_file_temporary:** `typing.Optional[bool]` — When true, generated files are scoped as temporary. Defaults to false.
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi, StorageFileRef
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.generate_avatar(
    avatar_presenter_id="avatarPresenterId",
    audio=StorageFileRef(
        storage_file_id="storageFileId",
        type="IMAGE",
    ),
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

**avatar_presenter_id:** `str` — Opaque presenter id from `GET /v1/resources/avatar-presenters`.
    
</dd>
</dl>

<dl>
<dd>

**audio:** `StorageFileRef` — Reference to an `AUDIO` file in your workspace. Typically obtained from a prior `text-to-speech` execution's `result.storageFileId`.
    
</dd>
</dl>

<dl>
<dd>

**num_candidates:** `typing.Optional[int]` — Number of output candidates to generate. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**is_output_file_temporary:** `typing.Optional[bool]` — When true, generated files are scoped as temporary. Defaults to false.
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi, StorageFileRef
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.vectorize_image(
    image=StorageFileRef(
        storage_file_id="storageFileId",
        type="IMAGE",
    ),
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi, StorageFileRef
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.remove_image_background(
    image=StorageFileRef(
        storage_file_id="storageFileId",
        type="IMAGE",
    ),
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi, StorageFileRef
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.remove_video_background(
    video=StorageFileRef(
        storage_file_id="storageFileId",
        type="IMAGE",
    ),
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi, StorageFileRef
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.upscale_image(
    image=StorageFileRef(
        storage_file_id="storageFileId",
        type="IMAGE",
    ),
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from videogen import VideoGenApi, StorageFileRef
from videogen.environment import VideoGenApiEnvironment

client = VideoGenApi(
    token="<token>",
    environment=VideoGenApiEnvironment.PRODUCTION,
)

client.tools.upscale_video(
    video=StorageFileRef(
        storage_file_id="storageFileId",
        type="IMAGE",
    ),
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
    api_task_execution_id="apiTaskExecutionId",
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

**api_task_execution_id:** `str` 
    
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

<details><summary><code>client.tools.<a href="src/videogen/tools/client.py">get_executed_tool</a>(...) -> ExecutedTool</code></summary>
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

client.tools.get_executed_tool(
    api_task_execution_id="apiTaskExecutionId",
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

**api_task_execution_id:** `str` 
    
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

## files
<details><summary><code>client.files.<a href="src/videogen/files/client.py">get_files</a>() -> GetFilesResponse</code></summary>
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

<details><summary><code>client.files.<a href="src/videogen/files/client.py">get_file</a>(...) -> StorageFile</code></summary>
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

client.files.get_file(
    storage_file_id="storageFileId",
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

**storage_file_id:** `str` 
    
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

## resources
<details><summary><code>client.resources.<a href="src/videogen/resources/client.py">list_avatar_presenters</a>() -> AvatarPresenterListResponse</code></summary>
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

<details><summary><code>client.resources.<a href="src/videogen/resources/client.py">list_tts_voices</a>() -> TtsVoiceListResponse</code></summary>
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## webhooks
<details><summary><code>client.webhooks.<a href="src/videogen/webhooks/client.py">list_webhook_endpoints</a>() -> WebhookEndpointListResponse</code></summary>
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

**url:** `str` — HTTPS URL VideoGen will POST to; must be reachable from our servers.
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.List[ToolExecutionWebhookEventName]` 
    
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

