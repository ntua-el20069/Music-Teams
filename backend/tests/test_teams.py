# import os
import unittest
import uuid
from typing import Any, Dict

import requests
from dotenv import load_dotenv

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)

# BASE_URL = (
#     "http://fastapi-app:8000/login"
#     if str(os.getenv("MODE")) == "CONTAINER"
#     else "http://localhost:8000/login"
# )
BASE_URL = "http://127.0.0.1:8000"  # Adjust for your local setup
TEST_DEBUG = True


class TestTeamEndpoints(unittest.TestCase):
    def setUp(self):
        """Set up test environment and authenticate with admin credentials."""
        print("Setting up the test environment...")
        self.session = requests.Session()
        self.valid_credentials = {"username": "admin", "password": "admin"}
        
        # Generate unique team names for testing
        self.test_team_name = f"test_team_{uuid.uuid4().hex[:8]}"
        self.test_team_name_2 = f"test_team_2_{uuid.uuid4().hex[:8]}"
        self.team_code = None  # Will be populated during tests

        # Log in to get a session
        response = self.session.post(
            f"{BASE_URL}/simple_login/login",
            json=self.valid_credentials,
            allow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        if TEST_DEBUG:
            print(f"Login successful: {response.status_code}")

    def tearDown(self):
        """Clean up test environment and logout."""
        # Try to leave any teams created during testing
        self._cleanup_teams()
        
        # logout
        logout_response = self.session.get(
            f"{BASE_URL}/home/logout",
            allow_redirects=False,
        )
        if TEST_DEBUG:
            print(f"Logout response: {logout_response.status_code}")

        # Expect a redirect to the frontend URL
        self.assertEqual(logout_response.status_code, 303)

        print("Tearing down the test environment...")
        self.session.close()

    def _cleanup_teams(self):
        """Helper method to clean up teams created during testing."""
        try:
            # Try to leave test teams
            for team_name in [self.test_team_name, self.test_team_name_2]:
                try:
                    self.session.get(
                        f"{BASE_URL}/teams/leave-team",
                        params={"team_name": team_name},
                        allow_redirects=False,
                    )
                except:
                    pass  # Ignore cleanup errors
        except:
            pass  # Ignore cleanup errors

    def test_create_team_success(self):
        """Test successful team creation."""
        print("\n=== Testing team creation ===")
        
        # Create a new team
        response = self.session.get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": self.test_team_name},
            allow_redirects=False,
        )
        
        if TEST_DEBUG:
            print(f"Create team response: {response.status_code}")
            print(f"Create team response body: {response.text}")
        
        self.assertEqual(response.status_code, 200)
        
        response_data = response.json()
        self.assertIn("team_name", response_data)
        self.assertIn("team_id", response_data)
        self.assertEqual(response_data["team_name"], self.test_team_name)
        
        # Store team_id for later use
        self.team_code = response_data["team_id"]
        
        print(f"Team created successfully: {self.test_team_name} with code {self.team_code}")

    def test_create_team_duplicate_name(self):
        """Test team creation with duplicate name should fail."""
        print("\n=== Testing duplicate team creation ===")
        
        # First, create a team
        response1 = self.session.get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": self.test_team_name},
            allow_redirects=False,
        )
        
        self.assertEqual(response1.status_code, 200)
        
        # Try to create another team with the same name
        response2 = self.session.get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": self.test_team_name},
            allow_redirects=False,
        )
        
        if TEST_DEBUG:
            print(f"Duplicate team creation response: {response2.status_code}")
            print(f"Duplicate team creation body: {response2.text}")
        
        # Should return 409 Conflict
        self.assertEqual(response2.status_code, 409)
        
        response_data = response2.json()
        self.assertIn("detail", response_data)
        self.assertIn("same name", response_data["detail"])

    def test_get_teams_empty(self):
        """Test getting teams when user has no teams."""
        print("\n=== Testing get teams (empty) ===")
        
        response = self.session.get(
            f"{BASE_URL}/teams/teams",
            allow_redirects=False,
        )
        
        if TEST_DEBUG:
            print(f"Get teams response: {response.status_code}")
            print(f"Get teams response body: {response.text}")
        
        self.assertEqual(response.status_code, 200)
        
        response_data = response.json()
        self.assertIn("teams", response_data)
        # Teams list might be empty or contain some teams
        self.assertIsInstance(response_data["teams"], list)

    def test_get_teams_with_teams(self):
        """Test getting teams after creating teams."""
        print("\n=== Testing get teams (with teams) ===")
        
        # First create a team
        create_response = self.session.get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": self.test_team_name},
            allow_redirects=False,
        )
        self.assertEqual(create_response.status_code, 200)
        
        # Get teams
        response = self.session.get(
            f"{BASE_URL}/teams/teams",
            allow_redirects=False,
        )
        
        if TEST_DEBUG:
            print(f"Get teams response: {response.status_code}")
            print(f"Get teams response body: {response.text}")
        
        self.assertEqual(response.status_code, 200)
        
        response_data = response.json()
        self.assertIn("teams", response_data)
        self.assertIsInstance(response_data["teams"], list)
        
        # Check if our created team is in the list
        team_names = [team["team_name"] for team in response_data["teams"]]
        self.assertIn(self.test_team_name, team_names)

    def test_enter_team_success(self):
        """Test successfully entering a team with a valid code."""
        print("\n=== Testing enter team ===")
        
        # First create a team to get a valid team code
        create_response = self.session.get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": self.test_team_name},
            allow_redirects=False,
        )
        self.assertEqual(create_response.status_code, 200)
        
        team_data = create_response.json()
        team_code = team_data["team_id"]
        
        # Leave the team first to test entering it
        leave_response = self.session.get(
            f"{BASE_URL}/teams/leave-team",
            params={"team_name": self.test_team_name},
            allow_redirects=False,
        )
        # May or may not be successful depending on state
        
        # Now try to enter the team using the code
        enter_response = self.session.post(
            f"{BASE_URL}/teams/enter-team",
            json={"team_code": team_code},
            allow_redirects=False,
        )
        
        if TEST_DEBUG:
            print(f"Enter team response: {enter_response.status_code}")
            print(f"Enter team response body: {enter_response.text}")
        
        self.assertEqual(enter_response.status_code, 200)
        
        response_data = enter_response.json()
        self.assertIn("message", response_data)

    def test_enter_team_invalid_code(self):
        """Test entering a team with an invalid code should fail."""
        print("\n=== Testing enter team with invalid code ===")
        
        # Try to enter a team with a non-existent code
        invalid_code = "invalid_team_code_12345"
        
        response = self.session.post(
            f"{BASE_URL}/teams/enter-team",
            json={"team_code": invalid_code},
            allow_redirects=False,
        )
        
        if TEST_DEBUG:
            print(f"Enter invalid team response: {response.status_code}")
            print(f"Enter invalid team response body: {response.text}")
        
        # Should return 404 Not Found
        self.assertEqual(response.status_code, 404)
        
        response_data = response.json()
        self.assertIn("detail", response_data)
        self.assertIn("Not found team with code", response_data["detail"])

    def test_team_details_success(self):
        """Test getting team details for an existing team."""
        print("\n=== Testing get team details ===")
        
        # First create a team
        create_response = self.session.get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": self.test_team_name},
            allow_redirects=False,
        )
        self.assertEqual(create_response.status_code, 200)
        
        # Get teams to set the team_data cookie
        teams_response = self.session.get(
            f"{BASE_URL}/teams/teams",
            allow_redirects=False,
        )
        self.assertEqual(teams_response.status_code, 200)
        
        # Get team details
        response = self.session.get(
            f"{BASE_URL}/teams/team_details",
            params={"team_name": self.test_team_name},
            allow_redirects=False,
        )
        
        if TEST_DEBUG:
            print(f"Team details response: {response.status_code}")
            print(f"Team details response body: {response.text}")
        
        self.assertEqual(response.status_code, 200)
        
        response_data = response.json()
        self.assertIn("team_name", response_data)
        self.assertIn("team_id", response_data)
        self.assertEqual(response_data["team_name"], self.test_team_name)

    def test_team_details_not_found(self):
        """Test getting team details for a non-existent team."""
        print("\n=== Testing get team details for non-existent team ===")
        
        # Get teams to set the team_data cookie
        teams_response = self.session.get(
            f"{BASE_URL}/teams/teams",
            allow_redirects=False,
        )
        # Don't assert status here as we may not have teams
        
        # Try to get details for a non-existent team
        non_existent_team = "non_existent_team_12345"
        
        response = self.session.get(
            f"{BASE_URL}/teams/team_details",
            params={"team_name": non_existent_team},
            allow_redirects=False,
        )
        
        if TEST_DEBUG:
            print(f"Non-existent team details response: {response.status_code}")
            print(f"Non-existent team details response body: {response.text}")
        
        # Should return 404 Not Found or 428 if no team token
        self.assertIn(response.status_code, [404, 428])

    def test_leave_team_success(self):
        """Test successfully leaving a team."""
        print("\n=== Testing leave team ===")
        
        # First create a team
        create_response = self.session.get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": self.test_team_name},
            allow_redirects=False,
        )
        self.assertEqual(create_response.status_code, 200)
        
        # Now leave the team
        response = self.session.get(
            f"{BASE_URL}/teams/leave-team",
            params={"team_name": self.test_team_name},
            allow_redirects=False,
        )
        
        if TEST_DEBUG:
            print(f"Leave team response: {response.status_code}")
            print(f"Leave team response body: {response.text}")
        
        self.assertEqual(response.status_code, 200)
        
        response_data = response.json()
        self.assertIn("message", response_data)

    def test_leave_team_not_member(self):
        """Test leaving a team that the user is not a member of."""
        print("\n=== Testing leave team (not a member) ===")
        
        # Try to leave a team we're not a member of
        non_member_team = "non_member_team_12345"
        
        response = self.session.get(
            f"{BASE_URL}/teams/leave-team",
            params={"team_name": non_member_team},
            allow_redirects=False,
        )
        
        if TEST_DEBUG:
            print(f"Leave non-member team response: {response.status_code}")
            print(f"Leave non-member team response body: {response.text}")
        
        # Should return 404 Not Found
        self.assertEqual(response.status_code, 404)
        
        response_data = response.json()
        self.assertIn("detail", response_data)

    def test_team_workflow_complete(self):
        """Test a complete workflow: create team, get teams, get details, leave team."""
        print("\n=== Testing complete team workflow ===")
        
        # 1. Create team
        create_response = self.session.get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": self.test_team_name},
            allow_redirects=False,
        )
        self.assertEqual(create_response.status_code, 200)
        create_data = create_response.json()
        team_code = create_data["team_id"]
        
        # 2. Get teams
        teams_response = self.session.get(
            f"{BASE_URL}/teams/teams",
            allow_redirects=False,
        )
        self.assertEqual(teams_response.status_code, 200)
        teams_data = teams_response.json()
        team_names = [team["team_name"] for team in teams_data["teams"]]
        self.assertIn(self.test_team_name, team_names)
        
        # 3. Get team details
        details_response = self.session.get(
            f"{BASE_URL}/teams/team_details",
            params={"team_name": self.test_team_name},
            allow_redirects=False,
        )
        self.assertEqual(details_response.status_code, 200)
        details_data = details_response.json()
        self.assertEqual(details_data["team_name"], self.test_team_name)
        self.assertEqual(details_data["team_id"], team_code)
        
        # 4. Leave team
        leave_response = self.session.get(
            f"{BASE_URL}/teams/leave-team",
            params={"team_name": self.test_team_name},
            allow_redirects=False,
        )
        self.assertEqual(leave_response.status_code, 200)
        
        # 5. Verify team is no longer in user's teams
        final_teams_response = self.session.get(
            f"{BASE_URL}/teams/teams",
            allow_redirects=False,
        )
        self.assertEqual(final_teams_response.status_code, 200)
        final_teams_data = final_teams_response.json()
        final_team_names = [team["team_name"] for team in final_teams_data["teams"]]
        self.assertNotIn(self.test_team_name, final_team_names)
        
        print("Complete workflow test passed!")


if __name__ == "__main__":
    unittest.main()