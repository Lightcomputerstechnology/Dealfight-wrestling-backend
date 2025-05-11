from pydantic import BaseModel
from typing import List
from datetime import datetime

class ReplayLog(BaseModel):
    match_id: int
    events: List[str]

class ReplayOut(BaseModel):
    id: int
    match_id: int
    events: List[str]
    created_at: datetime

    class Config:
        from_attributes = True  # Required for SQLAlchemy model compatibility