from fastapi import FastAPI

from src.app.models.database import Base, engine
from src.app.routers import topics, users

Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(users.router)
app.include_router(topics.router)
