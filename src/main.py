from fastapi import FastAPI

from src.routers.movies import router as movies_router

app = FastAPI(title="Movies API")
app.include_router(movies_router)


@app.get("/")
async def root():
    return {"message": "Movies API готов к работе!"}
