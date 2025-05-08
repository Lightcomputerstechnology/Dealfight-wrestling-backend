from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.wrestler import WrestlerCreate, WrestlerOut
from app.models.wrestler import Wrestler
from app.core.deps import get_current_user, get_db
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=WrestlerOut)
def create_wrestler(wrestler: WrestlerCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_wrestler = Wrestler(**wrestler.dict(), owner_id=current_user.id)
    db.add(db_wrestler)
    db.commit()
    db.refresh(db_wrestler)
    return db_wrestler

@router.get("/", response_model=list[WrestlerOut])
def get_my_wrestlers(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Wrestler).filter(Wrestler.owner_id == current_user.id).all()
