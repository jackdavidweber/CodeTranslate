import js_router as jr

def while_statement_to_gast(node):
    gast = {}
    gast["type"] = "whileStatement"

    """
    Code re-used from js_conditional. TODO: write a helper or figure out how to go through router
    """
    body = node.body
    if body.type == "BlockStatement":
        gast["body"] = jr.node_to_gast(body)
    else:
        gast["body"] = [jr.node_to_gast(body)]

    gast["test"] = jr.node_to_gast(node.test)
    return gast
