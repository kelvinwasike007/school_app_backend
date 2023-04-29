from mongoengine import *
from enum import Enum
from .School import School
class Roles(Enum):
    STAFF = 'staff'
    ADMIN = 'admin'
    PARENT = 'parent'
    STUDENT = 'student'

class Account(Document):
    """User Account"""
    username = StringField()
    password = StringField()
    role = EnumField(Roles, default=Roles.STUDENT)
    school = ReferenceField(School, required=True, reverse_delete_rule=CASCADE)
