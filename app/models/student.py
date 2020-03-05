from mongoengine import Document
from mongoengine.fields import StringField, DateField, IntField


class Student(Document):

    name = StringField(required=True)
    student_class = IntField(required=True)
    birth_date = DateField()
