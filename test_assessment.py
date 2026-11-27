import importlib.util
import os
import sys
import unittest
from pathlib import Path

os.environ.setdefault(
    "FLASK_SECRET_KEY",
    "local-idor-assessment-test-secret"
)

ROOT = Path(__file__).parent


def load_app(module_name, file_path):
    spec = importlib.util.spec_from_file_location(
        module_name, ROOT / file_path
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module.app


VULNERABLE_APP = load_app(
    "vulnerable_app",
    "vulnerable-demo/app.py"
)

REMEDIATED_APP = load_app(
    "remediated_app",
    "remediated-demo/app.py"
)


class VulnerableApplicationTests(unittest.TestCase):

    def setUp(self):
        self.client = VULNERABLE_APP.test_client()

    def login(self, user_id):
        response = self.client.get(
            f"/login/{user_id}",
            follow_redirects=False
        )
        self.assertEqual(response.status_code, 302)

    def test_unauthenticated_access_is_denied(self):
        response = self.client.get("/profile/1")
        self.assertEqual(response.status_code, 401)

    def test_alice_can_access_her_own_profile(self):
        self.login(1)
        response = self.client.get("/profile/1")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"alice@example.test", response.data)

    def test_alice_can_access_bobs_profile_vulnerability(self):
        self.login(1)
        response = self.client.get("/profile/2")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"bob@example.test", response.data)

    def test_bob_can_access_alices_profile_vulnerability(self):
        self.login(2)
        response = self.client.get("/profile/1")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"alice@example.test", response.data)


class RemediatedApplicationTests(unittest.TestCase):

    def setUp(self):
        self.client = REMEDIATED_APP.test_client()

    def login(self, user_id):
        response = self.client.get(
            f"/login/{user_id}",
            follow_redirects=False
        )
        self.assertEqual(response.status_code, 302)

    def test_unauthenticated_access_is_denied(self):
        response = self.client.get("/profile/1")
        self.assertEqual(response.status_code, 401)

    def test_alice_can_access_her_own_profile(self):
        self.login(1)
        response = self.client.get("/profile/1")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"alice@example.test", response.data)

    def test_alice_cannot_access_bobs_profile(self):
        self.login(1)
        response = self.client.get("/profile/2")

        self.assertEqual(response.status_code, 403)
        self.assertNotIn(b"bob@example.test", response.data)

    def test_bob_can_access_his_own_profile(self):
        self.login(2)
        response = self.client.get("/profile/2")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"bob@example.test", response.data)

    def test_bob_cannot_access_alices_profile(self):
        self.login(2)
        response = self.client.get("/profile/1")

        self.assertEqual(response.status_code, 403)
        self.assertNotIn(b"alice@example.test", response.data)

    def test_alice_cannot_access_invalid_profile_id(self):
        self.login(1)
        response = self.client.get("/profile/999")

        self.assertEqual(response.status_code, 403)


if __name__ == "__main__":
    unittest.main(verbosity=2)
