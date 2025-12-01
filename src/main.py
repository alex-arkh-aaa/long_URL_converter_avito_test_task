from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database import engine
from models import Base


@asynccontextmanager
async def lifespan():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
      
    yield


app = FastAPI(lifespan=lifespan)



@app.post('/short_url')
async def generate_short_url():
    return ...

@app.get('/{slug}')
async def redirect_to_url(slug: str):
    return ...
