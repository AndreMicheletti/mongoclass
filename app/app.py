from flask import Flask
from flask_restful import Resource, Api


class BookAPI(Resource):

    def get(self):
        from app.models.book import Book

        books = Book.objects()


def create_flask_app():

    flask_app = Flask(__name__)

    @flask_app.route("/hello")
    def hello_world():
        return "hello world"

    api = Api(flask_app)

    api.add_resource(BookAPI, '/books')
    api.add_resource(LogsAPI, '/logs')

    return flask_app
