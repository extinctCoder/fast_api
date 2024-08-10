from fastapi import FastAPI, Response, status

from books.routes import router as books_router

app = FastAPI()
app.include_router(books_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/healthcheck")
async def healthcheck():
    return Response(status_code=status.HTTP_200_OK)
