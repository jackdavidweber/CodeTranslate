import code_to_gast.js_main as js_main
import code_to_gast.py_main as py_main
import gast_to_code.gast_to_code_router as gtc

py_input = 'if (x==True):\n\tif (y==True):\n\t\tprint("y and x are true")'
gast = py_main.py_to_gast(py_input)
py_output = gtc.gast_to_code(gast, "py")

print("py_input:\n", py_input)
print("gast:\n", gast)
print("py_output:\n", py_output)
