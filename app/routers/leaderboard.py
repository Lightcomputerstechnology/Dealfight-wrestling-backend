# === 2. Leaderboard Router Update (app/routers/leaderboard.py) ===

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User

router = APIRouter(prefix="/leaderboard", tags=["Leaderboard"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("/")
def get_leaderboard(db: Session = Depends(get_db)):
    return db.query(User).order_by(User.level.desc(), User.xp.desc(), User.matches_won.desc()).limit(50).all()


# === 3. XP Tracking System (app/models/xp_log.py + router/schemas) ===

# models/xp_log.py
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class XPLog(Base):
    __tablename__ = "xp_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    xp_gained = Column(Integer)
    level = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
