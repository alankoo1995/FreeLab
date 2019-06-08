from . import bp as app
from flask import jsonify, current_app, request, escape
from flask_restful import Resource, Api, reqparse

api = Api(app)

class LabStatus(Resource):
    def get(self):
        from app.spider.spider import Spider
        result = Spider().get_data()
        return jsonify(result)
        # from app.models.api import search_by_course, add
        # result = []
        # for e in search_by_course('COMP9021'):
            # result.append({'type':e.lab_type, 'course': e.course, 'capacity':e.capacity})
        # return jsonify(result)

class SearchLabStatus(Resource):
    def get(self):
        from app.spider.spider import Spider
        from itertools import chain
        s = escape(request.args.get('s'))
        result = None
        
        raw_data = Spider().get_data()
        labs_name = chain.from_iterable([e.keys() for e in raw_data])
        if s in labs_name:
            result = list(filter(lambda x:s in x.keys(), raw_data))[0]
            print(result)

        if result:
            return result, 200
        return 'Not Found', 404

api.add_resource(LabStatus, '/today/')
api.add_resource(SearchLabStatus, '/search/')