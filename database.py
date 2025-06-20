from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DB_URL")

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

# Scoped session for use in web applications
db_session = scoped_session(SessionLocal)

Base = declarative_base()
Base.query = db_session.query_property()  # Optional but useful
