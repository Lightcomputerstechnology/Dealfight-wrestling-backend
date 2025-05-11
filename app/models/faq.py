from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.models.faq import FAQ
from app.schemas.faq import FAQCreate, FAQOut
from app.core.database import SessionLocal
from typing import List

router = APIRouter(prefix="/faq", tags=["FAQ"])

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET all FAQs
@router.get("/", response_model=List[FAQOut])
def list_faqs(db: Session = Depends(get_db)):
    return db.query(FAQ).order_by(FAQ.id.desc()).all()

# POST create FAQ
@router.post("/", response_model=FAQOut, status_code=status.HTTP_201_CREATED)
def create_faq(payload: FAQCreate, db: Session = Depends(get_db)):
    faq = FAQ(**payload.dict())
    db.add(faq)
    db.commit()
    db.refresh(faq)
    return faq