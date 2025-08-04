import os
from typing import Annotated

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from backend.monolith.database.database import get_db
from backend.monolith.models.models import UserUpdateModel
from backend.monolith.routes.home import get_current_user
from backend.monolith.utils.modify import modify_username_password

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
FRONTEND_URL = os.getenv("FRONTEND_URL")

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/update_user_details", summary="update user details and logout")
async def update_user_details(
    db: db_dependency,
    user_update_data: UserUpdateModel,
    current_user: dict = Depends(get_current_user),
) -> RedirectResponse:
    """
    Args: \n
        cookie: access_token \n
        username (payload): the new username to be set \n
        password (payload): the new password to be set (currently not implemented) \n
    Returns: \n
        After updating user details, \n
        Redirects (status 303) to the logout and then \n
        to frontend URL after updating user details. \n
    Raises: \n
        HTTPException: If the user is not authenticated (see /home/ for status)
        or if there is an error updating user details. (status 400)
    """
    try:
        user_id = current_user["user_id"]
        # user_email = current_user["email"]

        update_ok, message = modify_username_password(
            db,
            user_id,
            new_username=user_update_data.username,
            new_password=user_update_data.password,
        )

        if not update_ok:
            raise HTTPException(status_code=400, detail=message)

        return RedirectResponse(
            url=f"{FRONTEND_URL}/logout", status_code=status.HTTP_303_SEE_OTHER
        )
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Error updating user details: {str(e)}"
        )
