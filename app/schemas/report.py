from pydantic import BaseModel
from typing import Optional

class ReportCreate(BaseModel):
    match_id: int
    issue: str
    details: Optional[str] = None

class ReportOut(BaseModel):
    id: int
    match_id: int
    reporter_id: int
    issue: str
    details: Optional[str]

    class Config:
        from_attributes = True