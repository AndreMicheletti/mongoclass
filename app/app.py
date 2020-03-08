from flask import Flask
from flask_restful import Resource, Api


class TimelogAPI(Resource):

    def get(self, employee=None):
        from app.models.timelog import Timelog

        if not employee:

            tls = Timelog.objects()

        else:

            tls = Timelog.objects(employee=employee)

        return [tl.time.strftime("%d/%m/%Y") for tl in tls]


def create_flask_app():
    from app import db

    flask_app = Flask(__name__)

    @flask_app.route("/hello")
    def hello_world():
        return "hello world"

    api = Api(flask_app)

    api.add_resource(TimelogAPI, '/timelog', '/timelog/<string:employee>')

    return flask_app
