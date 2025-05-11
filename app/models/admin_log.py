# app/models/admin_log.py

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base

class AdminLog(Base):
    __tablename__ = "admin_logs"
    id        = Column(Integer, primary_key=True, index=True)
    action    = Column(String, nullable=False)
    target_id = Column(Integer, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
