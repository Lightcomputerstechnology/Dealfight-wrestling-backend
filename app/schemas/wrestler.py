from pydantic import BaseModel

class WrestlerCreate(BaseModel):
    name: str
    gender: str  # "male" or "female"
    strength: int = 50
    agility: int = 50
    charisma: int = 50

class WrestlerOut(BaseModel):
    id: int
    name: str
    gender: str
    strength: int
    agility: int
    charisma: int
    owner_id: int

    class Config:
        from_attributes = True  # Pydantic v2 replacement for orm_mode