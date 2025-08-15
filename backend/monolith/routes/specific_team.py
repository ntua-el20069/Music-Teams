from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from backend.monolith.database.database import get_db
from backend.monolith.models.models import TeamModel
from backend.monolith.routes.home import get_current_user
from backend.monolith.routes.teams import get_teams_of_user, team_if_enrolled
from backend.monolith.utils.all import (
    get_all_composers_in_team,
    get_all_lyricists_in_team,
    get_all_songs_in_team,
)

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/all-composers", summary="Get all composers in a specific team")
async def get_specific_team_composers(
    db: db_dependency,
    team_name: str,
    current_user: dict = Depends(get_current_user),
    teams: List[TeamModel] = Depends(get_teams_of_user)
) -> JSONResponse:
    """
    Get all composers that are in songs in a specific team.
    Requires authenticated user, access to team_data cookie, and enrollment in the specified team.
    
    Args:
        team_name: Name of the team to get composers from
    
    Returns:
        JSONResponse with list of composer names
        
    Raises:
        HTTPException with status 401 if user is not authenticated
        HTTPException with status 428 if team_data cookie is missing or invalid
        HTTPException with status 404 if team doesn't exist or user is not enrolled
        HTTPException with status 500 if database error occurs
    """
    try:
        # Verify user is enrolled in the specified team
        team = team_if_enrolled(team_name, teams)
        
        success, msg, composers = get_all_composers_in_team(db, team_name)
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=msg
            )
        
        return JSONResponse(
            status_code=200,
            content={"message": msg, "composers": composers}
        )
        
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(f"Unexpected error in get_specific_team_composers: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while retrieving composers from the specified team."
        )


@router.get("/all-lyricists", summary="Get all lyricists in a specific team")
async def get_specific_team_lyricists(
    db: db_dependency,
    team_name: str,
    current_user: dict = Depends(get_current_user),
    teams: List[TeamModel] = Depends(get_teams_of_user)
) -> JSONResponse:
    """
    Get all lyricists that are in songs in a specific team.
    Requires authenticated user, access to team_data cookie, and enrollment in the specified team.
    
    Args:
        team_name: Name of the team to get lyricists from
    
    Returns:
        JSONResponse with list of lyricist names
        
    Raises:
        HTTPException with status 401 if user is not authenticated
        HTTPException with status 428 if team_data cookie is missing or invalid
        HTTPException with status 404 if team doesn't exist or user is not enrolled
        HTTPException with status 500 if database error occurs
    """
    try:
        # Verify user is enrolled in the specified team
        team = team_if_enrolled(team_name, teams)
        
        success, msg, lyricists = get_all_lyricists_in_team(db, team_name)
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=msg
            )
        
        return JSONResponse(
            status_code=200,
            content={"message": msg, "lyricists": lyricists}
        )
        
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(f"Unexpected error in get_specific_team_lyricists: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while retrieving lyricists from the specified team."
        )


@router.get("/all-songs", summary="Get all songs in a specific team")
async def get_specific_team_songs(
    db: db_dependency,
    team_name: str,
    current_user: dict = Depends(get_current_user),
    teams: List[TeamModel] = Depends(get_teams_of_user)
) -> JSONResponse:
    """
    Get all songs in a specific team.
    Requires authenticated user, access to team_data cookie, and enrollment in the specified team.
    
    Args:
        team_name: Name of the team to get songs from
    
    Returns:
        JSONResponse with list of song titles
        
    Raises:
        HTTPException with status 401 if user is not authenticated
        HTTPException with status 428 if team_data cookie is missing or invalid
        HTTPException with status 404 if team doesn't exist or user is not enrolled
        HTTPException with status 500 if database error occurs
    """
    try:
        # Verify user is enrolled in the specified team
        team = team_if_enrolled(team_name, teams)
        
        success, msg, songs = get_all_songs_in_team(db, team_name)
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=msg
            )
        
        return JSONResponse(
            status_code=200,
            content={"message": msg, "songs": songs}
        )
        
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(f"Unexpected error in get_specific_team_songs: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while retrieving songs from the specified team."
        )