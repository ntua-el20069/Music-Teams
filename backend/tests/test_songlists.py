"""
Song list endpoints tests for Music Teams application.

This module tests the song list management functionality including
user and team song lists with proper authentication and access control.
"""

import json
import os
import tempfile
import unittest
from unittest.mock import Mock, patch

from backend.monolith.utils.songlists import (
    add_song_to_list,
    get_song_list,
    get_songlist_file_path,
    load_songlist_data,
    save_song_list,
    save_songlist_data,
    validate_song_access_for_list,
)


class TestSongListUtils(unittest.TestCase):
    """Test song list utility functions."""
    
    def setUp(self):
        """Set up test environment."""
        # Create a temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
        self.original_env = os.environ.get("MAX_SONGS_IN_LIST")
        os.environ["MAX_SONGS_IN_LIST"] = "5"  # Small limit for testing
        
    def tearDown(self):
        """Clean up test environment."""
        # Restore original environment
        if self.original_env is not None:
            os.environ["MAX_SONGS_IN_LIST"] = self.original_env
        else:
            os.environ.pop("MAX_SONGS_IN_LIST", None)
        
        # Clean up test files
        import shutil
        shutil.rmtree(self.test_dir, ignore_errors=True)
    
    def test_get_songlist_file_path_user(self):
        """Test file path generation for user song lists."""
        path = get_songlist_file_path(user_id=123)
        expected = os.path.join("backend", "monolith", "songlists", "songlist-user123.json")
        self.assertEqual(path, expected)
    
    def test_get_songlist_file_path_team(self):
        """Test file path generation for team song lists."""
        path = get_songlist_file_path(team_name="MyTeam")
        expected = os.path.join("backend", "monolith", "songlists", "songlist-teamMyTeam.json")
        self.assertEqual(path, expected)
    
    def test_get_songlist_file_path_invalid(self):
        """Test file path generation with invalid parameters."""
        with self.assertRaises(ValueError):
            get_songlist_file_path()  # Neither user_id nor team_name
        
        with self.assertRaises(ValueError):
            get_songlist_file_path(user_id=123, team_name="MyTeam")  # Both provided
    
    def test_load_songlist_data_nonexistent_file(self):
        """Test loading data from non-existent file."""
        nonexistent_path = os.path.join(self.test_dir, "nonexistent.json")
        data = load_songlist_data(nonexistent_path)
        expected = {"1": [], "2": [], "3": []}
        self.assertEqual(data, expected)
    
    def test_load_songlist_data_existing_file(self):
        """Test loading data from existing file."""
        test_file = os.path.join(self.test_dir, "test.json")
        test_data = {
            "1": [{"id": 1, "title": "Song 1"}],
            "2": [],
            "3": [{"id": 2, "title": "Song 2"}]
        }
        
        with open(test_file, 'w') as f:
            json.dump(test_data, f)
        
        data = load_songlist_data(test_file)
        self.assertEqual(data, test_data)
    
    def test_load_songlist_data_incomplete_file(self):
        """Test loading data from file missing some lists."""
        test_file = os.path.join(self.test_dir, "test.json")
        test_data = {"1": [{"id": 1, "title": "Song 1"}]}  # Missing lists 2 and 3
        
        with open(test_file, 'w') as f:
            json.dump(test_data, f)
        
        data = load_songlist_data(test_file)
        expected = {
            "1": [{"id": 1, "title": "Song 1"}],
            "2": [],
            "3": []
        }
        self.assertEqual(data, expected)
    
    def test_save_songlist_data(self):
        """Test saving song list data to file."""
        test_file = os.path.join(self.test_dir, "test.json")
        test_data = {
            "1": [{"id": 1, "title": "Song 1"}],
            "2": [],
            "3": [{"id": 2, "title": "Song 2"}]
        }
        
        success, message = save_songlist_data(test_file, test_data)
        self.assertTrue(success)
        self.assertIn("successfully", message)
        
        # Verify file was created and contains correct data
        self.assertTrue(os.path.exists(test_file))
        with open(test_file, 'r') as f:
            saved_data = json.load(f)
        self.assertEqual(saved_data, test_data)
    
    @patch('backend.monolith.utils.songlists.get_songlist_file_path')
    @patch('backend.monolith.utils.songlists.load_songlist_data')
    def test_get_song_list(self, mock_load, mock_get_path):
        """Test getting songs from a song list."""
        # Mock database session
        mock_db = Mock()
        
        # Setup mocks
        mock_get_path.return_value = "fake/path.json"
        mock_load.return_value = {
            "1": [{"id": 1, "title": "Song 1"}, {"id": 2, "title": "Song 2"}],
            "2": [],
            "3": []
        }
        
        # Test getting list 1
        success, message, songs = get_song_list(mock_db, 123, 1)
        
        self.assertTrue(success)
        self.assertEqual(len(songs), 2)
        self.assertEqual(songs[0].id, 1)
        self.assertEqual(songs[0].title, "Song 1")
        self.assertEqual(songs[1].id, 2)
        self.assertEqual(songs[1].title, "Song 2")
    
    def test_get_song_list_invalid_songlist_id(self):
        """Test getting song list with invalid ID."""
        mock_db = Mock()
        
        success, message, songs = get_song_list(mock_db, 123, 4)  # Invalid ID
        
        self.assertFalse(success)
        self.assertIn("must be 1, 2, or 3", message)
        self.assertEqual(songs, [])
    
    @patch('backend.monolith.utils.songlists.get_songlist_file_path')
    @patch('backend.monolith.utils.songlists.load_songlist_data')
    @patch('backend.monolith.utils.songlists.save_songlist_data')
    def test_add_song_to_list(self, mock_save, mock_load, mock_get_path):
        """Test adding a song to a song list."""
        # Mock database session
        mock_db = Mock()
        
        # Setup mocks
        mock_get_path.return_value = "fake/path.json"
        mock_load.return_value = {
            "1": [{"id": 1, "title": "Existing Song"}],
            "2": [],
            "3": []
        }
        mock_save.return_value = (True, "Song list saved successfully")
        
        # Test adding a new song
        success, message = add_song_to_list(mock_db, 123, 1, 2, "New Song")
        
        self.assertTrue(success)
        self.assertIn("New Song", message)
        
        # Verify save was called with updated data
        mock_save.assert_called_once()
        call_args = mock_save.call_args[0]  # Get positional arguments
        saved_data = call_args[1]  # Second argument is the data
        self.assertEqual(len(saved_data["1"]), 2)  # Should have 2 songs now
        self.assertEqual(saved_data["1"][1]["id"], 2)
        self.assertEqual(saved_data["1"][1]["title"], "New Song")
    
    @patch('backend.monolith.utils.songlists.get_songlist_file_path')
    @patch('backend.monolith.utils.songlists.load_songlist_data')
    def test_add_song_to_list_duplicate(self, mock_load, mock_get_path):
        """Test adding a duplicate song to a song list."""
        # Mock database session
        mock_db = Mock()
        
        # Setup mocks
        mock_get_path.return_value = "fake/path.json"
        mock_load.return_value = {
            "1": [{"id": 1, "title": "Existing Song"}],
            "2": [],
            "3": []
        }
        
        # Test adding a duplicate song
        success, message = add_song_to_list(mock_db, 123, 1, 1, "Existing Song")
        
        self.assertFalse(success)
        self.assertIn("already in the list", message)
    
    @patch('backend.monolith.utils.songlists.get_songlist_file_path')
    @patch('backend.monolith.utils.songlists.load_songlist_data')
    def test_add_song_to_list_full(self, mock_load, mock_get_path):
        """Test adding a song to a full song list."""
        # Mock database session
        mock_db = Mock()
        
        # Setup mocks - create a full list (5 songs, which is our test limit)
        mock_get_path.return_value = "fake/path.json"
        mock_load.return_value = {
            "1": [
                {"id": 1, "title": "Song 1"},
                {"id": 2, "title": "Song 2"},
                {"id": 3, "title": "Song 3"},
                {"id": 4, "title": "Song 4"},
                {"id": 5, "title": "Song 5"}
            ],
            "2": [],
            "3": []
        }
        
        # Test adding to full list
        success, message = add_song_to_list(mock_db, 123, 1, 6, "Song 6")
        
        self.assertFalse(success)
        self.assertIn("full", message)
        self.assertIn("5", message)  # Should mention the limit
    
    @patch('backend.monolith.utils.song_access.can_read_song')
    def test_validate_song_access_for_list(self, mock_can_read):
        """Test validating song access for lists."""
        # Mock database session
        mock_db = Mock()
        
        # Test successful validation
        mock_can_read.return_value = (True, "User has access")
        success, message = validate_song_access_for_list(mock_db, 123, 456)
        
        self.assertTrue(success)
        self.assertIn("validated", message)
        
        # Test failed validation
        mock_can_read.return_value = (False, "No access")
        success, message = validate_song_access_for_list(mock_db, 123, 456)
        
        self.assertFalse(success)
        self.assertIn("Cannot access song", message)


if __name__ == '__main__':
    unittest.main()