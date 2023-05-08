from fastapi import APIRouter, Depends
from ..views.school import add, list,update,delete
from pydantic import BaseModel
from ..helpers.auth import logout
router = APIRouter(
    prefix='/schools',
    tags=['Manage Schools']
)

class School(BaseModel):
    name:str
    email:str
    location:str
    logo:str
    domain:str
    phone:str

class updateSchema(BaseModel):
    key:str
    value:str

@router.get("/")
def list_schools():
    """Get list Schools"""
    return list()

@router.post('/new')
def new_school(school: School):
    """Add new school"""
    return add(school)

@router.put('/update/{schoolId}', dependencies=[Depends(logout)])
def update_school(updateInfo:updateSchema, schoolId):
    """Update school information"""
    return update(updateInfo, schoolId)

@router.delete('/delete/{schoolId}' , dependencies=[Depends(logout)])
def delete_school(schoolId:str):
    return delete(schoolId)
