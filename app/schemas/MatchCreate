from pydantic import BaseModel
from typing import Literal, Optional

class MatchCreate(BaseModel):
    type: Literal["single", "tag"] = "single"
    opponent_id: Optional[int] = None  # can be None for auto-matching

    model_config = {
        "from_attributes": True
    }