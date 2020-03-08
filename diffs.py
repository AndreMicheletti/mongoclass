from app.models.employee import Employee
from app.models.timelog import Timelog
from mongoengine.connection import connect
from pprint import pprint

from pymongo import MongoClient
from datetime import datetime, timedelta

# connect with MongoEngine
connect('project')

# connect with PyMongo
client = MongoClient()
db = client["project"]


# MONGOENGINE queries

emps = Employee.objects(name="funcionario 0").first()
emps = Employee.objects(routine__in=["5x2", "12x36"])
emps = Employee.objects(
    admission__gte=datetime(2020, 1, 1),
    admission__lte=datetime(2021, 1, 1),
).limit(3)

pprint(emps)
print()

# mesmas queries com PyMongo

emps = next(db.employee.find({"name": "funcionario 0"}))
emps = db.employee.find({
    "routine": {"$in": ["5x2", "12x36"]},
})
emps = db.employee.find({
    "admission": {
        "$gte": datetime(2020, 1, 1),
        "$lte": datetime(2021, 1, 1),
    }
}).limit(3)

pprint(emps)
print()
emps = list(emps)
pprint(emps)
print()


# MUITA ATENÇÃO COM TIPOS e dereferenciação

tls = Timelog.objects().limit(5)
for tl in tls:
    print(tl.employee)
    print(tl.employee.name)

print()

tls = list(db.timelog.find().limit(5))
for tl in tls:
    print(tl["employee"])

# e pra fazer as queries também

print()

tl = db.timelog.find({
    "employee": "5e60fbd330476ecc3faddfb2"
}, {"_id": 1})

pprint(list(tl))
print()

from bson import ObjectId

tl = db.timelog.find({
    "employee": ObjectId("5e60fbd330476ecc3faddfb2")
}, {"_id": 1})

pprint(list(tl))
print()
