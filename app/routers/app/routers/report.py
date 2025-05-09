from fastapi import APIRouter, HTTPException, status
from app.schemas.report import ReportCreate  # Corrected import path

router = APIRouter()

# Dummy storage for example
reports_db = []

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_report(report: ReportCreate):
    report_data = report.dict()
    reports_db.append(report_data)
    return {"message": "Report created successfully", "data": report_data}