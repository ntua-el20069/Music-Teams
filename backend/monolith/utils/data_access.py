import os
import uuid
from datetime import datetime
from typing import Optional, Tuple

from dotenv import load_dotenv
from itsdangerous import URLSafeTimedSerializer
from sqlalchemy.orm import Session

from backend.monolith.models.models import ActiveSession, ActiveSessionModel, User

# from werkzeug.security import check_password_hash


env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)
SECRET_KEY = str(os.getenv("SECRET_KEY"))
serializer = URLSafeTimedSerializer(SECRET_KEY)


def get_session_by_token(db: Session, token: str) -> Optional[ActiveSessionModel]:
    found_active_session = (
        db.query(ActiveSession).filter(ActiveSession.token == token).first()
    )
    if not found_active_session:
        return None
    active_session_instance = ActiveSessionModel(
        token=found_active_session.token,
        username=found_active_session.username,
        role=found_active_session.role,
        user_id=found_active_session.user_id,
    )
    return active_session_instance


def login_and_make_token(
    db: Session,
    username_input: str,
    password_input: str,
) -> Tuple[Optional[ActiveSessionModel], Optional[str]]:
    """
    Placeholder function for user login logic.
    This should be implemented to validate user credentials and create a session.
    """
    user_found = db.query(User).filter(User.username == username_input).first()
    # TODO: keep the check_password_hash logic in the database
    # if (user_found is None) or
    # not check_password_hash(user_found.password, password_input):
    if (user_found is None) or (user_found.password != password_input):
        return (None, "Invalid username or password")

    # TODO: how many active sessions can a user have?
    # Check if the user already has an active session
    number_of_active_sessions = (
        db.query(ActiveSession).filter(ActiveSession.username == username_input).count()
    )
    if number_of_active_sessions >= 3:
        return (
            None,
            """You have reached the maximum number of active sessions (3). \
                Please log out from another session/device.""",
        )

    # user login successful so create a session token
    try:
        # Generate a unique token with random data
        token_data = {
            "username": username_input,
            "session_id": str(uuid.uuid4()),  # Random UUID
            "timestamp": datetime.utcnow().isoformat(),  # Current time
        }
        token = serializer.dumps(token_data)[:48]  # Now unique per login

        new_session = ActiveSession(
            token=token,
            username=username_input,
            role=user_found.role,
            user_id=user_found.id,
        )
        db.add(new_session)
        db.commit()
        db.refresh(new_session)
    except Exception as e:
        print(f"Error creating session in database: {e}")
        return (None, "Error creating session in database")

    active_session_instance = ActiveSessionModel(
        token=new_session.token,
        username=new_session.username,
        role=new_session.role,
        user_id=new_session.user_id,
    )
    return (active_session_instance, "token created successfully")


def logout_and_remove_session(
    db: Session,
    token: str,
) -> Tuple[bool, Optional[str]]:
    """
    Placeholder function for user logout logic.
    This should be implemented to remove the session from the database.
    """
    try:
        active_session_instance = (
            db.query(ActiveSession).filter(ActiveSession.token == token).first()
        )
        if not active_session_instance:
            raise ValueError("Session does not exist or has already been removed")
        db.delete(active_session_instance)
        db.commit()
        return (True, "Session removed successfully")
    except Exception as e:
        print(f"Error removing session from database: {e}")
        return (
            False,
            """Error removing session from database: \
                You may already be logged out or the session does not exist""",
        )
