from mongoengine import Document
from mongoengine.fields import StringField, IntField, ReferenceField, DateTimeField

from .employee import Employee


class Timelog(Document):

    time = DateTimeField(required=True)
    kind = StringField(required=True)

    source = StringField()

    employee = ReferenceField(Employee, dbref=False)
