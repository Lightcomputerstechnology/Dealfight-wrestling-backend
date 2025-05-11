# === app/routers/leaderboard.py (Upgraded) ===
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserOut
from typing import List

router = APIRouter(prefix="/leaderboard", tags=["Leaderboard"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[UserOut])
def get_leaderboard(db: Session = Depends(get_db)):
    """Leaderboard ordered by level, xp, then matches won."""
    return db.query(User).order_by(
        User.level.desc(),
        User.xp.desc(),
        User.matches_won.desc()
    ).limit(50).all()


# === app/models/xp_log.py ===
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class XPLog(Base):
    __tablename__ = "xp_logs"

    id         = Column(Integer, primary_key=True, index=True)
    user_id    = Column(Integer, ForeignKey("users.id"))
    xp_gained  = Column(Integer, nullable=False)
    level      = Column(Integer, nullable=False)
    timestamp  = Column(DateTime, default=datetime.utcnow)

    user       = relationship("User")


# === app/schemas/xp_log.py ===
from pydantic import BaseModel
from datetime import datetime

class XPLogOut(BaseModel):
    xp_gained: int
    level: int
    timestamp: datetime

    class Config:
        from_attributes = True


# === app/routers/xp.py ===
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.core.security import get_current_user
from app.models.user import User
from app.models.xp_log import XPLog
from app.schemas.xp_log import XPLogOut
from typing import List

router = APIRouter(prefix="/xp", tags=["XP System"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/history", response_model=List[XPLogOut])
def xp_history(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return db.query(XPLog).filter(XPLog.user_id == user.id).order_by(XPLog.timestamp.desc()).all()
