from pydantic import BaseModel

class CharacterCreate(BaseModel):
    name: str
    role: str
    description: str
    universe_id: int


class CharacterResponse(BaseModel):
    id: int
    name: str
    role: str
    description: str
    universe_id: int

    class Config:
        from_attributes = True