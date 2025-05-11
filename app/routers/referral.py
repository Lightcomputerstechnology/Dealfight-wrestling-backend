### app/routers/referral.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.core.database import SessionLocal
from app.models.user import User
from app.models.referral import Referral
from app.schemas.referral import ReferralCreate, ReferralOut
from typing import List

router = APIRouter(prefix="/referrals", tags=["Referral"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/", status_code=status.HTTP_201_CREATED)
def refer_user(payload: ReferralCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    referral = Referral(user_id=user.id, referred_email=payload.referred_email)
    db.add(referral)
    db.commit()
    db.refresh(referral)
    return referral

@router.get("/mine", response_model=List[ReferralOut])
def get_my_referrals(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return db.query(Referral).filter(Referral.user_id == user.id).all()