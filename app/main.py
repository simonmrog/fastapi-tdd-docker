from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise

from app.config import settings

app = FastAPI()

register_tortoise(
    app,
    db_url=settings.DATABASE_URL,
    modules={"models": ["app.models.tortoise"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
