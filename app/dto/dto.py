from pydantic import BaseModel, Field
from typing import Optional

class TransactionCreate(BaseModel):
    amount: float = Field(..., gt=0)
    sender_name: str
    raw_message: str
    sync_method: str = "DIRECT"
    organization_id: str
    forwarded_by: Optional[str] = None

    class Config:
        from_attributes = True