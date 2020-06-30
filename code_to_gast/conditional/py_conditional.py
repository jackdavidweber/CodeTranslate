import py_router as pr

"""
converts if statement node recursively into our generic AST structure
"""
def if_statement_to_gast(node):
    gast = {}
    gast["type"] = "if"
    gast["body"] = pr.node_to_gast(node.body)
    gast["orelse"] = pr.node_to_gast(node.orelse)
    gast["test"] = pr.node_to_gast(node.test)
    return gast