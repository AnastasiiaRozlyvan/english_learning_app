from sqlalchemy import Column, ForeignKey, Integer, String

from .database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(
        Integer, primary_key=True, index=True, autoincrement=True
    )
    name = Column(String, index=True)
    chat_id = Column(Integer, unique=True, index=True)


class Topic(Base):
    __tablename__ = "topic"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)


class Word(Base):
    __tablename__ = "word"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
