from fastapi import FastAPI
from app.routers import auth, question_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(auth.router)
app.include_router(question_router.router)