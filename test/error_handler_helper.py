from shared.gast_to_code.converter_registry import ConverterRegistry
from bootstrap import bootstrap

def get_error_handler(output_lang):
    bootstrap()
    converter = ConverterRegistry.get_converter(output_lang)
    error_handler = converter.get_error_handler()
    return error_handler
