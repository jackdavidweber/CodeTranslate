from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from main import main
from bootstrap import bootstrap
from shared.gast_to_code.converter_registry import ConverterRegistry

app = Flask(__name__)
api = Api(app)
CORS(app)
bootstrap()

parser = reqparse.RequestParser()
parser.add_argument('input')
parser.add_argument('in_lang')
parser.add_argument('out_lang')
parser.add_argument('id')


class Translate(Resource):

    def __init__(self):
        self.lang_object = ConverterRegistry.get_lang_dict()

    def get(self):
        return {'supported_languages': self.lang_object}

    def post(self):
        # bring in post arguments
        args = parser.parse_args()
        input_code = args['input']
        input_lang = args['in_lang']
        output_lang = args['out_lang']
        session_id = args['id']

        if input_lang == "auto":
            # Gets non-beta (fully supported) languages for automatic detection
            fully_supported_lang_codes = ConverterRegistry.get_fully_supported_language_codes(
            )
            # automatic language detection (only fully supported languages) TODO: fall back on Beta if all else fails
            for lang in fully_supported_lang_codes:
                response_input_lang = lang
                output_code = main(input_code, response_input_lang, output_lang, session_id)

                if "Error" not in output_code:
                    break
        else:
            output_code = main(input_code, input_lang, output_lang, session_id)
            response_input_lang = input_lang


        # ensures that response_in_lang is the same as requested in_lang if no languages compile
        if output_code == "Error: did not compile":
            response_input_lang = input_lang

        return {
            'response': output_code,
            'response_in_lang': response_input_lang
        }


api.add_resource(Translate, '/')

if __name__ == '__main__':
    app.run(debug=True)
