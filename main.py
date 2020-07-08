import sys
from flask import abort

sys.path.append('code_to_gast')
sys.path.append('code_to_gast/assign')
sys.path.append('code_to_gast/expression')
sys.path.append('code_to_gast/conditional')
sys.path.append('code_to_gast/loop')
sys.path.append('code_to_gast/helpers')
sys.path.append('code_to_gast/routers')

import js_main
import py_main
import gast_to_code.gast_to_code_main as gtc
import pyrebase

"""
input_code: string representing input code
input_lang: string representing input language of code
output_lang: string representing output language of code
return: string representing output code or error message
"""
def main(input_code, input_lang, output_lang):

    if input_lang == None and output_lang == None:
        abort(400, "Error: must specify input and output languages")

    if input_lang == "js":
        gast = js_main.js_to_gast(input_code)
    elif input_lang == "py":
        gast = py_main.py_to_gast(input_code)
    else:
        #TODO: figure out hwo to do error messages
        return "Error must specify input language. For example, js for javascript and py for python"

    output_langs = ["js", "py"]
    if output_lang not in output_langs:
        # TODO: send 400 client error
        return "Error must specify output language. For example, js for javascript and py for python"
   
    if (type(gast) == str) :
        # return error if gast not built
        return "Error: did not compile"
    
    output_code = gtc.gast_to_code(gast, output_lang)

    config = {
    "apiKey": "AIzaSyBxiDkAmD5JmbQKT3RZqDgD2GdogoDViPU",
    "authDomain": "codetranslate-feedback.firebaseapp.com",
    "databaseURL": "https://codetranslate-feedback.firebaseio.com",
    "storageBucket": "codetranslate-feedback.appspot.com"
    }
    firebase = pyrebase.initialize_app(config)

    db = firebase.database()
    data = {'input': input_code, 'output': output_code, 'input-lang': input_lang, 'output-lang': output_lang}
    db.child("user-data").push(data)

    return output_code

