from pymongo import MongoClient
from datetime import datetime, timedelta

import random

client = MongoClient()
db = client["project"]

sources = ["android", "android", "web", "telephone"]
initial_days = [1, 15, 21]

admissions = [
    datetime(2020, 2, 8),
    datetime(2020, 3, 5),
    datetime(2020, 1, 19),
    datetime(2020, 1, 2),
    datetime(2020, 2, 20)
]

entrada = datetime.utcnow()
entrada.replace(hour=8, minute=0, second=0, microsecond=0)

saida = datetime.utcnow()
saida.replace(hour=17, minute=0, second=0, microsecond=0)

routines = ["12x36", "6x1", "5x2"]

# employees

for i in range(12):
    doc = {
        "name": f"funcionario {i}",
        "admission": random.choice(admissions),
        "initial_day": random.choice(initial_days),
        "routine": random.choice(routines)
    }

    if random.randrange(0, 6) == 0:
        print("demiti um")
        doc["resignation"] = datetime(2020, 3, 5)

    empid = db.employee.insert_one(doc).inserted_id

    print("ADDED EMPLOYEE")

    # timelogs
    tl_count = random.randrange(1, 9)

    for i in range(tl_count):
        db.timelog.insert({
            "time": entrada + timedelta(days=i),
            "kind": "entrada",
            "source": random.choice(sources),
            "employee": empid
        })
        db.timelog.insert({
            "time": saida + timedelta(days=i),
            "kind": "saida",
            "source": random.choice(sources),
            "employee": empid
        })
    print(f"added {tl_count} timelogs")

print("CABEI")
