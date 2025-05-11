### app/schemas/referral.py
from pydantic import BaseModel, EmailStr
from datetime import datetime

class ReferralCreate(BaseModel):
    referred_email: EmailStr

class ReferralOut(BaseModel):
    id: int
    referred_email: EmailStr
    reward_claimed: int
    created_at: datetime

    class Config:
        from_attributes = True
