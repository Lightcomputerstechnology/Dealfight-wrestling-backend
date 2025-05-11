from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.models.notification import Notification
from app.schemas.notification import NotificationOut
from app.core.database import SessionLocal
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/users", tags=["Notifications"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/notifications", response_model=List[NotificationOut])
def get_notifications(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return db.query(Notification).filter(Notification.user_id == user.id).order_by(Notification.timestamp.desc()).all()
