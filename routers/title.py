from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.title import TitleBelt
from app.schemas.title import TitleOut
from app.core.deps import get_db

router = APIRouter()

@router.get("/", response_model=list[TitleOut])
def get_titles(db: Session = Depends(get_db)):
    return db.query(TitleBelt).all()
