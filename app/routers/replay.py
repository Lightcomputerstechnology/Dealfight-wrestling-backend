from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.replay import ReplayLog
from app.models.replay import Replay
from app.models.user import User
from app.core.security import get_current_user
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/log")
def log_replay(data: ReplayLog, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_user = db.query(User).filter(User.username == user).first()
    replay = Replay(match_id=data.match_id, player_id=db_user.id, events=data.events)
    db.add(replay)
    db.commit()
    return {"message": "Replay saved"}

@router.get("/my")
def my_replays(db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_user = db.query(User).filter(User.username == user).first()
    return db.query(Replay).filter(Replay.player_id == db_user.id).all()
