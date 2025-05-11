# === 1. Password Reset via Email (Token-Based)
# File: app/routers/password_reset.py

from fastapi import APIRouter, Depends, status, HTTPException, BackgroundTasks
from pydantic import EmailStr
from app.core.security import get_db
from app.models.user import User
from sqlalchemy.orm import Session
import secrets, os

router = APIRouter(prefix="/password-reset", tags=["Password Reset"])

reset_tokens = {}  # in-memory dict, replace with DB for prod

@router.post("/request")
def request_reset(email: EmailStr, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    token = secrets.token_urlsafe(32)
    reset_tokens[token] = user.id  # Store token
    # Simulate email send (log instead)
    print(f"Reset link: https://yourdomain/reset-password?token={token}")
    return {"message": "Reset email sent"}

@router.post("/confirm")
def confirm_reset(token: str, new_password: str, db: Session = Depends(get_db)):
    user_id = reset_tokens.get(token)
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = db.query(User).get(user_id)
    from passlib.context import CryptContext
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    user.hashed_password = pwd_context.hash(new_password)
    db.commit()
    return {"message": "Password updated"}
