# app/routers/faq.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.faq import FAQCreate, FAQOut, FAQUpdate

router = APIRouter(prefix="/faq", tags=["FAQ"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[FAQOut])
def list_faqs(db: Session = Depends(get_db)):
    from app.models.faq import FAQ  # lazy import
    return db.query(FAQ).all()

@router.post("/", response_model=FAQOut)
def create_faq(payload: FAQCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    from app.models.faq import FAQ
    if user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    faq = FAQ(**payload.dict())
    db.add(faq)
    db.commit()
    db.refresh(faq)
    return faq

@router.put("/{faq_id}", response_model=FAQOut)
def update_faq(faq_id: int, payload: FAQUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    from app.models.faq import FAQ
    if user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
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
    from app.models.faq import FAQ
    if user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    faq = db.query(FAQ).filter(FAQ.id == faq_id).first()
    if not faq:
        raise HTTPException(status_code=404, detail="FAQ not found")
    db.delete(faq)
    db.commit()
    return {"detail": "FAQ deleted"}