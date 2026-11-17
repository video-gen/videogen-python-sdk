import asyncio
import json
import unittest
import httpx
from videogen import AsyncVideoGen, VideoGen, VideoGenError

QUOTA = {"model": "model-1", "callsPerHour": 3, "callsRemaining": 2, "nextCallAt": None, "totalSeconds": 600, "usedSeconds": 10, "reservedSeconds": 0, "remainingSeconds": 590}

class Model1TransportTests(unittest.TestCase):
    def test_sync_submit_and_quota(self):
        calls = []
        def handle(request):
            calls.append(request)
            return httpx.Response(202, json={"generationId": "vg_mgen_test"}) if request.method == "POST" else httpx.Response(200, json=QUOTA)
        http_client = httpx.Client(transport=httpx.MockTransport(handle))
        with VideoGen(api_key="test", http_client=http_client) as client:
            result = client.models.start_model1_generation(prompt="A product", idempotency_key="retry-python-key")
            self.assertEqual(result["generation_id"], "vg_mgen_test")
            self.assertEqual(client.models.get_model1_quota()["remaining_seconds"], 590)
        self.assertEqual(calls[0].headers["Idempotency-Key"], "retry-python-key")
        self.assertEqual(json.loads(calls[0].content), {"prompt": "A product", "seconds": 10, "imageFileIds": []})
        self.assertNotIn("Idempotency-Key", calls[1].headers)

    def test_retry_header_survives_api_error(self):
        def handle(request):
            return httpx.Response(429, json={"message": "Retry after the delay.", "code": "model_1_hourly_quota_exceeded"}, headers={"Retry-After": "120"})
        with VideoGen(api_key="test", http_client=httpx.Client(transport=httpx.MockTransport(handle))) as client:
            with self.assertRaises(VideoGenError) as caught:
                client.models.start_model1_generation(prompt="A product", idempotency_key="retry-python-key")
            self.assertEqual(caught.exception.status, 429)
            self.assertEqual(caught.exception.body["code"], "model_1_hourly_quota_exceeded")
            self.assertEqual(caught.exception.retry_after, "120")

    def test_async_submit_quota_and_encoded_poll(self):
        async def run():
            calls = []
            def handle(request):
                calls.append(request)
                if request.method == "POST": return httpx.Response(202, json={"generationId": "vg_mgen_test"})
                if request.url.path.endswith("/quota"): return httpx.Response(200, json=QUOTA)
                return httpx.Response(200, json={"generationId": "vg_mgen_test", "model": "model-1", "status": "queued", "seconds": 10, "createdAt": 1, "updatedAt": 1, "progressPercentage": None, "result": None, "error": None, "qualityWarnings": []})
            async with AsyncVideoGen(api_key="test", http_client=httpx.AsyncClient(transport=httpx.MockTransport(handle))) as client:
                self.assertEqual((await client.models.start_model1_generation(prompt="A product", idempotency_key="retry-async-key"))["generation_id"], "vg_mgen_test")
                self.assertEqual((await client.models.get_model1_quota())["remaining_seconds"], 590)
                self.assertIsNone((await client.models.get_model1_generation(generation_id="id/with?reserved"))["result"])
            self.assertEqual(calls[0].headers["Idempotency-Key"], "retry-async-key")
            self.assertIn(b"id%2Fwith%3Freserved", calls[2].url.raw_path)
        asyncio.run(run())
