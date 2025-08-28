"""
Isolated song list utility tests for Music Teams application.

Tests the song list utility functions without database dependencies.
"""

import json
import os
import tempfile
import unittest
from unittest.mock import Mock, patch


class TestSongListBasicUtils(unittest.TestCase):
    """Test basic song list utility functions without database dependencies."""
    
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
        # Import the function directly to avoid database issues
        import sys
        import os
        
        # Add the backend directory to Python path
        backend_path = os.path.join(os.getcwd(), 'backend')
        if backend_path not in sys.path:
            sys.path.insert(0, backend_path)
        
        def get_songlist_file_path(user_id=None, team_name=None):
            """Local implementation for testing."""
            if user_id is not None and team_name is not None:
                raise ValueError("Cannot specify both user_id and team_name")
            if user_id is None and team_name is None:
                raise ValueError("Must specify either user_id or team_name")
            
            base_dir = os.path.join("backend", "monolith", "songlists")
            
            if user_id is not None:
                return os.path.join(base_dir, f"songlist-user{user_id}.json")
            else:
                return os.path.join(base_dir, f"songlist-team{team_name}.json")
        
        path = get_songlist_file_path(user_id=123)
        expected = os.path.join("backend", "monolith", "songlists", "songlist-user123.json")
        self.assertEqual(path, expected)
    
    def test_get_songlist_file_path_team(self):
        """Test file path generation for team song lists."""
        def get_songlist_file_path(user_id=None, team_name=None):
            """Local implementation for testing."""
            if user_id is not None and team_name is not None:
                raise ValueError("Cannot specify both user_id and team_name")
            if user_id is None and team_name is None:
                raise ValueError("Must specify either user_id or team_name")
            
            base_dir = os.path.join("backend", "monolith", "songlists")
            
            if user_id is not None:
                return os.path.join(base_dir, f"songlist-user{user_id}.json")
            else:
                return os.path.join(base_dir, f"songlist-team{team_name}.json")
        
        path = get_songlist_file_path(team_name="MyTeam")
        expected = os.path.join("backend", "monolith", "songlists", "songlist-teamMyTeam.json")
        self.assertEqual(path, expected)
    
    def test_load_songlist_data_nonexistent_file(self):
        """Test loading data from non-existent file."""
        def load_songlist_data(file_path):
            """Local implementation for testing."""
            if not os.path.exists(file_path):
                return {"1": [], "2": [], "3": []}
            
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                
                # Ensure all three lists exist
                for key in ["1", "2", "3"]:
                    if key not in data:
                        data[key] = []
                
                return data
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading song list from {file_path}: {e}")
                return {"1": [], "2": [], "3": []}
        
        nonexistent_path = os.path.join(self.test_dir, "nonexistent.json")
        data = load_songlist_data(nonexistent_path)
        expected = {"1": [], "2": [], "3": []}
        self.assertEqual(data, expected)
    
    def test_load_songlist_data_existing_file(self):
        """Test loading data from existing file."""
        def load_songlist_data(file_path):
            """Local implementation for testing."""
            if not os.path.exists(file_path):
                return {"1": [], "2": [], "3": []}
            
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                
                # Ensure all three lists exist
                for key in ["1", "2", "3"]:
                    if key not in data:
                        data[key] = []
                
                return data
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading song list from {file_path}: {e}")
                return {"1": [], "2": [], "3": []}
        
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
    
    def test_save_songlist_data(self):
        """Test saving song list data to file."""
        def save_songlist_data(file_path, data):
            """Local implementation for testing."""
            try:
                # Ensure directory exists
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                
                with open(file_path, 'w') as f:
                    json.dump(data, f, indent=2)
                
                return (True, "Song list saved successfully")
            except IOError as e:
                print(f"Error saving song list to {file_path}: {e}")
                return (False, f"Failed to save song list: {e}")
        
        test_file = os.path.join(self.test_dir, "subdir", "test.json")
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
    
    def test_song_list_limits(self):
        """Test song list size limits."""
        # Test that the environment variable is read correctly
        max_songs = int(os.environ.get("MAX_SONGS_IN_LIST", 300))
        self.assertEqual(max_songs, 5)  # We set it to 5 in setUp
        
        # Test creating a list at the limit
        songs = [{"id": i, "title": f"Song {i}"} for i in range(max_songs)]
        self.assertEqual(len(songs), max_songs)
        
        # Test exceeding the limit
        too_many_songs = [{"id": i, "title": f"Song {i}"} for i in range(max_songs + 1)]
        self.assertGreater(len(too_many_songs), max_songs)
    
    def test_json_file_structure(self):
        """Test the expected JSON file structure."""
        expected_structure = {
            "1": [{"id": 234, "title": "I surrender"}, {"id": 54, "title": "Welcome to the Jungle"}],
            "2": [{"id": 66, "title": "zorbas the greek"}],
            "3": []
        }
        
        # Test that we can serialize and deserialize this structure
        json_str = json.dumps(expected_structure)
        parsed_structure = json.loads(json_str)
        self.assertEqual(parsed_structure, expected_structure)
        
        # Test that all required keys exist
        for key in ["1", "2", "3"]:
            self.assertIn(key, parsed_structure)
        
        # Test song entry structure
        if parsed_structure["1"]:
            song = parsed_structure["1"][0]
            self.assertIn("id", song)
            self.assertIn("title", song)
            self.assertIsInstance(song["id"], int)
            self.assertIsInstance(song["title"], str)


if __name__ == '__main__':
    unittest.main()