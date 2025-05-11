# app/routers/report.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.report import ReportCreate, ReportOut
from app.models.report import Report
from app.core.database import SessionLocal
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/reports", tags=["Reports"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ReportOut)
def create_report(
    payload: ReportCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    report = Report(
        reporter_id=user.id,
        reported_id=payload.reported_id,
        reason=payload.reason,
        details=payload.details,
    )
    db.add(report)
    db.commit()
    db.refresh(report)
    return report

@router.get("/my", response_model=List[ReportOut])
def my_reports(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return db.query(Report).filter(Report.reporter_id == user.id).all()

@router.get("/", response_model=List[ReportOut])
def all_reports(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    if not user.is_admin:
        return []
    return db.query(Report).all()