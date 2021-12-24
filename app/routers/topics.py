from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.models import Topic
from app.routers.utils import get_db

router = APIRouter()


@router.post("/topics/", tags=["topics"])
async def save_topics():
    return []  # ToDo


@router.get("/topics/{topic}", tags=["topics"])
async def read_topic(topic: str):
    return {}  # ToDo


@router.get("/topics/", tags=["topics"])
async def read_topics(db: Session = Depends(get_db)):
    topics = db.query(Topic).all()
    results = [topic.name for topic in topics]
    return results
