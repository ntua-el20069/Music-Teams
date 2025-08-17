"""
Song management endpoints for Music Teams application.

This module contains API endpoints for creating, updating, and retrieving songs
with proper authentication and team-based access control.
"""

from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field

from backend.monolith.database.database import get_db
from backend.monolith.models.models import SongModel, Song
from backend.monolith.routes.home import get_current_user
from backend.monolith.routes.teams import get_teams_of_user
from backend.monolith.utils.song_access import (
    song_exists_by_user,
    can_write_song,
    can_read_song,
    get_song_by_id_with_ownership
)
from backend.monolith.utils.create_song import (
    manage_song,
    get_song_with_teams,
    transpose_chords,
    update_song_chords_only
)

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]


class SongInsertModel(BaseModel):
    """Model for song insertion requests."""
    title: str = Field(..., title="Song Title")
    composers: List[str] = Field(default=[], title="Composers")
    lyricists: List[str] = Field(default=[], title="Lyricists")
    lyrics: str = Field(..., title="Song Lyrics")
    public: bool = Field(default=False, title="Public")
    shared_with_teams: List[str] = Field(default=[], title="Shared With Teams")


class SongUpdateModel(BaseModel):
    """Model for song update requests."""
    id: int = Field(..., title="Song ID")
    title: str = Field(..., title="Song Title")
    composers: List[str] = Field(default=[], title="Composers")
    lyricists: List[str] = Field(default=[], title="Lyricists")
    lyrics: str = Field(..., title="Song Lyrics")
    public: bool = Field(default=False, title="Public")
    shared_with_teams: List[str] = Field(default=[], title="Shared With Teams")


class TransportoModel(BaseModel):
    """Model for permanent transposition requests."""
    song_id: int = Field(..., title="Song ID")
    transporto_units: int = Field(..., title="Transposition Units")


@router.post("/insert-song", summary="Insert a new song")
async def insert_song(
    db: db_dependency,
    song_data: SongInsertModel,
    current_user: dict = Depends(get_current_user),
    teams: List = Depends(get_teams_of_user)
) -> JSONResponse:
    """
    Insert a new song with proper authentication and team permissions.
    
    Requires:
    - Authenticated user
    - team_data cookie with user teams
    - User must have can_edit = True in all teams specified in shared_with_teams
    """
    try:
        user_id = current_user["user_id"]
        user_teams = [team.team_name for team in teams]
        
        # Check if user can write to all specified teams
        can_write, write_msg = can_write_song(db, user_id, song_data.shared_with_teams)
        if not can_write:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=write_msg
            )
        
        # Check if song with same title already exists by this user
        exists, exists_msg = song_exists_by_user(db, user_id, song_data.title)
        if exists:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=exists_msg
            )
        
        # Create SongModel instance
        song_model = SongModel(
            title=song_data.title,
            lyrics=song_data.lyrics,
            chords="",  # Initially empty, will be added later
            made_by=user_id,
            public=song_data.public,
            composers=song_data.composers,
            lyricists=song_data.lyricists,
            shared_with_teams=song_data.shared_with_teams
        )
        
        # Insert the song
        success, message, song_id = manage_song(
            db=db,
            song_model=song_model,
            update_chords=False,
            update_song=False
        )
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=message
            )
        
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": message,
                "song_id": song_id,
                "status": "success"
            }
        )
        
    except HTTPException:
        raise
    except Exception as exc:
        print(f"Unexpected error in insert_song: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {exc}"
        )


