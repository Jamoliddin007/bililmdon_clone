from typing import Union
import time
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.routers import auth, question

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(auth.router)
app.include_router(question.router)