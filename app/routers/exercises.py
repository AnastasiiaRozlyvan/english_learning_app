from fastapi import APIRouter

router = APIRouter()


@router.post("/exercises/", tags=["exercises"])
async def write_users():
    return []  # ToDo


@router.get("/exercises/{word}", tags=["exercises"])
async def read_exercise(word: str):
    return {}  # ToDo
