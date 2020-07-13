import ast
import code_to_gast.routers.py_router as py_router

"""
takes pyton code and converts it to a node
node is then dealt with by node_to_gast 
"""
def py_to_gast(python_input): 
  input_ast = ''
  try:
    input_ast = ast.parse(python_input)
  except:
    return "Error: code could not compile"
  
  return py_router.node_to_gast(input_ast)
