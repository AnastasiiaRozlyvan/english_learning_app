from fastapi import FastAPI

from app.models.database import Base
from app.models.database import engine
from app.routers import users, topics

Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(users.router)
app.include_router(topics.router)
