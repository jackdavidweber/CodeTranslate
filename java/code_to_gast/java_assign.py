import java.code_to_gast.java_router as java_router

"""
Handles java var declarations to generic AST node
"""
def assign_to_gast(node):
    gast = {"type": "varAssign", "kind": "let"}
    gast["varValue"] = java_router.node_to_gast(node.initializer)
    # var name stored as string but we don't want to return gast string node
    gast["varId"] = {"type": "name", "value": node.name}
    return gast
