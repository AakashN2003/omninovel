from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.novel import Novel
from app.schemas.novel import NovelCreate, NovelResponse

router = APIRouter(
    prefix="/novels",
    tags=["Novels"]
)


@router.post("/", response_model=NovelResponse)
def create_novel(novel: NovelCreate, db: Session = Depends(get_db)):
    db_novel = Novel(**novel.model_dump())

    db.add(db_novel)
    db.commit()
    db.refresh(db_novel)

    return db_novel


@router.get("/", response_model=list[NovelResponse])
def get_novels(db: Session = Depends(get_db)):
    return db.query(Novel).all()


@router.get("/{novel_id}", response_model=NovelResponse)
def get_novel(novel_id: int, db: Session = Depends(get_db)):
    novel = db.query(Novel).filter(
        Novel.id == novel_id
    ).first()

    if not novel:
        raise HTTPException(
            status_code=404,
            detail="Novel not found"
        )

    return novel


@router.delete("/{novel_id}")
def delete_novel(novel_id: int, db: Session = Depends(get_db)):
    novel = db.query(Novel).filter(
        Novel.id == novel_id
    ).first()

    if not novel:
        raise HTTPException(
            status_code=404,
            detail="Novel not found"
        )

    db.delete(novel)
    db.commit()

    return {"message": "Novel deleted"}