"""
My Songs management endpoints for Music Teams application.

This module contains API endpoints for retrieving user's own songs,
composers, and lyricists with proper authentication.
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from backend.monolith.database.database import get_db
from backend.monolith.routes.home import get_current_user
from backend.monolith.utils.my_songs import (
    get_user_composers,
    get_user_lyricists,
    get_user_songs,
)

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/all-songs", summary="Get all songs created by the current user")
async def get_my_songs(
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
) -> JSONResponse:
    """
    Get all songs created by the current user.\n

    Returns on success (200):\n
    - songs: list[Dict[str,str]] (list of songs with id and title)\n
    - message: str (status message)\n

    Error codes:\n
    - 500: Internal server error\n

    Requires:\n
    - Authenticated user\n
    - team_data cookie with user teams\n

    Returns songs where song.made_by = current_user.user_id
    """
    try:
        user_id = current_user["user_id"]

        # Get all songs created by this user
        success, message, songs = get_user_songs(db, user_id)

        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=message
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": message, "songs": songs},
        )

    except HTTPException:
        raise
    except Exception as exc:
        print(f"Unexpected error in get_my_songs: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {exc}",
        )


@router.get("/all-composers", summary="Get all composers from current user's songs")
async def get_my_composers(
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
) -> JSONResponse:
    """
    Get all unique composers from songs created by the current user.\n

    Returns on success (200):\n
    - composers: list[str] (list of unique composer names)\n
    - message: str (status message)\n

    Error codes:\n
    - 500: Internal server error\n

    Requires:\n
    - Authenticated user\n
    - team_data cookie with user teams\n

    Returns composers from songs where song.made_by = current_user.user_id
    """
    try:
        user_id = current_user["user_id"]

        # Get all composers from this user's songs
        success, message, composers = get_user_composers(db, user_id)

        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=message
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": message, "composers": composers},
        )

    except HTTPException:
        raise
    except Exception as exc:
        print(f"Unexpected error in get_my_composers: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {exc}",
        )


@router.get("/all-lyricists", summary="Get all lyricists from current user's songs")
async def get_my_lyricists(
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
) -> JSONResponse:
    """
    Get all unique lyricists from songs created by the current user.\n

    Returns on success (200):\n
    - lyricists: list[str] (list of unique lyricist names)\n
    - message: str (status message)\n

    Error codes:\n
    - 500: Internal server error\n

    Requires:\n
    - Authenticated user\n
    - team_data cookie with user teams\n

    Returns lyricists from songs where song.made_by = current_user.user_id
    """
    try:
        user_id = current_user["user_id"]

        # Get all lyricists from this user's songs
        success, message, lyricists = get_user_lyricists(db, user_id)

        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=message
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": message, "lyricists": lyricists},
        )

    except HTTPException:
        raise
    except Exception as exc:
        print(f"Unexpected error in get_my_lyricists: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {exc}",
        )
