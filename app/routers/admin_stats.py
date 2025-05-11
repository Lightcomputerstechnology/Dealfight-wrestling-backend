# === 1. Admin Stats Router (app/routers/admin_stats.py) ===

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User
from app.models.match import Match
from app.models.replay import Replay
from app.models.report import Report

router = APIRouter(prefix="/admin", tags=["Admin"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("/stats")
def get_admin_stats(db: Session = Depends(get_db)):
    return {
        "users": db.query(User).count(),
        "matches": db.query(Match).count(),
        "replays": db.query(Replay).count(),
        "reports": db.query(Report).count(),
    }
