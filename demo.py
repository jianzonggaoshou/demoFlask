from flask import Flask
from flask_restful import Resource, Api, reqparse
import classENV

app = Flask(__name__)
api = Api(app)

PAYLOAD = {
    'name': '',
    'age': ''
}

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('age', type=int)

class UserResource(Resource):
    def get(self):
        result = classENV.queryUser()
        classENV.logging.debug(result)
        return result

api.add_resource(UserResource, '/user')

if __name__ == '__main__':
    app.run(debug=True)