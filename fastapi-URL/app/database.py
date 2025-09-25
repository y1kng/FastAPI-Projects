from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine    

from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")   # read the production database URL from .env

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind = engine, autocommit = False, autoflush = False)

Base = declarative_base()    # Base class for models

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()