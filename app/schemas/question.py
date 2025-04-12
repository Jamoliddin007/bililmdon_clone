from pydantic import BaseModel
class QuestionCreate(BaseModel):
    title: str
    description: str
    topic_id: int

class QuestionRead(QuestionCreate):
    id: int
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True
