import esprima
import sys

# add path so imports possible in other files without sys
sys.path.append('assign')
sys.path.append('expression')
sys.path.append('helpers')
sys.path.append('routers')

import js_router as router

program = "let my_container = 20\n console.log('eh')"

def js_to_gast(program):
    input_ast = esprima.parseScript(program, {"tokens": True})
    # TODO: can add more fields to the generic ast
    gast = {"type": "root", "body": []}
    for node in input_ast.body:
        # call router
        router.js_to_node(node, gast)
    return gast

print(js_to_gast(program))
