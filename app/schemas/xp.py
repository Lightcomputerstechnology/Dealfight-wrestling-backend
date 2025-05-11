from pydantic import BaseModel
from datetime import datetime

class XPUpdate(BaseModel):
    won: bool  # Whether the user won the match or not

class XPTrackerOut(BaseModel):  # <-- renamed to match the new model
    id: int
    xp_gained: int
    level: int
    timestamp: datetime

    model_config = {
        "from_attributes": True
    }
