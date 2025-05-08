from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.deps import get_current_user, get_db
from app.schemas.user import WalletOut

router = APIRouter()

@router.get("/", response_model=WalletOut)
def get_wallet(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return current_user

@router.post("/add")
def add_wallet(coins: int = 0, diamonds: int = 0, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    current_user.coins += coins
    current_user.diamonds += diamonds
    db.commit()
    return {"message": "Wallet updated successfully"}
