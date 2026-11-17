import asyncio
import json
import unittest
import httpx
from videogen import AsyncVideoGen, VideoGen

PROJECT_ID = "vg_proj_0000000000000000000000"
EDIT_ID = "11111111-1111-4111-8111-111111111111"
UNDO_ID = "22222222-2222-4222-8222-222222222222"
RECEIPT = {"projectId": PROJECT_ID, "mutationId": UNDO_ID, "outcome": "APPLIED", "projectRevision": 3}

class UndoProjectEditTests(unittest.TestCase):
    def test_sync_accepts_snake_and_camel_new_mutation_id(self):
        calls = []
        def handle(request):
            calls.append(request)
            return httpx.Response(200, json=RECEIPT)
        with VideoGen(api_key="test", http_client=httpx.Client(transport=httpx.MockTransport(handle))) as client:
            client.projects.undo_project_edit(project_id=PROJECT_ID, mutation_id=EDIT_ID, new_mutation_id=UNDO_ID)
            client.projects.undo_project_edit(projectId=PROJECT_ID, mutationId=EDIT_ID, newMutationId=UNDO_ID)
        for call in calls:
            self.assertEqual(call.method, "POST")
            self.assertEqual(call.url.path, f"/v1/projects/{PROJECT_ID}/mutations/{EDIT_ID}/undo")
            self.assertEqual(json.loads(call.content), {"mutationId": UNDO_ID})

    def test_sync_rejects_missing_and_unexpected_arguments(self):
        def handle(request):
            raise AssertionError("no request expected")
        with VideoGen(api_key="test", http_client=httpx.Client(transport=httpx.MockTransport(handle))) as client:
            with self.assertRaisesRegex(TypeError, "missing required argument: new_mutation_id"):
                client.projects.undo_project_edit(project_id=PROJECT_ID, mutation_id=EDIT_ID)
            with self.assertRaisesRegex(TypeError, "missing required argument: mutation_id"):
                client.projects.undo_project_edit(project_id=PROJECT_ID, new_mutation_id=UNDO_ID)
            with self.assertRaisesRegex(TypeError, "unexpected argument"):
                client.projects.undo_project_edit(project_id=PROJECT_ID, mutation_id=EDIT_ID, new_mutation_id=UNDO_ID, reason="oops")

    def test_async_sends_new_mutation_id_as_body(self):
        async def run():
            calls = []
            def handle(request):
                calls.append(request)
                return httpx.Response(200, json=RECEIPT)
            async with AsyncVideoGen(api_key="test", http_client=httpx.AsyncClient(transport=httpx.MockTransport(handle))) as client:
                receipt = await client.projects.undo_project_edit(project_id=PROJECT_ID, mutation_id=EDIT_ID, newMutationId=UNDO_ID)
                self.assertEqual(receipt["outcome"], "APPLIED")
                with self.assertRaisesRegex(TypeError, "missing required argument: new_mutation_id"):
                    await client.projects.undo_project_edit(project_id=PROJECT_ID, mutation_id=EDIT_ID)
            self.assertEqual(len(calls), 1)
            self.assertEqual(json.loads(calls[0].content), {"mutationId": UNDO_ID})
        asyncio.run(run())
