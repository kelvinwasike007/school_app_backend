from fastapi import APIRouter
from ..views.accounts import login, createaccount,updateaccount,deleteaccount,accountlist
from .schools import updateSchema
from pydantic import BaseModel
from typing import Annotated


router = APIRouter(
    prefix='/account',
    tags = ['User Accounts Management']
)
class Account(BaseModel):
    username:str
    password:str
    role:str

@router.post('/login/{schoolId}')
def login_user(schoolId:str, acInfo: Account):
    """Log in a User"""
    return login(schoolId, acInfo)

@router.post('/register/{schoolId}')
def add_user(schoolId:str, acInfo:Account):
    """Create a user account"""
    return createaccount(schoolId, acInfo)

@router.put('/update/{schoolId}/{acId}')
def edit_user(schoolId:str, acId:str, updateInfo: updateSchema):
    """Updates a user info"""
    return updateaccount(schoolId, acId, updateInfo)

@router.delete('/delete/{schoolId}/{acId}')
def delete_user(schoolId:str, acId:str):
    """Deletes a user account"""
    return deleteaccount(schoolId, acId)

@router.get('/{schoolId}')
def users(schoolId: str):
    """Get list of all accounts"""
    return accountlist(schoolId)
