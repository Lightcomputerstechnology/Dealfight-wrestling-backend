# === 2. Token Refresh / Blacklist System (Simple Refresh Endpoint)
# File: app/routers/token.py

from fastapi import APIRouter, Depends
from app.core.security import get_current_user, create_access_token
from app.models.user import User

router = APIRouter(prefix="/token", tags=["Auth"])

@router.post("/refresh")
def refresh_token(user: User = Depends(get_current_user)):
    new_token = create_access_token({"sub": user.id})
    return {"access_token": new_token, "token_type": "bearer"}
