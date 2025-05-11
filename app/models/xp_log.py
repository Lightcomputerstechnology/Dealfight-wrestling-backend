# app/models/xp_log.py

from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class XPLog(Base):
    __tablename__ = "xp_logs"

    # ← this tells SQLAlchemy “if this table is already in Base.metadata, just merge these columns”
    __table_args__ = {"extend_existing": True}

    id         = Column(Integer, primary_key=True, index=True)
    user_id    = Column(Integer, ForeignKey("users.id"), nullable=False)
    xp_gained  = Column(Integer, nullable=False)
    level      = Column(Integer, nullable=False)
    timestamp  = Column(DateTime, default=datetime.utcnow)

    user       = relationship("User", backref="xp_logs")