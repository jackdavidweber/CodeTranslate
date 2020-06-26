import sys
from flask import abort

sys.path.append('translate')
sys.path.append('translate/assign')
sys.path.append('translate/expression')
sys.path.append('translate/helpers')
sys.path.append('translate/routers')

import js_main
import py_main
import gast_to_py
import gast_to_code as gtc

"""
input_code: string representing input code
input_lang: string representing input language of code
output_lang: string representing output language of code
return: string representing output code or error message
"""
def main(input_code, input_lang, output_lang):
    # TODO: eventually replace this with 400 error
    if input_lang == None and output_lang == None:
        abort(400, "Error: must specify input and output languages")
        input_lang = "js"
        output_lang = "py"

    #TODO: also do error checking on the output language
    if input_lang == "js":
        gast = js_main.js_to_gast(input_code)
    elif input_lang == "py":
        gast = py_main.py_to_gast(input_code)
    else:
        #TODO: figure out hwo to do error messages
        return "Error must specify language. For example, js for javascript and py for python"


    if (type(gast) == str) :
        # return error if gast not built
        return "Error: did not compile"
    output_code = gtc.gast_router(gast, output_lang)

    return output_code
