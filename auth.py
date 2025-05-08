from app.core.deps import get_current_user
from app.models.user import User
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.models.user import User
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(username=user.username, email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
@router.get("/me")
def read_profile(current_user: User = Depends(get_current_user)):
    return current_user