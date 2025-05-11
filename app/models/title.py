import enum
from datetime import datetime
from sqlalchemy import Column, Integer, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class TitleType(str, enum.Enum):
    World   = "World"
    TagTeam = "Tag Team"
    Women   = "Women"

class TitleBelt(Base):
    __tablename__ = "title_belts"

    id         = Column(Integer, primary_key=True, index=True)
    type       = Column(Enum(TitleType), nullable=False)
    holder_id  = Column(Integer, ForeignKey("users.id"))
    updated_at = Column(DateTime, default=datetime.utcnow)

    holder     = relationship("User", back_populates="titles")