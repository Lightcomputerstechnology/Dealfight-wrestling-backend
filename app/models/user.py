from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    id             = Column(Integer, primary_key=True, index=True)
    username       = Column(String, unique=True, index=True, nullable=False)
    email          = Column(String, unique=True, index=True, nullable=False)
    hashed_password= Column(String, nullable=False)
    is_admin       = Column(Integer, default=0)
    coins          = Column(Integer, default=0)
    diamonds       = Column(Integer, default=0)
    xp             = Column(Integer, default=0)
    level          = Column(Integer, default=1)
    matches_won    = Column(Integer, default=0)

    wrestlers      = relationship("Wrestler", back_populates="owner", cascade="all, delete")
    titles         = relationship("TitleBelt", back_populates="holder")
    matches_as_p1  = relationship("Match", foreign_keys="Match.player1_id")
    matches_as_p2  = relationship("Match", foreign_keys="Match.player2_id")
