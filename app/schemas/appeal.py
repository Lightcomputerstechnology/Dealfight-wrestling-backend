# app/schemas/appeal.py

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class AppealStatus(str, Enum):
    pending = "pending"
    reviewed = "reviewed"
    resolved = "resolved"
    rejected = "rejected"


class AppealCreate(BaseModel):
    title: str = Field(..., example="Wrong Match Result")
    message: str = Field(..., example="I was incorrectly declared the loser.")
    attachment_url: Optional[str] = Field(None, example="https://example.com/screenshot.png")


class AppealOut(BaseModel):
    id: int
    user_id: int
    title: str
    message: str
    attachment_url: Optional[str]
    status: AppealStatus
    submitted_at: datetime

    class Config:
        orm_mode = True