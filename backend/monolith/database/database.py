import os
from typing import Tuple

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def db_type_url(DB_USERSNAME, DB_PASSWORD, DB_HOST, DB_DATABASE) -> Tuple[str, str]:

    env_path = ".env"
    load_dotenv(dotenv_path=env_path)

    DB_TYPE = "postgresql"
    try:
        DB_TYPE = str(os.getenv("DB_TYPE"))
    except Exception as e:
        print(f"Error getting DB_TYPE from environment: {e}")
        pass

    DATABASE_URL = f"{DB_USERSNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"  # noqa: E231
    DATABASE_URL = "postgresql://" + DATABASE_URL

    if DB_TYPE == "mysql":
        DATABASE_URL = "mysql+pymysql://" + DATABASE_URL

    return (DB_TYPE, DATABASE_URL)


env_path = ".env"
load_dotenv(dotenv_path=env_path)

DB_USERSNAME = str(os.getenv("DB_USERNAME"))
DB_PASSWORD = str(os.getenv("DB_PASSWORD"))
DB_HOST = str(os.getenv("DB_HOST"))
DB_DATABASE = str(os.getenv("DB_DATABASE"))

DB_TYPE, DATABASE_URL = db_type_url(DB_USERSNAME, DB_PASSWORD, DB_HOST, DB_DATABASE)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
