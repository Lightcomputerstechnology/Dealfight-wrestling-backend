# app/routers/admin.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.user import User
from app.models.report import Report
from app.models.admin_log import AdminLog
from app.schemas.admin import AdminLogOut
from app.core.database import SessionLocal
from app.core.security import get_current_user

router = APIRouter(prefix="/admin", tags=["Admin"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def require_admin(user: User = Depends(get_current_user)):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")
    return user

@router.get("/users", response_model=List[dict])
def list_users(db: Session = Depends(get_db), _: User = Depends(require_admin)):
    return db.query(User).all()

@router.delete("/users/{user_id}")
def ban_user(user_id: int, db: Session = Depends(get_db), _: User = Depends(require_admin)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    log = AdminLog(action=f"Banned user {user_id}", target_id=user_id)
    db.add(log)
    db.commit()
    return {"detail": f"User {user_id} banned"}

@router.get("/reports", response_model=List[dict])
def view_reports(db: Session = Depends(get_db), _: User = Depends(require_admin)):
    return db.query(Report).order_by(Report.timestamp.desc()).all()

@router.get("/logs", response_model=List[AdminLogOut])
def get_admin_logs(db: Session = Depends(get_db), _: User = Depends(require_admin)):
    return db.query(AdminLog).order_by(AdminLog.timestamp.desc()).all()
