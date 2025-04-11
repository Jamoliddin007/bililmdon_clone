from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class TopicCreate(BaseModel):
    name: str


class TopicRead(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


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
    option_ids: List[OptionRead] = []

    class Config:
        from_attributes = True
