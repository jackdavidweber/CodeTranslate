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
def py_to_gast(python_input_filename):
    input_ast =  astor.code_to_ast.parse_file(python_input_filename)
    print(astor.dump_tree(input_ast))
    return py_router.node_to_gast(input_ast)

fileName = "py_sample_code.py"
gast = py_to_gast(fileName)
print(gast)