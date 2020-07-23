from shared.gast_to_code.converter_registry import ConverterRegistry
from bootstrap import bootstrap
bootstrap()
import main

pycode = 'class Bar:\n\tdef __init__(self):\n\t\tpass'

print(main.main(pycode, "py", "java"))

py_converter = ConverterRegistry.get_converter("py")
print(py_converter.error_handler.get_error_obj())

js_converter = ConverterRegistry.get_converter("java")
print(js_converter.error_handler.get_error_obj())


# print(converter.error_handler)
# converter.error_handler.unsupported_feature()
# print(converter.error_handler)

