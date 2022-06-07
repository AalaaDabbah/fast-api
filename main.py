# from fastapi import FastAPI
# import uvicorn
# import os

# app=FastAPI()

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port='3000')
# @app.get("/")
# def nothing():
#     return {"message":"Hello world"}

from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel
app = FastAPI()
class person(BaseModel):
    name: str
    password: int

@app.post("/per")
def create_person(per: person):
    #return request
    return {'data':f"person is created {per.name}"}

@app.get("/")
def nothing():
    return {"message":"Hello world"}

@app.get("/api")
def nothing(name:str="alaa"):
    return {"name":f'{name}'}
@app.get("/{id}")
def nothing(id):
    return {"message":id}




