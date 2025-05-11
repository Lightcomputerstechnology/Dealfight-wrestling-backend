from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class SupportTicket(Base):
    __tablename__ = "support_tickets"

    id        = Column(Integer, primary_key=True, index=True)
    user_id   = Column(Integer, ForeignKey("users.id"))
    subject   = Column(String, nullable=False)
    message   = Column(String, nullable=False)
    status    = Column(String, default="open")
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")