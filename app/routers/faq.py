# app/schemas/faq.py

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class FAQBase(BaseModel):
    question: str = Field(..., min_length=5, max_length=300)
    answer: str = Field(..., min_length=5)

class FAQCreate(FAQBase):
    pass

class FAQUpdate(BaseModel):
    question: Optional[str] = Field(None, min_length=5, max_length=300)
    answer: Optional[str] = Field(None, min_length=5)
    is_active: Optional[bool] = True  # Optional toggle to deactivate FAQ

class FAQOut(FAQBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }