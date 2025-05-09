from pydantic import BaseModel
from typing import Optional

class ReportCreate(BaseModel):
    match_id: int
    issue: str
    details: Optional[str] = None

    model_config = {
        "from_attributes": True
    }