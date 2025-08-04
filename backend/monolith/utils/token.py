import os

from dotenv import load_dotenv
from jose import jwt

env_path = "backend/.env"
load_dotenv(dotenv_path=env_path)
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


def create_access_token(data: dict) -> str:
    global JWT_SECRET_KEY, ALGORITHM
    to_encode = data.copy()
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
