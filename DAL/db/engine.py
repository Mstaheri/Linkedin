from sqlalchemy.ext.asyncio import create_async_engine , async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:55805580@localhost:5432/postgres"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = async_sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

class Base(DeclarativeBase,MappedAsDataclass):
    pass

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()