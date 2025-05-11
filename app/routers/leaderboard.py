# app/routers/leaderboard.py
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User
from app.schemas.leaderboard import LeaderboardUser

router = APIRouter(prefix="/leaderboard", tags=["Leaderboard"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[LeaderboardUser])
def get_leaderboard(
    limit: int = Query(20, le=100),
    db: Session = Depends(get_db)
):
    return (
        db.query(User)
        .order_by(User.xp.desc(), User.matches_won.desc())
        .limit(limit)
        .all()
    )