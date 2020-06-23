import sys
sys.path.insert(1, '/home/stephwalsh/capstone/cjs_capstone/translate/helpers')
import steph_helpers


"""
Handles js var declerations to generic AST node
"""
def jsassign_to_gast(node):
  gast = {}
  gast["type"] = "varAssign"

  # only works with single assignment
  gast["varId"] = node[0].id.name
  gast["varValue"] = steph_helpers.jsarg_to_str(node[0].init) 
  return gast