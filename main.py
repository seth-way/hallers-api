# main.py
from fastapi import FastAPI
from routers import players

app = FastAPI()

app.include_router(players.router)

@app.get("/")
def read_root():
    return {"Hello": "Hallers API"}

# to run app, use command --> uvicorn main:app --reload