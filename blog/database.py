from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from blog import config


SQLALCHEMY_DATABASE_URL = config.DATABASE_URL


engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()