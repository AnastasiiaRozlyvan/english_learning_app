from fastapi import Depends
from sqlalchemy.orm import Session

from src.app.api.routers.utils import get_db
from src.app.models.models import Topic


class TopicRepo:
    def __init__(self):
        pass

    async def create(self, user_name, db: Session = Depends(get_db)):
        db.add(Topic(name=user_name))
        db.commit()
