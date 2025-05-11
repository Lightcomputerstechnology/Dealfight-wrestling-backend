from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.wallet import Wallet
from app.schemas.wallet import WalletOut, WalletAdd
from app.core.security import get_current_user
from app.core.database import SessionLocal
from app.models.user import User

router = APIRouter(prefix="/wallet", tags=["Wallet"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=WalletOut)
def get_wallet(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    wallet = db.query(Wallet).filter(Wallet.user_id == user.id).first()
    if not wallet:
        wallet = Wallet(user_id=user.id)
        db.add(wallet)
        db.commit()
        db.refresh(wallet)
    return wallet

@router.post("/add")
def add_currency(
    data: WalletAdd,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    wallet = db.query(Wallet).filter(Wallet.user_id == user.id).first()
    if not wallet:
        wallet = Wallet(user_id=user.id)
        db.add(wallet)
        db.commit()
        db.refresh(wallet)

    if data.amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount")

    if data.type == "coins":
        wallet.coins += data.amount
    elif data.type == "diamonds":
        wallet.diamonds += data.amount
    else:
        raise HTTPException(status_code=400, detail="Invalid currency type")

    db.commit()
    return {"message": f"{data.amount} {data.type} added"}
