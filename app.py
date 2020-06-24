from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('name')

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    
    def post(self):
        args = parser.parse_args()
        print(args['name'])
        return {'hello': args['name']}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)