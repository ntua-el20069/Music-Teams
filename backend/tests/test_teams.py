# Team endpoints tests for Music Teams application
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
NUM_USERS = 2  # Number of admin users to create for testing


class TestTeamEndpoints(unittest.TestCase):
    """Test suite for team endpoints - assumes server is running."""

    def setUp(self):
        """Set up test environment following project guidelines."""
        print("Setting up test environment...")
        self.sessions = [requests.Session() for _ in range(NUM_USERS)]
        self.valid_credentials = [
            {"username": f"admin{i}", "password": f"admin{i}"} for i in range(NUM_USERS)
        ]

        self.test_team_name = f"test_team_{uuid.uuid4().hex[:8]}"
        self.created_teams = []  # Track teams created during test for cleanup
        self.logged_in = [False] * NUM_USERS

        # Log in for the test
        for i, session in enumerate(self.sessions):
            response = session.post(
                f"{BASE_URL}/simple_login/login",
                json=self.valid_credentials[i],
                allow_redirects=True,
            )
            if response.status_code == 200:
                self.logged_in[i] = True
                print(f"✅ Successfully logged in for user {i}")
            else:
                raise Exception(
                    f"Failed to log in for user {i}: {response.status_code}"
                )

    def tearDown(self):
        """Clean up test environment to leave database in same state."""
        print("Cleaning up test environment...")

        # Clean up any teams that were created during the test and logout users

        # for each user
        for i, session in enumerate(self.sessions):
            if not self.logged_in[i]:
                continue
            # Leave teams in which this user is enrolled
            for team_name in self.created_teams:
                try:
                    leave_response = session.get(
                        f"{BASE_URL}/teams/leave-team",
                        params={"team_name": team_name},
                        timeout=5,
                    )
                    if leave_response.status_code == 200:
                        print(f"✅ Successfully left team: {team_name}")
                    elif leave_response.status_code == 404:
                        print(
                            f"⚠️ Team {team_name} not found for user {i}, \
                              might have been deleted already or user left it."
                        )
                    else:
                        print(
                            f"⚠️ Could not leave team {team_name}: {leave_response.status_code}"
                        )
                        raise Exception(
                            f"Failed to leave team {team_name} for user {i}: \
                                {leave_response.status_code}"
                        )

                except Exception as e:
                    print(f"⚠️ Error leaving team {team_name}: {e}")
                    raise e

            # Log out user
            logout_response = session.get(
                f"{BASE_URL}/home/logout", timeout=5, allow_redirects=False
            )

            if TEST_DEBUG:
                print(
                    f"Logout response for user {i}: \
                        {logout_response.status_code} - {logout_response.text}"
                )

            self.assertEqual(
                logout_response.status_code,
                303,
                f"Logout failed for user {i}: {logout_response.status_code}",
            )
            self.logged_in[i] = False
            print(f"✅ User {i} logged out successfully")

        for session in self.sessions:
            session.close()
        print("✅ Test cleanup completed")

    def test_create_team(self):
        """Test: Create a team and track it for cleanup."""
        print("\n=== Testing team creation ===")

        response = self.sessions[0].get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": self.test_team_name},
            timeout=10,
        )
        # Track created team for cleanup
        self.created_teams.append(self.test_team_name)

        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["team_name"], self.test_team_name)
        self.assertIn("team_id", data)

        print("✅ Team creation test passed - team tracked for cleanup")

    def test_create_team_exceeding_participation_threshold(self):
        """Test: Attempt to create a team exceeding participation threshold. (code 403 forbidden)"""
        print("\n=== Testing team creation exceeding participation threshold ===")

        # Create multiple teams to exceed the threshold
        # TODO: identify why workflows do not get env variable
        # set it same as in .env file until fixed
        max_teams = int(os.getenv("MAX_TEAMS_TO_PARTICIPATE", "2"))
        print(f"Max teams allowed per user: {max_teams}")
        for i in range(max_teams + 1):
            team_name = f"test_team_exceed_{i}_{uuid.uuid4().hex[:8]}"
            response = self.sessions[0].get(
                f"{BASE_URL}/teams/create-team",
                params={"team_name": team_name},
                timeout=10,
            )
            self.created_teams.append(team_name)

            if TEST_DEBUG:
                print(f"Response: {response.status_code} - {response.text}")

            if i == max_teams:
                self.assertEqual(response.status_code, 412)
            else:
                self.assertEqual(response.status_code, 200)

    def test_create_team_already_exists(self):
        """Test: Attempt to create a team that already exists. (code 409 conflict)"""
        print("\n=== Testing team creation with existing team ===")

        # First create the team
        create_response = self.sessions[0].get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": self.test_team_name},
            timeout=10,
        )
        # Track created team for cleanup
        self.created_teams.append(self.test_team_name)

        self.assertEqual(create_response.status_code, 200)

        # Now try to create it again (team name conflict)
        response = self.sessions[0].get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": self.test_team_name},
            timeout=10,
        )

        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")

        self.assertEqual(response.status_code, 409)
        data = response.json()
        self.assertIn("detail", data)
        self.assertEqual(data["detail"], "There exists another team with the same name")
        print("✅ Team creation with existing team test passed")

    def test_get_teams(self):
        """Test: Get teams list after ensuring clean state."""
        print("\n=== Testing get teams ===")

        response = self.sessions[0].get(f"{BASE_URL}/teams/teams", timeout=10)

        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("teams", data)
        self.assertIsInstance(data["teams"], list)
        print("✅ Get teams test passed")

    def test_leave_team_not_enrolled(self):
        """Test: Attempt to leave a team when not enrolled. (code 404 not found)"""
        print("\n=== Testing leave team when not enrolled ===")

        response = self.sessions[0].get(
            f"{BASE_URL}/teams/leave-team",
            params={"team_name": "non_existent_team"},
            timeout=10,
        )

        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")

        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertIn("detail", data)
        self.assertIn("User is not a member of team", data["detail"])
        print("✅ Leave team not enrolled test passed")

    def test_enter_team(self):
        """Test: Enter a team and check if user can participate."""
        print("\n=== Testing enter team ===")

        # First create the team
        create_response = self.sessions[0].get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": self.test_team_name},
            timeout=10,
        )
        # track created team for cleanup
        self.created_teams.append(self.test_team_name)

        self.assertEqual(create_response.status_code, 200)

        data = create_response.json()
        team_code = data["team_id"]

        # Now try to enter the team
        response = self.sessions[1].post(
            f"{BASE_URL}/teams/enter-team", json={"team_code": team_code}, timeout=10
        )

        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")

        self.assertEqual(response.status_code, 200)
        data = response.json()
        print("✅ Enter team test passed")

    def test_enter_team_invalid_code(self):
        """Test: Attempt to enter a team with an invalid code. (code 404 not found)"""
        print("\n=== Testing enter team with invalid code ===")

        response = self.sessions[1].post(
            f"{BASE_URL}/teams/enter-team",
            json={"team_code": "invalid_code"},
            timeout=10,
        )

        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")

        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertIn("detail", data)
        self.assertIn("Not found team with code", data["detail"])
        print("✅ Enter team with invalid code test passed")

    def test_team_workflow(self):
        """Test: Complete team workflow (create -> teams -> details -> leave)."""
        print("\n=== Testing complete team workflow ===")

        # Step 0: Create team
        create_response = self.sessions[0].get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": self.test_team_name},
            timeout=10,
        )
        # Track created team for cleanup
        self.created_teams.append(self.test_team_name)

        self.assertEqual(create_response.status_code, 200)
        # create_data = create_response.json()
        # team_id = create_data["team_id"]

        print("✅ Step 0: Team created with ID: {team_id}")

        # Step 1: Get teams list
        teams_response = self.sessions[0].get(f"{BASE_URL}/teams/teams", timeout=10)
        self.assertEqual(teams_response.status_code, 200)
        teams_data = teams_response.json()
        self.assertIn("teams", teams_data)
        self.assertIsInstance(teams_data["teams"], list)
        self.assertIn("team_data", self.sessions[0].cookies.get_dict())
        print("✅ Step 1: Teams list retrieved successfully")

        # Step 2: Get team details
        details_response = self.sessions[0].get(
            f"{BASE_URL}/teams/team_details",
            params={"team_name": self.test_team_name},
            timeout=10,
        )

        self.assertEqual(details_response.status_code, 200)
        details_data = details_response.json()
        self.assertEqual(details_data["team_name"], self.test_team_name)
        print("✅ Step 2: Team details retrieved successfully")

        # Step 3: Leave team (cleanup will also try this, but explicit test)
        leave_response = self.sessions[0].get(
            f"{BASE_URL}/teams/leave-team",
            params={"team_name": self.test_team_name},
            timeout=10,
        )

        # Remove from cleanup list since we're leaving manually
        self.created_teams.remove(self.test_team_name)

        self.assertEqual(leave_response.status_code, 200)
        leave_data = leave_response.json()
        self.assertIn("message", leave_data)
        print("✅ Step 3: Successfully left team - workflow completed")
        print("✅ Complete team workflow test passed - database left in clean state")

    def test_team_details_without_cookie(self):
        """Test: Attempt to get team details without team cookie. (code 403 forbidden)"""
        print("\n=== Testing team details without cookie ===")

        response = self.sessions[0].get(
            f"{BASE_URL}/teams/team_details",
            params={"team_name": self.test_team_name},
            timeout=10,
        )

        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")

        self.assertEqual(response.status_code, 428)
        data = response.json()
        self.assertIn("detail", data)
        print("✅ Team details without cookie test passed")

    def test_team_details_with_invalid_team_name(self):
        """Test: Attempt to get team details with an invalid team name. (code 404 not found)"""
        print("\n=== Testing team details with invalid team name ===")

        # create team1
        response = self.sessions[0].get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": "team1"},
        )
        self.created_teams.append("team1")

        self.assertEqual(response.status_code, 200)

        # create team2
        response = self.sessions[1].get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": "team2"},
        )
        self.created_teams.append("team2")

        self.assertEqual(response.status_code, 200)

        # visit /teams/teams
        response = self.sessions[0].get(f"{BASE_URL}/teams/teams")
        self.assertEqual(response.status_code, 200)

        # Now try to get details of a non-existent team
        response = self.sessions[0].get(
            f"{BASE_URL}/teams/team_details",
            params={
                "team_name": "team2"
            },  # This team exists, but the user is not enrolled
            timeout=10,
        )

        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")

        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertIn("detail", data)
        self.assertIn(
            "does not exist or you are not registered in this team", data["detail"]
        )
        print("✅ Team details with invalid team name test passed")
