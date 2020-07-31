from translate import translate
from shared.gast_to_code.converter_registry import ConverterRegistry
from bootstrap import bootstrap
from shared.gast_to_code.error_handler import ErrorHandler
from data_service import DataService


def main(input_code=None, input_lang=None, output_lang=None, session_id=-1):
    # First we check arguments since creation of error handler depends on valid args
    valid_input_langs = ConverterRegistry.get_language_codes_by_property(
        "is_input_lang")
    valid_output_langs = ConverterRegistry.get_language_codes_by_property(
        "is_output_lang")
    
    invalid_args_list = valid_args_checker(input_code, input_lang, output_lang,
                                   valid_input_langs, valid_output_langs)
    
    # If there are no invalid arguments, we can safely use them to produce output code and error_handler
    if (len(invalid_args_list) == 0):
        bootstrap()
        output_code = translate(input_code, input_lang, output_lang)
        error_handler = ConverterRegistry.get_converter(
            output_lang).get_error_handler()

    else:
        error_handler = ErrorHandler()
        output_code = error_handler.invalid_arguments(*invalid_args_list)

    return {"translation": output_code, "error": error_handler.get_error_obj()}


def valid_args_checker(input_code, input_lang, output_lang, valid_input_langs,
                       valid_output_langs):
    args_are_all_valid = True
    invalid_args_list = [None, None, None]

    # check if input code is valid
    if (type(input_code) != str):
        args_are_all_valid = False
        invalid_args_list[0] = input_code

    # check if input language is valid
    if (type(input_lang) != str) or (input_lang not in valid_input_langs):
        args_are_all_valid = False
        invalid_args_list[1] = input_lang

    # check if output language is valid
    if (type(output_lang) != str) or (output_lang not in valid_output_langs):
        args_are_all_valid = False
        invalid_args_list[2] = output_lang

    # if arguments are all valid, return empty list
    if args_are_all_valid:
        return []
    else:
        return invalid_args_list
