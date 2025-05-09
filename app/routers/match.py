from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.match import MatchCreate
from app.models.match import Match
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

@router.post("/create")
def create_match(data: MatchCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_user = db.query(User).filter(User.username == user).first()
    match = Match(type=data.type, player1_id=db_user.id, player2_id=data.opponent_id)
    db.add(match)
    db.commit()
    db.refresh(match)
    return {"match_id": match.id, "status": match.status}

@router.get("/my-matches")
def my_matches(db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_user = db.query(User).filter(User.username == user).first()
    matches = db.query(Match).filter(
        (Match.player1_id == db_user.id) | (Match.player2_id == db_user.id)
    ).all()
    return matches
