"""
Song management endpoints for Music Teams application.

This module contains API endpoints for creating, updating, and retrieving songs
with proper authentication and team-based access control.
"""

from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from backend.monolith.database.database import get_db
from backend.monolith.models.models import (
    SongInsertModel,
    SongModel,
    SongUpdateModel,
    TransportoModel,
    UpdateLyricsChordsModel,
)
from backend.monolith.routes.home import get_current_user
from backend.monolith.routes.teams import get_teams_of_user
from backend.monolith.utils.create_song import (
    get_song_with_teams,
    manage_song,
    transpose_chords,
    update_song_chords_only,
    update_song_lyrics_chords,
)
from backend.monolith.utils.song_access import (
    can_read_song,
    can_write_song,
    get_song_by_id_with_ownership,
    song_exists_by_user,
)

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/insert-song", summary="Insert a new song")
async def insert_song(
    db: db_dependency,
    song_data: SongInsertModel,
    current_user: dict = Depends(get_current_user),
    teams: List = Depends(get_teams_of_user),
) -> JSONResponse:
    """
    Insert a new song with proper authentication and team permissions.\n

    Payload:\n
    - title: str (song title)\n
    - composers: list[str] (list of composer names)\n
    - lyricists: list[str] (list of lyricist names)\n
    - lyrics: str (song lyrics)\n
    - public: bool (whether song is public)\n
    - shared_with_teams: list[str] (teams to share the song with)\n

    Returns on success (201):\n
    - message: str (success message)\n
    - song_id: int (ID of created song)\n
    - status: "success"\n

    Error codes:\n
    - 403: User lacks edit permissions in specified teams\n
    - 409: Song with same title already exists by this user\n
    - 500: Internal server error\n

    Requires:\n
    - Authenticated user\n
    - team_data cookie with user teams\n
    - User must have can_edit = True in all teams specified in shared_with_teams
    """
    try:
        user_id = current_user["user_id"]

        # Check if user can write to all specified teams
        can_write, write_msg = can_write_song(db, user_id, song_data.shared_with_teams)
        if not can_write:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=write_msg)

        # Check if song with same title already exists by this user
        exists, exists_msg = song_exists_by_user(db, user_id, song_data.title)
        if exists:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=exists_msg)

        # Create SongModel instance
        song_model = SongModel(
            title=song_data.title,
            lyrics=song_data.lyrics,
            chords="",  # Initially empty, will be added later
            made_by=user_id,
            public=song_data.public,
            composers=song_data.composers,
            lyricists=song_data.lyricists,
            shared_with_teams=song_data.shared_with_teams,
        )

        # Insert the song
        success, message, song_id = manage_song(
            db=db, song_model=song_model, update_chords=False, update_song=False
        )

        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=message
            )

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"message": message, "song_id": song_id, "status": "success"},
        )

    except HTTPException:
        raise
    except Exception as exc:
        print(f"Unexpected error in insert_song: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {exc}",
        )


@router.post("/update-song", summary="Update an existing song")
async def update_song(
    db: db_dependency,
    song_data: SongUpdateModel,
    current_user: dict = Depends(get_current_user),
    teams: List = Depends(get_teams_of_user),
) -> JSONResponse:
    """
    Update an existing song with proper authentication and ownership checks.\n

    Payload:\n
    - id: int (song ID)\n
    - title: str (song title)\n
    - composers: list[str] (list of composer names)\n
    - lyricists: list[str] (list of lyricist names)\n
    - lyrics: str (song lyrics)\n
    - public: bool (whether song is public)\n
    - shared_with_teams: list[str] (teams to share the song with)\n

    Returns on success (200):\n
    - message: str (success message)\n
    - status: "success"\n

    Error codes:\n
    - 403: User lacks edit permissions or doesn't own the song\n
    - 404: Song not found\n
    - 409: Song with same title already exists by this user\n
    - 500: Internal server error\n

    Requires:\n
    - Authenticated user\n
    - team_data cookie with user teams\n
    - Song must be made_by this user\n
    - User must have can_edit = True in all teams specified in shared_with_teams
    """
    try:
        user_id = current_user["user_id"]

        # Check if song exists and is owned by this user
        existing_song, ownership_msg = get_song_by_id_with_ownership(
            db, song_data.id, user_id
        )
        if not existing_song:
            if "not found" in ownership_msg:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail=ownership_msg
                )
            else:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN, detail=ownership_msg
                )

        # Check if user can write to all specified teams
        can_write, write_msg = can_write_song(db, user_id, song_data.shared_with_teams)
        if not can_write:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=write_msg)

        # Check for title conflicts (only if title changed)
        if existing_song.title != song_data.title:
            exists, exists_msg = song_exists_by_user(db, user_id, song_data.title)
            if exists:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT, detail=exists_msg
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
            shared_with_teams=song_data.shared_with_teams,
        )

        # Update the song
        success, message, _ = manage_song(
            db=db, song_model=song_model, update_chords=False, update_song=True
        )

        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=message
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": message, "status": "success"},
        )

    except HTTPException:
        raise
    except Exception as exc:
        print(f"Unexpected error in update_song: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {exc}",
        )


