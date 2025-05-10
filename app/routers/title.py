# app/routers/title.py

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.title import TitleCreate
from app.models.title import Title
from app.core.database import SessionLocal
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/titles", tags=["Titles"])


# ───────────────────────── dependencies ──────────────────────────
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ─────────────────────────── routes ──────────────────────────────
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_title(
    payload: TitleCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """
    Create a new wrestling title (championship).
    """
    title = Title(
        name=payload.name,
        description=payload.description,
        created_by=user.id,
    )
    db.add(title)
    db.commit()
    db.refresh(title)
    return title