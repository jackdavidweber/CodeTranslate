import js_helpers
import js_router

"""
Handles js var declarations to generic AST node
"""
def jsassign_to_gast(node):
  gast = {}
  gast["type"] = "varAssign"
  # only works with single assignment
  gast["varId"] = js_router.node_to_gast(node[0].id)
  gast["varValue"] = js_helpers.jsarg_to_str(node[0].init)
  return gast