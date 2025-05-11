### app/routers/faq.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.faq import FAQ
from app.schemas.faq import FAQCreate, FAQOut
from app.core.database import SessionLocal
from typing import List

router = APIRouter(prefix="/faqs", tags=["FAQ"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/", response_model=FAQOut)
def create_faq(payload: FAQCreate, db: Session = Depends(get_db)):
    faq = FAQ(**payload.dict())
    db.add(faq)
    db.commit()
    db.refresh(faq)
    return faq

@router.get("/", response_model=List[FAQOut])
def get_faqs(db: Session = Depends(get_db)):
    return db.query(FAQ).all()
