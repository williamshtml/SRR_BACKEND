from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Tus datos de Docker: williams / 1234
DATABASE_URL = "postgresql+asyncpg://williams:1234@localhost:5432/srr_recaudacion"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

# Dependencia para los Controllers
async def get_db():
    async with SessionLocal() as session:
        yield session