from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.report import Report
from app.schemas.report import ReportCreate
from app.core.deps import get_current_user, get_db
from app.models.user import User

router = APIRouter()

@router.post("/")
def submit_report(data: ReportCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.id == data.reported_id:
        raise HTTPException(status_code=400, detail="You cannot report yourself.")
    report = Report(reporter_id=current_user.id, reported_id=data.reported_id, reason=data.reason)
    db.add(report)
    db.commit()
    return {"message": "Report submitted successfully."}
