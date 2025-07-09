import os

from dotenv import load_dotenv
from fastapi import FastAPI

from backend.monolith.database.database import engine
from backend.monolith.models.models import Base
from backend.monolith.routes.API import router as API_router
from backend.monolith.routes.user_management import router as user_management_router

env_path = ".env"
load_dotenv(dotenv_path=env_path)


app = FastAPI()
app.debug = bool(int(os.getenv("DEBUG")))  # type: ignore


@app.on_event("startup")  # type: ignore
async def start_database() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/", tags=["Root"])  # type: ignore
async def read_root() -> dict:
    return {"message": "welcome"}


app.include_router(API_router, prefix="/API", tags=["API"])
app.include_router(
    user_management_router, prefix="/user_management", tags=["user_management"]
)
