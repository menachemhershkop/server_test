from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

from encrypt.caeser import Caesar
from encrypt.fance import Fence
from list_names.saving_names import saveing_names

class Massage(BaseModel):
    text: str
    offset: int
    mode: str

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
def caesar(msg:Massage):
    caesar=Caesar()
    if msg.mode=="encrypt":
        return {"encrypted_text":caesar.encrypy(msg.text,msg.offset)}
    if msg.mode=="decrypt":
        return {"decryptes_text":caesar.decrypt(msg.text,msg.offset)}
@app.get("/fence/encrypt")
def encrypt(text):
    encrypt=Fence()
    return {"encrypted_text":encrypt.encrypy(text)}
@app.post("/fence/decrypt")
def decrypt(msg):
    decrypt=Fence()
    return {"decrypted":decrypt.encrypy(msg)}