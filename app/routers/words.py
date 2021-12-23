from fastapi import APIRouter

router = APIRouter()


@router.post("/words/", tags=["words"])
async def save_word_progress():
    return []  # ToDo


@router.get("/words/{word}", tags=["words"])
async def read_word_progress(username: str):
    return {}   # ToDo
