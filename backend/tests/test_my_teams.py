# My teams endpoints tests for Music Teams application
#
# Implementation follows project guidelines:
# - Tests leave database in same state as before test (proper cleanup in tearDown)
# - Login in setUp and logout in tearDown
# - Uses API routes only, no direct database queries
# - Tracks created resources for proper cleanup
# - Uses unique test data to prevent conflicts

import os
import unittest
import uuid

import requests
from dotenv import load_dotenv

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)

BASE_URL = "http://127.0.0.1:8000"
TEST_DEBUG = True


class TestMyTeamsEndpoints(unittest.TestCase):
    """Test suite for my teams endpoints - assumes server is running."""

    def setUp(self):
        """Set up test environment following project guidelines."""
        print("Setting up test environment...")
        self.session = requests.Session()
        self.valid_credentials = {"username": "admin0", "password": "admin0"}
        
        self.logged_in = False
        self.teams_loaded = False

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
            self.fail(f"Setup failed: Could not log in")

        # Load teams data (required for my_teams endpoints)
        teams_response = self.session.get(f"{BASE_URL}/teams/teams", timeout=10)
        if teams_response.status_code == 200:
            self.teams_loaded = True
            print("✅ Teams data loaded successfully")
        else:
            print(f"❌ Teams loading failed: {teams_response.status_code} - {teams_response.text}")
            self.fail(f"Setup failed: Could not load teams data")

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

    def test_get_my_teams_composers(self):
        """Test: Get all composers in user's teams."""
        print("\n=== Testing get my teams composers ===")

        response = self.session.get(f"{BASE_URL}/my_teams/all-composers", timeout=10)

        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")

        self.assertEqual(
            response.status_code,
            200,
            f"Get my teams composers failed: {response.status_code}",
        )

        data = response.json()
        self.assertIn("composers", data)
        self.assertIsInstance(data["composers"], list)
        print(f"✅ Retrieved {len(data['composers'])} composers from user's teams")

    def test_get_my_teams_lyricists(self):
        """Test: Get all lyricists in user's teams."""
        print("\n=== Testing get my teams lyricists ===")

        response = self.session.get(f"{BASE_URL}/my_teams/all-lyricists", timeout=10)

        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")

        self.assertEqual(
            response.status_code,
            200,
            f"Get my teams lyricists failed: {response.status_code}",
        )

        data = response.json()
        self.assertIn("lyricists", data)
        self.assertIsInstance(data["lyricists"], list)
        print(f"✅ Retrieved {len(data['lyricists'])} lyricists from user's teams")

    def test_get_my_teams_songs(self):
        """Test: Get all songs in user's teams."""
        print("\n=== Testing get my teams songs ===")

        response = self.session.get(f"{BASE_URL}/my_teams/all-songs", timeout=10)

        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")

        self.assertEqual(
            response.status_code,
            200,
            f"Get my teams songs failed: {response.status_code}",
        )

        data = response.json()
        self.assertIn("songs", data)
        self.assertIsInstance(data["songs"], list)
        print(f"✅ Retrieved {len(data['songs'])} songs from user's teams")

    def test_missing_team_data_cookie(self):
        """Test: Verify endpoints require team_data cookie."""
        print("\n=== Testing missing team_data cookie ===")

        # Create a new session without teams data
        new_session = requests.Session()
        
        # Log in but don't load teams
        login_response = new_session.post(
            f"{BASE_URL}/simple_login/login",
            json=self.valid_credentials,
            allow_redirects=True,
        )
        self.assertEqual(login_response.status_code, 200)

        # Try to access endpoints without team_data cookie
        endpoints = [
            "/my_teams/all-composers",
            "/my_teams/all-lyricists", 
            "/my_teams/all-songs"
        ]

        for endpoint in endpoints:
            response = new_session.get(f"{BASE_URL}{endpoint}", timeout=10)
            
            if TEST_DEBUG:
                print(f"Access to {endpoint} without team_data: {response.status_code}")
            
            self.assertEqual(
                response.status_code,
                428,
                f"Expected 428 for missing team_data cookie on {endpoint}, got {response.status_code}",
            )

        # Cleanup
        new_session.get(f"{BASE_URL}/home/logout", allow_redirects=False)
        new_session.close()
        print("✅ All endpoints properly require team_data cookie")

    def test_unauthorized_access(self):
        """Test: Verify endpoints require authentication."""
        print("\n=== Testing unauthorized access ===")

        # Create a new session without login
        new_session = requests.Session()

        # Try to access endpoints without authentication
        endpoints = [
            "/my_teams/all-composers",
            "/my_teams/all-lyricists", 
            "/my_teams/all-songs"
        ]

        for endpoint in endpoints:
            response = new_session.get(f"{BASE_URL}{endpoint}", timeout=10)
            
            if TEST_DEBUG:
                print(f"Unauthorized access to {endpoint}: {response.status_code}")
            
            self.assertEqual(
                response.status_code,
                401,
                f"Expected 401 for unauthorized access to {endpoint}, got {response.status_code}",
            )

        new_session.close()
        print("✅ All endpoints properly require authentication")


if __name__ == "__main__":
    unittest.main()