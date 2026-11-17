from __future__ import annotations

import asyncio
import json
import threading
import unittest

import httpx

from videogen import (
    AsyncVideoGen,
    PollCancelledError,
    VideoGen,
    VideoGenError,
)


ORDER_ID = "9f23cfe9-2278-43be-8d1c-8ce207873828"
TOKEN = "spt_test_transport_only"
ACCOUNT = {
    "teamId": "team-test", "teamName": "Test team", "creditsRemaining": 42,
    "currency": "usd", "purchaseLimitMinor": 2000,
    "accessExpiresAt": 1800000000, "canPurchase": True,
    "purchaseRestriction": None,
    "creditPack": {"minimumCredits": 2000, "stepCredits": 100, "maximumCredits": 1000000},
}
ORDER = {
    "orderId": ORDER_ID, "state": "requires_approval", "revision": 3,
    "teamId": "team-test", "teamName": "Test team", "seller": "VideoGen",
    "product": "credits", "credits": 2000, "currency": "usd",
    "subtotalMinor": 2000, "discountMinor": 0, "taxMinor": 100,
    "feesMinor": 0, "totalMinor": 2100, "expiresAt": 1800000000,
    "termsVersion": "agent-billing-v1", "refundTerms": "Contact support.",
    "refundStatus": "none", "receiptUrl": None,
    "retryGuidance": "Check this order before retrying.",
    "paymentHandler": {"id": "stripe_payments"},
    "verificationUrl": "https://app.videogen.io/settings/account?verify=test-order",
}
CALLS = [
    ("get_billing_account", {}, "GET", "/v1/billing/account", None),
    ("create_billing_order", {"order_id": ORDER_ID, "credits": 2000},
     "POST", "/v1/billing/orders", {"orderId": ORDER_ID, "credits": 2000}),
    ("get_billing_order", {"order_id": ORDER_ID},
     "GET", f"/v1/billing/orders/{ORDER_ID}", None),
    ("complete_billing_order", {
        "order_id": ORDER_ID, "revision": 3, "idempotency_key": "test-key-identical-retry",
        "payment_token": TOKEN,
     }, "POST", f"/v1/billing/orders/{ORDER_ID}/complete",
     {"revision": 3, "idempotencyKey": "test-key-identical-retry"}),
    ("cancel_billing_order", {"order_id": ORDER_ID},
     "POST", f"/v1/billing/orders/{ORDER_ID}/cancel", {}),
    ("request_billing_refund", {"order_id": ORDER_ID, "reason": "Unused purchase"},
     "POST", f"/v1/billing/orders/{ORDER_ID}/refund", {"reason": "Unused purchase"}),
]


class BillingTransportAssertions:
    def check_request(self, request, method, path, body):
        self.assertEqual(request.method, method)
        self.assertEqual(request.url.path, path)
        self.assertEqual(request.url.query, b"")
        self.assertEqual(request.headers["Authorization"], "Bearer api-key-test")
        self.assertEqual(request.headers["X-VideoGen-Client"], "sdk-python")
        self.assertEqual(json.loads(request.content) if request.content else None, body)
        self.assertNotIn(TOKEN, request.content.decode())
        self.assertNotIn(TOKEN, str(request.url))
        if path.endswith("/complete"):
            self.assertEqual(request.headers["Stripe-Shared-Payment-Token"], TOKEN)
        else:
            self.assertNotIn("Stripe-Shared-Payment-Token", request.headers)

    def check_response(self, response, method_name):
        if method_name == "get_billing_account":
            self.assertIsInstance(response, dict)
            self.assertEqual(response["team_id"], "team-test")
            self.assertEqual(response["credits_remaining"], 42)
            self.assertIsNone(response["purchase_restriction"])
            self.assertEqual(response["credit_pack"], {
                "minimum_credits": 2000, "step_credits": 100, "maximum_credits": 1000000,
            })
        else:
            self.assertIsInstance(response, dict)
            self.assertEqual(response["order_id"], ORDER_ID)
            self.assertEqual(response["total_minor"], 2100)
            self.assertEqual(response["refund_status"], "none")
            self.assertIsNone(response["receipt_url"])
            self.assertEqual(response["verification_url"], ORDER["verificationUrl"])


