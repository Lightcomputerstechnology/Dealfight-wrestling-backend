from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.faq import FAQ
from app.models.user import User
from app.schemas.faq import FAQCreate, FAQUpdate, FAQOut
from app.core.database import SessionLocal
from app.core.security import get_current_user

router = APIRouter(prefix="/faq", tags=["FAQ"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[FAQOut])
def list_faqs(
    category: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    """List FAQs, optionally filter by category or search keyword."""
    query = db.query(FAQ).filter(FAQ.is_active == True)

    if category:
        query = query.filter(FAQ.category == category)

    if search:
        query = query.filter(FAQ.question.ilike(f"%{search}%"))

    return query.order_by(FAQ.id.desc()).all()

@router.post("/", response_model=FAQOut, status_code=status.HTTP_201_CREATED)
def create_faq(payload: FAQCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    """Create a new FAQ (admin only)."""
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can create FAQs.")
    faq = FAQ(**payload.dict())
    db.add(faq)
    db.commit()
    db.refresh(faq)
    return faq

@router.put("/{faq_id}", response_model=FAQOut)
def update_faq(faq_id: int, payload: FAQUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    """Update a FAQ (admin only)."""
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can update FAQs.")
    faq = db.query(FAQ).filter(FAQ.id == faq_id).first()
    if not faq:
        raise HTTPException(status_code=404, detail="FAQ not found")
    for key, value in payload.dict(exclude_unset=True).items():
        setattr(faq, key, value)
    db.commit()
    db.refresh(faq)
    return faq

@router.delete("/{faq_id}")
def delete_faq(faq_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    """Delete a FAQ (admin only)."""
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can delete FAQs.")
    faq = db.query(FAQ).filter(FAQ.id == faq_id).first()
    if not faq:
        raise HTTPException(status_code=404, detail="FAQ not found")
    db.delete(faq)
    db.commit()
    return {"detail": "FAQ deleted successfully"}