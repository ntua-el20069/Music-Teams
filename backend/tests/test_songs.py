# Song endpoints tests for Music Teams application
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


class TestSongEndpoints(unittest.TestCase):
    """Test suite for song endpoints - assumes server is running."""

    def setUp(self):
        """Set up test environment following project guidelines."""
        print("Setting up test environment for songs...")
        self.sessions = [requests.Session() for _ in range(NUM_USERS)]
        self.valid_credentials = [
            {"username": f"admin{i}", "password": f"admin{i}"} for i in range(NUM_USERS)
        ]

        self.test_song_title = f"test_song_{uuid.uuid4().hex[:8]}"
        self.test_team_name = f"test_team_{uuid.uuid4().hex[:8]}"
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
                    self.fail(
                        f"⚠️ Failed to delete song {song_id}: \
                            {delete_response.status_code} - {delete_response.text}"
                    )
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

    def test_01_insert_song_success(self):
        """Test successful song insertion."""
        if not self.logged_in[0]:
            self.fail("User 0 not logged in")

        song_data = {
            "title": self.test_song_title,
            "composers": ["Test Composer"],
            "lyricists": ["Test Lyricist"],
            "lyrics": "Test lyrics\nSecond line",
            "public": True,
            "shared_with_teams": [],
        }

        response = self.sessions[0].post(
            f"{BASE_URL}/songs/insert-song", json=song_data
        )

        print(f"Insert song response: {response.status_code}")
        print(f"Response content: {response.text}")

        self.assertEqual(response.status_code, 201)

        response_data = response.json()
        self.assertIn("song_id", response_data)
        self.assertIn("message", response_data)
        self.assertEqual(response_data["status"], "success")

        # Track created song for cleanup
        self.created_songs.append(response_data["song_id"])

    def test_02_insert_song_duplicate_title(self):
        """Test inserting song with duplicate title by same user fails."""
        if not self.logged_in[0]:
            self.fail("User 0 not logged in")

        # First song
        song_data = {
            "title": f"duplicate_{self.test_song_title}",
            "composers": ["Test Composer"],
            "lyricists": ["Test Lyricist"],
            "lyrics": "Test lyrics",
            "public": True,
            "shared_with_teams": [],
        }

        response1 = self.sessions[0].post(
            f"{BASE_URL}/songs/insert-song", json=song_data
        )

        self.assertEqual(response1.status_code, 201)
        self.created_songs.append(response1.json()["song_id"])

        # Second song with same title
        response2 = self.sessions[0].post(
            f"{BASE_URL}/songs/insert-song", json=song_data
        )

        print(f"Duplicate song response: {response2.status_code}")
        print(f"Response content: {response2.text}")

        self.assertEqual(response2.status_code, 409)  # Conflict

    def test_03_insert_song_with_team_sharing(self):
        """Test inserting song with team sharing."""
        if not self.logged_in[0] or not self.created_teams:
            self.fail("User 0 not logged in or no test team available")

        song_data = {
            "title": f"team_song_{self.test_song_title}",
            "composers": ["Team Composer"],
            "lyricists": ["Team Lyricist"],
            "lyrics": "Team song lyrics",
            "public": False,
            "shared_with_teams": [self.test_team_name],
        }

        response = self.sessions[0].post(
            f"{BASE_URL}/songs/insert-song", json=song_data
        )

        print(f"Team song response: {response.status_code}")
        print(f"Response content: {response.text}")

        self.assertEqual(response.status_code, 201)
        self.created_songs.append(response.json()["song_id"])
        self.assertEqual(response.json()["status"], "success")

    def test_04_get_song_success(self):
        """Test successful song retrieval."""
        if not self.logged_in[0]:
            self.fail("User 0 not logged in")

        # First create a song
        song_data = {
            "title": f"get_test_{self.test_song_title}",
            "composers": ["Get Test Composer"],
            "lyricists": ["Get Test Lyricist"],
            "lyrics": "Get test lyrics",
            "public": True,
            "shared_with_teams": [],
        }

        create_response = self.sessions[0].post(
            f"{BASE_URL}/songs/insert-song", json=song_data
        )

        self.assertEqual(
            create_response.status_code, 201, "Song creation failed in get test"
        )

        song_id = create_response.json()["song_id"]
        self.created_songs.append(song_id)

        # Now get the song
        get_response = self.sessions[0].get(f"{BASE_URL}/songs/song?song_id={song_id}")

        print(f"Get song response: {get_response.status_code}")
        print(f"Response content: {get_response.text}")

        self.assertEqual(get_response.status_code, 200)

        song = get_response.json()
        self.assertEqual(song["id"], song_id)
        self.assertEqual(song["title"], song_data["title"])
        self.assertEqual(song["lyrics"], song_data["lyrics"])
        self.assertIn("composers", song)
        self.assertIn("lyricists", song)

    def test_05_get_song_with_transposition(self):
        """Test song retrieval with chord transposition."""
        if not self.logged_in[0]:
            self.fail("User 0 not logged in")

        # Create a song with chords (this would normally be done via add-chords endpoint)
        song_data = {
            "title": f"transpose_test_{self.test_song_title}",
            "composers": ["Transpose Composer"],
            "lyricists": ["Transpose Lyricist"],
            "lyrics": "Transpose test lyrics",
            "public": True,
            "shared_with_teams": [],
        }

        create_response = self.sessions[0].post(
            f"{BASE_URL}/songs/insert-song", json=song_data
        )

        self.assertEqual(
            create_response.status_code, 201, "Song creation failed in transpose test"
        )

        song_id = create_response.json()["song_id"]
        self.created_songs.append(song_id)

        # Add chords to the song via /songs/update-lyrics-chords endpoint
        chords_data = {
            "song_id": song_id,
            "lyrics": "Transpose test lyrics",
            "chords": "C# F Gb",
        }

        chords_response = self.sessions[0].post(
            f"{BASE_URL}/songs/update-lyrics-chords", json=chords_data
        )

        print(f"Add chords response: {chords_response.status_code}")
        print(f"Response content: {chords_response.text}")

        self.assertEqual(
            chords_response.status_code, 200, "Failed to add chords to song"
        )

        # Get the song with transposition
        get_response = self.sessions[0].get(
            f"{BASE_URL}/songs/song?song_id={song_id}&transporto_units=2"
        )

        print(f"Transpose get response: {get_response.status_code}")
        print(f"Response content: {get_response.text}")

        self.assertEqual(get_response.status_code, 200)

        song = get_response.json()
        self.assertEqual(song["transposed_by"], 2)

        # Verify that chords in lyrics are transposed correctly
        # The original chords "C# F Gb" transposed by 2 semitones should become "D# G G#"
        # (only hash in chords, not flat)
        self.assertIn(
            "D#", song["chords"], "Chords should contain D# after transposition"
        )
        self.assertIn(
            "G#", song["chords"], "Chords should contain G# after transposition"
        )
        self.assertIn(
            "G", song["chords"], "Chords should contain G after transposition"
        )

    def test_06_update_song_success(self):
        """Test successful song update."""
        if not self.logged_in[0]:
            self.fail("User 0 not logged in")

        # First create a song
        song_data = {
            "title": f"update_test_{self.test_song_title}",
            "composers": ["Original Composer"],
            "lyricists": ["Original Lyricist"],
            "lyrics": "Original lyrics",
            "public": True,
            "shared_with_teams": [],
        }

        create_response = self.sessions[0].post(
            f"{BASE_URL}/songs/insert-song", json=song_data
        )

        self.assertEqual(
            create_response.status_code, 201, "Song creation failed in update test"
        )

        song_id = create_response.json()["song_id"]
        self.created_songs.append(song_id)

        # Now update the song
        update_data = {
            "id": song_id,
            "title": f"updated_{self.test_song_title}",
            "composers": ["Updated Composer"],
            "lyricists": ["Updated Lyricist"],
            "lyrics": "Updated lyrics",
            "public": False,
            "shared_with_teams": [],
        }

        update_response = self.sessions[0].post(
            f"{BASE_URL}/songs/update-song", json=update_data
        )

        print(f"Update song response: {update_response.status_code}")
        print(f"Response content: {update_response.text}")

        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.json()["status"], "success")

    def test_07_update_song_not_owner(self):
        """Test that updating someone else's song fails."""
        if not all(self.logged_in[:2]):
            self.fail("Both users not logged in")

        # User 0 creates a song
        song_data = {
            "title": f"owner_test_{self.test_song_title}",
            "composers": ["Owner Composer"],
            "lyricists": ["Owner Lyricist"],
            "lyrics": "Owner lyrics",
            "public": True,
            "shared_with_teams": [],
        }

        create_response = self.sessions[0].post(
            f"{BASE_URL}/songs/insert-song", json=song_data
        )

        self.assertEqual(
            create_response.status_code, 201, "Song creation failed in owner test"
        )

        song_id = create_response.json()["song_id"]
        self.created_songs.append(song_id)

        # User 1 tries to update it
        update_data = {
            "id": song_id,
            "title": f"hacked_{self.test_song_title}",
            "composers": ["Hacker Composer"],
            "lyricists": ["Hacker Lyricist"],
            "lyrics": "Hacked lyrics",
            "public": True,
            "shared_with_teams": [],
        }

        update_response = self.sessions[1].post(
            f"{BASE_URL}/songs/update-song", json=update_data
        )

        print(f"Unauthorized update response: {update_response.status_code}")
        print(f"Response content: {update_response.text}")

        self.assertEqual(update_response.status_code, 403)  # Forbidden

    def test_08_permanent_transporto(self):
        """Test permanent chord transposition."""
        if not self.logged_in[0]:
            self.fail("User 0 not logged in")

        # Create a song with chords
        song_data = {
            "title": f"permanent_transpose_{self.test_song_title}",
            "composers": ["Transpose Composer"],
            "lyricists": ["Transpose Lyricist"],
            "lyrics": "Some lyrics here...",
            "public": True,
            "shared_with_teams": [],
        }

        create_response = self.sessions[0].post(
            f"{BASE_URL}/songs/insert-song", json=song_data
        )

        self.assertEqual(
            create_response.status_code, 201, "Song creation failed in transpose test"
        )

        song_id = create_response.json()["song_id"]
        self.created_songs.append(song_id)

        # Add chords to the song via /songs/update-lyrics-chords endpoint
        chords_data = {
            "song_id": song_id,
            "lyrics": "Some lyrics here...",
            "chords": "C# F Gb",
        }

        chords_response = self.sessions[0].post(
            f"{BASE_URL}/songs/update-lyrics-chords", json=chords_data
        )

        print(f"Add chords response: {chords_response.status_code}")
        print(f"Response content: {chords_response.text}")

        self.assertEqual(
            chords_response.status_code, 200, "Failed to add chords to song"
        )

        # Apply permanent transposition
        transpose_data = {"song_id": song_id, "transporto_units": 2}

        transpose_response = self.sessions[0].post(
            f"{BASE_URL}/songs/permanent-transporto", json=transpose_data
        )

        print(f"Permanent transpose response: {transpose_response.status_code}")
        print(f"Response content: {transpose_response.text}")

        self.assertEqual(transpose_response.status_code, 200)
        self.assertEqual(transpose_response.json()["status"], "success")

        # Fetch song and check chords have been transposed permanently
        get_response = self.sessions[0].get(f"{BASE_URL}/songs/song?song_id={song_id}")

        print(f"Get song after transpose response: {get_response.status_code}")
        print(f"Response content: {get_response.text}")

        self.assertEqual(
            get_response.status_code, 200, "Failed to get song after transposition"
        )

        song = get_response.json()
        # Verify chords are now "D# G G#" (C# F Gb transposed by 2 semitones)
        # Note: Gb is enharmonic equivalent of F#, so F# + 2 semitones = G# (not A#)
        self.assertIn(
            "D#",
            song["chords"],
            "Chords should contain D# after permanent transposition",
        )
        self.assertIn(
            "G#",
            song["chords"],
            "Chords should contain G# after permanent transposition",
        )
        self.assertIn(
            "G",
            song["chords"],
            "Chords should contain G after permanent transposition",
        )

    def test_09_get_nonexistent_song(self):
        """Test getting a non-existent song."""
        if not self.logged_in[0]:
            self.fail("User 0 not logged in")

        response = self.sessions[0].get(f"{BASE_URL}/songs/song?song_id=999999")

        print(f"Non-existent song response: {response.status_code}")
        print(f"Response content: {response.text}")

        self.assertEqual(response.status_code, 404)

    def test_10_unauthorized_access(self):
        """Test accessing song endpoints without authentication."""
        # Create a session without logging in
        unauthorized_session = requests.Session()

        song_data = {
            "title": "unauthorized_song",
            "composers": ["Unauthorized Composer"],
            "lyricists": ["Unauthorized Lyricist"],
            "lyrics": "Unauthorized lyrics",
            "public": True,
            "shared_with_teams": [],
        }

        response = unauthorized_session.post(
            f"{BASE_URL}/songs/insert-song", json=song_data
        )

        print(f"Unauthorized access response: {response.status_code}")
        print(f"Response content: {response.text}")

        self.assertEqual(response.status_code, 401)  # Unauthorized


if __name__ == "__main__":
    unittest.main()
