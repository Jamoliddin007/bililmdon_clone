from fastapi import APIRouter, HTTPException
from typing import List

from app.dependencies import db_dep
from app import models
from app.schemas import question as schemas

router = APIRouter(prefix="/questions")

# These endpoints are for topics
@router.post("/topics", response_model=schemas.TopicRead, tags=["Topics"])
def create_topic(topic: schemas.TopicCreate, db: db_dep):
    topic_obj = models.Topic(**topic.model_dump())
    db.add(topic_obj)
    db.commit()
    db.refresh(topic_obj)
    return topic_obj


@router.delete("/topics/{topic_id}", tags=["Topics"])
def delete_topic(topic_id: int, db: db_dep):
    topic = db.query(models.Topic).get(topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    db.delete(topic)
    db.commit()
    return {"detail": "Topic deleted"}


# These endpoints are for question
@router.post("/", response_model=schemas.QuestionRead, tags=["Questions"])
def create_question(question: schemas.QuestionCreate, db: db_dep):
    question_obj = models.Question(**question.model_dump())
    db.add(question_obj)
    db.commit()
    db.refresh(question_obj)
    return question_obj


@router.get("/", response_model=List[schemas.QuestionRead], tags=["Questions"])
def list_questions(db: db_dep):
    return db.query(models.Question).all()


@router.delete("/{question_id}", tags=["Questions"])
def delete_question(question_id: int, db: db_dep):
    question = db.query(models.Question).get(question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    db.delete(question)
    db.commit()
    return {"detail": "Question deleted"}


# These endpoints are for option
@router.post("/options", response_model=schemas.OptionRead, tags=["Options"])
def create_option(option: schemas.OptionCreate, db: db_dep):
    option_obj = models.Option(**option.model_dump())
    db.add(option_obj)
    db.commit()
    db.refresh(option_obj)
    return option_obj


@router.get("/options", response_model=List[schemas.OptionRead], tags=["Options"])
def list_options(db: db_dep):
    return db.query(models.Option).all()


@router.delete("/options/{option_id}", tags=["Options"])
def delete_option(option_id: int, db: db_dep):
    option = db.query(models.Option).get(option_id)
    if not option:
        raise HTTPException(status_code=404, detail="Option not found")
    db.delete(option)
    db.commit()
    return {"detail": "Option deleted"}
