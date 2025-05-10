from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from app.core.database import Base

class Replay(Base):
    __tablename__ = "replays"
    id         = Column(Integer, primary_key=True, index=True)
    match_id   = Column(Integer, index=True)
    player_id  = Column(Integer, ForeignKey("users.id"))
    events     = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    player     = relationship("User")
