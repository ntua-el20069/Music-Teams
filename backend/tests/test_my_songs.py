# My Songs endpoints tests for Music Teams application
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

from backend.tests.helpers import (
    create_team,
    get_teams,
    leave_team,
    login_user,
    logout_user,
)

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)

BASE_URL = "http://127.0.0.1:8000"
TEST_DEBUG = True
NUM_USERS = 2  # Number of admin users to create for testing


class TestMySongsEndpoints(unittest.TestCase):
    """Test suite for my songs endpoints - assumes server is running."""

    def setUp(self):
        """Set up test environment following project guidelines."""
        print("Setting up test environment for my songs...")
        self.sessions = [requests.Session() for _ in range(NUM_USERS)]
        self.valid_credentials = [
            {"username": f"admin{i}", "password": f"admin{i}"} for i in range(NUM_USERS)
        ]

        self.test_song_title = f"my_songs_test_{uuid.uuid4().hex[:8]}"
        self.test_team_name = f"my_songs_team_{uuid.uuid4().hex[:8]}"
        self.created_songs = []  # Track songs created during test for cleanup
        self.created_teams = []  # Track teams created for testing
        self.logged_in = [False] * NUM_USERS

        # Log in for the test (login all users)
        for i, session in enumerate(self.sessions):
            login_ok, login_status, response = login_user(
                session, self.valid_credentials[i]
            )
            if login_ok:
                self.logged_in[i] = True
                print(f"✅ Successfully logged in for user {i}")
            else:
                self.fail(
                    f"❌ Failed to log in for user {i}: {login_status} \
                    \n Response: {response}"
                )

        # Create a test team for user 0 (only user 0 creates and participates in team)
        if self.logged_in[0]:
            team_create_ok, team_create_status, response = create_team(
                self.sessions[0], self.test_team_name
            )
            if team_create_ok:
                self.created_teams.append(self.test_team_name)
                print(f"✅ Successfully created test team: {self.test_team_name}")
            else:
                self.fail(
                    f"❌ Failed to create test team: {team_create_status} \
                    \n Response: {response}"
                )

        # Load team data for all users (required for song endpoints) - sets team_data cookie
        for i in range(NUM_USERS):
            if self.logged_in[i]:
                get_teams_ok, get_teams_status, response = get_teams(self.sessions[i])
                if get_teams_ok:
                    print(f"✅ Successfully loaded teams for user {i}")
                else:
                    self.fail(
                        f"❌ Failed to load teams for user {i}: {get_teams_status} \
                        \n Response: {response}"
                    )

    def tearDown(self):
        """Clean up test environment following project guidelines."""
        print("Cleaning up test environment...")

        # Clean up created songs using the delete endpoint
        for song_id in self.created_songs:
            try:
                delete_response = self.sessions[0].delete(
                    f"{BASE_URL}/songs/delete-song?song_id={song_id}"
                )
                if delete_response.status_code == 200:
                    print(f"✅ Successfully deleted song {song_id}")
                else:
                    print(f"⚠️ Failed to delete song {song_id}: {delete_response.status_code} - {delete_response.text}")
            except Exception as e:
                print(f"Error deleting song {song_id}: {e}")

        # Clean up teams (only user 0 created and participates in a team)
        if self.logged_in[0]:
            leave_team_ok, leave_team_status, response = leave_team(
                self.sessions[0], self.test_team_name
            )
            if leave_team_ok:
                print(f"✅ User {0} left team {self.test_team_name}")
            else:
                self.fail(
                    f"❌ Failed to leave team {self.test_team_name} for user {0}: \
                        {leave_team_status} \n Response: {response}"
                )

        # Log out all users
        for i, session in enumerate(self.sessions):
            if self.logged_in[i]:
                logout_ok, logout_status, response = logout_user(session)
                if logout_ok:
                    self.logged_in[i] = False
                    print(f"✅ Successfully logged out user {i}")
                else:
                    self.fail(
                        f"❌ Failed to logout user {i}: {logout_status} \
                        \n Response: {response}"
                    )

    def test_01_get_my_songs_empty(self):
        """Test getting songs when user has no songs."""
        if not self.logged_in[0]:
            self.fail("User 0 not logged in")

        response = self.sessions[0].get(f"{BASE_URL}/my_songs/all-songs")

        print(f"Get my songs (empty) response: {response.status_code}")
        print(f"Response content: {response.text}")

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["count"], 0)
        self.assertEqual(len(data["songs"]), 0)

    def test_02_get_my_composers_empty(self):
        """Test getting composers when user has no songs."""
        if not self.logged_in[0]:
            self.fail("User 0 not logged in")

        response = self.sessions[0].get(f"{BASE_URL}/my_songs/all-composers")

        print(f"Get my composers (empty) response: {response.status_code}")
        print(f"Response content: {response.text}")

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["count"], 0)
        self.assertEqual(len(data["composers"]), 0)

    def test_03_get_my_lyricists_empty(self):
        """Test getting lyricists when user has no songs."""
        if not self.logged_in[0]:
            self.fail("User 0 not logged in")

        response = self.sessions[0].get(f"{BASE_URL}/my_songs/all-lyricists")

        print(f"Get my lyricists (empty) response: {response.status_code}")
        print(f"Response content: {response.text}")

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["count"], 0)
        self.assertEqual(len(data["lyricists"]), 0)

    def test_04_create_songs_and_get_my_songs(self):
        """Test creating songs and retrieving them with my_songs endpoint."""
        if not self.logged_in[0]:
            self.fail("User 0 not logged in")

        # Create first song
        song_data_1 = {
            "title": f"my_song_1_{self.test_song_title}",
            "composers": ["My Composer 1", "Shared Composer"],
            "lyricists": ["My Lyricist 1"],
            "lyrics": "First song lyrics",
            "public": True,
            "shared_with_teams": [],
        }

        response1 = self.sessions[0].post(
            f"{BASE_URL}/songs/insert-song", json=song_data_1
        )

        self.assertEqual(response1.status_code, 201)
        song_id_1 = response1.json()["song_id"]
        self.created_songs.append(song_id_1)

        # Create second song
        song_data_2 = {
            "title": f"my_song_2_{self.test_song_title}",
            "composers": ["My Composer 2", "Shared Composer"],
            "lyricists": ["My Lyricist 2", "Shared Lyricist"],
            "lyrics": "Second song lyrics",
            "public": False,
            "shared_with_teams": [self.test_team_name],
        }

        response2 = self.sessions[0].post(
            f"{BASE_URL}/songs/insert-song", json=song_data_2
        )

        self.assertEqual(response2.status_code, 201)
        song_id_2 = response2.json()["song_id"]
        self.created_songs.append(song_id_2)

        # Now test getting my songs
        response = self.sessions[0].get(f"{BASE_URL}/my_songs/all-songs")

        print(f"Get my songs response: {response.status_code}")
        print(f"Response content: {response.text}")

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["count"], 2)
        self.assertEqual(len(data["songs"]), 2)

        # Verify song details
        song_titles = [song["title"] for song in data["songs"]]
        self.assertIn(song_data_1["title"], song_titles)
        self.assertIn(song_data_2["title"], song_titles)

        # Find and verify individual songs
        for song in data["songs"]:
            if song["title"] == song_data_1["title"]:
                self.assertEqual(song["public"], True)
                self.assertIn("My Composer 1", song["composers"])
                self.assertIn("Shared Composer", song["composers"])
                self.assertIn("My Lyricist 1", song["lyricists"])
            elif song["title"] == song_data_2["title"]:
                self.assertEqual(song["public"], False)
                self.assertIn("My Composer 2", song["composers"])
                self.assertIn("Shared Composer", song["composers"])
                self.assertIn("My Lyricist 2", song["lyricists"])
                self.assertIn("Shared Lyricist", song["lyricists"])
                self.assertIn(self.test_team_name, song["shared_with_teams"])

    def test_05_get_my_composers_with_songs(self):
        """Test getting composers after creating songs."""
        if not self.logged_in[0]:
            self.fail("User 0 not logged in")

        # Create a song first (using data from previous test)
        song_data = {
            "title": f"composer_test_{self.test_song_title}",
            "composers": ["Test Composer A", "Test Composer B"],
            "lyricists": ["Test Lyricist"],
            "lyrics": "Composer test lyrics",
            "public": True,
            "shared_with_teams": [],
        }

        create_response = self.sessions[0].post(
            f"{BASE_URL}/songs/insert-song", json=song_data
        )

        self.assertEqual(create_response.status_code, 201)
        song_id = create_response.json()["song_id"]
        self.created_songs.append(song_id)

        # Now test getting composers
        response = self.sessions[0].get(f"{BASE_URL}/my_songs/all-composers")

        print(f"Get my composers response: {response.status_code}")
        print(f"Response content: {response.text}")

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertGreaterEqual(data["count"], 2)  # At least the 2 we just added
        self.assertIn("Test Composer A", data["composers"])
        self.assertIn("Test Composer B", data["composers"])

    def test_06_get_my_lyricists_with_songs(self):
        """Test getting lyricists after creating songs."""
        if not self.logged_in[0]:
            self.fail("User 0 not logged in")

        # Create a song first
        song_data = {
            "title": f"lyricist_test_{self.test_song_title}",
            "composers": ["Test Composer"],
            "lyricists": ["Test Lyricist A", "Test Lyricist B"],
            "lyrics": "Lyricist test lyrics",
            "public": True,
            "shared_with_teams": [],
        }

        create_response = self.sessions[0].post(
            f"{BASE_URL}/songs/insert-song", json=song_data
        )

        self.assertEqual(create_response.status_code, 201)
        song_id = create_response.json()["song_id"]
        self.created_songs.append(song_id)

        # Now test getting lyricists
        response = self.sessions[0].get(f"{BASE_URL}/my_songs/all-lyricists")

        print(f"Get my lyricists response: {response.status_code}")
        print(f"Response content: {response.text}")

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertGreaterEqual(data["count"], 2)  # At least the 2 we just added
        self.assertIn("Test Lyricist A", data["lyricists"])
        self.assertIn("Test Lyricist B", data["lyricists"])

    def test_07_my_songs_isolation(self):
        """Test that my songs endpoints only return current user's songs."""
        if not all(self.logged_in[:2]):
            self.fail("Both users not logged in")

        # User 0 creates a song
        song_data_user0 = {
            "title": f"user0_song_{self.test_song_title}",
            "composers": ["User0 Composer"],
            "lyricists": ["User0 Lyricist"],
            "lyrics": "User 0 song lyrics",
            "public": True,
            "shared_with_teams": [],
        }

        response0 = self.sessions[0].post(
            f"{BASE_URL}/songs/insert-song", json=song_data_user0
        )

        self.assertEqual(response0.status_code, 201)
        song_id_0 = response0.json()["song_id"]
        self.created_songs.append(song_id_0)

        # User 1 creates a song
        song_data_user1 = {
            "title": f"user1_song_{self.test_song_title}",
            "composers": ["User1 Composer"],
            "lyricists": ["User1 Lyricist"],
            "lyrics": "User 1 song lyrics",
            "public": True,
            "shared_with_teams": [],
        }

        response1 = self.sessions[1].post(
            f"{BASE_URL}/songs/insert-song", json=song_data_user1
        )

        self.assertEqual(response1.status_code, 201)
        song_id_1 = response1.json()["song_id"]

        # User 0 checks their songs - should only see their own
        user0_songs = self.sessions[0].get(f"{BASE_URL}/my_songs/all-songs")
        self.assertEqual(user0_songs.status_code, 200)

        user0_data = user0_songs.json()
        user0_titles = [song["title"] for song in user0_data["songs"]]
        
        self.assertIn(song_data_user0["title"], user0_titles)
        self.assertNotIn(song_data_user1["title"], user0_titles)

        # User 1 checks their songs - should only see their own
        user1_songs = self.sessions[1].get(f"{BASE_URL}/my_songs/all-songs")
        self.assertEqual(user1_songs.status_code, 200)

        user1_data = user1_songs.json()
        user1_titles = [song["title"] for song in user1_data["songs"]]
        
        self.assertIn(song_data_user1["title"], user1_titles)
        self.assertNotIn(song_data_user0["title"], user1_titles)

        # Clean up user 1's song (user 1 must delete their own song)
        delete_response = self.sessions[1].delete(
            f"{BASE_URL}/songs/delete-song?song_id={song_id_1}"
        )
        self.assertEqual(delete_response.status_code, 200)

    def test_08_delete_song_functionality(self):
        """Test the delete song endpoint functionality."""
        if not self.logged_in[0]:
            self.fail("User 0 not logged in")

        # Create a song to delete
        song_data = {
            "title": f"delete_test_{self.test_song_title}",
            "composers": ["Delete Composer"],
            "lyricists": ["Delete Lyricist"],
            "lyrics": "Song to be deleted",
            "public": False,
            "shared_with_teams": [self.test_team_name],
        }

        create_response = self.sessions[0].post(
            f"{BASE_URL}/songs/insert-song", json=song_data
        )

        self.assertEqual(create_response.status_code, 201)
        song_id = create_response.json()["song_id"]

        # Verify song exists
        get_response = self.sessions[0].get(f"{BASE_URL}/songs/song?song_id={song_id}")
        self.assertEqual(get_response.status_code, 200)

        # Delete the song
        delete_response = self.sessions[0].delete(
            f"{BASE_URL}/songs/delete-song?song_id={song_id}"
        )

        print(f"Delete song response: {delete_response.status_code}")
        print(f"Response content: {delete_response.text}")

        self.assertEqual(delete_response.status_code, 200)

        delete_data = delete_response.json()
        self.assertEqual(delete_data["status"], "success")
        self.assertIn("deleted successfully", delete_data["message"])

        # Verify song no longer exists
        get_response_after = self.sessions[0].get(f"{BASE_URL}/songs/song?song_id={song_id}")
        self.assertEqual(get_response_after.status_code, 404)

        # Don't add to cleanup list since it's already deleted

    def test_09_unauthorized_access(self):
        """Test accessing my songs endpoints without authentication."""
        # Create a session without logging in
        unauthorized_session = requests.Session()

        endpoints = [
            "/my_songs/all-songs",
            "/my_songs/all-composers",
            "/my_songs/all-lyricists",
        ]

        for endpoint in endpoints:
            response = unauthorized_session.get(f"{BASE_URL}{endpoint}")

            print(f"Unauthorized access to {endpoint}: {response.status_code}")
            print(f"Response content: {response.text}")

            self.assertEqual(response.status_code, 401)  # Unauthorized


if __name__ == "__main__":
    unittest.main()