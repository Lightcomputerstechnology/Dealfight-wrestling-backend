# app/schemas/xp.py
from pydantic import BaseModel

class XPUpdate(BaseModel):
    match_id: int
    won: bool  # True if user won, else False