from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.wrestler import WrestlerCreate, WrestlerOut
from app.schemas.response import MessageResponse  # ✅ Added
from app.models.wrestler import Wrestler
from app.core.security import get_current_user
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create", response_model=MessageResponse)  # ✅ Updated from dict to proper model
def create_wrestler(
    wrestler: WrestlerCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    new = Wrestler(**wrestler.dict(), owner_id=user.id)
    db.add(new)
    db.commit()
    db.refresh(new)
    return {"message": "Wrestler created", "id": new.id}

@router.get("/my-wrestlers", response_model=List[WrestlerOut])
def my_wrestlers(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return db.query(Wrestler).filter(Wrestler.owner_id == user.id).all()