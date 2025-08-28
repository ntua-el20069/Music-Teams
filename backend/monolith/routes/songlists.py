"""
Song list management endpoints for Music Teams application.

This module contains API endpoints for managing user and team song lists
with proper authentication and access control.
"""

import os
from typing import Annotated, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from backend.monolith.database.database import get_db
from backend.monolith.models.models import (
    Song,
    SongInListModel,
    SongListSaveModel,
)
from backend.monolith.routes.home import get_current_user
from backend.monolith.routes.teams import get_teams_of_user, team_if_enrolled
from backend.monolith.utils.song_access import can_read_song, can_write_song
from backend.monolith.utils.songlists import (
    add_song_to_list,
    get_song_list,
    save_song_list,
    validate_song_access_for_list,
)

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/get-list", summary="Get songs from a song list")
async def get_songlist(
    db: db_dependency,
    songlist: int = Query(..., ge=1, le=3, description="Song list number (1, 2, or 3)"),
    team_name: Optional[str] = Query(None, description="Team name for team song lists"),
    current_user: dict = Depends(get_current_user),
    teams: List = Depends(get_teams_of_user),
) -> JSONResponse:
    """
    Get songs from a personal or team song list.
    
    Args:
        songlist: Song list number (1, 2, or 3)
        team_name: Optional team name for team song lists
        
    Returns:
        JSONResponse with list of songs in format:
        {
            "songs": [{"id": 234, "title": "Song Title"}, ...]
        }
        
    Raises:
        HTTPException 400: Invalid song list number
        HTTPException 403: User not enrolled in team
        HTTPException 500: Internal server error
    """
    try:
        user_id = current_user["user_id"]
        
        # If team_name is provided, verify user is enrolled in the team
        if team_name:
            team_if_enrolled(team_name, teams)
        
        # Get the song list
        success, message, songs = get_song_list(db, user_id, songlist, team_name)
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=message
            )
        
        # Convert to dict format for JSON response
        songs_data = [{"id": song.id, "title": song.title} for song in songs]
        
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"songs": songs_data}
        )
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Unexpected error in get_songlist: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while retrieving the song list"
        )


@router.get("/add-song", summary="Add a song to a song list")
async def add_song_to_songlist(
    db: db_dependency,
    songlist: int = Query(..., ge=1, le=3, description="Song list number (1, 2, or 3)"),
    song_id: int = Query(..., description="ID of the song to add"),
    team_name: Optional[str] = Query(None, description="Team name for team song lists"),
    current_user: dict = Depends(get_current_user),
    teams: List = Depends(get_teams_of_user),
) -> JSONResponse:
    """
    Add a song to a personal or team song list.
    
    Args:
        songlist: Song list number (1, 2, or 3)
        song_id: ID of the song to add
        team_name: Optional team name for team song lists
        
    Returns:
        JSONResponse with success message
        
    Raises:
        HTTPException 400: Invalid parameters or song list full
        HTTPException 403: User not enrolled in team or doesn't have edit permissions
        HTTPException 404: Song not found or not accessible
        HTTPException 500: Internal server error
    """
    try:
        user_id = current_user["user_id"]
        
        # If team_name is provided, verify user is enrolled and has edit permissions
        if team_name:
            team_if_enrolled(team_name, teams)
            # For team lists, check if user has can_edit = True
            can_write, write_msg = can_write_song(db, user_id, [team_name])
            if not can_write:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=write_msg
                )
        
        # Validate song access
        can_access, access_msg = validate_song_access_for_list(db, user_id, song_id, team_name)
        if not can_access:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=access_msg
            )
        
        # Check if user can read the song to get its title
        can_read, read_msg = can_read_song(db, user_id, song_id)
        if not can_read:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Song not found or not accessible"
            )
        
        # Get song title from database
        # For now, we'll use a placeholder - this should query the actual song
        from backend.monolith.utils.song_access import get_song_by_id_with_ownership
        song, song_msg = get_song_by_id_with_ownership(db, song_id, user_id)
        if song is None:
            # Try to get basic song info if user can read it
            db_song = db.query(Song).filter(Song.id == song_id).first()
            if db_song is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Song not found"
                )
            song_title = db_song.title
        else:
            song_title = song.title
        
        # Add the song to the list
        success, message = add_song_to_list(db, user_id, songlist, song_id, song_title, team_name)
        
        if not success:
            if "already in the list" in message:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=message
                )
            elif "full" in message:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=message
                )
            else:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=message
                )
        
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": message}
        )
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Unexpected error in add_song_to_songlist: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while adding the song to the list"
        )


