from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from backend.monolith.database.database import get_db
from backend.monolith.models.models import ActiveSessionModel
from backend.monolith.utils.data_access import (
    get_session_by_token,
    login_and_make_token,
    logout_and_remove_session,
)

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/check_access")
async def check_access(
    db: db_dependency,
    token: str,
):
    """
    Validates a session token and returns the user's role/privileges \n
    Args: token (str): The session token to validate. \n
    Returns: JSONResponse with privilege level (role) and username if valid \n

    Raises: \n
        HTTPException 401: Invalid token \n
        HTTPException 500: Database error \n
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
                "user_id": active_session_instance.user_id,
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


@router.post("/login")
async def login(
    db: db_dependency,
    username: str,
    password: str,
):
    """
    Placeholder for login functionality. \n
    Args: username (str): The username of the user. \n
          password (str): The password of the user. \n
    Returns: JSONResponse with \n
    - message indicating login success or failure the token \n
    - token if login is successful \n
    """
    try:
        active_session_instance, message = login_and_make_token(db, username, password)

        if not active_session_instance:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=message,
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": message,
                "token": active_session_instance.token,
                "role": active_session_instance.role,
                "username": active_session_instance.username,
                "user_id": active_session_instance.user_id,
            },
        )

    except HTTPException:
        # Re-raise HTTP exceptions
        raise

    except Exception as e:
        # Log the error for debugging
        print(f"Error during login: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during login",
        )


@router.post("/logout")
async def logout(
    db: db_dependency,
    token: str,
):
    """
    Placeholder for logout functionality. \n
    Args: token (str): The session token to invalidate. \n
    Returns: JSONResponse with message indicating logout success or failure \n
    """
    try:
        if not token:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Token is required for logout",
            )

        success, message = logout_and_remove_session(db, token)

        if not success:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=message,
            )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": message},
        )
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        # Log the error for debugging
        print(f"Error during logout: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during logout",
        )
