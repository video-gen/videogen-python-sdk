from __future__ import annotations

from typing import TYPE_CHECKING, Any, Mapping, Optional
from urllib.parse import quote

if TYPE_CHECKING:
    from ..client import AsyncVideoGen, VideoGen


def _cancel_event(cancel_event: Any, options: Optional[Mapping[str, Any]]) -> Any:
    if cancel_event is not None:
        return cancel_event
    return options.get("cancel_event") if options is not None else None


class BillingResource:
    def __init__(self, client: VideoGen) -> None:
        self._client = client._http

    # @sdk-operation getBillingAccount
    def get_billing_account(
        self, *,
        options: Optional[Mapping[str, Any]] = None, cancel_event: Any = None,
    ) -> Any:
        """Read billing access and balance without collecting payment."""
        return self._client.request(
            method="GET",
            path='/v1/billing/account',
            body=None,
            cancel_event=_cancel_event(cancel_event, options),
        )

    # @sdk-operation createBillingOrder
    def create_billing_order(
        self, *, order_id: str, credits: int,
        options: Optional[Mapping[str, Any]] = None, cancel_event: Any = None,
    ) -> Any:
        """Prepare a quote. Reuse the same order UUID for an identical retry."""
        return self._client.request(
            method="POST",
            path='/v1/billing/orders',
            body={"order_id": order_id, "credits": credits},
            cancel_event=_cancel_event(cancel_event, options),
        )

    # @sdk-operation getBillingOrder
    def get_billing_order(
        self, *, order_id: str,
        options: Optional[Mapping[str, Any]] = None, cancel_event: Any = None,
    ) -> Any:
        """Read the original order before retrying an uncertain purchase."""
        encoded_order_id = quote(order_id, safe="")
        return self._client.request(
            method="GET",
            path=f'/v1/billing/orders/{encoded_order_id}',
            body=None,
            cancel_event=_cancel_event(cancel_event, options),
        )

    # @sdk-operation completeBillingOrder
    def complete_billing_order(
        self, *, order_id: str, revision: int, idempotency_key: str,
        payment_token: str,
        options: Optional[Mapping[str, Any]] = None, cancel_event: Any = None,
    ) -> Any:
        """Complete this quote only after exact user approval. The token is transport-only."""
        encoded_order_id = quote(order_id, safe="")
        return self._client.request(
            method="POST",
            path=f'/v1/billing/orders/{encoded_order_id}/complete',
            body={"revision": revision, "idempotency_key": idempotency_key},
            cancel_event=_cancel_event(cancel_event, options),
            payment_token=payment_token,
        )

    # @sdk-operation cancelBillingOrder
    def cancel_billing_order(
        self, *, order_id: str,
        options: Optional[Mapping[str, Any]] = None, cancel_event: Any = None,
    ) -> Any:
        """Cancel an unpaid order. This does not refund an already settled payment."""
        encoded_order_id = quote(order_id, safe="")
        return self._client.request(
            method="POST",
            path=f'/v1/billing/orders/{encoded_order_id}/cancel',
            body={},
            cancel_event=_cancel_event(cancel_event, options),
        )

    # @sdk-operation requestBillingRefund
    def request_billing_refund(
        self, *, order_id: str, reason: str,
        options: Optional[Mapping[str, Any]] = None, cancel_event: Any = None,
    ) -> Any:
        """Request a support-reviewed refund; this does not complete a refund."""
        encoded_order_id = quote(order_id, safe="")
        return self._client.request(
            method="POST",
            path=f'/v1/billing/orders/{encoded_order_id}/refund',
            body={"reason": reason},
            cancel_event=_cancel_event(cancel_event, options),
        )


class AsyncBillingResource:
    def __init__(self, client: AsyncVideoGen) -> None:
        self._client = client._http

    # @sdk-operation getBillingAccount
    async def get_billing_account(
        self, *,
        options: Optional[Mapping[str, Any]] = None, cancel_event: Any = None,
    ) -> Any:
        """Read billing access and balance without collecting payment."""
        return await self._client.request(
            method="GET",
            path='/v1/billing/account',
            body=None,
            cancel_event=_cancel_event(cancel_event, options),
        )

    # @sdk-operation createBillingOrder
    async def create_billing_order(
        self, *, order_id: str, credits: int,
        options: Optional[Mapping[str, Any]] = None, cancel_event: Any = None,
    ) -> Any:
        """Prepare a quote. Reuse the same order UUID for an identical retry."""
        return await self._client.request(
            method="POST",
            path='/v1/billing/orders',
            body={"order_id": order_id, "credits": credits},
            cancel_event=_cancel_event(cancel_event, options),
        )

    # @sdk-operation getBillingOrder
    async def get_billing_order(
        self, *, order_id: str,
        options: Optional[Mapping[str, Any]] = None, cancel_event: Any = None,
    ) -> Any:
        """Read the original order before retrying an uncertain purchase."""
        encoded_order_id = quote(order_id, safe="")
        return await self._client.request(
            method="GET",
            path=f'/v1/billing/orders/{encoded_order_id}',
            body=None,
            cancel_event=_cancel_event(cancel_event, options),
        )

    # @sdk-operation completeBillingOrder
    async def complete_billing_order(
        self, *, order_id: str, revision: int, idempotency_key: str,
        payment_token: str,
        options: Optional[Mapping[str, Any]] = None, cancel_event: Any = None,
    ) -> Any:
        """Complete this quote only after exact user approval. The token is transport-only."""
        encoded_order_id = quote(order_id, safe="")
        return await self._client.request(
            method="POST",
            path=f'/v1/billing/orders/{encoded_order_id}/complete',
            body={"revision": revision, "idempotency_key": idempotency_key},
            cancel_event=_cancel_event(cancel_event, options),
            payment_token=payment_token,
        )

    # @sdk-operation cancelBillingOrder
    async def cancel_billing_order(
        self, *, order_id: str,
        options: Optional[Mapping[str, Any]] = None, cancel_event: Any = None,
    ) -> Any:
        """Cancel an unpaid order. This does not refund an already settled payment."""
        encoded_order_id = quote(order_id, safe="")
        return await self._client.request(
            method="POST",
            path=f'/v1/billing/orders/{encoded_order_id}/cancel',
            body={},
            cancel_event=_cancel_event(cancel_event, options),
        )

    # @sdk-operation requestBillingRefund
    async def request_billing_refund(
        self, *, order_id: str, reason: str,
        options: Optional[Mapping[str, Any]] = None, cancel_event: Any = None,
    ) -> Any:
        """Request a support-reviewed refund; this does not complete a refund."""
        encoded_order_id = quote(order_id, safe="")
        return await self._client.request(
            method="POST",
            path=f'/v1/billing/orders/{encoded_order_id}/refund',
            body={"reason": reason},
            cancel_event=_cancel_event(cancel_event, options),
        )
