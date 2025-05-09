from pydantic import BaseModel
from enum import Enum

class MatchType(str, Enum):
    single = "single"
    tag = "tag"

class MatchCreate(BaseModel):
    type: MatchType

class MatchOut(BaseModel):
    id: int
    type: MatchType
    status: str

    class Config:
        orm_mode = True
