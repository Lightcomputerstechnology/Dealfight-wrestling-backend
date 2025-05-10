from pydantic import BaseModel
from typing import Optional

class ReportCreate(BaseModel):
    reporter_id: int
    reported_id: int
    reason: str
    details: Optional[str] = None