@router.post("/save-list", summary="Save/reshape a song list")
async def save_songlist(
    db: db_dependency,
    song_list_data: SongListSaveModel,
    current_user: dict = Depends(get_current_user),
    teams: List = Depends(get_teams_of_user),
) -> JSONResponse:
    """
    Save/reshape a complete song list.
    
    Args:
        song_list_data: Song list data containing songlist_id, songs, and optional team_name
        
    Returns:
        JSONResponse with success message
        
    Raises:
        HTTPException 400: Invalid parameters or too many songs
        HTTPException 403: User not enrolled in team or doesn't have edit permissions
        HTTPException 404: One or more songs not accessible
        HTTPException 500: Internal server error
    """
    try:
        user_id = current_user["user_id"]
        team_name = song_list_data.team_name
        
        # If team_name is provided, verify user is enrolled and has edit permissions
        if team_name:
            team_if_enrolled(team_name, teams)
            # For team lists, check if user has can_edit = True
            can_write, write_msg = can_write_song(db, user_id, [team_name])
            if not can_write:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=write_msg
                )
        
        # Validate access to all songs in the list
        inaccessible_songs = []
        for song_id in song_list_data.songs:
            can_access, access_msg = validate_song_access_for_list(db, user_id, song_id, team_name)
            if not can_access:
                inaccessible_songs.append(song_id)
        
        if inaccessible_songs:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Cannot access songs with IDs: {inaccessible_songs}"
            )
        
        # We need to get song titles for all songs
        # For now, we'll do a basic implementation and improve later
        song_data_list = []
        
        for song_id in song_list_data.songs:
            db_song = db.query(Song).filter(Song.id == song_id).first()
            if db_song is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Song with ID {song_id} not found"
                )
            song_data_list.append({"id": song_id, "title": db_song.title})
        
        # Save the song list with proper data structure
        # We'll modify the save_song_list function to accept full song data
        success, message = save_song_list_with_titles(
            db, user_id, song_list_data.songlist_id, song_data_list, team_name
        )
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=message
            )
        
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": message}
        )
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Unexpected error in save_songlist: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while saving the song list"
        )


def save_song_list_with_titles(
    db: Session,
    user_id: int,
    songlist_id: int,
    song_data_list: List[dict],
    team_name: Optional[str] = None
) -> tuple[bool, str]:
    """
    Helper function to save song list with full song data including titles.
    """
    try:
        from backend.monolith.utils.songlists import get_songlist_file_path, load_songlist_data, save_songlist_data
        
        if songlist_id not in [1, 2, 3]:
            return (False, "Song list ID must be 1, 2, or 3")
        
        # Check max songs limit
        max_songs = int(os.getenv("MAX_SONGS_IN_LIST", 300))
        if len(song_data_list) > max_songs:
            return (False, f"Too many songs (max {max_songs} allowed)")
        
        # Get file path based on whether this is a user or team list
        if team_name:
            file_path = get_songlist_file_path(team_name=team_name)
        else:
            file_path = get_songlist_file_path(user_id=user_id)
        
        # Load existing data
        data = load_songlist_data(file_path)
        
        # Update the specific list
        data[str(songlist_id)] = song_data_list
        
        # Save the updated data
        success, message = save_songlist_data(file_path, data)
        if success:
            return (True, f"Song list {songlist_id} saved with {len(song_data_list)} songs")
        else:
            return (False, message)
        
    except Exception as e:
        print(f"Error saving song list with titles: {e}")
        return (False, f"Error saving song list: {e}")