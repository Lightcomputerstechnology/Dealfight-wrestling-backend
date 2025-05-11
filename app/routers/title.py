from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.title import TitleCreate
from app.models.title import TitleBelt
from app.core.database import SessionLocal
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/titles", tags=["Titles"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_title(
    payload: TitleCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    if not user.is_admin:
        return {"error": "Only admin can assign titles."}

    new_title = TitleBelt(
        type=payload.type,
        holder_id=payload.holder_id,
    )
    db.add(new_title)
    db.commit()
    db.refresh(new_title)
    return new_title

@router.get("/")
def list_titles(db: Session = Depends(get_db)):
    return db.query(TitleBelt).all()