from pydantic import BaseModel

class UniverseCreate(BaseModel):
    name: str
    genre: str
    description: str


class UniverseResponse(UniverseCreate):
    id: int

    class Config:
        from_attributes = True