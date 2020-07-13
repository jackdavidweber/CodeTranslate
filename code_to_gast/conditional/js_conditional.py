import code_to_gast.routers.js_router as jr

def if_statement_to_gast(node):
    gast = {}
    gast["type"] = "if"

    """
    The reason for the below logic is to make the following two expressions evaluate to the same gast
        if (true) {console.log("This is true")}
        if (true) console.log("This is true")
    In the future, we should have a discussion about how we want to handle single line vs. block statements
    for javascript. This works for now.
    TODO
    """
    body = node.consequent
    if body.type == "BlockStatement":
        gast["body"] = jr.node_to_gast(body)
    else:
        gast["body"] = [jr.node_to_gast(body)]

    """
    For now, I added in this logic so that the none type would be replaced by an 
    empty list as specified in gast contract. Since Cory is working on none types, 
    I did not want to add this in until merge. Eventually the whole code block should
    be replaced with gast["orelse"] = jr.node_to_gast(node.alternate)
    TODO
    """
    alt = node.alternate
    if alt == None:
        gast["orelse"] = jr.node_to_gast([])
    else:
        # FIXME: nested if statement same problem as in body
        if alt.type == "BlockStatement":
            gast["orelse"] = jr.node_to_gast(alt)
        else:
            gast["orelse"] = [jr.node_to_gast(alt)] # 


    gast["test"] = jr.node_to_gast(node.test)

    return gast