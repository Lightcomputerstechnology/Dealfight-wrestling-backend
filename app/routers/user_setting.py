from pydantic import BaseModel
from datetime import datetime

class UserSettingCreate(BaseModel):
    key: str
    value: str
    description: str | None = None
    is_active: bool = True

class UserSettingUpdate(BaseModel):
    value: str
    description: str | None = None
    is_active: bool = True

class UserSettingOut(BaseModel):
    id: int
    key: str
    value: str
    description: str | None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }
