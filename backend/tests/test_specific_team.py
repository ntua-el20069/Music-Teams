# Specific team endpoints tests for Music Teams application
#
# Implementation follows project guidelines:
# - Tests leave database in same state as before test (proper cleanup in tearDown)
# - Login in setUp and logout in tearDown
# - Uses API routes only, no direct database queries
# - Tracks created resources for proper cleanup
# - Uses unique test data to prevent conflicts

import unittest
import uuid

import requests
from dotenv import load_dotenv

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)

BASE_URL = "http://127.0.0.1:8000"
TEST_DEBUG = True


class TestSpecificTeamEndpoints(unittest.TestCase):
    """Test suite for specific team endpoints - assumes server is running."""

    def setUp(self):
        """Set up test environment following project guidelines."""
        print("Setting up test environment...")
        self.session = requests.Session()
        self.valid_credentials = {"username": "admin0", "password": "admin0"}

        self.logged_in = False
        self.teams_loaded = False
        self.test_team_name = f"test_team_{uuid.uuid4().hex[:8]}"
        self.created_teams = []

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

        # Create a test team for testing
        create_team_response = self.session.get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": self.test_team_name},
            timeout=10,
        )
        if create_team_response.status_code == 200:
            self.created_teams.append(self.test_team_name)
            print(f"✅ Test team '{self.test_team_name}' created successfully")
        else:
            print(
                f"❌ Team creation failed: {create_team_response.status_code} - "
                f"{create_team_response.text}"
            )
            self.fail("Setup failed: Could not create test team")

        # Load teams data (required for specific_team endpoints)
        teams_response = self.session.get(f"{BASE_URL}/teams/teams", timeout=10)
        if teams_response.status_code == 200:
            self.teams_loaded = True
            print("✅ Teams data loaded successfully")
        else:
            print(
                f"❌ Teams loading failed: {teams_response.status_code} - {teams_response.text}"
            )
            self.fail("Setup failed: Could not load teams data")

    def tearDown(self):
        """Clean up test environment following project guidelines."""
        print("Cleaning up test environment...")

        # Clean up created teams
        for team_name in self.created_teams:
            try:
                leave_response = self.session.get(
                    f"{BASE_URL}/teams/leave-team",
                    params={"team_name": team_name},
                    timeout=10,
                )
                if leave_response.status_code == 200:
                    print(f"✅ Successfully left team {team_name}")
                else:
                    print(
                        f"⚠️ Could not leave team {team_name}: {leave_response.status_code}"
                    )

            except Exception as e:
                print(f"⚠️ Error leaving team {team_name}: {e}")

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

    def test_get_specific_team_composers(self):
        """Test: Get all composers in a specific team."""
        print("\n=== Testing get specific team composers ===")

        response = self.session.get(
            f"{BASE_URL}/specific_team/all-composers",
            params={"team_name": self.test_team_name},
            timeout=10,
        )

        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")

        self.assertEqual(
            response.status_code,
            200,
            f"Get specific team composers failed: {response.status_code}",
        )

        data = response.json()
        self.assertIn("composers", data)
        self.assertIsInstance(data["composers"], list)
        print(
            f"✅ Retrieved {len(data['composers'])} composers from team {self.test_team_name}"
        )

    def test_get_specific_team_lyricists(self):
        """Test: Get all lyricists in a specific team."""
        print("\n=== Testing get specific team lyricists ===")

        response = self.session.get(
            f"{BASE_URL}/specific_team/all-lyricists",
            params={"team_name": self.test_team_name},
            timeout=10,
        )

        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")

        self.assertEqual(
            response.status_code,
            200,
            f"Get specific team lyricists failed: {response.status_code}",
        )

        data = response.json()
        self.assertIn("lyricists", data)
        self.assertIsInstance(data["lyricists"], list)
        print(
            f"✅ Retrieved {len(data['lyricists'])} lyricists from team {self.test_team_name}"
        )

    def test_get_specific_team_songs(self):
        """Test: Get all songs in a specific team."""
        print("\n=== Testing get specific team songs ===")

        response = self.session.get(
            f"{BASE_URL}/specific_team/all-songs",
            params={"team_name": self.test_team_name},
            timeout=10,
        )

        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")

        self.assertEqual(
            response.status_code,
            200,
            f"Get specific team songs failed: {response.status_code}",
        )

        data = response.json()
        self.assertIn("songs", data)
        self.assertIsInstance(data["songs"], list)
        print(
            f"✅ Retrieved {len(data['songs'])} songs from team {self.test_team_name}"
        )

    def test_non_enrolled_team_access(self):
        """Test: Verify endpoints reject access to teams user is not enrolled in."""
        print("\n=== Testing non-enrolled team access ===")

        fake_team_name = f"fake_team_{uuid.uuid4().hex[:8]}"

        endpoints = [
            "/specific_team/all-composers",
            "/specific_team/all-lyricists",
            "/specific_team/all-songs",
        ]

        for endpoint in endpoints:
            response = self.session.get(
                f"{BASE_URL}{endpoint}",
                params={"team_name": fake_team_name},
                timeout=10,
            )

            if TEST_DEBUG:
                print(f"Access to {endpoint} with fake team: {response.status_code}")

            self.assertEqual(
                response.status_code,
                404,
                (
                    f"Expected 404 for non-enrolled team access to {endpoint}, "
                    f"got {response.status_code}"
                ),
            )

        print("✅ All endpoints properly reject non-enrolled team access")

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
            "/specific_team/all-composers",
            "/specific_team/all-lyricists",
            "/specific_team/all-songs",
        ]

        for endpoint in endpoints:
            response = new_session.get(
                f"{BASE_URL}{endpoint}",
                params={"team_name": self.test_team_name},
                timeout=10,
            )

            if TEST_DEBUG:
                print(f"Access to {endpoint} without team_data: {response.status_code}")

            self.assertEqual(
                response.status_code,
                428,
                (
                    f"Expected 428 for missing team_data cookie on {endpoint}, "
                    f"got {response.status_code}"
                ),
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
            "/specific_team/all-composers",
            "/specific_team/all-lyricists",
            "/specific_team/all-songs",
        ]

        for endpoint in endpoints:
            response = new_session.get(
                f"{BASE_URL}{endpoint}",
                params={"team_name": self.test_team_name},
                timeout=10,
            )

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
