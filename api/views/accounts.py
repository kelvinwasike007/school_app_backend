from ..models.accounts import Account
from ..models.School import School
from mongoengine import ValidationError
import json
from hashlib import md5
from dotenv import load_dotenv
import os
import jwt
import datetime

"""Authentications"""
def login(schoolId, creds) -> int:
    """Log In user"""
    lookUp = Account.objects(school=schoolId,username=creds.username).first()
    if(lookUp.password != md5(creds.password.encode()).hexdigest()):
         return {"status": "error", "msg": "Invalid Credentials"}
    
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    role = lookUp.role
    payload = {
         "username":lookUp.username,
         "schoolId": schoolId,
         "role": f'{role}'
    }

    load_dotenv()
    key = os.getenv('APP_KEY')
    token = jwt.encode({"exp": expiration_time, **payload}, key, algorithm="HS256")
    return {"status": "ok", "token": token}


def createaccount(schoolId, accounts) -> int:
    """Create a new account"""
    error = None
    try:
            activeSchool = School.objects(id=schoolId).first()
            print(activeSchool)
            new_user = Account()
            new_user.username = accounts.username
            new_user.password = md5(accounts.password.encode()).hexdigest()
            new_user.role = accounts.role
            new_user.school = activeSchool
            new_user.save()
    except ValidationError as e:
         error = e
         print(e)
    except Exception as e:
         error = e
         print(e)
    if error:
        return {"status":"error", "msg":error}
    return {"status": "ok", "msg": "Account has been created"}

def deleteaccount(schoolId, acId)->int:
    """delete an account"""
    Account.objects(school=schoolId, id=acId).delete()
    return {"status": "Deleted Account Successfully"}

def updateaccount(schoolId, acId, updateInfo)->int:
    """update an account"""
    uptdRec = Account.objects(school=schoolId, id=acId)
    uptdRec.update(**{f'set__{updateInfo.key}': updateInfo.value if updateInfo.key != 'password' else md5(updateInfo.value.encode()).hexdigest()})
    return {"status": "User successfully update"}

def accountlist(schoolId)->list:
    """get list of accounts"""
    resp = Account.objects(school=schoolId)
    return json.loads(resp.to_json())
