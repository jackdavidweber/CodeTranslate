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
parser.add_argument('in_code')
parser.add_argument('in_lang')
parser.add_argument('out_lang')

class Translate(Resource):
    def get(self):
        return {'work': 'ing'}

    def post(self):
        # bring in post arguments
        args = parser.parse_args()
        input_code = args['in_code']
        input_lang = args['in_lang']
        output_lang = args['out_lang']

        print(input_code, input_lang, output_lang)
        if input_lang == "js":
            gast = js_main.js_to_gast(input_code)
        elif input_lang == "py":
            pass # TODO: fill this in
        else:
            return {"Error": "must specify valid input language"}
        
        output_code = gast_to_py.gast_to_py(gast)
        return {'response': output_code}

api.add_resource(Translate, '/')

if __name__ == '__main__':
    app.run(debug=True)