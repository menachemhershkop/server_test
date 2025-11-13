from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
def saveing_names(name):
    with open("names.txt","a") as file:
        file.write(name)
app=FastAPI()
@app.get("/")
def main():
    return {"msg":"Welcome"}

@app.get("/test")
def test():
    return {"msg:":"hi from test"}
@app.get("/test/{name}")
def save_user(name):
    saveing_names(name)
    return {"msg":"saved user"}

