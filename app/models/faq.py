# app/routers/faq.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.models.faq import FAQ
from app.schemas.faq import FAQCreate, FAQOut
from app.core.database import SessionLocal

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
    """Retrieve all FAQ entries."""
    return db.query(FAQ).order_by(FAQ.id.desc()).all()

# POST create FAQ
@router.post("/", response_model=FAQOut, status_code=status.HTTP_201_CREATED)
def create_faq(payload: FAQCreate, db: Session = Depends(get_db)):
    """Create a new FAQ entry."""
    try:
        faq = FAQ(**payload.dict())
        db.add(faq)
        db.commit()
        db.refresh(faq)
        return faq
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create FAQ")