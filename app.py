from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from main import main
from bootstrap import bootstrap

app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('input')
parser.add_argument('in_lang')
parser.add_argument('out_lang')

class Translate(Resource):

    def get(self):
        bootstrap() # TODO: run bootstrap at loading of translate rather than on get request
        return {'work': 'ing'}

    def post(self):
        languages = ["py", "js"] 

        # bring in post arguments
        args = parser.parse_args()
        input_code = args['input']
        input_lang = args['in_lang']
        output_lang = args['out_lang']

        output_code = main(input_code, input_lang, output_lang)

        i = 0
        while (output_code == "Error: did not compile") and (i < len(languages)):
            input_lang = languages[i]
            output_code = main(input_code, input_lang, output_lang)
            i += 1

        return {'response': output_code, 'response_in_lang': input_lang}

api.add_resource(Translate, '/')

if __name__ == '__main__':
    app.run(debug=True)