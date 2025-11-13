from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

from encrypt.fance import Fence


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
@app.post("/caesar")
def caeser(msg):
    pass
@app.get("/fence/encrypt")
def encrypt(text):
    encrypt=Fence()
    return {"encrypted_text":encrypt.encrypy(text)}
@app.post("/fence/decrypt")
def decrypt(msg):
    decrypt=Fence()
    return {"decrypted":decrypt.encrypy(msg)}