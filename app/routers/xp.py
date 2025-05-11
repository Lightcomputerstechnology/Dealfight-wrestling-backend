# app/routers/xp.py

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.xp import XPUpdate, XPLogOut
from app.models import XPLog  # ✅ Indirect import to avoid duplicate table
from app.core.database import SessionLocal
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/xp", tags=["XP / Levels"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST: Update XP
@router.post("/update", status_code=status.HTTP_200_OK)
def update_xp(payload: XPUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    base_xp = 20
    win_bonus = 30 if payload.won else 0

    user.xp += base_xp + win_bonus
    user.matches_played += 1
    if payload.won:
        user.matches_won += 1

    user.level = user.xp // 100 + 1

    log = XPLog(
        user_id=user.id,
        xp_gained=base_xp + win_bonus,
        level=user.level
    )
    db.add(log)
    db.commit()
    db.refresh(user)

    return {"xp": user.xp, "level": user.level}

# GET: XP History
@router.get("/history", response_model=list[XPLogOut])
def get_xp_history(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return db.query(XPLog).filter(XPLog.user_id == user.id).order_by(XPLog.timestamp.desc()).all()