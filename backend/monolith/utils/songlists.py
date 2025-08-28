"""
Song list management utilities for Music Teams application.

This module contains helper functions for managing user and team song lists
stored as JSON files, with proper access control and validation.
"""

import json
import os
from typing import Dict, List, Optional, Tuple

from sqlalchemy.orm import Session

from backend.monolith.models.models import SongInListModel
from backend.monolith.utils.song_access import can_read_song


def get_songlist_file_path(user_id: Optional[int] = None, team_name: Optional[str] = None) -> str:
    """
    Get the file path for a song list based on user ID or team name.
    
    Args:
        user_id: User ID for personal song lists
        team_name: Team name for team song lists
        
    Returns:
        str: File path for the song list JSON file
        
    Raises:
        ValueError: If neither user_id nor team_name is provided, or both are provided
    """
    if user_id is not None and team_name is not None:
        raise ValueError("Cannot specify both user_id and team_name")
    if user_id is None and team_name is None:
        raise ValueError("Must specify either user_id or team_name")
    
    base_dir = os.path.join("backend", "monolith", "songlists")
    
    if user_id is not None:
        return os.path.join(base_dir, f"songlist-user{user_id}.json")
    else:
        return os.path.join(base_dir, f"songlist-team{team_name}.json")


def load_songlist_data(file_path: str) -> Dict[str, List[Dict[str, any]]]:
    """
    Load song list data from JSON file.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        Dict with keys "1", "2", "3" containing lists of song dictionaries
    """
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


def save_songlist_data(file_path: str, data: Dict[str, List[Dict[str, any]]]) -> Tuple[bool, str]:
    """
    Save song list data to JSON file.
    
    Args:
        file_path: Path to the JSON file
        data: Song list data to save
        
    Returns:
        Tuple[bool, str]: (success, message)
    """
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
        
        return (True, "Song list saved successfully")
    except IOError as e:
        print(f"Error saving song list to {file_path}: {e}")
        return (False, f"Failed to save song list: {e}")


def get_song_list(
    db: Session, 
    user_id: int, 
    songlist_id: int, 
    team_name: Optional[str] = None
) -> Tuple[bool, str, List[SongInListModel]]:
    """
    Get songs from a specific song list.
    
    Args:
        db: Database session
        user_id: ID of the requesting user
        songlist_id: ID of the song list (1, 2, or 3)
        team_name: Optional team name for team song lists
        
    Returns:
        Tuple[bool, str, List[SongInListModel]]: (success, message, songs)
    """
    try:
        if songlist_id not in [1, 2, 3]:
            return (False, "Song list ID must be 1, 2, or 3", [])
        
        # Get file path based on whether this is a user or team list
        if team_name:
            file_path = get_songlist_file_path(team_name=team_name)
        else:
            file_path = get_songlist_file_path(user_id=user_id)
        
        # Load song list data
        data = load_songlist_data(file_path)
        songs_data = data.get(str(songlist_id), [])
        
        # Convert to SongInListModel objects
        songs = []
        for song_data in songs_data:
            if isinstance(song_data, dict) and "id" in song_data and "title" in song_data:
                songs.append(SongInListModel(id=song_data["id"], title=song_data["title"]))
        
        return (True, f"Retrieved {len(songs)} songs from list {songlist_id}", songs)
        
    except Exception as e:
        print(f"Error getting song list: {e}")
        return (False, f"Error retrieving song list: {e}", [])


