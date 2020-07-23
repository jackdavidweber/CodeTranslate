from flask import abort
import javascript.code_to_gast.js_main as js_main
import python.code_to_gast.py_main as py_main
import java.code_to_gast.java_main as java_main
import shared.gast_to_code.gast_to_code_router as gtc
import shared.gast_to_code.general_helpers as general_helpers
from data_service import DataService
from bootstrap import bootstrap
import subprocess
"""
input_code: string representing input code
input_lang: string representing input language of code
output_lang: string representing output language of code
return: string representing output code or error message
"""


def main(input_code, input_lang, output_lang, session_id=-1):
    try:
        # check arguments TODO(taiga#172): remove hard coded references
        check_valid_args(input_code, input_lang, output_lang,
                         ["js", "py", "java"], ["js", "py", "bash", "java"])

        # code to gast
        gast = main_code_to_gast(input_code, input_lang)
        check_valid_gast(gast)

        #gast to code
        output_code = main_gast_to_code(gast, output_lang)

        # analytics
        main_store_analytics(input_code, output_code, input_lang, output_lang,
                             session_id)

        return output_code
    except:
        # This error should never occur but probably a good thing to have in case
        return "Error: unable to execute main function"


def main_code_to_gast(input_code, input_lang):
    try:
        # TODO(taiga#172): remove hard coded references
        if input_lang == "js":
            gast = js_main.js_to_gast(input_code)
        elif input_lang == "py":
            gast = py_main.py_to_gast(input_code)
        elif input_lang == "java":
            gast = java_main.java_to_gast(input_code)
        else:
            return "Error must specify input language. For example, js for javascript and py for python"

        return gast
    except:
        return "Error: unable to convert code to generic ast"


def check_valid_args(input_code, input_lang, output_lang, valid_input_langs,
                     valid_output_langs):
    if not (type(input_code) == str and type(input_lang) == str and
            type(output_lang) == str):
        abort(400, "Error: invalid argument types")

    if input_lang not in valid_input_langs:
        abort(
            400,
            "Error must specify valid input language. For example, js for javascript and py for python"
        )

    if output_lang not in valid_output_langs:
        abort(
            400,
            "Error must specify valid output language. For example, js for javascript and py for python"
        )


def check_valid_gast(gast):
    if (type(gast) == str):  # FIXME(swalsh15) why is this necessary??
        # return error if gast not built - dont store in database
        abort(400, "Error: did not compile")


def main_gast_to_code(gast, output_lang):
    try:
        output_code = gtc.gast_to_code(gast, output_lang)

        if output_lang == "java":
            output_code = general_helpers.java_linter(output_code)

        return output_code
    except:
        return "Error: unable to convert generic ast to code"


def main_store_analytics(input_code, output_code, input_lang, output_lang,
                         session_id):
    # if the user deletes their translation don't store empty translation "" -> ""
    if (input_code == "" and output_code == ""):
        pass
    else:
        # store translation on firebase
        data_service = DataService.getInstance()
        data_service.store_query(input_code, output_code, input_lang,
                                 output_lang, session_id)
