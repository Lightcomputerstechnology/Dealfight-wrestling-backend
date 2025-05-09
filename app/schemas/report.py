app/schemas/report.py

from pydantic import BaseModel
from typing import Optional

class ReportCreate(BaseModel):
    match_id: int
    reporter_id: int
    reason: str
    details: Optional[str] = None

