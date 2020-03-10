from flask import Flask
from flask_restful import Resource, Api


class TimelogAPI(Resource):

    def get(self, employee=None):
        from app.models.timelog import Timelog
        from pymongo import MongoClient
        from datetime import datetime, timedelta

        # connect with PyMongo
        client = MongoClient()
        db = client["project"]

        base_query = {
            "kind__in": ["entrada", "saida"],
            "time__gte": datetime(2020, 1, 1),
            "time__lte": datetime(2021, 1, 1),
        }

        if not employee:
            tls = Timelog.objects(**base_query)

        else:
            tls = Timelog.objects(employee=employee, **base_query)

        result = []
        for tl in tls:
            result.append({
                "empId": str(tl.employee.id),
                "empName": tl.employee.name,
                "time": tl.time.strftime("%d/%m/%Y"),
                "kind": tl.kind
            })

        return result


def create_flask_app():
    from app import db

    flask_app = Flask(__name__)

    @flask_app.route("/hello")
    def hello_world():
        return "hello world"

    api = Api(flask_app)

    api.add_resource(TimelogAPI, '/timelog', '/timelog/<string:employee>')

    return flask_app
