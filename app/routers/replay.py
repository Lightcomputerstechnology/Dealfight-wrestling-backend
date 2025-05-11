# app/routers/replay.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.core.security import get_current_user
from app.models.replay import Replay
from app.schemas.replay import ReplayLog, ReplayOut
from app.models.user import User
from typing import List

router = APIRouter(prefix="/replays", tags=["Replays"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=dict)
def log_replay(data: ReplayLog, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    replay = Replay(match_id=data.match_id, player_id=user.id, events=data.events)
    db.add(replay)
    db.commit()
    db.refresh(replay)
    return {"message": "Replay saved", "id": replay.id}

@router.get("/mine", response_model=List[ReplayOut])
def get_my_replays(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return db.query(Replay).filter(Replay.player_id == user.id).order_by(Replay.created_at.desc()).all()

