import esprima
import sys

# add path so imports possible in other files without sys
sys.path.append('assign')
sys.path.append('expression')
sys.path.append('helpers')
sys.path.append('routers')

import js_router

"""
takes js string and converts it to a generic AST
"""
def js_to_gast(js_input):
    try:
        input_ast = esprima.parseScript(js_input, {"tokens": False})
        return js_router.node_to_gast(input_ast)
    except:
        return "Error: code could not compile"

print(js_to_gast("(1 + 2) && 3"))
