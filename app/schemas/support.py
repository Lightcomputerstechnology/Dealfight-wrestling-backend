### app/schemas/support.py
from pydantic import BaseModel
from datetime import datetime

class TicketCreate(BaseModel):
    subject: str
    message: str

class TicketOut(BaseModel):
    id: int
    subject: str
    message: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
