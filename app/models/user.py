wrestlers = relationship("Wrestler", back_populates="owner", cascade="all, delete")
matches_as_player1 = relationship("Match", foreign_keys='Match.player1_id')
matches_as_player2 = relationship("Match", foreign_keys='Match.player2_id')