class BillingSyncTests(BillingTransportAssertions, unittest.TestCase):
    def test_unknown_response_fields_and_states_pass_through(self):
        def handler(request):
            return httpx.Response(200, json={**ORDER, "state": "future_state", "newField": 1})

        with httpx.Client(transport=httpx.MockTransport(handler)) as http:
            client = VideoGen(api_key="api-key-test", http_client=http)
            order = client.billing.get_billing_order(order_id=ORDER_ID)
        self.assertEqual(order["state"], "future_state")
        self.assertEqual(order["new_field"], 1)

    def test_all_six_operations_use_expected_transport_and_responses(self):
        requests = []

        def handler(request):
            requests.append(request)
            return httpx.Response(200, json=ACCOUNT if request.url.path.endswith("/account") else ORDER)

        with httpx.Client(transport=httpx.MockTransport(handler)) as http:
            client = VideoGen(api_key="api-key-test", http_client=http)
            for method_name, kwargs, method, path, body in CALLS:
                with self.subTest(operation=method_name):
                    previous = len(requests)
                    response = getattr(client.billing, method_name)(**kwargs)
                    self.assertEqual(len(requests), previous + 1)
                    self.check_request(requests[-1], method, path, body)
                    self.check_response(response, method_name)

    def test_failed_completion_is_not_retried_or_exposed_in_error(self):
        requests = []

        def handler(request):
            requests.append(request)
            return httpx.Response(409, json={"message": "Check the original order"}, headers={"x-request-id": "req-test"})

        with httpx.Client(transport=httpx.MockTransport(handler)) as http:
            client = VideoGen(api_key="api-key-test", http_client=http)
            with self.assertRaises(VideoGenError) as caught:
                client.billing.complete_billing_order(**CALLS[3][1])
            self.assertEqual(len(requests), 1)
            self.assertEqual(caught.exception.status, 409)
            self.assertEqual(caught.exception.request_id, "req-test")
            self.assertNotIn(TOKEN, str(caught.exception))
            self.assertNotIn(TOKEN, repr(caught.exception.body))

    def test_canceled_completion_does_not_send_payment(self):
        requests = []
        event = threading.Event()
        event.set()
        with httpx.Client(transport=httpx.MockTransport(lambda request: requests.append(request))) as http:
            client = VideoGen(api_key="api-key-test", http_client=http)
            with self.assertRaises(PollCancelledError):
                client.billing.complete_billing_order(**CALLS[3][1], options={"cancel_event": event})
        self.assertEqual(requests, [])

    def test_token_cannot_be_sent_as_unrecognized_quote_argument(self):
        client = VideoGen(api_key="api-key-test")
        try:
            with self.assertRaises(TypeError):
                client.billing.create_billing_order(
                    order_id=ORDER_ID, credits=2000, payment_token=TOKEN,
                )
        finally:
            client.close()

    def test_transport_timeout_is_not_retried(self):
        requests = []

        def handler(request):
            requests.append(request)
            raise httpx.ReadTimeout("Response uncertain", request=request)

        with httpx.Client(transport=httpx.MockTransport(handler)) as http:
            client = VideoGen(api_key="api-key-test", http_client=http)
            with self.assertRaises(httpx.ReadTimeout):
                client.billing.complete_billing_order(**CALLS[3][1])
        self.assertEqual(len(requests), 1)

    def test_order_path_cannot_inject_a_different_endpoint_or_query(self):
        requests = []

        def handler(request):
            requests.append(request)
            return httpx.Response(200, json=ORDER)

        with httpx.Client(transport=httpx.MockTransport(handler)) as http:
            client = VideoGen(api_key="api-key-test", http_client=http)
            client.billing.get_billing_order(order_id="unexpected/id?another=value")
        self.assertEqual(requests[0].url.query, b"")
        self.assertEqual(
            requests[0].url.raw_path,
            b"/v1/billing/orders/unexpected%2Fid%3Fanother%3Dvalue",
        )


class BillingAsyncTests(BillingTransportAssertions, unittest.IsolatedAsyncioTestCase):
    async def test_all_six_operations_use_expected_transport_and_responses(self):
        requests = []

        def handler(request):
            requests.append(request)
            return httpx.Response(200, json=ACCOUNT if request.url.path.endswith("/account") else ORDER)

        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as http:
            client = AsyncVideoGen(api_key="api-key-test", http_client=http)
            for method_name, kwargs, method, path, body in CALLS:
                with self.subTest(operation=method_name):
                    previous = len(requests)
                    response = await getattr(client.billing, method_name)(**kwargs)
                    self.assertEqual(len(requests), previous + 1)
                    self.check_request(requests[-1], method, path, body)
                    self.check_response(response, method_name)

    async def test_failed_completion_is_not_retried_or_exposed_in_error(self):
        requests = []

        def handler(request):
            requests.append(request)
            return httpx.Response(422, json={"message": "Payment rejected"})

        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as http:
            client = AsyncVideoGen(api_key="api-key-test", http_client=http)
            with self.assertRaises(VideoGenError) as caught:
                await client.billing.complete_billing_order(**CALLS[3][1])
            self.assertEqual(len(requests), 1)
            self.assertEqual(caught.exception.status, 422)
            self.assertNotIn(TOKEN, str(caught.exception))

    async def test_canceled_completion_does_not_send_payment(self):
        requests = []
        event = asyncio.Event()
        event.set()
        async with httpx.AsyncClient(transport=httpx.MockTransport(lambda request: requests.append(request))) as http:
            client = AsyncVideoGen(api_key="api-key-test", http_client=http)
            with self.assertRaises(PollCancelledError):
                await client.billing.complete_billing_order(**CALLS[3][1], cancel_event=event)
        self.assertEqual(requests, [])

    async def test_transport_timeout_is_not_retried(self):
        requests = []

        def handler(request):
            requests.append(request)
            raise httpx.ReadTimeout("Response uncertain", request=request)

        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as http:
            client = AsyncVideoGen(api_key="api-key-test", http_client=http)
            with self.assertRaises(httpx.ReadTimeout):
                await client.billing.complete_billing_order(**CALLS[3][1])
        self.assertEqual(len(requests), 1)


if __name__ == "__main__":
    unittest.main()
