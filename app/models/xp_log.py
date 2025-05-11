class XPLog(Base):
    __tablename__ = "xp_logs"
    __table_args__ = {'extend_existing': True}  # <-- ADD THIS LINE

    id         = Column(Integer, primary_key=True, index=True)
    user_id    = Column(Integer, ForeignKey("users.id"), nullable=False)
    xp_gained  = Column(Integer, nullable=False)
    level      = Column(Integer, nullable=False)
    timestamp  = Column(DateTime, default=datetime.utcnow)

    user       = relationship("User", backref="xp_logs")