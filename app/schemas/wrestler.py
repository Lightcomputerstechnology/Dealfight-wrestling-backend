from pydantic import BaseModel
from typing import Literal

class WrestlerCreate(BaseModel):
    name: str
    gender: Literal["male", "female"]
    strength: int = 50
    agility: int = 50
    charisma: int = 50
