from pydantic import BaseModel


class TopicCreate(BaseModel):
    name: str


class TopicRead(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True