import os
import traceback
from typing import Annotated

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import JSONResponse, RedirectResponse
from jose import ExpiredSignatureError, JWTError, jwt
from sqlalchemy.orm import Session

from backend.monolith.database.database import get_db

# from backend.monolith.utils.modify import modify_username_password
# from backend.monolith.models.models import UserUpdateModel
from backend.monolith.utils.log_user_session import remove_session

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
FRONTEND_URL = os.getenv("FRONTEND_URL")

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]


def get_current_user(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated. Please login before accessing this page.",
        )

    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials. \
            Be sure to login before accessing this page.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[ALGORITHM],
            options={"require": ["exp", "user_id", "email", "session_id"]},
        )

        user_id: str = payload.get("user_id")
        user_email: str = payload.get("email")
        session_id: str = payload.get("session_id")
        role: str = payload.get("role")

        if user_id is None or user_email is None or session_id is None or role is None:
            raise credentials_exception

        return payload

    except ExpiredSignatureError:
        # Specifically handle expired tokens
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session expired. Please login again.",
        )
    except JWTError:
        # Handle other JWT-related errors
        traceback.print_exc()
        raise credentials_exception
    except Exception as e:
        print(f"Unexpected error: {e}")
        traceback.print_exc()
        raise HTTPException(
            status_code=401,
            detail="Not Authenticated. \
            Please login before accessing this page. \
            If the problem persists, please contact support.",
        )


@router.get("/", summary="Home (after login) that returns user details")
async def get_response(
    request: Request, current_user: dict = Depends(get_current_user)
) -> JSONResponse:
    """
    Args: \n
        cookie: access_token (str): JWT token containing user details. \n
    Returns: \n
        JSONResponse with status 200 and content \n
        - message: Welcome message \n
        - user_details: Details of the current user \n
    Raises: \n
        HTTPException if user details cannot be retrieved. \n
        Specifically status code 401 if not authenticated. \n
        and 'detail' specifying the cause \n
        - Session expired \n
        - Not authenticated if token missing \n
        - Could not validate credentials if token does not match \n
    """
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Welcome to the home route!", "user_details": current_user},
    )


@router.get("/logout", summary="Logs out the user and clears the session")
async def logout(
    request: Request, db: db_dependency, current_user: dict = Depends(get_current_user)
) -> RedirectResponse:
    """
    Args: \n
        cookie: access_token (str): JWT token containing user details.\n
        (see /home endpoint for explanation on 401 HTTPExceptions) \n
    Returns: \n
        RedirectResponse to the frontend URL after logging out. \n
    """
    try:
        request.session.clear()
        response = RedirectResponse(
            url=FRONTEND_URL, status_code=status.HTTP_303_SEE_OTHER
        )
        action_ok, message = remove_session(
            db, current_user["user_id"], current_user["session_id"]
        )
        if not action_ok:
            raise HTTPException(status_code=400, detail=message)
        response.delete_cookie("access_token", path="/")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid session data {e}")
    return response
