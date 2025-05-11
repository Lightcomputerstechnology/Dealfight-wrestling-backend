# app/schemas/leaderboard.py
from pydantic import BaseModel

class LeaderboardUser(BaseModel):
    id: int
    username: str
    total_wins: int
    total_xp: int
    level: int

    class Config:
        from_attributes = True