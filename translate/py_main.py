import sys
import ast
import astor

sys.path.append('assign')
sys.path.append('expression')
sys.path.append('helpers')
sys.path.append('routers')

import py_router

"""
takes pyton file and converts it to a node
node is then dealt with by node_to_gast 
"""
def py_to_gast(python_input):
    input_ast = ast.parse(python_input)
    print(astor.dump_tree(input_ast))
    return py_router.node_to_gast(input_ast)

file = "print('hello world')"
gast = py_to_gast(file)
print(gast)