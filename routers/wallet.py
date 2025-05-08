from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.deps import get_current_user, get_db
from app.schemas.user import WalletOut
from app.core.permissions import admin_required  # NEW LINE

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

# NEW ADMIN ROUTE
@router.post("/admin-add")
def admin_add_wallet(
    user_id: int,
    coins: int = 0,
    diamonds: int = 0,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.coins += coins
    user.diamonds += diamonds
    db.commit()
    return {"message": f"Wallet updated for user {user.username}"}