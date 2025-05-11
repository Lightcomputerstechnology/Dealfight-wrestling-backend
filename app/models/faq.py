# app/schemas/faq.py

from pydantic import BaseModel
from datetime import datetime

class FAQBase(BaseModel):
    question: str
    answer: str

class FAQCreate(FAQBase):
    pass

class FAQUpdate(FAQBase):
    pass  # You can also make fields optional here if partial updates are allowed

class FAQOut(FAQBase):
    id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }