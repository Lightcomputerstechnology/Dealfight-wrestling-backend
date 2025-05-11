from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id         = Column(Integer, primary_key=True, index=True)
    user_id    = Column(Integer, ForeignKey("users.id"))
    message    = Column(String, nullable=False)
    timestamp  = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="notifications")