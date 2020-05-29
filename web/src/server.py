from flask import Flask
from flask_restful import Resource, Api, abort
import pymongo

app = Flask(__name__)
api = Api(app)

DATA = {
    '442561000': {'zip5': '44256', 'zip4': '1000', 'score': 89.232},
    '442562001': {'zip5': '44256', 'zip4': '2001', 'score': 82.993},
    '123450001': {'zip5': '12345', 'zip4': '0001', 'score': 22.021}
}

def abort_if_zip9_doesnt_exist(zip9):
    if zip9 not in DATA:
        abort(404, message="Zip9 {} doesn't exist".format(zip9))

class Zip9Resource(Resource):
    def get(self, zip9):
        abort_if_zip9_doesnt_exist(zip9)
        return DATA[zip9]

api.add_resource(Zip9Resource, '/api/v1/<zip9>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)