from . import bp as app
from flask import jsonify, current_app
from flask_restful import Resource, Api, reqparse

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        from app.models.api import search_by_course, add
        result = []
        for e in search_by_course('COMP9021'):
            result.append({'type':e.lab_type, 'course': e.course, 'capacity':e.capacity})
        return jsonify(result)

api.add_resource(HelloWorld, '/search/')