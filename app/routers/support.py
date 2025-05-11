### app/routers/support.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.support import SupportTicket
from app.schemas.support import TicketCreate, TicketOut
from app.core.security import get_current_user
from app.core.database import SessionLocal
from app.models.user import User
from typing import List

router = APIRouter(prefix="/support", tags=["Support"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/", response_model=TicketOut)
def open_ticket(payload: TicketCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    ticket = SupportTicket(user_id=user.id, **payload.dict())
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket

@router.get("/my-tickets", response_model=List[TicketOut])
def get_my_tickets(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return db.query(SupportTicket).filter(SupportTicket.user_id == user.id).all()
