from dotenv import load_dotenv
from fastapi import APIRouter

from backend.monolith.database.database import get_db
from backend.monolith.models.models import User

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)

router = APIRouter()


@router.get("/create-admin")  # type: ignore
async def init_database() -> dict:
    try:
        db = next(get_db())
        admin_user = User(
            username="admin",
            password="admin",  # TODO: hash this password
            email="",
            role="admin",
        )
        db.add(admin_user)
        db.commit()
        return {"message": "Database initialized with admin user."}
    except Exception as e:
        return {"message": f"Error initializing database: {str(e)}"}
