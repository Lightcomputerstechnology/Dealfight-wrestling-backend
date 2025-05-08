from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime

class ReplayCreate(BaseModel):
    match_id: int
    events: List[Dict]

class ReplayOut(ReplayCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True