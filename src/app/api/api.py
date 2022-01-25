from fastapi import APIRouter

from src.app.api.routers import topics, users

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(topics.router)
