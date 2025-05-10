from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Wrestler(Base):
    __tablename__ = "wrestlers"
    id        = Column(Integer, primary_key=True, index=True)
    name      = Column(String, nullable=False)
    gender    = Column(String, nullable=False)
    strength  = Column(Integer, default=50)
    agility   = Column(Integer, default=50)
    charisma  = Column(Integer, default=50)
    owner_id  = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    owner     = relationship("User", back_populates="wrestlers")
