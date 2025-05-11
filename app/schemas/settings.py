### app/schemas/settings.py
from pydantic import BaseModel

class SettingsUpdate(BaseModel):
    theme: str
    notifications: bool
    sound: bool
