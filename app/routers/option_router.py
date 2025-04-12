from fastapi import APIRouter, HTTPException
from typing import List

from app.dependencies import db_dep
from app import models
from app.schemas import questions as schemas

router = APIRouter(prefix="/options", tags=["Options"])

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
