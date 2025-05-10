from pydantic import BaseModel
from typing import Literal, Optional

class MatchCreate(BaseModel):
    type: Literal["single", "tag"] = "single"
    opponent_id: Optional[int] = None

class MatchOut(BaseModel):
    id: int
    type: Literal["single", "tag"]
    status: str
    player1_id: int
    player2_id: Optional[int]

    class Config:
        from_attributes = True