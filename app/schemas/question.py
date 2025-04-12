from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
class QuestionCreate(BaseModel):
    title: str
    description: Optional[str] = None
    topic_id: int
    owner_id: int


class QuestionRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    topic_id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
