from app.models.xp_log import XPLog  # make sure this import is included

@router.post("/update", status_code=status.HTTP_200_OK)
def update_xp(payload: XPUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    """
    Increase XP and level after a match, and store in log.
    """
    base_xp = 20
    win_bonus = 30 if payload.won else 0

    user.xp += base_xp + win_bonus
    user.matches_played += 1
    if payload.won:
        user.matches_won += 1

    user.level = user.xp // 100 + 1

    # Log XP event
    log = XPLog(
        user_id=user.id,
        xp_gained=base_xp + win_bonus,
        level=user.level
    )
    db.add(log)
    db.commit()
    db.refresh(user)

    return {"xp": user.xp, "level": user.level}