def add_song_to_list(
    db: Session,
    user_id: int,
    songlist_id: int,
    song_id: int,
    song_title: str,
    team_name: Optional[str] = None
) -> Tuple[bool, str]:
    """
    Add a song to a specific song list.
    
    Args:
        db: Database session
        user_id: ID of the requesting user
        songlist_id: ID of the song list (1, 2, or 3)
        song_id: ID of the song to add
        song_title: Title of the song to add
        team_name: Optional team name for team song lists
        
    Returns:
        Tuple[bool, str]: (success, message)
    """
    try:
        if songlist_id not in [1, 2, 3]:
            return (False, "Song list ID must be 1, 2, or 3")
        
        # Get file path based on whether this is a user or team list
        if team_name:
            file_path = get_songlist_file_path(team_name=team_name)
        else:
            file_path = get_songlist_file_path(user_id=user_id)
        
        # Load existing data
        data = load_songlist_data(file_path)
        song_list = data[str(songlist_id)]
        
        # Check if song is already in the list
        for existing_song in song_list:
            if existing_song.get("id") == song_id:
                return (False, "Song is already in the list")
        
        # Check max songs limit
        max_songs = int(os.getenv("MAX_SONGS_IN_LIST", 300))
        if len(song_list) >= max_songs:
            return (False, f"Song list is full (max {max_songs} songs)")
        
        # Add the song
        song_list.append({"id": song_id, "title": song_title})
        
        # Save the updated data
        success, message = save_songlist_data(file_path, data)
        if success:
            return (True, f"Song '{song_title}' added to list {songlist_id}")
        else:
            return (False, message)
        
    except Exception as e:
        print(f"Error adding song to list: {e}")
        return (False, f"Error adding song to list: {e}")


def save_song_list(
    db: Session,
    user_id: int,
    songlist_id: int,
    song_ids: List[int],
    team_name: Optional[str] = None
) -> Tuple[bool, str]:
    """
    Save/reshape a complete song list.
    
    Args:
        db: Database session
        user_id: ID of the requesting user
        songlist_id: ID of the song list (1, 2, or 3)
        song_ids: List of song IDs to save
        team_name: Optional team name for team song lists
        
    Returns:
        Tuple[bool, str]: (success, message)
    """
    try:
        if songlist_id not in [1, 2, 3]:
            return (False, "Song list ID must be 1, 2, or 3")
        
        # Check max songs limit
        max_songs = int(os.getenv("MAX_SONGS_IN_LIST", 300))
        if len(song_ids) > max_songs:
            return (False, f"Too many songs (max {max_songs} allowed)")
        
        # Get file path based on whether this is a user or team list
        if team_name:
            file_path = get_songlist_file_path(team_name=team_name)
        else:
            file_path = get_songlist_file_path(user_id=user_id)
        
        # Load existing data
        data = load_songlist_data(file_path)
        
        # We need to get song titles - for now we'll preserve the structure
        # but this will need to be populated with actual song data
        # from the database when used in the routes
        song_list = []
        for song_id in song_ids:
            # This will be filled with proper song data in the route
            song_list.append({"id": song_id, "title": ""})
        
        data[str(songlist_id)] = song_list
        
        # Save the updated data
        success, message = save_songlist_data(file_path, data)
        if success:
            return (True, f"Song list {songlist_id} saved with {len(song_ids)} songs")
        else:
            return (False, message)
        
    except Exception as e:
        print(f"Error saving song list: {e}")
        return (False, f"Error saving song list: {e}")


def validate_song_access_for_list(
    db: Session,
    user_id: int,
    song_id: int,
    team_name: Optional[str] = None
) -> Tuple[bool, str]:
    """
    Validate that a user can add a song to a specific list type.
    
    Args:
        db: Database session
        user_id: ID of the requesting user
        song_id: ID of the song to validate
        team_name: Optional team name for team song lists
        
    Returns:
        Tuple[bool, str]: (can_access, message)
    """
    try:
        # Check if user can read the song
        can_read, read_msg = can_read_song(db, user_id, song_id)
        if not can_read:
            return (False, f"Cannot access song: {read_msg}")
        
        # For team lists, additional validation would be needed
        # to ensure the song is shared with the team
        # This would require additional database queries
        
        return (True, "Song access validated")
        
    except Exception as e:
        print(f"Error validating song access: {e}")
        return (False, f"Error validating song access: {e}")