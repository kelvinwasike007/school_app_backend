from fastapi import FastAPI
from api.routes import accounts
app = FastAPI()
app.include_router(accounts.router)
@app.get("/")
def root()->dict:
    """yes"""
    return {"hello":"world"}

