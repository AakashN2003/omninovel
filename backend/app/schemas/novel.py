from pydantic import BaseModel


class NovelCreate(BaseModel):
    universe_id: int
    title: str
    description: str | None = None
    genre: str | None = None
    status: str = "Planning"
    author: str | None = None


class NovelResponse(BaseModel):
    id: int
    universe_id: int
    title: str
    description: str | None = None
    genre: str | None = None
    status: str
    author: str | None = None
    total_chapters: int

    class Config:
        from_attributes = True