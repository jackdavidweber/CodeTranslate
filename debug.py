from shared.gast_to_code.converter_registry import ConverterRegistry
from bootstrap import bootstrap
import main
import javascript.code_to_gast.js_main as js_main

out = main.main('print()', 'py', 'uk')
print(out)

# bootstrap()

# pycode = 'class Bar:\n\tdef __init__(self):\n\t\tpass'
# print(main.main(pycode, 'py', 'js'))

# print(main.main('print()', 'py', 'js'))

# bootstrap()
# print(translate.translate('console.log(8)', 'js', 'bash'))

#------------------

# pycode = 'class Bar:\n\tdef __init__(self):\n\t\tpass'

# bootstrap()
# print(translate.translate(pycode, "py", "java"))

# java_converter = ConverterRegistry.get_converter("java")
# print(java_converter.get_error_handler().get_error_obj())

# #......

# bootstrap()
# print(translate.translate(pycode, "py", "java"))

# java_converter = ConverterRegistry.get_converter("java")
# print(java_converter.get_error_handler().get_error_obj())
