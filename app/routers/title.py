from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.title import TitleAssign
from app.models.title import TitleBelt
from app.core.database import SessionLocal
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter()
def get_db(): db=SessionLocal(); 
    try: yield db
    finally: db.close()

@router.post("/assign")
def assign_title(t: TitleAssign, db: Session=Depends(get_db), user: User=Depends(get_current_user)):
    belt = TitleBelt(type=t.type, holder_id=t.holder_id)
    db.add(belt); db.commit(); db.refresh(belt)
    return belt
