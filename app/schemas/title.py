from pydantic import BaseModel
from typing import Literal

class TitleAssign(BaseModel):
    type: Literal["World", "Tag Team", "Women"]
    holder_id: int

class TitleOut(BaseModel):
    id: int
    type: Literal["World", "Tag Team", "Women"]
    holder_id: int

    class Config:
        from_attributes = True