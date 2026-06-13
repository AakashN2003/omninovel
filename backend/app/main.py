from fastapi import FastAPI

from app.routes.universes import router as universe_router
from app.routes import characters
from app.routes import novels

app = FastAPI(title="OmniNovel API")

app.include_router(universe_router)
app.include_router(characters.router)
app.include_router(novels.router)


@app.get("/")
def root():
    return {
        "message": "OmniNovel API Running"
    }