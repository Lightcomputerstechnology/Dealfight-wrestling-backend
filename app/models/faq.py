from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.models.faq import FAQ
from app.schemas.faq import FAQCreate, FAQUpdate, FAQOut
from app.core.database import SessionLocal

router = APIRouter(prefix="/faq", tags=["FAQ"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[FAQOut])
def list_faqs(db: Session = Depends(get_db)):
    """Retrieve all active FAQ entries."""
    return db.query(FAQ).filter(FAQ.is_active == True).order_by(FAQ.id.desc()).all()

@router.post("/", response_model=FAQOut, status_code=status.HTTP_201_CREATED)
def create_faq(payload: FAQCreate, db: Session = Depends(get_db)):
    """Create a new FAQ entry."""
    try:
        faq = FAQ(**payload.dict())
        db.add(faq)
        db.commit()
        db.refresh(faq)
        return faq
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create FAQ")

@router.put("/{faq_id}", response_model=FAQOut)
def update_faq(faq_id: int, payload: FAQUpdate, db: Session = Depends(get_db)):
    """Update an existing FAQ entry."""
    faq = db.query(FAQ).filter(FAQ.id == faq_id).first()
    if not faq:
        raise HTTPException(status_code=404, detail="FAQ not found")
    for key, value in payload.dict(exclude_unset=True).items():
        setattr(faq, key, value)
    db.commit()
    db.refresh(faq)
    return faq

@router.delete("/{faq_id}")
def delete_faq(faq_id: int, db: Session = Depends(get_db)):
    """Delete a FAQ entry by ID."""
    faq = db.query(FAQ).filter(FAQ.id == faq_id).first()
    if not faq:
        raise HTTPException(status_code=404, detail="FAQ not found")
    db.delete(faq)
    db.commit()
    return {"detail": "FAQ deleted successfully"}