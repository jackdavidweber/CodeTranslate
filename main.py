import sys

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
    # TODO: remove this once frontend is updated
    if input_lang == None and output_lang == None:
        input_lang = "js"
        output_lang = "py"

    if input_lang == "js":
        gast = js_main.js_to_gast(input_code)
    elif input_lang == "py":
        gast = py_main.py_to_gast(input_code)
    else:
        return "Error must specify language. For example, js for javascript and py for python"

    output_code = gtc.gast_router(gast, output_lang)

    return output_code
