import os
import uuid
from datetime import datetime, timedelta
from typing import Optional, Tuple

from dotenv import load_dotenv
from sqlalchemy.exc import IntegrityError

# from itsdangerous import URLSafeTimedSerializer
from sqlalchemy.orm import Session

from backend.monolith.models.models import (
    ActiveSession,
    ActiveSessionModel,
    User,
    UserModel,
)

# from werkzeug.security import check_password_hash


env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)
# SECRET_KEY = str(os.getenv("SECRET_KEY"))
# serializer = URLSafeTimedSerializer(SECRET_KEY)


def check_credentials(
    db: Session,
    username_input: str,
    password_input: str,
) -> Tuple[Optional[UserModel], str]:
    """
    user login logic: validate user credentials. (used for testing purposes)
    """

    try:
        user_found = db.query(User).filter(User.username == username_input).first()
        # TODO: keep the check_password_hash logic in the database
        # if (user_found is None) or
        # not check_password_hash(user_found.password, password_input):
        if (user_found is None) or (user_found.password != password_input):
            return (None, "Invalid username or password")

        user_model_instance = UserModel(
            id=user_found.id,
            username=user_found.username,
            password=user_found.password,  # This should be hashed in production
            email=user_found.email,
            role=user_found.role,
            registered_with_google=user_found.registered_with_google,
        )
        return (user_model_instance, "Credentials validated successfully")

    except Exception as e:
        print(f"Unexpected Error checking credentials: {str(e)}")
        return (None, f"Unexpected Error checking credentials: {str(e)}")


def log_user(
    db: Session, user_model_instance: UserModel
) -> Tuple[Optional[UserModel], str]:
    """
    Registers a user in the database if does not already exist.
    """
    try:
        found_user = (
            db.query(User).filter(User.email == user_model_instance.email).first()
        )
        if not found_user:
            if (
                (not user_model_instance.password)
                or (user_model_instance.password is None)
            ) and (user_model_instance.registered_with_google is True):
                # make a random password for the user registered with Google
                user_model_instance.password = str(uuid.uuid4())[:20]

            # TODO: what about the username selection
            # now username is taken from the email (part before @)
            # this is not the best solution, but it works for now
            # what if there are conflicts?
            # (consider gmail accounts with the same email prefix but different domains
            # e.g. google.com and gmail.com and googlemail.com)
            new_user = User(
                username=user_model_instance.email.split("@")[
                    0
                ],  # not the best solution, but works for now
                password=user_model_instance.password,  # TODO: hash this password
                email=user_model_instance.email,
                role=user_model_instance.role,
                registered_with_google=user_model_instance.registered_with_google,
            )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)  # Refresh to get the new user ID
            user_model_instance = UserModel(
                id=new_user.id,
                username=new_user.username,
                password=new_user.password,  # This should be hashed in production
                email=new_user.email,
                role=new_user.role,
                registered_with_google=new_user.registered_with_google,
            )
            print("User registered successfully.")
            return (new_user, "User registered successfully.")
        else:
            user_model_instance = UserModel(
                id=found_user.id,
                username=found_user.username,
                password=found_user.password,  # This should be hashed in production
                email=found_user.email,
                role=found_user.role,
                registered_with_google=found_user.registered_with_google,
            )
            print("User already exists in the database.")
            return (user_model_instance, "User already exists.")

    except IntegrityError as e:
        if db:
            db.rollback()
        # Handle specific integrity errors, e.g. unique constraint violations
        print(f"Integrity error: {str(e)}")
        return (None, f"Integrity error: {str(e)} - Try using a different username.")

    except Exception as e:
        if db:
            db.rollback()
        print(f"Error registering user: {str(e)}")
        return (None, f"Error registering user: {str(e)}")


def log_session(
    db: Session, user_email: str, session_id: str
) -> Tuple[Optional[ActiveSessionModel], str]:
    """
    Logs a session in the database.
    """
    try:
        # TODO: remove expired sessions
        # remove sessions of the user that have expired
        expired_sessions = (
            db.query(ActiveSession)
            .filter(
                ActiveSession.user_email == user_email,
                ActiveSession.expires_at < datetime.utcnow(),
            )
            .all()
        )
        for exp_session in expired_sessions:
            db.delete(exp_session)
        db.commit()

        # TODO: how many active sessions can a user have?
        # Check if the user already has an active session
        number_of_active_sessions = (
            db.query(ActiveSession)
            .filter(ActiveSession.user_email == user_email)
            .count()
        )
        if number_of_active_sessions >= 3:
            print("User has reached the maximum number of active sessions.")
            return (
                None,
                """You have reached the maximum number of active sessions (3). \
                    Please log out from another session/device.""",
            )
        user_found = db.query(User).filter(User.email == user_email).first()
        if not user_found:
            raise ValueError("User not found in the database.")

        # Define session expiration time
        expiration_datetime = datetime.utcnow() + timedelta(
            seconds=int(os.getenv("ACCESS_TOKEN_EXPIRE_SECONDS", "3600"))
        )

        new_session = ActiveSession(
            session_id=session_id,
            user_id=user_found.id,
            user_email=user_email,
            username=user_found.username,
            role=user_found.role,
            expires_at=expiration_datetime,
        )
        db.add(new_session)
        db.commit()
        print("Session logged successfully.")
        return (
            ActiveSessionModel(
                session_id=session_id,
                user_id=user_found.id,
                user_email=user_email,
                username=user_found.username,
                role=user_found.role,
                expires_at=expiration_datetime.isoformat(),
            ),
            "Session logged successfully.",
        )
    except Exception as e:
        if db:
            db.rollback()
        print(f"Error logging session: {str(e)}")
        return (None, f"Error logging session: {str(e)}")


def remove_session(db: Session, user_id: int, session_id: str) -> Tuple[bool, str]:
    """
    Removes a session from the database.
    """
    try:
        session_to_remove = (
            db.query(ActiveSession)
            .filter(
                ActiveSession.user_id == user_id, ActiveSession.session_id == session_id
            )
            .first()
        )

        if not session_to_remove:
            print("Session not found.")
            return (False, "Session not found.")

        db.delete(session_to_remove)
        db.commit()
        print("Session removed successfully.")
        return (True, "Session removed successfully.")
    except Exception as e:
        if db:
            db.rollback()
        print(f"Error removing session: {str(e)}")
        return (False, f"Error removing session: {str(e)}")
