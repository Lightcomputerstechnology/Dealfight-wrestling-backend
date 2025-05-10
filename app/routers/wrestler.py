from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.wrestler import WrestlerCreate, WrestlerOut
from app.models.wrestler import Wrestler
from app.models.user import User
from app.core.security import get_current_user
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create", response_model=WrestlerOut)
def create_wrestler(
    wrestler: WrestlerCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    db_user = db.query(User).filter(User.username == user).first()
    new = Wrestler(**wrestler.dict(), owner_id=db_user.id)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@router.get("/my-wrestlers", response_model=List[WrestlerOut])
def my_wrestlers(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    db_user = db.query(User).filter(User.username == user).first()
    return db.query(Wrestler).filter(Wrestler.owner_id == db_user.id).all()