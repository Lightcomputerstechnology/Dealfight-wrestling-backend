from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from app.core.database import Base

class Referral(Base):
    __tablename__ = "referrals"

    id             = Column(Integer, primary_key=True, index=True)
    user_id        = Column(Integer, ForeignKey("users.id"))
    referred_email = Column(String, nullable=False)
    reward_claimed = Column(Integer, default=0)
    created_at     = Column(DateTime, default=datetime.utcnow)