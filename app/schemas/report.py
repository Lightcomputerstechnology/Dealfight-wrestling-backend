# app/schemas/report.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReportCreate(BaseModel):
    reported_id: int
    reason: str
    details: Optional[str] = None

class ReportOut(BaseModel):
    id: int
    reported_id: int
    reason: str
    details: Optional[str]
    timestamp: datetime

    class Config:
        from_attributes = True