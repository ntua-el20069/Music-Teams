"""
Public endpoints router.
These endpoints provide access to public songs data.
"""

from fastapi import APIRouter, HTTPException
from ..models.responses import ComposersResponse, LyricistsResponse, SongsResponse, ErrorResponse
from ..utils.database import get_public_composers, get_public_lyricists, get_public_songs

router = APIRouter()


@router.get(
    "/all-composers",
    response_model=ComposersResponse,
    responses={500: {"model": ErrorResponse}},
    summary="Get all composers from public songs",
    description="Returns a list of all composers who have written music for public songs."
)
async def get_all_public_composers():
    """Get all composers from public songs."""
    try:
        composers = get_public_composers()
        return ComposersResponse(composers=composers, count=len(composers))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get(
    "/all-lyricists",
    response_model=LyricistsResponse,
    responses={500: {"model": ErrorResponse}},
    summary="Get all lyricists from public songs",
    description="Returns a list of all lyricists who have written lyrics for public songs."
)
async def get_all_public_lyricists():
    """Get all lyricists from public songs."""
    try:
        lyricists = get_public_lyricists()
        return LyricistsResponse(lyricists=lyricists, count=len(lyricists))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get(
    "/all-songs",
    response_model=SongsResponse,
    responses={500: {"model": ErrorResponse}},
    summary="Get all public songs",
    description="Returns a list of all public songs."
)
async def get_all_public_songs():
    """Get all public songs."""
    try:
        songs = get_public_songs()
        return SongsResponse(songs=songs, count=len(songs))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")