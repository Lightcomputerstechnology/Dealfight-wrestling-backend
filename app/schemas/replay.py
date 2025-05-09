from pydantic import BaseModel
from typing import List

class ReplayLog(BaseModel):
    match_id: int
    events: List[str]  # e.g. ["strike", "block", "tag"]