from pydantic import BaseModel
from typing import Dict


class TimelineEvent(BaseModel):
    time: str
    event: str
    actor: str
    details: Dict
