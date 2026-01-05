from pydantic import BaseModel
from typing import Dict, Optional

class LogEntry(BaseModel):
    timestamp: str
    event: str
    user: Optional[str]
    details: Dict
