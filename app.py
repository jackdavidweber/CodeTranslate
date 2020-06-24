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
import py_main as py_main
import gast_to_py as gast_to_py
import gast_to_code as gtc


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

        # TODO: remove this once frontend is updated
        if input_lang == None and output_lang == None:
            input_lang = "js"
            output_lang = "py"

        print(input_code, input_lang, output_lang)
        if input_lang == "js":
            gast = js_main.js_to_gast(input_code)
        elif input_lang == "py":
            gast = py_main.py_to_gast(input_code)
        else:
            return {"Error": "must specify valid input language"}

        output_code = gtc.gast_router(gast, output_lang)

        return {'response': output_code}

api.add_resource(Translate, '/')

if __name__ == '__main__':
    app.run(debug=True)