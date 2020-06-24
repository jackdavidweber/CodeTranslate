import esprima
import sys

# add path so imports possible in other files without sys
sys.path.append('assign')
sys.path.append('expression')
sys.path.append('helpers')
sys.path.append('routers')

import js_router

program = "let x = 's' + 1 + 3\n console.log(x)"

"""
takes js string and converts it to a general AST
"""
def js_to_gast(program):
    input_ast = esprima.parseScript(program, {"tokens": False})
    return js_router.node_to_gast(input_ast)

print(js_to_gast(program))
