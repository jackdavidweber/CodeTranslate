import js_router as jr

def if_statement(node):
    print("you hit if)")
    gast = {}
    gast["type"] = "if"
    # gast["body"] = jr.node_to_gast(node.consequent.body) # FIXME: remove .body and add to router
    gast["test"] = jr.node_to_gast(node.test)

    alt = node.alternate
    print("alt", alt, type(alt))
    # gast["orelse"] = jr.node_to_gast(alt)

    return gast