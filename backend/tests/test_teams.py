# Team endpoints tests for Music Teams application
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


class TestTeamEndpoints(unittest.TestCase):
    """Test suite for team endpoints - assumes server is running."""

    def setUp(self):
        """Set up test environment following project guidelines."""
        print("Setting up test environment...")
        self.session = requests.Session()
        self.valid_credentials = {"username": "admin", "password": "admin"}
        self.test_team_name = f"test_team_{uuid.uuid4().hex[:8]}"
        self.created_teams = []  # Track teams created during test for cleanup
        self.logged_in = False
        
        # Log in for the test
        response = self.session.post(
            f"{BASE_URL}/simple_login/login",
            json=self.valid_credentials,
            timeout=5
        )
        if response.status_code != 200:
            raise Exception("Server login failed")
        self.logged_in = True
        print("✅ Successfully logged in for test")

    def tearDown(self):
        """Clean up test environment to leave database in same state."""
        print("Cleaning up test environment...")
        
        # Clean up any teams that were created during the test
        for team_name in self.created_teams:
            try:
                leave_response = self.session.get(
                    f"{BASE_URL}/teams/leave-team",
                    params={"team_name": team_name},
                    timeout=5
                )
                if leave_response.status_code == 200:
                    print(f"✅ Successfully left team: {team_name}")
                else:
                    print(f"⚠️ Could not leave team {team_name}: {leave_response.status_code}")
            except Exception as e:
                print(f"⚠️ Error leaving team {team_name}: {e}")
        
        # Logout to ensure session is clean
        if self.logged_in:
            try:
                logout_response = self.session.get(f"{BASE_URL}/home/logout", timeout=5)
                if logout_response.status_code == 200:
                    print("✅ Successfully logged out")
                else:
                    print(f"⚠️ Logout returned status: {logout_response.status_code}")
            except Exception as e:
                print(f"⚠️ Error during logout: {e}")
        
        self.session.close()
        print("✅ Test cleanup completed")

    def test_create_team(self):
        """Test: Create a team and track it for cleanup."""
        print("\n=== Testing team creation ===")
        
        response = self.session.get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": self.test_team_name},
            timeout=10
        )
        
        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["team_name"], self.test_team_name)
        self.assertIn("team_id", data)
        
        # Track created team for cleanup
        self.created_teams.append(self.test_team_name)
        print(f"✅ Team creation test passed - team tracked for cleanup")

    def test_get_teams(self):
        """Test: Get teams list after ensuring clean state."""
        print("\n=== Testing get teams ===")
        
        response = self.session.get(f"{BASE_URL}/teams/teams", timeout=10)
        
        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("teams", data)
        self.assertIsInstance(data["teams"], list)
        print(f"✅ Get teams test passed")
        
    def test_team_workflow(self):
        """Test: Complete team workflow (create -> details -> leave)."""
        print("\n=== Testing complete team workflow ===")
        
        # Step 1: Create team
        create_response = self.session.get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": self.test_team_name},
            timeout=10
        )
        
        self.assertEqual(create_response.status_code, 200)
        create_data = create_response.json()
        team_id = create_data["team_id"]
        
        # Track created team for cleanup
        self.created_teams.append(self.test_team_name)
        print(f"✅ Step 1: Team created with ID: {team_id}")
        
        # Step 2: Get team details
        details_response = self.session.get(
            f"{BASE_URL}/teams/team_details",
            params={"team_name": self.test_team_name},
            timeout=10
        )
        
        self.assertEqual(details_response.status_code, 200)
        details_data = details_response.json()
        self.assertEqual(details_data["team_name"], self.test_team_name)
        print(f"✅ Step 2: Team details retrieved successfully")
        
        # Step 3: Leave team (cleanup will also try this, but explicit test)
        leave_response = self.session.get(
            f"{BASE_URL}/teams/leave-team",
            params={"team_name": self.test_team_name},
            timeout=10
        )
        
        # Remove from cleanup list since we're leaving manually
        self.created_teams.remove(self.test_team_name)
        
        self.assertEqual(leave_response.status_code, 200)
        leave_data = leave_response.json()
        self.assertIn("message", leave_data)
        print(f"✅ Step 3: Successfully left team - workflow completed")
        print(f"✅ Complete team workflow test passed - database left in clean state")


if __name__ == "__main__":
    # Run the team endpoint tests assuming server is running
    unittest.main(verbosity=2)