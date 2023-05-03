from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import accounts, schools
from mongoengine import connect
import os
from dotenv import load_dotenv
load_dotenv()
db=os.getenv('DB_URL')
connect('school', host=db)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"]
    )

#School Management Routes
app.include_router(schools.router)

#User Account Routes
app.include_router(accounts.router)

@app.get("/health", status_code=200)
def root()->dict:
    """yes"""
    return {"hello":"world"} 

