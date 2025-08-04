import os
import uuid
from typing import Annotated

import requests
from authlib.integrations.starlette_client import OAuth
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from backend.monolith.database.database import get_db
from backend.monolith.models.models import UserManualLoginModel, UserModel
from backend.monolith.utils.log_user_session import (
    check_credentials,
    log_session,
    log_user,
)
from backend.monolith.utils.token import create_access_token

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)

# JWT Configurations
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
FRONTEND_URL = os.getenv("FRONTEND_URL")

google_login_router = APIRouter()
simple_login_router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]


# OAuth Setup
oauth = OAuth()
oauth.register(
    name="auth_demo",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    authorize_params=None,
    access_token_url="https://accounts.google.com/o/oauth2/token",
    access_token_params=None,
    refresh_token_url=None,
    authorize_state=os.getenv("JWT_SECRET_KEY"),
    redirect_uri=os.getenv("REDIRECT_URL"),
    jwks_uri="https://www.googleapis.com/oauth2/v3/certs",
    client_kwargs={
        "scope": "openid profile email",
        "state": True,  # Enable state parameter for CSRF protection
    },
)


def create_session_set_cookie_and_redirect(
    db: db_dependency, expires_in: int, user_model_instance: UserModel
) -> RedirectResponse:
    """
    This function creates a session for the user, sets a cookie with the access token,
    and redirects to the frontend URL.
    """
    session_id = str(uuid.uuid4())

    token_data = {
        "user_id": user_model_instance.id,
        "email": user_model_instance.email,
        "username": user_model_instance.username,
        "role": user_model_instance.role,
        "registered_with_google": user_model_instance.registered_with_google,
        "session_id": session_id,
    }
    access_token = create_access_token(data=token_data)

    user_session_instance, message = log_session(
        db, user_model_instance.email, session_id
    )

    if not user_session_instance:
        raise HTTPException(status_code=400, detail=message)

    response = RedirectResponse(
        os.getenv("FRONTEND_URL"), status_code=status.HTTP_303_SEE_OTHER
    )
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,  # TODO: how to set on production?
        secure=False,  # TODO: Set to True in production with HTTPS
        samesite="lax",  # Changed from "strict" to allow top-level navigation
        path="/",  # Make cookie available to all routes
        max_age=expires_in,  # TODO: decide the expiration time
    )

    print(
        f"\n\n\t Access token created for user {user_model_instance.username} \
        with ID {user_model_instance.id}: \n\t {access_token}\n\n"  # noqa: E272
    )

    return response


# Google login routes
@google_login_router.get(
    "/login", summary="Route that Redirects to Google Accounts OAuth"
)
async def google_login(request: Request):
    """
    Initiates the Google OAuth login process. \n
    Clears the session and redirects to the Google authorization URL. \n
    Returns: \n
        RedirectResponse to the Google authorization URL. \n
    """
    request.session.clear()
    # referer = request.headers.get("referer")
    frontend_url = os.getenv("FRONTEND_URL")
    redirect_url = os.getenv("REDIRECT_URL")
    state = str(uuid.uuid4())
    request.session["oauth_state"] = state
    request.session["login_redirect"] = frontend_url
    request.session.setdefault("_session_saved", True)  # Ensure session is saved
    print("Session state saved:", request.session["oauth_state"])  # Debug

    return await oauth.auth_demo.authorize_redirect(
        request, redirect_url, state=state, prompt="consent"
    )


