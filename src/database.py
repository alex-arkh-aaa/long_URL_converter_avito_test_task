import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

DATABASE_URL= f'postgresql+asyncpg://admin:{os.getenv('POSTGRES_PASSWORD')}@localhost:5432/users_db'

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/urls"
print(DATABASE_URL)


engine = create_async_engine(DATABASE_URL)

new_session = async_sessionmaker(bind=engine, expire_on_commit=False)


