from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.replay import Replay
from app.schemas.replay import ReplayCreate, ReplayOut
from app.core.deps import get_current_user, get_db
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=ReplayOut)
def save_replay(data: ReplayCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    replay = Replay(match_id=data.match_id, player_id=current_user.id, events=data.events)
    db.add(replay)
    db.commit()
    db.refresh(replay)
    return replay

@router.get("/", response_model=list[ReplayOut])
def get_replays(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Replay).filter(Replay.player_id == current_user.id).all()
