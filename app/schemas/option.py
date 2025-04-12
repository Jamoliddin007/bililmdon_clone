from pydantic import BaseModel
from datetime import datetime

class OptionCreate(BaseModel):
    question_id: int
    title: str
    is_correct: bool


class OptionRead(BaseModel):
    id: int
    question_id: int
    title: str
    is_correct: bool
    created_at: datetime

    class Config:
        from_attributes = True
