from pydantic import BaseModel
from datetime import datetime

class NotificationOut(BaseModel):
    message: str
    timestamp: datetime

    class Config:
        from_attributes = True
      
