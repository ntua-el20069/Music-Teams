# Public endpoints tests for Music Teams application
#
# Implementation follows project guidelines:
# - Tests leave database in same state as before test (proper cleanup in tearDown)
# - Login in setUp and logout in tearDown
# - Uses API routes only, no direct database queries
# - Tracks created resources for proper cleanup
# - Uses unique test data to prevent conflicts

import unittest

import requests
from dotenv import load_dotenv

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)

BASE_URL = "http://127.0.0.1:8000"
TEST_DEBUG = True


class TestPublicEndpoints(unittest.TestCase):
    """Test suite for public endpoints - assumes server is running."""

    def setUp(self):
        """Set up test environment following project guidelines."""
        print("Setting up test environment...")
        self.session = requests.Session()
        self.valid_credentials = {"username": "admin0", "password": "admin0"}

        self.logged_in = False

        # Log in for the test
        response = self.session.post(
            f"{BASE_URL}/simple_login/login",
            json=self.valid_credentials,
            allow_redirects=True,
        )
        if response.status_code == 200:
            self.logged_in = True
            print("✅ Successfully logged in")
        else:
            print(f"❌ Login failed: {response.status_code} - {response.text}")
            self.fail("Setup failed: Could not log in")

    def tearDown(self):
        """Clean up test environment following project guidelines."""
        print("Cleaning up test environment...")

        if self.logged_in:
            # Log out user
            logout_response = self.session.get(
                f"{BASE_URL}/home/logout", timeout=5, allow_redirects=False
            )

            if TEST_DEBUG:
                print(
                    f"Logout response: {logout_response.status_code} - {logout_response.text}"
                )

            self.assertEqual(
                logout_response.status_code,
                303,
                f"Logout failed: {logout_response.status_code}",
            )
            self.logged_in = False
            print("✅ User logged out successfully")

        self.session.close()
        print("✅ Test cleanup completed")

    def test_get_public_composers(self):
        """Test: Get all composers in public songs."""
        print("\n=== Testing get public composers ===")

        response = self.session.get(f"{BASE_URL}/public/all-composers", timeout=10)

        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")

        self.assertEqual(
            response.status_code,
            200,
            f"Get public composers failed: {response.status_code}",
        )

        data = response.json()
        self.assertIn("composers", data)
        self.assertIsInstance(data["composers"], list)
        print(f"✅ Retrieved {len(data['composers'])} public composers")

    def test_get_public_lyricists(self):
        """Test: Get all lyricists in public songs."""
        print("\n=== Testing get public lyricists ===")

        response = self.session.get(f"{BASE_URL}/public/all-lyricists", timeout=10)

        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")

        self.assertEqual(
            response.status_code,
            200,
            f"Get public lyricists failed: {response.status_code}",
        )

        data = response.json()
        self.assertIn("lyricists", data)
        self.assertIsInstance(data["lyricists"], list)
        print(f"✅ Retrieved {len(data['lyricists'])} public lyricists")

    def test_get_public_songs(self):
        """Test: Get all public songs."""
        print("\n=== Testing get public songs ===")

        response = self.session.get(f"{BASE_URL}/public/all-songs", timeout=10)

        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")

        self.assertEqual(
            response.status_code,
            200,
            f"Get public songs failed: {response.status_code}",
        )

        data = response.json()
        self.assertIn("songs", data)
        self.assertIsInstance(data["songs"], list)
        print(f"✅ Retrieved {len(data['songs'])} public songs")

    def test_unauthorized_access(self):
        """Test: Verify endpoints require authentication."""
        print("\n=== Testing unauthorized access ===")

        # Log out first
        self.session.get(f"{BASE_URL}/home/logout", allow_redirects=False)
        self.logged_in = False

        # Try to access endpoints without authentication
        endpoints = [
            "/public/all-composers",
            "/public/all-lyricists",
            "/public/all-songs",
        ]

        for endpoint in endpoints:
            response = self.session.get(f"{BASE_URL}{endpoint}", timeout=10)

            if TEST_DEBUG:
                print(f"Unauthorized access to {endpoint}: {response.status_code}")

            self.assertEqual(
                response.status_code,
                401,
                f"Expected 401 for unauthorized access to {endpoint}, got {response.status_code}",
            )

        print("✅ All endpoints properly require authentication")


if __name__ == "__main__":
    unittest.main()
