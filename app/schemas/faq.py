from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class FAQBase(BaseModel):
    question: str = Field(..., min_length=5)
    answer: str = Field(..., min_length=5)
    category: Optional[str] = Field(None, description="Optional FAQ category/tag")
    is_active: bool = True

class FAQCreate(FAQBase):
    """Schema for creating a new FAQ."""
    pass

class FAQUpdate(BaseModel):
    """Schema for updating a FAQ (partial update allowed)."""
    question: Optional[str] = None
    answer: Optional[str] = None
    category: Optional[str] = None
    is_active: Optional[bool] = None

class FAQOut(FAQBase):
    """Schema for returning FAQ data."""
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }