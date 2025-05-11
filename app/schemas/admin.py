# app/schemas/admin.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AdminLogOut(BaseModel):
    action: str
    target_id: Optional[int] = None
    timestamp: datetime

    class Config:
        from_attributes = True
