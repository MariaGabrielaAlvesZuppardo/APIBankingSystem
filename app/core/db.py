from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL

# Cria o motor assíncrono para o banco de dados PostgreSQL
engine = create_async_engine(DATABASE_URL, echo=True)

# Cria uma sessão assíncrona
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base = declarative_base()

# Função para obter a sessão do banco de dados
async def get_db():
    async with SessionLocal() as session:
        yield session
