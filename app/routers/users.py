from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.routers.utils import get_db
from app.models.models import User
from uuid import uuid4

router = APIRouter()


@router.post("/users/", tags=["users"])
async def save_user(request: Request, db: Session = Depends(get_db)):
    json = await request.json()
    user_name, user_id = json['name'], uuid4()
    db.add(User(id=user_id, name=user_name))
    db.commit()
    return {"id": user_id, "name": user_name}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {}  # ToDo
