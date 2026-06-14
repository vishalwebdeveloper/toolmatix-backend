from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from config import settings

DATABASE_URL=(
    f"mysql+pymysql://"
    f"{settings.DATABASE_USER}:"
    f"{settings.DATABASE_PASSWORD}@"
    f"{settings.DATABASE_HOST}:"
    f"{settings.DATABASE_PORT}/"
    f"{settings.DATABASE_NAME}"
)

engine=create_engine(
    DATABASE_URL,
    connect_args={
        "ssl":{
            "ca":settings.SSL_CA
        }
    },
    pool_pre_ping=True,
    pool_recycle=3600
)

SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base=declarative_base()

def get_db():

    db=SessionLocal()

    try:
        yield db

    finally:
        db.close()