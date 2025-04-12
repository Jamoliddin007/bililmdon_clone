from fastapi import APIRouter, HTTPException
from app.dependencies import db_dep
from app import models
from app.schemas import questions as schemas
from typing import List

router = APIRouter(prefix="/questions", tags=["Questions"])

@router.post("/", response_model=schemas.QuestionRead)
def create_question(question: schemas.QuestionCreate, db: db_dep):
    question_obj = models.Question(**question.dict())
    db.add(question_obj)
    db.commit()
    db.refresh(question_obj)
    return question_obj

@router.get("/", response_model=List[schemas.QuestionRead])
def list_questions(db: db_dep):
    return db.query(models.Question).all()

@router.delete("/{question_id}")
def delete_question(question_id: int, db: db_dep):
    question = db.query(models.Question).get(question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    db.delete(question)
    db.commit()
    return {"detail": "Question deleted"}
