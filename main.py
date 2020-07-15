from flask import abort
import javascript.code_to_gast.js_main as js_main
import python.code_to_gast.py_main as py_main
import shared.gast_to_code.gast_to_code_router as gtc
from data_service import DataService
from bootstrap import bootstrap

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
    elif input_lang == "java":
        gast = java_main.java_to_gast(input_code)
    elif input_lang == "bash":
        gast = bash_main.bash_to_gast(input_code)
    else:
        #TODO: figure out hwo to do error messages
        return "Error must specify input language. For example, js for javascript and py for python"

    output_langs = ["js", "py", "bash", "java"]
    if output_lang not in output_langs:
        # TODO: send 400 client error
        return "Error must specify output language. For example, js for javascript and py for python"
   
    output_code = ""

    if (type(gast) == str) :
        # return error if gast not built - dont store in database
        output_code = "Error: did not compile"
    else:
        output_code = gtc.gast_to_code(gast, output_lang)
    
    # if the user deletes their translation don't store empty translation "" -> ""
    if (input_code == "" and output_code == ""):
        return output_code
    
    # store translation on firebase
    data_service = DataService.getInstance()
    data_service.store_query(input_code, output_code, input_lang, output_lang)

    return output_code
