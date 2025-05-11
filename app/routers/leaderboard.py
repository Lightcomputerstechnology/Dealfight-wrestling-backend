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