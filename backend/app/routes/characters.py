from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.character import Character
from app.schemas.character import (
    CharacterCreate,
    CharacterResponse
)

router = APIRouter(
    prefix="/characters",
    tags=["Characters"]
)

@router.post("/", response_model=CharacterResponse)
def create_character(
    character: CharacterCreate,
    db: Session = Depends(get_db)
):
    db_character = Character(
        name=character.name,
        role=character.role,
        description=character.description,
        universe_id=character.universe_id
    )

    db.add(db_character)
    db.commit()
    db.refresh(db_character)

    return db_character

@router.get("/", response_model=list[CharacterResponse])
def get_characters(
    db: Session = Depends(get_db)
):
    return db.query(Character).all()

@router.get("/{character_id}", response_model=CharacterResponse)
def get_character(
    character_id: int,
    db: Session = Depends(get_db)
):
    character = (
        db.query(Character)
        .filter(Character.id == character_id)
        .first()
    )

    if not character:
        raise HTTPException(
            status_code=404,
            detail="Character not found"
        )

    return character

@router.put("/{character_id}", response_model=CharacterResponse)
def update_character(
    character_id: int,
    character_data: CharacterCreate,
    db: Session = Depends(get_db)
):
    character = (
        db.query(Character)
        .filter(Character.id == character_id)
        .first()
    )

    if not character:
        raise HTTPException(
            status_code=404,
            detail="Character not found"
        )

    character.name = character_data.name
    character.role = character_data.role
    character.description = character_data.description
    character.universe_id = character_data.universe_id

    db.commit()
    db.refresh(character)

    return character

@router.delete("/{character_id}")
def delete_character(
    character_id: int,
    db: Session = Depends(get_db)
):
    character = (
        db.query(Character)
        .filter(Character.id == character_id)
        .first()
    )

    if not character:
        raise HTTPException(
            status_code=404,
            detail="Character not found"
        )

    db.delete(character)
    db.commit()

    return {
        "message": "Character deleted successfully"
    }