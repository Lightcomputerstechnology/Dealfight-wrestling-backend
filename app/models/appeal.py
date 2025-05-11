### app/models/appeal.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from app.core.database import Base

class BanAppeal(Base):
    __tablename__ = "ban_appeals"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    reason = Column(String, nullable=False)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)


### app/schemas/appeal.py
from pydantic import BaseModel
from datetime import datetime

class AppealCreate(BaseModel):
    reason: str

class AppealOut(BaseModel):
    id: int
    reason: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
