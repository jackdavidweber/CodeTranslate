import shared.gast_to_code.gast_to_code_router as gtc
import shared.gast_to_code.general_helpers as general_helpers
from shared.gast_to_code.converter_registry import ConverterRegistry


def translate(input_code, input_lang, output_lang):
    """
    input_code: string representing input code
    input_lang: string representing input language of code
    output_lang: string representing output language of code
    return: string representing output code or error message
    """
    error_handler = ConverterRegistry.get_converter(
        output_lang).get_error_handler()

    # code to gast
    converter = ConverterRegistry.get_converter(input_lang)
    gast = converter.code_to_gast(input_code)
    if (not is_valid_gast(gast)):
        output_code = error_handler.compilation()
        return output_code

    #gast to code
    output_code = gast_to_code_caller(gast, output_lang, error_handler)

    return output_code


def is_valid_gast(gast):
    if (type(gast) == dict):
        return True
    else:
        return False


def gast_to_code_caller(gast, output_lang, error_handler):
    # try:
    output_code = gtc.gast_to_code(gast, output_lang)

    # TODO: remove last static reference to language
    if output_lang == "java":
        output_code = general_helpers.java_linter(output_code)

    return output_code
    # except:
    #     artifact = {'gast': gast, 'outputLang': output_lang}
    #     return error_handler.unknown_error("translate.py", artifact)
