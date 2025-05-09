from fastapi import APIRouter
from app.schemas.report import ReportCreate

router = APIRouter()

@router.post("/")
def create_report(report: ReportCreate):
    return {"status": "Report received", "data": report}

