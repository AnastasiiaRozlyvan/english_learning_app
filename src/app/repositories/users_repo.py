from fastapi import Depends
from sqlalchemy.orm import Session

from src.app.api.routers.utils import get_db
from src.app.models.models import User


class UserRepo:
    def __init__(self):
        pass

    async def create(self, user_name, chat_id, db: Session = Depends(get_db)):
        db.add(User(name=user_name, chat_id=chat_id))
        db.commit()
