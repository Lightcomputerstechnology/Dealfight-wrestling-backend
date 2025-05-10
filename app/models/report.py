from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base

class Report(Base):
    __tablename__ = "reports"
    id          = Column(Integer, primary_key=True, index=True)
    reporter_id = Column(Integer, ForeignKey("users.id"))
    reported_id = Column(Integer, ForeignKey("users.id"))
    reason      = Column(String, nullable=False)
    timestamp   = Column(DateTime, default=datetime.utcnow)

    reporter    = relationship("User", foreign_keys=[reporter_id])
    reported    = relationship("User", foreign_keys=[reported_id])
