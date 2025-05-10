from pydantic import BaseModel
from typing import List

class ReplayLog(BaseModel):
    match_id: int
    events: List[str]  # e.g., ["strike", "tag", "block"]

class ReplayOut(BaseModel):
    id: int
    match_id: int
    player_id: int
    events: List[str]

    class Config:
        from_attributes = True