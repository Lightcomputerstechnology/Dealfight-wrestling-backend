### app/schemas/blog.py
from pydantic import BaseModel
from datetime import datetime

class BlogCreate(BaseModel):
    title: str
    content: str

class BlogOut(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True
