from fastapi import FastAPI

from src.app.api.api import api_router
from src.app.models.database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(api_router)
