from translate import translate
from shared.gast_to_code.converter_registry import ConverterRegistry
from bootstrap import bootstrap


def main(input_code, input_lang, output_lang):
    bootstrap()
    output_code = translate(input_code, input_lang, output_lang)

    converter = ConverterRegistry.get_converter(output_lang)
    error_obj = converter.get_error_handler().get_error_obj()

    return {"translation": output_code, "error": error_obj }
