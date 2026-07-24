from __future__ import annotations

import base64
import hashlib
import hmac
import json
import time
from typing import Any, Mapping, Optional, Union

from ._http import to_python_keys
from .errors import VideoGenError


def _header_get(headers: Mapping[str, Any], name: str) -> Optional[str]:
    lower = name.lower()
    for key, value in headers.items():
        if str(key).lower() == lower:
            if isinstance(value, (list, tuple)):
                return str(value[0]) if value else None
            return str(value) if value is not None else None
    return None


def _decode_secret(secret: str) -> bytes:
    value = secret.strip()
    if value.startswith("whsec_"):
        value = value[len("whsec_") :]
    try:
        return base64.b64decode(value)
    except Exception:
        return value.encode("utf-8")


def verify_webhook_signature(
    raw_body: Union[str, bytes, None] = None,
    headers: Optional[Mapping[str, Any]] = None,
    secret: Optional[str] = None,
    *,
    signing_secret: Optional[str] = None,
    tolerance_seconds: int = 300,
) -> dict:
    """Verify a Standard Webhooks signature and return the parsed event dict.

    Accepts either positional ``(raw_body, headers, secret)`` or keyword args.
    ``signing_secret`` is accepted as an alias of ``secret``.
    """
    resolved_secret = secret if secret is not None else signing_secret
    if raw_body is None or headers is None or resolved_secret is None:
        raise TypeError(
            "verify_webhook_signature requires raw_body, headers, and secret "
            "(or signing_secret)."
        )

    body_bytes = raw_body.encode("utf-8") if isinstance(raw_body, str) else bytes(raw_body)
    msg_id = _header_get(headers, "webhook-id")
    timestamp = _header_get(headers, "webhook-timestamp")
    signatures = _header_get(headers, "webhook-signature")
    if not msg_id or not timestamp or not signatures:
        raise VideoGenError(
            "Missing Standard Webhooks headers.",
            status=401,
            body={"message": "Missing webhook-id, webhook-timestamp, or webhook-signature."},
        )

    try:
        ts = int(timestamp)
    except ValueError as exc:
        raise VideoGenError(
            "Invalid webhook timestamp.",
            status=401,
            body={"message": "Invalid webhook-timestamp."},
        ) from exc

    if abs(int(time.time()) - ts) > tolerance_seconds:
        raise VideoGenError(
            "Webhook timestamp outside tolerance.",
            status=401,
            body={"message": "Webhook timestamp outside tolerance."},
        )

    signed_content = f"{msg_id}.{timestamp}.".encode("utf-8") + body_bytes
    key = _decode_secret(resolved_secret)
    digest = hmac.new(key, signed_content, hashlib.sha256).digest()
    expected = base64.b64encode(digest).decode("ascii")

    matched = False
    for part in signatures.split(" "):
        if "," not in part:
            continue
        version, signature = part.split(",", 1)
        if version != "v1":
            continue
        if hmac.compare_digest(signature, expected):
            matched = True
            break

    if not matched:
        raise VideoGenError(
            "Invalid webhook signature.",
            status=401,
            body={"message": "Invalid webhook signature."},
        )

    try:
        payload = json.loads(body_bytes.decode("utf-8"))
    except Exception as exc:
        raise VideoGenError(
            "Webhook body is not valid JSON.",
            status=400,
            body={"message": "Webhook body is not valid JSON."},
        ) from exc

    if not isinstance(payload, dict):
        raise VideoGenError(
            "Webhook body must be a JSON object.",
            status=400,
            body={"message": "Webhook body must be a JSON object."},
        )
    return to_python_keys(payload)
