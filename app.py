from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from main import main

app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('input')
parser.add_argument('in_lang')
parser.add_argument('out_lang')

class Translate(Resource):
    def get(self):
        return {'work': 'ing'}

    def post(self):
        # bring in post arguments
        args = parser.parse_args()
        input_code = args['input']
        input_lang = args['in_lang']
        output_lang = args['out_lang']

        output_code = main(input_code, input_lang, output_lang)

        return {'response': output_code}

api.add_resource(Translate, '/')

if __name__ == '__main__':
    app.run(debug=True)