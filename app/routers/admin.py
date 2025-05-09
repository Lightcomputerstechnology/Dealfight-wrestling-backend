from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User
from app.models.match import Match
from app.models.report import Report
from app.core.security import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/stats")
def admin_dashboard(user=Depends(get_current_user), db: Session = Depends(get_db)):
    if user != "admin":
        return {"error": "Admins only"}

    total_users = db.query(User).count()
    total_matches = db.query(Match).count()
    total_reports = db.query(Report).count()

    return {
        "total_users": total_users,
        "total_matches": total_matches,
        "total_reports": total_reports
    }
