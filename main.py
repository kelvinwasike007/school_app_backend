from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root()->dict:
    """yes"""
    return {"hello":"world"}

