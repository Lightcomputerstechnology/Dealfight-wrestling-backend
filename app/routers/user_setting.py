# app/routers/user_setting.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.settings import UserSetting
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.settings import SettingsUpdate

router = APIRouter(prefix="/user-settings", tags=["User Settings"])  # <-- This must be present

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("/")
def get_user_settings(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return db.query(UserSetting).filter(UserSetting.user_id == user.id).first()

@router.put("/")
def update_user_settings(payload: SettingsUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    setting = db.query(UserSetting).filter(UserSetting.user_id == user.id).first()
    if setting:
        for key, value in payload.dict().items():
            setattr(setting, key, value)
    else:
        setting = UserSetting(user_id=user.id, **payload.dict())
        db.add(setting)
    db.commit()
    return setting