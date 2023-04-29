from ..models.School import School
from mongoengine import ValidationError
import json 

def add(school):
    errors = None
    try:
        new_school = School()
        new_school.schoolName = school.name
        new_school.schoolLogo = school.logo
        new_school.schoolLocation = school.location
        new_school.schoolEmail = school.email
        new_school.schoolPhone = school.phone
        new_school.schooldomain = school.domain
        new_school.save()
    except ValidationError as e:
        errors = e.message
    except Exception as e:
        pass

    
    if errors:
        return {'status':'error','error':errors}
    return {"status":"School successfully registered"}

def update(updateInfo, schoolId):
    resSchool = School.objects(id=schoolId)
    resSchool.update(**{f"set__{updateInfo.key}":updateInfo.value})
    return {"status": "updated"}

def list():
    schools = School.objects
    return json.loads(schools.to_json())

def delete(schoolId):
    resSch = School.objects(id=schoolId)
    schName = School.objects(id=schoolId)
    resSch.delete()
    return {"msg":f"Deleted School"}

