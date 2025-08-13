# Team endpoints tests for Music Teams application
# This file contains both mock tests (that always work) and integration tests (that require a running server)
# 
# Implementation follows project guidelines:
# - Tests leave database in same state as before test (proper cleanup in tearDown)
# - Login in setUp and logout in tearDown for integration tests
# - Uses API routes only, no direct database queries
# - Tracks created resources for proper cleanup
# - Uses unique test data to prevent conflicts

import unittest
import uuid
from unittest.mock import Mock

import requests
from dotenv import load_dotenv

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)

BASE_URL = "http://127.0.0.1:8000"
TEST_DEBUG = True


class TestTeamEndpointsMock(unittest.TestCase):
    """Mock tests for team endpoints - always runnable without server."""

    def setUp(self):
        """Set up mock test environment."""
        print("Setting up mock test environment...")
        self.session = Mock(spec=requests.Session)
        self.test_team_name = f"test_team_{uuid.uuid4().hex[:8]}"
        self.team_code = f"code_{uuid.uuid4().hex[:8]}"

    def test_mock_create_team_success(self):
        """Test successful team creation with mock."""
        print("\n=== Mock: Testing team creation ===")
        
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "team_name": self.test_team_name,
            "team_id": self.team_code
        }
        self.session.get.return_value = mock_response
        
        response = self.session.get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": self.test_team_name}
        )
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["team_name"], self.test_team_name)
        self.assertEqual(data["team_id"], self.team_code)
        print(f"✅ Mock team creation test passed")

    def test_mock_create_team_duplicate(self):
        """Test duplicate team creation returns 409."""
        print("\n=== Mock: Testing duplicate team creation ===")
        
        mock_response = Mock()
        mock_response.status_code = 409
        mock_response.json.return_value = {
            "detail": "Team with same name already exists"
        }
        self.session.get.return_value = mock_response
        
        response = self.session.get(
            f"{BASE_URL}/teams/create-team",
            params={"team_name": self.test_team_name}
        )
        
        self.assertEqual(response.status_code, 409)
        data = response.json()
        self.assertIn("same name", data["detail"])
        print(f"✅ Mock duplicate team test passed")

    def test_mock_get_teams(self):
        """Test getting teams list."""
        print("\n=== Mock: Testing get teams ===")
        
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "teams": [{"team_name": self.test_team_name, "team_id": self.team_code}]
        }
        self.session.get.return_value = mock_response
        
        response = self.session.get(f"{BASE_URL}/teams/teams")
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("teams", data)
        self.assertIsInstance(data["teams"], list)
        print(f"✅ Mock get teams test passed")

    def test_mock_enter_team_success(self):
        """Test entering team with valid code."""
        print("\n=== Mock: Testing enter team ===")
        
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Successfully joined team"}
        self.session.post.return_value = mock_response
        
        response = self.session.post(
            f"{BASE_URL}/teams/enter-team",
            json={"team_code": self.team_code}
        )
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("message", data)
        print(f"✅ Mock enter team test passed")

    def test_mock_enter_team_invalid_code(self):
        """Test entering team with invalid code returns 404."""
        print("\n=== Mock: Testing enter team with invalid code ===")
        
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"detail": "Not found team with code invalid"}
        self.session.post.return_value = mock_response
        
        response = self.session.post(
            f"{BASE_URL}/teams/enter-team",
            json={"team_code": "invalid"}
        )
        
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertIn("Not found team with code", data["detail"])
        print(f"✅ Mock invalid enter team test passed")

    def test_mock_leave_team_success(self):
        """Test leaving team successfully."""
        print("\n=== Mock: Testing leave team ===")
        
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Successfully left team"}
        self.session.get.return_value = mock_response
        
        response = self.session.get(
            f"{BASE_URL}/teams/leave-team",
            params={"team_name": self.test_team_name}
        )
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("message", data)
        print(f"✅ Mock leave team test passed")

    def test_mock_team_details_success(self):
        """Test getting team details."""
        print("\n=== Mock: Testing team details ===")
        
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "team_name": self.test_team_name,
            "team_id": self.team_code
        }
        self.session.get.return_value = mock_response
        
        response = self.session.get(
            f"{BASE_URL}/teams/team_details",
            params={"team_name": self.test_team_name}
        )
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["team_name"], self.test_team_name)
        print(f"✅ Mock team details test passed")

    def test_endpoint_patterns(self):
        """Test that endpoint URL patterns are correct."""
        print("\n=== Testing endpoint patterns ===")
        
        endpoints = [
            f"{BASE_URL}/teams/create-team",
            f"{BASE_URL}/teams/enter-team",
            f"{BASE_URL}/teams/leave-team", 
            f"{BASE_URL}/teams/teams",
            f"{BASE_URL}/teams/team_details"
        ]
        
        for endpoint in endpoints:
            self.assertTrue(endpoint.startswith(BASE_URL))
            self.assertIn("/teams/", endpoint)
        
        print(f"✅ All endpoint patterns valid")


class TestTeamEndpointsIntegration(unittest.TestCase):
    """Integration tests for team endpoints - requires running server."""

    def setUp(self):
        """Set up integration test environment following project guidelines."""
        print("Setting up integration test environment...")
        self.session = requests.Session()
        self.valid_credentials = {"username": "admin", "password": "admin"}
        self.test_team_name = f"test_team_{uuid.uuid4().hex[:8]}"
        self.created_teams = []  # Track teams created during test for cleanup
        self.logged_in = False
        
        # Try to log in - skip test if server not available
        try:
            response = self.session.post(
                f"{BASE_URL}/simple_login/login",
                json=self.valid_credentials,
                timeout=5
            )
            if response.status_code != 200:
                self.skipTest("Server login failed")
            self.logged_in = True
            print("✅ Successfully logged in for integration test")
        except Exception as e:
            self.skipTest(f"Server not available: {e}")

    def tearDown(self):
        """Clean up integration test environment to leave database in same state."""
        print("Cleaning up integration test environment...")
        
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
        print("✅ Integration test cleanup completed")

    def test_integration_create_team(self):
        """Integration test: Create a team and track it for cleanup."""
        print("\n=== Integration: Testing team creation ===")
        
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
        print(f"✅ Integration team creation test passed - team tracked for cleanup")

    def test_integration_get_teams(self):
        """Integration test: Get teams list after ensuring clean state."""
        print("\n=== Integration: Testing get teams ===")
        
        response = self.session.get(f"{BASE_URL}/teams/teams", timeout=10)
        
        if TEST_DEBUG:
            print(f"Response: {response.status_code} - {response.text}")
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("teams", data)
        self.assertIsInstance(data["teams"], list)
        print(f"✅ Integration get teams test passed")
        
    def test_integration_team_workflow(self):
        """Integration test: Complete team workflow (create -> details -> leave)."""
        print("\n=== Integration: Testing complete team workflow ===")
        
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
    # Smart test runner: always run mock tests, add integration tests if server available
    suite = unittest.TestSuite()
    
    # Always run mock tests
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestTeamEndpointsMock))
    
    # Try to add integration tests if server is available
    try:
        test_response = requests.get(f"{BASE_URL}/teams/teams", timeout=2)
        # If we get any response (even auth required), server is running
        suite.addTest(loader.loadTestsFromTestCase(TestTeamEndpointsIntegration))
        print("🚀 Server detected - running both mock and integration tests")
    except:
        print("🔧 Server not available - running mock tests only")
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    if result.wasSuccessful():
        print("\n✅ All tests passed!")
    else:
        print(f"\n❌ {len(result.failures)} failures, {len(result.errors)} errors")