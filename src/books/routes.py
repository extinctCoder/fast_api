from fastapi import APIRouter

router = APIRouter(tags=["Book"])


@router.get("")
async def root():
    return {"message": "BOOKS END POINT"}
