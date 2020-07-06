import py_router as pr

def while_statement_to_gast(node):
    gast = {}
    gast["type"] = "whileStatement"
    gast["body"] = pr.node_to_gast(node.body)
    gast["test"] = pr.node_to_gast(node.test)
    return gast