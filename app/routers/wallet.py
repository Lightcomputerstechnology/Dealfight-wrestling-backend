from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User
from app.core.security import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/balance")
def get_balance(user=Depends(get_current_user), db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"coins": db_user.coins, "diamonds": db_user.diamonds}

