import javascript.code_to_gast.js_router as js_router


def array_expression_to_gast(node):
    """
    handles arrays and recursively calls node_to_gast on all its elements
    """
    gast = {"type": "arr"}
    gast["elements"] = []
    for elm in node.elements:
        gast["elements"].append(js_router.node_to_gast(elm))
    return gast


def dictionary_to_gast(node):
    """
    handles dictionaries conversion to generic AST with list of properties
    """
    gast = {"type": "dict"}
    gast["elements"] = js_router.node_to_gast(node.properties)
    return gast


def property_to_gast(node):
    """
    takes each property of a dictionary and turns it into a property type
    """
    gast = {"type": "property"}
    gast["key"] = js_router.node_to_gast(node.key)
    gast["value"] = js_router.node_to_gast(node.value)
    return gast


def program_to_gast(node):
    """
    takes ast node of type program and returns
    a generic ast for that node
    example print("hello"):
        node (input): Program(body=[ExpressionStatement(value=Call(func=Name(id='print'), args=[Str(s='hello')], keywords=[]))])
        gast (output): {'type': 'root', 'body': [{'type': 'funcCall', 'value': {'type': 'logStatement'}, 'args': [{'type': 'str', 'value': 'hello'}]}]}
    """
    gast = {"type": "root"}
    gast["body"] = js_router.node_to_gast(node.body)
    return gast


def bin_op_to_gast(bop):
    """
    converts a python ast BinOp and converts it to a gast node
    """
    gast = {"type": "binOp"}
    if bop.left.type != "BinaryExpression" and bop.right.type != "BinaryExpression":
        gast["left"] = js_router.node_to_gast(bop.left)
        gast["op"] = bop.operator
        gast["right"] = js_router.node_to_gast(bop.right)
    if bop.left.type == "BinaryExpression":
        gast["left"] = bin_op_to_gast(bop.left)
        gast["op"] = bop.operator
        gast["right"] = js_router.node_to_gast(bop.right)
    if bop.right.type == "BinaryExpression":
        gast["left"] = js_router.node_to_gast(bop.left)
        gast["op"] = bop.operator
        gast["right"] = bin_op_to_gast(bop.right)
    return gast


def bool_op_to_gast(node):
    """
    takes a type boolean operator and turns it into our generic AST
    """
    gast = {"type": "boolOp"}
    gast["left"] = js_router.node_to_gast(node.left)
    gast["op"] = node.operator
    gast["right"] = js_router.node_to_gast(node.right)
    return gast


def node_list(node):
    """
    takes a node that represents a list of nodes.
    returns a list of gast
    example console.log("hello"):
        node (input):
        gast (output): [{'type': 'funcCall', 'value': {'type': 'logStatement'}, 'args': [{'type': 'str', 'value': 'hello'}]}]
    example array of strings:
        input: [Str(s='hello'), Str(s='world')]
        output:[{'type': 'str', 'value': 'hello'}, {'type': 'str', 'value': 'world'}]
    """
    gast_list = []
    for i in range(0, len(node)):
        gast_list.append(js_router.node_to_gast(node[i]))
    return gast_list


def block_statement_to_gast(node):
    """
    Seems like this block statement type is called
    whenever there are curly braces. Probably will need 
    to end up making this function more robust.
    """
    return js_router.node_to_gast(node.body)


def unary_to_gast(node):
    """
    Takes unary operation such as ! and converts it to generic AST.
    javascript makes negative numbers unary expressions. This is our
    current workaround.
    """
    if node.operator == "-":
        return {"type": "num", "value": node.argument.value * -1}

    return {
        "type": "unaryOp",
        "op": node.operator,
        "arg": js_router.node_to_gast(node.argument)
    }


def return_statement_to_gast(node):
    """
    Handles return statement to gast operation
    """
    return {
        "type": "returnStatement",
        "value": js_router.node_to_gast(node.argument)
    }


def assign_pattern_to_gast(node):
    """
    Handles assignment patterns ie x = 3, used to set default values in functions
    """
    gast = {"type": "assignPattern"}
    gast["left"] = js_router.node_to_gast(node.left)
    gast["right"] = js_router.node_to_gast(node.right)
    return gast


def update_expression_to_gast(node):
    """
    Currently handles ++ and -- operations
    """
    gast = {"type": "augAssign"}
    gast["left"] = js_router.node_to_gast(node.argument)
    gast["op"] = node.operator
    return gast
