from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float = 0.15
    description: str | None = None
    tax: float | None = None
    tags: list[str] = []


@app.post("/items")
async def update_item(item: Item):
    result = {"item": item}
    return result
