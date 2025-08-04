from typing import Optional, Tuple

from dotenv import load_dotenv
from sqlalchemy import exc as sqlalchemy_exc
from sqlalchemy.orm import Session

from backend.monolith.models.models import User

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)

password_criteria = """
    Check if the password meets the criteria:
    - Must be a string
    - Cannot be empty
    - Maximum length of 20 characters
    - Minimum length of 8 characters
    - contains at least one digit
    - contains at least one uppercase letter
    - contains at least one special character
"""


def password_check(password: str) -> bool:
    f"""{password_criteria}"""

    if (
        not isinstance(password, str)
        or len(password) == 0
        or len(password) > 20
        or len(password) < 8
    ):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
        return False
    return True


def modify_username_password(
    db: Session,
    user_id: int,
    new_username: Optional[str] = None,
    new_password: Optional[str] = None,
) -> Tuple[bool, str]:
    """
    Modifies the username and/or password of a user in the database.
    """
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return (False, "User not found.")

        if new_username and len(new_username) <= 80:
            user.username = new_username
        else:
            return (
                False,
                "Username cannot be empty. It must be a string with \
                      a maximum length of 80 characters.",
            )

        # TODO: if password logic is needed, uncomment the following lines and hash
        # if new_password and password_check(new_password):
        #     user.password = new_password  # TODO: hash this password
        # else:
        #     # TODO: specify the criteria in a descriptive way
        #       return (None, "Password cannot be empty and
        #       should meet the criteria specified. ")

        db.commit()
        db.refresh(user)
        return (True, "User updated successfully.")
    except sqlalchemy_exc.IntegrityError as e:
        # Handle unique constraint violation for username
        print(f"IntegrityError: {e}")
        db.rollback()
        if "UNIQUE constraint failed" in str(e):
            return (
                False,
                "Username already exists. Please choose a different username. Details: "
                + str(e),
            )
        else:
            return (False, f"An error occurred: {str(e)}")
    except Exception as e:
        print(f"Error modifying user: {e}")
        return (False, f"An error occurred while modifying the user. {str(e)}")
