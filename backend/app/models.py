from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Request model (from frontend)
class UserQuery(BaseModel):
    message: str


# Database model (MongoDB document structure)
class ChatRecord(BaseModel):
    query: str
    response: str
    created_at: Optional[datetime] = datetime.utcnow()
