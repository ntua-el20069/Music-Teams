from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from backend.monolith.database.database import get_db
from backend.monolith.models.models import ActiveSessionModel
from backend.monolith.utils.data_access import get_session_by_token

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/check_access")
async def check_access(
    db: db_dependency,
    token: str,
):
    """
    Validates a session token and returns the user's role/privileges
    Args:
        token (str): The session token to validate.
    Returns:
        JSONResponse with privilege level (role) and username if valid

    Raises:
        HTTPException 401: Invalid token
        HTTPException 500: Database error
    """
    try:
        # Query the session table for the token
        active_session_instance: Optional[ActiveSessionModel] = get_session_by_token(
            db, token
        )

        if not active_session_instance:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired session token",
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Session is valid",
                "role": active_session_instance.role,
                "username": active_session_instance.username,
            },
        )

    except HTTPException:
        # Re-raise HTTP exceptions
        raise

    except Exception as e:
        # Log the error for debugging
        print(f"Error checking access: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error while validating session",
        )
