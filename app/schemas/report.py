schemas/report.py

from pydantic import BaseModel
from typing import Optional

class ReportCreate(BaseModel):
    title: str
    description: Optional[str] = None
    user_id: int