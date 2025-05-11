# app/routers/xp.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.xp import XPUpdate
from app.core.database import SessionLocal
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/xp", tags=["XP / Levels"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/update", status_code=status.HTTP_200_OK)
def update_xp(payload: XPUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    """
    Increase XP and level after a match.
    """
    user.xp += 20  # base XP for participating
    user.matches_played += 1
    if payload.won:
        user.xp += 30  # bonus XP for win
        user.matches_won += 1

    # Auto level-up
    user.level = user.xp // 100 + 1
    db.commit()
    return {"xp": user.xp, "level": user.level}