from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.report import ReportCreate
from app.models.report import Report
from app.core.database import SessionLocal
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter()
def get_db(): db=SessionLocal(); 
    try: yield db
    finally: db.close()

@router.post("/")
def create_report(r: ReportCreate, db: Session=Depends(get_db), user: User=Depends(get_current_user)):
    report = Report(reporter_id=user.id, reported_id=r.reported_id, reason=r.reason)
    db.add(report); db.commit(); db.refresh(report)
    return report
