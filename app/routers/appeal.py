### app/routers/appeal.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.core.database import SessionLocal
from app.models.user import User
from app.models.appeal import BanAppeal
from app.schemas.appeal import AppealCreate, AppealOut
from typing import List

router = APIRouter(prefix="/ban-appeals", tags=["BanAppeal"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/", status_code=status.HTTP_201_CREATED)
def submit_appeal(payload: AppealCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    appeal = BanAppeal(user_id=user.id, reason=payload.reason)
    db.add(appeal)
    db.commit()
    db.refresh(appeal)
    return appeal

@router.get("/mine", response_model=List[AppealOut])
def get_my_appeals(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return db.query(BanAppeal).filter(BanAppeal.user_id == user.id).all()
