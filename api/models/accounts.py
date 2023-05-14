from mongoengine import *
from .School import School

class Account(Document):
    """User Account"""
    username = StringField()
    password = StringField()
    role = StringField()
    school = ReferenceField(School, required=True, reverse_delete_rule=CASCADE)
