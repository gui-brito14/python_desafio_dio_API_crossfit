from fastapi import FastAPI
from fastapi_pagination import add_pagination
from .routers import atleta

app = FastAPI()

app.include_router(atleta.router)

add_pagination(app)
