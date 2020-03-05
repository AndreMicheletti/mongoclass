from mongoengine import Document
from mongoengine.fields import StringField, IntField, ReferenceField, DateTimeField

from .author import Author
from .student import Student


class Book(Document):

    title = StringField(required=True)
    author = ReferenceField(Author, required=True, dbref=False)
    year = IntField(required=True)

    borrowed_to = ReferenceField(Student, dbref=False)
    borrowed_date = DateTimeField()
    return_date = DateTimeField()
