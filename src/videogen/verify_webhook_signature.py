from __future__ import annotations

from typing import Dict, Union

from standardwebhooks.webhooks import Webhook

from .types.file_upload_webhook_payload import FileUploadWebhookPayload
from .types.tool_execution_webhook_payload import ToolExecutionWebhookPayload

WebhookEvent = Union[ToolExecutionWebhookPayload, FileUploadWebhookPayload]
"""Discriminated union of all webhook payloads. Narrow on the ``event`` field."""


def verify_webhook_signature(
    raw_body: str,
    headers: Dict[str, str],
    signing_secret: str,
) -> WebhookEvent:
    """Verify a Standard Webhooks signature and return the parsed, typed payload.

    The returned event is a union — narrow on the ``event`` field::

        event = verify_webhook_signature(raw_body, headers, secret)
        if event.event == "tool_execution.succeeded":
            print(event.results)  # ToolExecutionWebhookPayload

    Args:
        raw_body: The **raw** request body string (not parsed JSON).
        headers: A dict containing ``webhook-id``, ``webhook-timestamp``,
            and ``webhook-signature``.
        signing_secret: The ``signing_secret`` returned when you created
            the webhook endpoint.

    Raises:
        Exception: If the signature is invalid, the timestamp is too old,
            or any required header is missing.
    """
    wh = Webhook(signing_secret)
    return wh.verify(raw_body, headers)  # type: ignore[return-value]
