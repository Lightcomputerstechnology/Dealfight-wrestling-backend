### app/routers/settings.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.settings import UserSetting
from app.schemas.settings import SettingsUpdate
from app.core.security import get_current_user
from app.core.database import SessionLocal
from app.models.user import User

router = APIRouter(prefix="/settings", tags=["Settings"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("/")
def get_settings(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    setting = db.query(UserSetting).filter(UserSetting.user_id == user.id).first()
    return setting

@router.put("/")
def update_settings(payload: SettingsUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    setting = db.query(UserSetting).filter(UserSetting.user_id == user.id).first()
    if setting:
        for key, value in payload.dict().items():
            setattr(setting, key, value)
    else:
        setting = UserSetting(user_id=user.id, **payload.dict())
        db.add(setting)
    db.commit()
    return setting
