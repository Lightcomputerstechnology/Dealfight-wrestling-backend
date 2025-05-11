from pydantic import BaseModel

class WalletOut(BaseModel):
    coins: int
    diamonds: int

    model_config = {
        "from_attributes": True
    }

class WalletAdd(BaseModel):
    type: str  # either "coins" or "diamonds"
    amount: int