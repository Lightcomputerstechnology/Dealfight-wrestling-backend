from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_current_user, get_db
from app.models.match import Match
from app.schemas.match import MatchCreate, MatchOut
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=MatchOut)
def create_match(data: MatchCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    match = Match(type=data.type, player1_id=current_user.id)
    db.add(match)
    db.commit()
    db.refresh(match)
    return match

@router.get("/my-matches", response_model=list[MatchOut])
def get_my_matches(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Match).filter(
        (Match.player1_id == current_user.id) | (Match.player2_id == current_user.id)
    ).all()
