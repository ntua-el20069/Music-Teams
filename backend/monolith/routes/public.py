from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from backend.monolith.database.database import get_db
from backend.monolith.routes.home import get_current_user
from backend.monolith.utils.all import (
    get_all_public_composers,
    get_all_public_lyricists,
    get_all_public_songs,
)

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/all-composers", summary="Get all composers in public songs")
async def get_public_composers(
    db: db_dependency, current_user: dict = Depends(get_current_user)
) -> JSONResponse:
    """
    Get all composers that are in public songs. \n
    Requires authenticated user. \n

    Returns: \n
        JSONResponse (200) with list of composer names \n
        (message: str, composers: list) \n

    Raises: \n
        HTTPException with status 401 if user is not authenticated \n
        HTTPException with status 500 if database error occurs \n
    """
    try:
        success, msg, composers = get_all_public_composers(db)

        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=msg
            )

        return JSONResponse(
            status_code=200, content={"message": msg, "composers": composers}
        )

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(f"Unexpected error in get_public_composers: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while retrieving public composers.",
        )


@router.get("/all-lyricists", summary="Get all lyricists in public songs")
async def get_public_lyricists(
    db: db_dependency, current_user: dict = Depends(get_current_user)
) -> JSONResponse:
    """
    Get all lyricists that are in public songs. \n
    Requires authenticated user. \n

    Returns: \n
        JSONResponse (200) with list of lyricist names \n
        (message: str, lyricists: list) \n

    Raises: \n
        HTTPException with status 401 if user is not authenticated \n
        HTTPException with status 500 if database error occurs \n
    """
    try:
        success, msg, lyricists = get_all_public_lyricists(db)

        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=msg
            )

        return JSONResponse(
            status_code=200, content={"message": msg, "lyricists": lyricists}
        )

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(f"Unexpected error in get_public_lyricists: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while retrieving public lyricists.",
        )


@router.get("/all-songs", summary="Get all public songs")
async def get_public_songs(
    db: db_dependency, current_user: dict = Depends(get_current_user)
) -> JSONResponse:
    """
    Get all public songs. \n
    Requires authenticated user. \n

    Returns: \n
        JSONResponse (200) with list of songs \n
        (message: str, songs: list of  \n
        dictionaries with keys (id, title) ) \n

    Raises: \n
        HTTPException with status 401 if user is not authenticated \n
        HTTPException with status 500 if database error occurs \n
    """
    try:
        success, msg, songs = get_all_public_songs(db)

        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=msg
            )

        return JSONResponse(status_code=200, content={"message": msg, "songs": songs})

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(f"Unexpected error in get_public_songs: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while retrieving public songs.",
        )
