# Import necessary libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from datetime import date

def db_type_url(DB_USERSNAME, DB_PASSWORD, DB_HOST, DB_DATABASE) -> (str, str):

    env_path = '.env'
    load_dotenv(dotenv_path=env_path)

    DB_TYPE = 'postgresql'
    try:
        DB_TYPE = str(os.getenv('DB_TYPE'))
    except:
        pass

    # Replace 'your_username', 'your_password', 'your_database', and 'your_host' with your PostgreSQL credentials
    DATABASE_URL = f"postgresql://{DB_USERSNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
    #DATABASE_URL = "sqlite+pysqlite:///ntuaflix.sqlite3" #### TODO: ONLY FOR DEV

    if DB_TYPE == 'mysql':
        DATABASE_URL = f"mysql+pymysql://{DB_USERSNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
    
    return (DB_TYPE, DATABASE_URL)


env_path = '.env'
load_dotenv(dotenv_path=env_path)

DB_USERSNAME = str(os.getenv('DB_USERNAME'))
DB_PASSWORD = str(os.getenv('DB_PASSWORD'))
DB_HOST = str(os.getenv('DB_HOST'))
DB_DATABASE = str(os.getenv('DB_DATABASE'))

DB_TYPE, DATABASE_URL = db_type_url(DB_USERSNAME, DB_PASSWORD, DB_HOST, DB_DATABASE)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