@google_login_router.get("/auth", summary="Google Authentication Callback Handler")
async def google_auth(request: Request, db: db_dependency):
    """
    Handles the Google authentication callback. \n
    A state parameter is used to prevent CSRF attacks. \n
    Calls Google API to authorize the user and again
         to fetch user information. \n
    Returns: \n
        a RedirectResponse to the frontend URL after successful login. \n
        Status code 303 (See Other) \n
    Raises: \n
        HTTPException if authentication fails or user registration fails. \n
        Status codes include: (see 'detail') \n
        - 401 if Google authentication fails \n
        - 406 if state mismatch (possible CSRF attack) \n
        - 400 if user registration fails or session not created \n
        - 500 for internal server errors \n
    """
    # Verify state first
    stored_state = request.session.pop("oauth_state", None)
    query_state = request.query_params.get("state")
    print(f"Stored state: {stored_state}, Query state: {query_state}")
    if not stored_state or stored_state != query_state:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="State mismatch. Possible CSRF attack.",
        )

    try:
        token = await oauth.auth_demo.authorize_access_token(request)
    except Exception as e:
        print(f"Error during Google authentication: {str(e)}")
        raise HTTPException(status_code=401, detail="Google authentication failed.")

    # Get more information about the user from Google
    try:
        user_info_endpoint = "https://www.googleapis.com/oauth2/v2/userinfo"
        headers = {"Authorization": f'Bearer {token["access_token"]}'}
        google_response = requests.get(user_info_endpoint, headers=headers)
        user_info = google_response.json()
        if user_info.get("error"):
            print(f"Error fetching user info: {user_info['error']}")
    except Exception as e:
        print(f"Error fetching user info: {str(e)}")
        raise HTTPException(status_code=401, detail="Google authentication failed.")

    try:
        user = token.get("userinfo")
        # expires_in = token.get("expires_in")
        # bypass Google expiration time (no strict expiration)
        expires_in = int(os.getenv("ACCESS_TOKEN_EXPIRE_SECONDS", "3600"))
        user_google_id = user.get("sub")
        iss = user.get("iss")
        user_email = user.get("email")

        if iss not in ["https://accounts.google.com", "accounts.google.com"]:
            print(f"Invalid issuer: {iss}")
            raise HTTPException(status_code=401, detail="Google authentication failed.")

        if user_google_id is None:
            print("User Google ID not found in Google response.")
            raise HTTPException(status_code=401, detail="Google authentication failed.")

        # register the user in the database or check if already exists
        user_input_model_instance = UserModel(
            username="",  # username selection logic in the function implementation
            password="",  # if registered by Google, Password is randomly generated
            email=user_email,
            role="user",  # Default role, can be changed later
            registered_with_google=True,
        )
        user_model_instance, message = log_user(db, user_input_model_instance)

        if not user_model_instance:
            raise HTTPException(
                status_code=400, detail=f"Error registering user. {message}"
            )

        response = create_session_set_cookie_and_redirect(
            db, expires_in, user_model_instance
        )

        return response

    except HTTPException as e:
        print(f"Unexpected HTTP Exception during Google authentication: {str(e)}")
        raise e
    except Exception as e:
        print(f"Error during Google authentication: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# Simple login route
@simple_login_router.post("/login", summary="Simple User Login - username/password")
async def simple_login(
    db: db_dependency,
    user_model: UserManualLoginModel,
):
    """
    Placeholder for login functionality. \n
    Args: (payload) \n
            username (str): The username of the user. \n
            password (str): The password of the user. \n
    Returns: \n
            RedirectResponse to the frontend URL after successful login. \n
            Status code 303 (See Other) \n
    Raises: \n
            HTTPException if login fails. (see 'detail') \n
            Status codes include: \n
            - 401 if credentials are invalid \n
            - 500 for internal server errors \n
    """
    try:
        user_model_instance, message = check_credentials(
            db, user_model.username, user_model.password
        )

        if not user_model_instance:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=message,
            )

        expires_in = int(os.getenv("ACCESS_TOKEN_EXPIRE_SECONDS", "3600"))

        response = create_session_set_cookie_and_redirect(
            db, expires_in, user_model_instance
        )

        return response

    except HTTPException as e:
        print(f"Unexpected HTTP Exception during login: {str(e)}")
        raise e
    except Exception as e:
        print(f"Error during login: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
