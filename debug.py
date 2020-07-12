import code_to_gast.js_main as js_main
import code_to_gast.py_main as py_main
import gast_to_code.gast_to_code_router as gtc

py_input = 'for j in [1,2]:\n\tfor k in [3,4]:\n\t\tj\n\t\tk'
js_input = 'for j of [1,2] {\n\tfor k of [3,4] {\n\t\tj\n\t\tk\n\t}\n}'
gast = py_main.py_to_gast(py_input)
py_output = gtc.gast_to_code(gast, "py")

print("py_input:\n", py_input)
print("gast:\n", gast)
print("py_output:\n", py_output)

print(js_input)
