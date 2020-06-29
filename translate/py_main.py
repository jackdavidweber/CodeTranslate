import sys
import ast

sys.path.append('assign')
sys.path.append('expression')
sys.path.append('helpers')
sys.path.append('routers')

import py_router

"""
takes pyton code and converts it to a node
node is then dealt with by node_to_gast 
"""
def py_to_gast(python_input): 
  try:
    input_ast = ast.parse(python_input)
    print(ast.dump(input_ast))
    return py_router.node_to_gast(input_ast)
  except:
    return "Error: code could not compile"
  
i = "print()"
print(py_to_gast(i))
