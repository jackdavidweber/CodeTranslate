import py_router as pr

def if_statement(node):
    gast = {}
    gast["type"] = "if"
    gast["body"] = pr.node_to_gast(node.body)
    gast["orelse"] = pr.node_to_gast(node.orelse)
    gast["test"] = pr.node_to_gast(node.test)
    return gast