from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from src.app.api.routers.utils import get_db
from src.app.models.models import Topic
from src.app.repositories.topics_repo import TopicRepo

router = APIRouter()


@router.post("/topics/", tags=["topics"])
async def save_topics(request: Request, db: Session = Depends(get_db)):
    json = await request.json()
    topic = TopicRepo()
    name = json["name"]
    await topic.create(name, db)
    return {"name": name}


@router.get("/topics/{topic}", tags=["topics"])
async def read_topic(topic: str):
    return {}  # ToDo


@router.get("/topics/", tags=["topics"])
async def read_topics(db: Session = Depends(get_db)):
    topics = db.query(Topic).all()
    results = [topic.name for topic in topics]
    return results
