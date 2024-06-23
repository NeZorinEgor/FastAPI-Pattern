# FastAPI ecosystem
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# Redis ecosystem
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis
from redis import Redis

# Local modules
from src.config import settings

# Utils
import time


redis: Redis | None


# Event-Manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    global redis
    # Startup
    redis = aioredis.from_url(settings.redis_url)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield
    # Shutdown
    print("shutdown")
    await redis.close()


app = FastAPI(
    title="Best Practice FastAPI",
    description="PydanticSettings, Alembic, RedisCache",
    lifespan=lifespan,
    docs_url="/docs",
)

# Origins url's for CORS
origins = [
    'http://localhost',
    'https://localhost',
]

# Cors settings
# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "PUT", "DELETE"],
    allow_headers=["*"],
)


# Moc cache
@app.get("/moc-transactions")
@cache(expire=5)
async def long_translation():
    time.sleep(5)
    return {
        "ok": True,
        "message": "Successful test cache at long operations"
    }
