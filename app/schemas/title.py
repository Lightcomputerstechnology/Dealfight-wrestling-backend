# app/schemas/title.py
from pydantic import BaseModel


class TitleBase(BaseModel):
    name: str
    description: str | None = None


class TitleCreate(TitleBase):
    """Fields required when a user creates a new title."""
    pass


class TitleOut(TitleBase):
    id: int
    created_by: int

    class Config:
        orm_mode = True