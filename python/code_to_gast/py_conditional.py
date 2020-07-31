import python.code_to_gast.py_router as pr


def if_statement_to_gast(node):
    """
    converts if statement node recursively into our generic AST structure
    """
    gast = {}
    gast["type"] = "if"
    gast["body"] = pr.node_to_gast(node.body)
    gast["orelse"] = pr.node_to_gast(node.orelse)
    gast["test"] = pr.node_to_gast(node.test)
    return gast
