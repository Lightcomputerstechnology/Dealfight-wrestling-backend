from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.match import MatchCreate, MatchOut
from app.models.match import Match
from app.models.user import User
from app.core.database import SessionLocal
from app.core.security import get_current_user

router = APIRouter(prefix="/matches", tags=["Matches"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# === Create match
@router.post("/create", response_model=MatchOut)
def create_match(
    m: MatchCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    match = Match(
        type=m.type,
        player1_id=user.id,
        player2_id=m.opponent_id
    )
    db.add(match)
    db.commit()
    db.refresh(match)
    return match


# === List all matches for user
@router.get("/my-matches", response_model=List[MatchOut])
def my_matches(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return db.query(Match).filter(
        (Match.player1_id == user.id) | (Match.player2_id == user.id)
    ).order_by(Match.created_at.desc()).all()


# === Incomplete matches (for result submission)
@router.get("/incomplete", response_model=List[MatchOut])
def incomplete_matches(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return db.query(Match).filter(
        ((Match.player1_id == user.id) | (Match.player2_id == user.id)) &
        (Match.status == "pending")
    ).all()


# === Submit match result
@router.post("/submit-result")
def submit_result(
    match_id: int,
    winner: str,  # "self" or "opponent"
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    match = db.query(Match).filter(Match.id == match_id).first()
    if not match or (match.player1_id != user.id and match.player2_id != user.id):
        raise HTTPException(status_code=404, detail="Match not found or unauthorized")

    match.status = "completed"
    winner_user_id = user.id if winner == "self" else (
        match.player2_id if match.player1_id == user.id else match.player1_id
    )

    winner_user = db.query(User).filter(User.id == winner_user_id).first()
    if winner_user:
        winner_user.matches_won += 1
        winner_user.xp += 10  # reward XP
    db.commit()
    return {"message": "Result submitted", "winner_id": winner_user_id}


# === Matchmaking route (random AI or player)
@router.post("/search", response_model=MatchOut)
def search_match(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    # Check for existing open match
    open_match = db.query(Match).filter(
        Match.status == "pending",
        Match.player2_id == None,
        Match.player1_id != user.id
    ).first()

    if open_match:
        open_match.player2_id = user.id
        db.commit()
        db.refresh(open_match)
        return open_match

    # If not found, create match and wait
    new_match = Match(type="single", player1_id=user.id)
    db.add(new_match)
    db.commit()
    db.refresh(new_match)
    return new_match