from pydantic import BaseModel
from typing import Literal

class TitleAssign(BaseModel):
    type: Literal["World", "Tag Team", "Women"]
    holder_id: int

    model_config = {
        "from_attributes": True
    }