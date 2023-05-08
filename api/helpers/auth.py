from fastapi import HTTPException, Header, responses
from typing import List, Union
from dotenv import load_dotenv
load_dotenv()
import os
import jwt
def logout(token: Union[List[str], None] = Header(default=None)):
    if not token:
        raise HTTPException(status_code=403, detail="You Are Forbidden To Make This Request")
    try:
        account = jwt.decode(token[0], os.getenv('APP_KEY'), algorithms=["HS256"])
    except Exception as e:
        raise HTTPException(status_code=403, detail=f"{e}",headers = {'Location': '/'})

    return account 