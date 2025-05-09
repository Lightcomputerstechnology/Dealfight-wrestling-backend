from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.report import ReportCreate
from app.models.report import Report
from app.models.user import User
from app.core.security import get_current_user
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_report(report: ReportCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_user = db.query(User).filter(User.username == user).first()
    new_report = Report(**report.dict(), reporter_id=db_user.id)
    db.add(new_report)
    db.commit()
    db.refresh(new_report)
    return {"message": "Report submitted", "report_id": new_report.id}