@router.post("/update-song", summary="Update an existing song")
async def update_song(
    db: db_dependency,
    song_data: SongUpdateModel,
    current_user: dict = Depends(get_current_user),
    teams: List = Depends(get_teams_of_user)
) -> JSONResponse:
    """
    Update an existing song with proper authentication and ownership checks.
    
    Requires:
    - Authenticated user
    - team_data cookie with user teams
    - Song must be made_by this user
    - User must have can_edit = True in all teams specified in shared_with_teams
    """
    try:
        user_id = current_user["user_id"]
        
        # Check if song exists and is owned by this user
        existing_song, ownership_msg = get_song_by_id_with_ownership(db, song_data.id, user_id)
        if not existing_song:
            if "not found" in ownership_msg:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=ownership_msg
                )
            else:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=ownership_msg
                )
        
        # Check if user can write to all specified teams
        can_write, write_msg = can_write_song(db, user_id, song_data.shared_with_teams)
        if not can_write:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=write_msg
            )
        
        # Check for title conflicts (only if title changed)
        if existing_song.title != song_data.title:
            exists, exists_msg = song_exists_by_user(db, user_id, song_data.title)
            if exists:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=exists_msg
                )
        
        # Create SongModel instance
        song_model = SongModel(
            id=song_data.id,
            title=song_data.title,
            lyrics=song_data.lyrics,
            chords=existing_song.chords,  # Keep existing chords
            made_by=user_id,
            public=song_data.public,
            composers=song_data.composers,
            lyricists=song_data.lyricists,
            shared_with_teams=song_data.shared_with_teams
        )
        
        # Update the song
        success, message, _ = manage_song(
            db=db,
            song_model=song_model,
            update_chords=False,
            update_song=True
        )
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=message
            )
        
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": message,
                "status": "success"
            }
        )
        
    except HTTPException:
        raise
    except Exception as exc:
        print(f"Unexpected error in update_song: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {exc}"
        )


@router.post("/permanent-transporto", summary="Permanently transpose song chords")
async def permanent_transporto(
    db: db_dependency,
    transporto_data: TransportoModel,
    current_user: dict = Depends(get_current_user),
    teams: List = Depends(get_teams_of_user)
) -> JSONResponse:
    """
    Permanently transpose the chords of a song in the database.
    
    Requires:
    - Authenticated user
    - team_data cookie with user teams  
    - Song must be made_by this user
    - User must have can_edit = True in all teams the song is shared with
    """
    try:
        user_id = current_user["user_id"]
        
        # Get song and its teams
        song, song_teams = get_song_with_teams(db, transporto_data.song_id)
        if not song:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Song with ID {transporto_data.song_id} not found"
            )
        
        # Check ownership
        if song.made_by != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can only transpose songs that you created"
            )
        
        # Check if user can write to all teams the song is shared with
        can_write, write_msg = can_write_song(db, user_id, song_teams)
        if not can_write:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=write_msg
            )
        
        # Transpose the chords
        transposed_chords = transpose_chords(song.chords, transporto_data.transporto_units)
        
        # Update only the chords field
        success, message = update_song_chords_only(db, song.id, transposed_chords)
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=message
            )
        
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": f"Song chords transposed by {transporto_data.transporto_units} semitones",
                "status": "success"
            }
        )
        
    except HTTPException:
        raise
    except Exception as exc:
        print(f"Unexpected error in permanent_transporto: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {exc}"
        )


@router.get("/song", summary="Get song with optional transposition")
async def get_song(
    db: db_dependency,
    song_id: int,
    transporto_units: int = 0,
    current_user: dict = Depends(get_current_user),
    teams: List = Depends(get_teams_of_user)
) -> JSONResponse:
    """
    Get a song with optional chord transposition (no database changes).
    
    Requires:
    - Authenticated user
    - team_data cookie with user teams
    - User must be enrolled in at least one team the song is shared with
    """
    try:
        user_id = current_user["user_id"]
        
        # Get song and its teams
        song, song_teams = get_song_with_teams(db, song_id)
        if not song:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Song with ID {song_id} not found"
            )
        
        # Check if song is public or if user owns it
        if not song.public and song.made_by != user_id:
            # Check read permissions
            can_read, read_msg = can_read_song(db, user_id, song_teams)
            if not can_read:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=read_msg
                )
        
        # Get composers and lyricists from relationships
        composers = [c.name for c in song.composers]
        lyricists = [l.name for l in song.lyricists]
        
        # Apply transposition if requested
        chords = song.chords
        if transporto_units != 0:
            chords = transpose_chords(chords, transporto_units)
        
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "id": song.id,
                "title": song.title,
                "lyrics": song.lyrics,
                "chords": chords,
                "likes": song.likes,
                "made_by": song.made_by,
                "public": song.public,
                "composers": composers,
                "lyricists": lyricists,
                "shared_with_teams": song_teams,
                "transposed_by": transporto_units if transporto_units != 0 else None
            }
        )
        
    except HTTPException:
        raise
    except Exception as exc:
        print(f"Unexpected error in get_song: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {exc}"
        )