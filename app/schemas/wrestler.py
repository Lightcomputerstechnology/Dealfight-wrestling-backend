from pydantic import BaseModel

class WrestlerBase(BaseModel):
    name: str
    gender: str
    strength: int = 50
    agility: int = 50
    charisma: int = 50

class WrestlerCreate(WrestlerBase):
    pass

class WrestlerOut(WrestlerBase):
    id: int

    class Config:
        orm_mode = True
