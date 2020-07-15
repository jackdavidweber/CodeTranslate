from shared.gast_to_code.converter_registry import ConverterRegistry
from python.gast_to_code.py_gast_to_code_converter import PyGastToCodeConverter
from javascript.gast_to_code.js_gast_to_code_converter import JsGastToCodeConverter



def bootstrap():
    ConverterRegistry.register(PyGastToCodeConverter, "py")
    ConverterRegistry.register(JsGastToCodeConverter, "js")

