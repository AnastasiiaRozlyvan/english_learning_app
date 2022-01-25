from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from src.app.api.routers.utils import get_db
from src.app.models.models import User
from src.app.repositories.users_repo import UserRepo

router = APIRouter()


@router.post("/users/", tags=["users"])
async def save_user(request: Request, db: Session = Depends(get_db)):
    json = await request.json()
    user_name, chat_id = json["name"], json["chat_id"]
    user = UserRepo()
    await user.create(user_name, chat_id, db)
    return {"name": user_name}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {}  # ToDo


@router.get("/users/", tags=["users"])
async def read_users(db: Session = Depends(get_db)):
    users = db.query(User.all())
    results = [user.name for user in users]
    return results
