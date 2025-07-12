import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.monolith.database.database import engine, get_db
from backend.monolith.models.models import Base, User
from backend.monolith.routes.API import router as API_router
from backend.monolith.routes.login import router as login_router

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)


app = FastAPI()
app.debug = bool(int(os.getenv("DEBUG")))  # type: ignore
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")  # type: ignore
async def start_database() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/", tags=["Root"])  # type: ignore
async def read_root() -> dict:
    return {"message": "welcome"}


# TODO: remove this endpoint in production
@app.get("/init", tags=["Init"])  # type: ignore
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


app.include_router(API_router, prefix="/API", tags=["API"])
app.include_router(login_router, prefix="/login", tags=["login"])
