# app/routers/replay.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.replay import ReplayLog
from app.models.replay import Replay
from app.core.database import SessionLocal
from app.core.security import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/log")
def log_replay(
    log: ReplayLog,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    new = Replay(
        match_id=log.match_id,
        events=log.events,
        player_id=user.id,
    )
    db.add(new)
    db.commit()
    db.refresh(new)
    return {"message": "Replay logged", "id": new.id}