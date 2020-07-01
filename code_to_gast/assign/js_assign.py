import js_helpers
import js_router

"""
Handles js var declarations to generic AST node
"""
def assign_to_gast(node):
  gast = {}
  gast["type"] = "varAssign"
  # only works with single assignment
  gast["kind"] = node.kind
  gast["varId"] = js_router.node_to_gast(node.declarations[0].id)
  gast["varValue"] = js_router.node_to_gast(node.declarations[0].init)
  return gast