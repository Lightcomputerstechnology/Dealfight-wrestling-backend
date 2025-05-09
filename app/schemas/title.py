from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class TitleType(str, Enum):
    world = "World"
    tag = "Tag Team"
    women = "Women"

class TitleOut(BaseModel):
    type: TitleType
    holder_id: int
    updated_at: datetime

    class Config:
        orm_mode = True
