from mongoengine import Document
from mongoengine.fields import StringField, DateField


class Author(Document):

    name = StringField()
    birth_date = DateField()
