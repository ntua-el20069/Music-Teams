import json
import os
import time
import traceback
from typing import Annotated

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import JSONResponse, RedirectResponse
from jose import ExpiredSignatureError, JWTError, jwt
from sqlalchemy.orm import Session

from backend.monolith.database.database import get_db
from backend.monolith.routes.login import create_session_set_cookie_and_redirect

# from backend.monolith.utils.modify import modify_username_password
# from backend.monolith.models.models import UserUpdateModel
from backend.monolith.utils.log_user_session import find_user_by_email, remove_session

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
FRONTEND_URL = os.getenv("FRONTEND_URL")
response_examples_path = "backend/monolith/routes/example-responses.json"
response_examples = None
with open(response_examples_path, "r", encoding="utf-8") as file:
    response_examples = json.load(file)

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
            options={"require": ["user_id", "email", "session_id", "role", "exp_time"]},
        )

        user_id: str = payload.get("user_id")
        user_email: str = payload.get("email")
        session_id: str = payload.get("session_id")
        role: str = payload.get("role")
        exp_time: int = payload.get("exp_time")

        if (
            user_id is None
            or user_email is None
            or session_id is None
            or role is None
            or exp_time is None
        ):
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


@router.get(
    "/",
    summary="Home (after login) that returns user details",
    responses={
        200: {
            "description": "Welcome message with user details",
            "content": {
                "application/json": {"example": response_examples["/home/"]["get"]}
            },
        },
    },
)
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


@router.get("/check-token", summary="Checks token expiration and refreshes if needed")
async def check_token(
    request: Request, db: db_dependency, current_user: dict = Depends(get_current_user)
) -> RedirectResponse:
    """
    Args: \n
        cookie: access_token (str): JWT token containing user details. \n
    Returns: \n
        RedirectResponse to: \n
        - /token-refresh (status 307) if token is about to expire \n
        (less than half of ACCESS_TOKEN_EXPIRE_SECONDS remaining) \n
        - /home (status 303) if token is still valid \n
    Raises: \n
        HTTPException if token is invalid or other errors occur. \n
    """
    try:
        exp = current_user.get("exp_time")

        if not exp:
            raise HTTPException(status_code=400, detail="Token has no expiration")

        current_time = int(time.time())
        time_remaining = exp - current_time

        # Get threshold for refresh (default to 30 minutes if not set)
        refresh_threshold = int(os.getenv("ACCESS_TOKEN_EXPIRE_SECONDS", "3600")) // 2

        if time_remaining < refresh_threshold:
            # Token is about to expire, redirect to refresh
            return RedirectResponse(
                url="/home/token-refresh",
                status_code=status.HTTP_307_TEMPORARY_REDIRECT,
            )

        # Token is still valid, redirect to home
        return RedirectResponse(url="/home", status_code=status.HTTP_303_SEE_OTHER)

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.get("/token-refresh", summary="Refreshes the JWT token")
async def refresh_token(
    request: Request, db: db_dependency, current_user: dict = Depends(get_current_user)
) -> RedirectResponse:
    """
    Args: \n
        cookie: access_token (str): JWT token containing user details. \n
    Returns: \n
        RedirectResponse to the frontend URL with a new JWT token. \n
    Raises: \n
        HTTPException if token refresh fails. \n
        Specifically status code 401 if not authenticated. \n
    """
    try:
        action_ok, message = remove_session(
            db, current_user["user_id"], current_user["session_id"]
        )
        if not action_ok:
            raise HTTPException(status_code=400, detail=message)

        user_found, message = find_user_by_email(db, current_user["email"])
        if not user_found:
            raise HTTPException(status_code=404, detail=message)

        expires_in = int(
            os.getenv("ACCESS_TOKEN_EXPIRE_SECONDS", "3600")
        )  # Default to 1 hour
        response = create_session_set_cookie_and_redirect(db, expires_in, user_found)
        return response
    except HTTPException as e:
        print(f"HTTP Exception during token refresh: {str(e)}")
        raise e
    except Exception as e:
        print(f"Error during token refresh: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
