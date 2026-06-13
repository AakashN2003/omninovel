from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.universe import Universe
from app.schemas.universe import (
    UniverseCreate,
    UniverseResponse
)

router = APIRouter(
    prefix="/universes",
    tags=["Universes"]
)

@router.post("/", response_model=UniverseResponse)
def create_universe(
    universe: UniverseCreate,
    db: Session = Depends(get_db)
):
    db_universe = Universe(
        name=universe.name,
        genre=universe.genre,
        description=universe.description
    )

    db.add(db_universe)
    db.commit()
    db.refresh(db_universe)

    return db_universe


@router.get("/", response_model=list[UniverseResponse])
def get_universes(
    db: Session = Depends(get_db)
):
    return db.query(Universe).all()