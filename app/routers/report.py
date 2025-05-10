# app/routers/report.py

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.report import ReportCreate
from app.models.report import Report
from app.core.database import SessionLocal
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/reports", tags=["Reports"])


# Dependency ────────────────────────────────────────────────────────────────
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Routes ────────────────────────────────────────────────────────────────────
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_report(
    payload: ReportCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """
    Create a new user-generated report.
    """
    report = Report(
        reporter_id=user.id,
        reported_id=payload.reported_id,
        reason=payload.reason,
    )
    db.add(report)
    db.commit()
    db.refresh(report)
    return report