from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        return jsonify({'hello': 'world'})

api.add_resource(HelloWorld,'/search')