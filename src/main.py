from fastapi import FastAPI, Response, status

from .books.routes import router as books_router
from .utils import CONTACT, DESCRIPTION, SERVERS, TITLE, latest_tag

app = FastAPI(
    title=TITLE,
    description=DESCRIPTION,
    version=latest_tag(),
    docs_url="/docs",
    redoc_url=None,
    contact=CONTACT,
    servers=SERVERS,
    license_info={"name": "MIT"},
    openapi_url="/openapi.json",
)
app.include_router(books_router, prefix="/books")


@app.get("/")
async def root():
    return {"message": "BOOKS API", "docs": "http://127.0.0.1:8000/docs"}


@app.get("/healthcheck")
async def healthcheck():
    return Response(status_code=status.HTTP_200_OK)
