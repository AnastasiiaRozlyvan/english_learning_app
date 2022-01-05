from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from .database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid4
    )
    name = Column(String, index=True)
    chat_id = Column(Integer, unique=True, index=True)


class Topic(Base):
    __tablename__ = "topic"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Word(Base):
    __tablename__ = "word"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
