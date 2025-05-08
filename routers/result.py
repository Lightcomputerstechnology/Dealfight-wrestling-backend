from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.deps import get_current_user, get_db
from app.models.user import User
from app.models.title import TitleBelt, TitleType
from datetime import datetime

router = APIRouter()

@router.post("/complete-match")
def complete_match(
    winner_id: int,
    loser_id: int,
    title_type: TitleType = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Reward winner
    winner = db.query(User).filter(User.id == winner_id).first()
    if not winner:
        raise HTTPException(status_code=404, detail="Winner not found")
    
    winner.coins += 100
    winner.xp += 50
    winner.matches_won += 1
    winner.ranking_points += 10

    # Optional: Update title holder
    if title_type:
        belt = db.query(TitleBelt).filter(TitleBelt.type == title_type).first()
        if belt:
            belt.holder_id = winner.id
            belt.updated_at = datetime.utcnow()
        else:
            new_belt = TitleBelt(type=title_type, holder_id=winner.id)
            db.add(new_belt)

    db.commit()
    return {"message": f"{winner.username} rewarded and title updated if applicable."}