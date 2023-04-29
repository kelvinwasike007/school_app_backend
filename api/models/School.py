from mongoengine import *

class School(Document):
    schoolName = StringField()
    schooldomain = StringField()
    schoolLogo = StringField()
    schoolEmail = EmailField()
    schoolPhone = [StringField()]
    schoolLocation = StringField()