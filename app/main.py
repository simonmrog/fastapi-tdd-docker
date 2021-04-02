from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise

from app.config import Settings, settings

app = FastAPI()


@app.get("/ping")
async def pong():
    return {
        "ping": "pong!",
        "environment": settings.ENVIRONMENT,
        "testing": settings.TESTING
    }


register_tortoise(
    app,
    db_url=settings.DATABASE_URL,
    modules={"models": ["app.models.tortoise"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
