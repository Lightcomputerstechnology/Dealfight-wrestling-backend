from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    reporter_id = Column(Integer, ForeignKey("users.id"))
    match_id = Column(Integer, ForeignKey("matches.id"))
    issue = Column(String)
    details = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

    reporter = relationship("User")
    match = relationship("Match")
