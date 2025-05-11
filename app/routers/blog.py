### app/routers/blog.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.blog import Blog
from app.schemas.blog import BlogCreate, BlogOut
from app.core.database import SessionLocal
from typing import List

router = APIRouter(prefix="/blogs", tags=["Blog"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/", response_model=BlogOut)
def create_blog(payload: BlogCreate, db: Session = Depends(get_db)):
    blog = Blog(**payload.dict())
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

@router.get("/", response_model=List[BlogOut])
def list_blogs(db: Session = Depends(get_db)):
    return db.query(Blog).all()
