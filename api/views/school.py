from ..models.School import School
from ..models.accounts import Account
from mongoengine import ValidationError
import random
import string
import hashlib
import json 
from ..helpers.sms import signup_msg
from ..helpers.mail import signup_mail

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
        #create a user account
        admin = Account()
        text_length = 10

        # Generate a random text consisting of lowercase letters and digits
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=text_length))
        password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=text_length))

        admin.username = username
        admin.password = hashlib.md5(password.encode()).hexdigest()
        admin.school = new_school
        admin.role = 'admin'
        admin.save()
        #send new user account
        signup_msg(school.phone, f"https://school-platform.wesempire.co.ke/{school.domain}", {'username':username, "password":password})
        signup_mail([school.email], f"https://school-platform.wesempire.co.ke/{school.domain}", {"username":username, "password":password})
    except ValidationError as e:
        errors = e.message
    except Exception as e:
        pass

    
    if errors:
        return {'status':'error','error':errors}
    return {"status":"School successfully registered, Check Your Email and Phone For Further Instructions"}

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

