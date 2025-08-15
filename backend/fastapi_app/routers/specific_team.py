"""
Specific Team endpoints router.
These endpoints provide access to songs from a specific team.
"""

from fastapi import APIRouter, HTTPException, Depends, Query
from typing import Optional
from ..models.responses import ComposersResponse, LyricistsResponse, SongsResponse, ErrorResponse
from ..utils.database import get_team_composers, get_team_lyricists, get_team_songs
from ..utils.auth import get_current_user, team_if_enrolled, validate_team_name

router = APIRouter()


@router.get(
    "/all-composers",
    response_model=ComposersResponse,
    responses={
        400: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        500: {"model": ErrorResponse}
    },
    summary="Get all composers from specific team songs",
    description="Returns a list of all composers who have written music for songs in the specified team."
)
async def get_specific_team_composers(
    team_name: Optional[str] = Query(None, description="Name of the team"),
    current_user: str = Depends(get_current_user)
):
    """Get all composers from a specific team's songs."""
    try:
        # Validate team_name parameter
        validated_team_name = validate_team_name(team_name)
        
        # Check if user is enrolled in the team
        team_if_enrolled(validated_team_name, current_user)
        
        # Get composers
        composers = get_team_composers(validated_team_name)
        return ComposersResponse(composers=composers, count=len(composers))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get(
    "/all-lyricists",
    response_model=LyricistsResponse,
    responses={
        400: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        500: {"model": ErrorResponse}
    },
    summary="Get all lyricists from specific team songs",
    description="Returns a list of all lyricists who have written lyrics for songs in the specified team."
)
async def get_specific_team_lyricists(
    team_name: Optional[str] = Query(None, description="Name of the team"),
    current_user: str = Depends(get_current_user)
):
    """Get all lyricists from a specific team's songs."""
    try:
        # Validate team_name parameter
        validated_team_name = validate_team_name(team_name)
        
        # Check if user is enrolled in the team
        team_if_enrolled(validated_team_name, current_user)
        
        # Get lyricists
        lyricists = get_team_lyricists(validated_team_name)
        return LyricistsResponse(lyricists=lyricists, count=len(lyricists))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get(
    "/all-songs",
    response_model=SongsResponse,
    responses={
        400: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        500: {"model": ErrorResponse}
    },
    summary="Get all songs from specific team",
    description="Returns a list of all songs from the specified team."
)
async def get_specific_team_songs(
    team_name: Optional[str] = Query(None, description="Name of the team"),
    current_user: str = Depends(get_current_user)
):
    """Get all songs from a specific team."""
    try:
        # Validate team_name parameter
        validated_team_name = validate_team_name(team_name)
        
        # Check if user is enrolled in the team
        team_if_enrolled(validated_team_name, current_user)
        
        # Get songs
        songs = get_team_songs(validated_team_name)
        return SongsResponse(songs=songs, count=len(songs))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")