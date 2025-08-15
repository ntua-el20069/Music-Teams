from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from backend.monolith.database.database import get_db
from backend.monolith.models.models import TeamModel
from backend.monolith.routes.home import get_current_user
from backend.monolith.routes.teams import get_teams_of_user
from backend.monolith.utils.all import (
    get_all_composers_in_user_teams,
    get_all_lyricists_in_user_teams,
    get_all_songs_in_user_teams,
)

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/all-composers", summary="Get all composers in user's teams")
async def get_my_teams_composers(
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
    teams: List[TeamModel] = Depends(get_teams_of_user)
) -> JSONResponse:
    """
    Get all composers that are in songs in teams the user participates in.
    Requires authenticated user and access to team_data cookie.
    
    Returns:
        JSONResponse with list of composer names
        
    Raises:
        HTTPException with status 401 if user is not authenticated
        HTTPException with status 428 if team_data cookie is missing or invalid
        HTTPException with status 500 if database error occurs
    """
    try:
        user_id = current_user["user_id"]
        success, msg, composers = get_all_composers_in_user_teams(db, user_id)
        
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
        print(f"Unexpected error in get_my_teams_composers: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while retrieving composers from your teams."
        )


@router.get("/all-lyricists", summary="Get all lyricists in user's teams")
async def get_my_teams_lyricists(
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
    teams: List[TeamModel] = Depends(get_teams_of_user)
) -> JSONResponse:
    """
    Get all lyricists that are in songs in teams the user participates in.
    Requires authenticated user and access to team_data cookie.
    
    Returns:
        JSONResponse with list of lyricist names
        
    Raises:
        HTTPException with status 401 if user is not authenticated
        HTTPException with status 428 if team_data cookie is missing or invalid
        HTTPException with status 500 if database error occurs
    """
    try:
        user_id = current_user["user_id"]
        success, msg, lyricists = get_all_lyricists_in_user_teams(db, user_id)
        
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
        print(f"Unexpected error in get_my_teams_lyricists: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while retrieving lyricists from your teams."
        )


@router.get("/all-songs", summary="Get all songs in user's teams")
async def get_my_teams_songs(
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
    teams: List[TeamModel] = Depends(get_teams_of_user)
) -> JSONResponse:
    """
    Get all songs in teams the user participates in.
    Requires authenticated user and access to team_data cookie.
    
    Returns:
        JSONResponse with list of song titles
        
    Raises:
        HTTPException with status 401 if user is not authenticated
        HTTPException with status 428 if team_data cookie is missing or invalid
        HTTPException with status 500 if database error occurs
    """
    try:
        user_id = current_user["user_id"]
        success, msg, songs = get_all_songs_in_user_teams(db, user_id)
        
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
        print(f"Unexpected error in get_my_teams_songs: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while retrieving songs from your teams."
        )