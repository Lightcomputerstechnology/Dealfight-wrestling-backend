# app/schemas/xp.py

from pydantic import BaseModel
from datetime import datetime

class XPUpdate(BaseModel):
    won: bool  # Whether the user won the match or not

class XPLogOut(BaseModel):
    id: int
    xp_gained: int
    level: int
    timestamp: datetime

    class Config:
        from_attributes = True