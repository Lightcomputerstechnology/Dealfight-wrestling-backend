from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.replay import ReplayLog
from app.models.replay import Replay
from app.core.database import SessionLocal
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter()
def get_db(): db=SessionLocal(); 
    try: yield db
    finally: db.close()

@router.post("/")
def log_replay(r: ReplayLog, db: Session=Depends(get_db), user: User=Depends(get_current_user)):
    rep = Replay(match_id=r.match_id, player_id=user.id, events=r.events)
    db.add(rep); db.commit(); db.refresh(rep)
    return rep