@router.post("/permanent-transporto", summary="Permanently transpose song chords")
async def permanent_transporto(
    db: db_dependency,
    transporto_data: TransportoModel,
    current_user: dict = Depends(get_current_user),
    teams: List = Depends(get_teams_of_user),
) -> JSONResponse:
    """
    Permanently transpose the chords of a song in the database.\n

    Payload:\n
    - song_id: int (ID of song to transpose)\n
    - transporto_units: int (number of semitones to transpose)\n

    Returns on success (200):\n
    - message: str (success message with transposition info)\n
    - status: "success"\n

    Error codes:\n
    - 403: User lacks edit permissions or doesn't own the song\n
    - 404: Song not found\n
    - 500: Internal server error\n

    Requires:\n
    - Authenticated user\n
    - team_data cookie with user teams\n
    - Song must be made_by this user\n
    - User must have can_edit = True in all teams the song is shared with
    """
    try:
        user_id = current_user["user_id"]

        # Get song and its teams
        song, song_teams = get_song_with_teams(db, transporto_data.song_id)
        if not song:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Song with ID {transporto_data.song_id} not found",
            )

        # Check ownership
        if song.made_by != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can only transpose songs that you created",
            )

        # Check if user can write to all teams the song is shared with
        can_write, write_msg = can_write_song(db, user_id, song_teams)
        if not can_write:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=write_msg)

        # Transpose the chords
        transposed_chords = transpose_chords(
            song.chords, transporto_data.transporto_units
        )

        # Update only the chords field
        success, message = update_song_chords_only(db, song.id, transposed_chords)

        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=message
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": f"chords transposed by {transporto_data.transporto_units} semitones",
                "status": "success",
            },
        )

    except HTTPException:
        raise
    except Exception as exc:
        print(f"Unexpected error in permanent_transporto: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {exc}",
        )


@router.get("/song", summary="Get song with optional transposition")
async def get_song(
    db: db_dependency,
    song_id: int,
    transporto_units: int = 0,
    current_user: dict = Depends(get_current_user),
    teams: List = Depends(get_teams_of_user),
) -> JSONResponse:
    """
    Get a song with optional chord transposition (no database changes).\n

    Query parameters:\n
    - song_id: int (ID of song to retrieve)\n
    - transporto_units: int (optional, semitones to transpose, default 0)\n

    Returns on success (200):\n
    - id: int (song ID)\n
    - title: str (song title)\n
    - lyrics: str (song lyrics)\n
    - chords: str (song chords, possibly transposed)\n
    - likes: int (number of likes)\n
    - made_by: int (user ID of creator)\n
    - public: bool (whether song is public)\n
    - composers: list[str] (composer names)\n
    - lyricists: list[str] (lyricist names)\n
    - shared_with_teams: list[str] (teams song is shared with)\n
    - transposed_by: int|null (transposition applied, if any)\n

    Error codes:\n
    - 403: User lacks read permissions\n
    - 404: Song not found\n
    - 500: Internal server error\n

    Requires:\n
    - Authenticated user\n
    - team_data cookie with user teams\n
    - User must have access (song is public, user owns it, or user is in a team that has access)
    """
    try:
        user_id = current_user["user_id"]

        # Get song and its teams
        song, song_teams = get_song_with_teams(db, song_id)
        if not song:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Song with ID {song_id} not found",
            )

        # Check read permissions
        can_read, read_msg = can_read_song(db, user_id, song_id)
        if not can_read:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=read_msg)

        # Get composers and lyricists from relationships
        composers = [comp.name for comp in song.composers]
        lyricists = [lyr.name for lyr in song.lyricists]

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
                "transposed_by": transporto_units if transporto_units != 0 else None,
            },
        )

    except HTTPException:
        raise
    except Exception as exc:
        print(f"Unexpected error in get_song: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {exc}",
        )


@router.post("/update-lyrics-chords", summary="Update song lyrics and chords")
async def update_lyrics_chords(
    db: db_dependency,
    song_data: UpdateLyricsChordsModel,
    current_user: dict = Depends(get_current_user),
    teams: List = Depends(get_teams_of_user),
) -> JSONResponse:
    """
    Update both lyrics and chords of an existing song.\n

    Payload:\n
    - song_id: int (ID of song to update)\n
    - lyrics: str (new song lyrics)\n
    - chords: str (new song chords)\n

    Returns on success (200):\n
    - message: str (success message)\n
    - status: "success"\n

    Error codes:\n
    - 403: User lacks edit permissions or doesn't own the song\n
    - 404: Song not found\n
    - 500: Internal server error\n

    Requires:\n
    - Authenticated user\n
    - team_data cookie with user teams\n
    - Song must be made_by this user\n
    - User must have can_edit = True in all teams the song is shared with
    """
    try:
        user_id = current_user["user_id"]

        # Check if song exists and is owned by this user
        existing_song, ownership_msg = get_song_by_id_with_ownership(
            db, song_data.song_id, user_id
        )
        if not existing_song:
            if "not found" in ownership_msg:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail=ownership_msg
                )
            else:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN, detail=ownership_msg
                )

        # Get song teams to check permissions
        song, song_teams = get_song_with_teams(db, song_data.song_id)
        if not song:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Song with ID {song_data.song_id} not found",
            )

        # Check if user can write to all teams the song is shared with
        can_write, write_msg = can_write_song(db, user_id, song_teams)
        if not can_write:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=write_msg)

        # Update the song lyrics and chords
        success, message = update_song_lyrics_chords(
            db=db,
            song_id=song_data.song_id,
            new_lyrics=song_data.lyrics,
            new_chords=song_data.chords,
        )

        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=message
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": message, "status": "success"},
        )

    except HTTPException:
        raise
    except Exception as exc:
        print(f"Unexpected error in update_lyrics_chords: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {exc}",
        )
