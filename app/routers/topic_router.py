from fastapi import APIRouter, HTTPException
from app.dependencies import db_dep
from app import models
from app.schemas import topic as schemas
from typing import List

router = APIRouter(prefix="/topics", tags=["Topics"])

@router.post("/", response_model=schemas.TopicRead)
def create_topic(topic: schemas.TopicCreate, db: db_dep):
    topic_obj = models.Topic(**topic.dict())
    db.add(topic_obj)
    db.commit()
    db.refresh(topic_obj)
    return topic_obj

@router.get("/", response_model=List[schemas.TopicRead])
def list_topics(db: db_dep):
    return db.query(models.Topic).all()

@router.delete("/{topic_id}")
def delete_topic(topic_id: int, db: db_dep):
    topic = db.query(models.Topic).get(topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    db.delete(topic)
    db.commit()
    return {"detail": "Topic deleted"}
