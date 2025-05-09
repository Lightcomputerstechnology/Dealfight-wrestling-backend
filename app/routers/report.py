from fastapi import APIRouter, Depends
from app.schemas.report import ReportCreate
from app.core.security import get_current_user

router = APIRouter()

@router.post("/")
def create_report(report: ReportCreate, user=Depends(get_current_user)):
    return {"status": "Report received", "report": report, "by": user}