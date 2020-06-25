from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import sys

sys.path.append('translate')
sys.path.append('translate/assign')
sys.path.append('translate/expression')
sys.path.append('translate/helpers')
sys.path.append('translate/routers')

import js_main as js_main
import gast_to_py as gast_to_py


app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('input')

class Translate(Resource):
    def get(self):
        return {'work': 'ing'}

    def post(self):
        args = parser.parse_args()
        input_text = args['input']
        gast = js_main.js_to_gast(input_text)
        output_code = gast_to_py.gast_to_py(gast)
        return {'response': output_code}

api.add_resource(Translate, '/')

if __name__ == '__main__':
    app.run(debug=True)