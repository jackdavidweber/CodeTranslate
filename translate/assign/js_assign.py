import js_helpers

"""
Handles js var declarations to generic AST node
"""
def jsassign_to_gast(node):
  gast = {}
  gast["type"] = "varAssign"

  # only works with single assignment
  gast["varId"] = node[0].id.name
  gast["varValue"] = js_helpers.jsarg_to_str(node[0].init)
  return gast