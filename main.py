from fastapi import FastAPI
from api.routes import accounts, schools
from mongoengine import connect
import os
from dotenv import load_dotenv
load_dotenv()
db=os.getenv('DB_URL')
connect('school', host=db)
app = FastAPI()

#School Management Routes
app.include_router(schools.router)

#User Account Routes
app.include_router(accounts.router)

@app.get("/")
def root()->dict:
    """yes"""
    return {"hello":"world"}

