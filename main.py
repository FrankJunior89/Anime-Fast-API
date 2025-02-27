from fastapi import FastAPI, HTTPException
import sqlite3
from pydantic import BaseModel
from anime import Anime
from routes import users, animes

app = FastAPI()



@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI User Authentication!"}


app.include_router(users.router)
app.include_router(animes.router)
