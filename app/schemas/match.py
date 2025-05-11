from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class MatchCreate(BaseModel):
    type: Literal["single", "tag"] = "single"
    opponent_id: Optional[int] = None

class MatchOut(BaseModel):
    id: int
    type: str
    status: str
    created_at: datetime
    player1_id: int
    player2_id: Optional[int]

    class Config:
        from_attributes = True