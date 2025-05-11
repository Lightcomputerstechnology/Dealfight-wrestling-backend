# app/models/faq.py

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.core.database import Base

class FAQ(Base):
    __tablename__ = "faqs"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)