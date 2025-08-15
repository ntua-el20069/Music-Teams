"""
MyTeams endpoints router.
These endpoints provide access to songs from the current user's teams.
"""

from fastapi import APIRouter, HTTPException, Depends
from ..models.responses import ComposersResponse, LyricistsResponse, SongsResponse, ErrorResponse
from ..utils.database import get_myteams_composers, get_myteams_lyricists, get_myteams_songs
from ..utils.auth import get_current_user

router = APIRouter()


@router.get(
    "/all-composers",
    response_model=ComposersResponse,
    responses={
        401: {"model": ErrorResponse},
        500: {"model": ErrorResponse}
    },
    summary="Get all composers from user's team songs",
    description="Returns a list of all composers who have written music for songs in the current user's teams."
)
async def get_myteams_composers(current_user: str = Depends(get_current_user)):
    """Get all composers from the current user's team songs."""
    try:
        composers = get_myteams_composers(current_user)
        return ComposersResponse(composers=composers, count=len(composers))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get(
    "/all-lyricists",
    response_model=LyricistsResponse,
    responses={
        401: {"model": ErrorResponse},
        500: {"model": ErrorResponse}
    },
    summary="Get all lyricists from user's team songs",
    description="Returns a list of all lyricists who have written lyrics for songs in the current user's teams."
)
async def get_myteams_lyricists(current_user: str = Depends(get_current_user)):
    """Get all lyricists from the current user's team songs."""
    try:
        lyricists = get_myteams_lyricists(current_user)
        return LyricistsResponse(lyricists=lyricists, count=len(lyricists))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get(
    "/all-songs",
    response_model=SongsResponse,
    responses={
        401: {"model": ErrorResponse},
        500: {"model": ErrorResponse}
    },
    summary="Get all songs from user's teams",
    description="Returns a list of all songs from the current user's teams."
)
async def get_myteams_songs(current_user: str = Depends(get_current_user)):
    """Get all songs from the current user's teams."""
    try:
        songs = get_myteams_songs(current_user)
        return SongsResponse(songs=songs, count=len(songs))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")