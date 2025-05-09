from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base
import enum

class TitleType(str, enum.Enum):
    world = "World"
    tag = "Tag Team"
    women = "Women"

class TitleBelt(Base):
    __tablename__ = "title_belts"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum(TitleType), nullable=False)
    holder_id = Column(Integer, ForeignKey("users.id"))
    updated_at = Column(DateTime, default=datetime.utcnow)

    holder = relationship("User", back_populates="titles")
