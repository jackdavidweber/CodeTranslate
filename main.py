from translate import translate
from shared.gast_to_code.converter_registry import ConverterRegistry
from bootstrap import bootstrap
from shared.gast_to_code.error_handler import ErrorHandler

def main(input_code=None, input_lang=None, output_lang=None):
    # First we check arguments since creation of error handler depends on valid args 
    # TODO(taiga#172): remove hard coded references
    args_are_valid = is_valid_args(input_code, input_lang, output_lang,
                        ["js", "py", "java"], ["js", "py", "bash", "java"])
    if (not args_are_valid):
        error_handler = ErrorHandler()
        output_code = error_handler.invalid_arguments()
        
    # If arguments are valid, we can safely use them to produce output code and error_handler
    else:
        bootstrap()
        output_code = translate(input_code, input_lang, output_lang)
        error_handler = ConverterRegistry.get_converter(output_lang).get_error_handler()

    return {"translation": output_code, "error": error_handler.get_error_obj() }


def is_valid_args(input_code, input_lang, output_lang, valid_input_langs,
                     valid_output_langs):
    if not (type(input_code) == str and type(input_lang) == str and
            type(output_lang) == str):
        return False # "Error: invalid argument types"

    if input_lang not in valid_input_langs:
        return False # invalid input language

    if output_lang not in valid_output_langs:
        return False # invalid output language

    return True
