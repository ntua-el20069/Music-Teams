from dotenv import load_dotenv
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from backend.monolith.database.database import get_db
from backend.monolith.models.models import User

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)

router = APIRouter()


@router.get("/create-admin")  # type: ignore
async def init_database() -> JSONResponse:
    """
    Initializes the database with an admin user \n.
    Returns: \n
        JSONResponse with 'message' in content \n
        status code 200 if successful \n
        status code 500 if an error occurs \n
    """
    try:
        db = next(get_db())
        for i in range(10):
            admin_user = User(
                username=f"admin{i}",
                password=f"admin{i}",  # TODO: hash this password
                email=f"admin{i}@emaildomain.gr",
                role="admin",
            )
            db.add(admin_user)
        db.commit()
        return JSONResponse(
            status_code=200,
            content={"message": "Database initialized with admin users."},
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": f"Error initializing database: {str(e)}"},
        )
