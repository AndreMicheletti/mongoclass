from mongoengine import Document
from mongoengine.fields import StringField, DateField, IntField


class Employee(Document):

    name = StringField(required=True)
    admission = DateField(required=True)
    initial_day = IntField(required=True)

    resignation = DateField()

    routine = StringField()
