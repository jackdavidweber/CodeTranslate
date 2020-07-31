from shared.gast_to_code.converter_registry import ConverterRegistry
from python.gast_to_code.py_gast_to_code_converter import PyGastToCodeConverter
from javascript.gast_to_code.js_gast_to_code_converter import JsGastToCodeConverter
from java.gast_to_code.java_gast_to_code_converter import JavaGastToCodeConverter
from bash.gast_to_code.bash_gast_to_code_converter import BashGastToCodeConverter


def bootstrap():
    ConverterRegistry.register(JsGastToCodeConverter(), "js")
    ConverterRegistry.register(PyGastToCodeConverter(), "py")
    ConverterRegistry.register(JavaGastToCodeConverter(), "java")
    ConverterRegistry.register(BashGastToCodeConverter(), "bash")
