import os
from datetime import datetime

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.middleware.sessions import SessionMiddleware

from backend.monolith.database.database import engine
from backend.monolith.models.models import Base
from backend.monolith.routes.API import router as API_router
from backend.monolith.routes.helpers import router as database_init_router
from backend.monolith.routes.home import router as home_router
from backend.monolith.routes.login import google_login_router, simple_login_router

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)


app = FastAPI()

app.debug = bool(int(os.getenv("DEBUG")))  # type: ignore

app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SECRET_KEY"),
    session_cookie="sessionid",  # Unique name
    same_site="lax",
    max_age=3600,  # session expires in 1 hour
    https_only=False,  # TODO: True in production (use MODE environment variable)
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # TODO: Adjust for production (if frontend is hosted elsewhere)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")  # type: ignore
async def start_database() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/", tags=["Root"], summary="Welcome message with status code 200")
async def read_root() -> JSONResponse:
    return JSONResponse(
        status_code=200,
        content={
            "message": "Welcome to the Music Teams API",
        },
    )


@app.get(
    "/health",
    tags=["Health"],
    summary="Indicates healthy app and running with status 200",
)
async def health_check() -> JSONResponse:
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "message": "Application server up and running.",
        },
    )


app.include_router(API_router, prefix="/API", tags=["API"])
app.include_router(google_login_router, prefix="/google_login", tags=["Google login"])
app.include_router(home_router, prefix="/home", tags=["home"])

if os.getenv("MODE") == "DEVELOPMENT":
    app.include_router(database_init_router, prefix="/init-db", tags=["Init Database"])
    app.include_router(
        simple_login_router, prefix="/simple_login", tags=["Simple Login"]
    )
