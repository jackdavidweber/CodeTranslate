import sys 
from routers.py_router import *
from expression.py_expression import *
from assign.py_assign import *
from helpers.jack_py_helpers import *
import ast
import astor

"""
takes pyton file and converts it to a node
node is then dealt with by node_to_gast 
"""
def py_to_gast(python_input_filename):
    input_ast =  astor.code_to_ast.parse_file(python_input_filename)
    print(astor.dump_tree(input_ast))
    return node_to_gast(input_ast)


fileName = "/home/jackweber/cjs_capstone/experimental/jackPython/astMapping/sampleCode.py"
gast = py_to_gast(fileName)
print(gast)