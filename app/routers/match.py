from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.match import MatchCreate
from app.models.match import Match
from app.models.user import User
from app.core.database import SessionLocal
from app.core.security import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal(); 
    try: yield db
    finally: db.close()

@router.post("/create")
def create_match(m: MatchCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    match = Match(type=m.type, player1_id=user.id, player2_id=m.opponent_id)
    db.add(match); db.commit(); db.refresh(match)
    return match

# etc...