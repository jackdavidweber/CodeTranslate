from translate import translate
from shared.gast_to_code.converter_registry import ConverterRegistry


def main(input_code, input_lang, output_lang):
    output_code = translate(input_code, input_lang, output_lang)

    converter = ConverterRegistry.get_converter(input_lang)
    error_obj = converter.error_handler.get_error_obj()

    return {"translation": output_code, "error": error_obj }
