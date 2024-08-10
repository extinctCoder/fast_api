from fastapi import APIRouter

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/")
async def root():
    return {"message": "BOOKS END POINT"}
