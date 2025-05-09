from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.title import TitleAssign
from app.models.title import TitleBelt
from app.models.user import User
from app.core.security import get_current_user
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/assign")
def assign_title(data: TitleAssign, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if user != "admin":  # change this to role-based check if needed
        raise HTTPException(status_code=403, detail="Admins only")
    new_title = TitleBelt(type=data.type, holder_id=data.holder_id)
    db.add(new_title)
    db.commit()
    return {"message": "Title assigned"}

@router.get("/all")
def view_titles(db: Session = Depends(get_db)):
    return db.query(TitleBelt).all()

