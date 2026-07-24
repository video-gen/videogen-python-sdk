from __future__ import annotations

from typing import Any, Optional


class VideoGenError(Exception):
    """HTTP or API error returned by the VideoGen API."""

    def __init__(
        self,
        message: str,
        *,
        status: int,
        body: Any = None,
        request_id: Optional[str] = None,
    ) -> None:
        super().__init__(message)
        self.status = status
        self.body = body
        self.request_id = request_id
        # camelCase alias for cross-language parity with the TypeScript SDK
        self.requestId = request_id

    def __str__(self) -> str:
        base = super().__str__()
        if self.request_id:
            return f"{base} (request_id={self.request_id})"
        return base


class PollCancelledError(Exception):
    """Raised when a poll helper or request is cancelled via cancel_event."""

    def __init__(self, message: str = "Polling cancelled.") -> None:
        super().__init__(message)
