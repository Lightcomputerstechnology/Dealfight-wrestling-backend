import enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class MatchType(str, enum.Enum):
    single = "single"
    tag    = "tag"

class Match(Base):
    __tablename__ = "matches"

    id         = Column(Integer, primary_key=True, index=True)
    type       = Column(Enum(MatchType), default=MatchType.single)
    status     = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    player1_id = Column(Integer, ForeignKey("users.id"))
    player2_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    player1    = relationship("User", foreign_keys=[player1_id])
    player2    = relationship("User", foreign_keys=[player2_id])