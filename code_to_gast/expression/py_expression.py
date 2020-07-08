import py_router as pr

"""
Takes python ast.expr node and converts them to the generic
ast format
example print('hello')
    exampleIn Expr(value=Call(func=Name(id='print'), args=[Str(s='hello')], keywords=[]))
    exampleOut {'type': 'funcCall', 'value': {'type': 'logStatement'}, 'args': [{'type': 'str', 'value': 'hello'}]}
"""
def expr_to_gast(node):
    return pr.node_to_gast(node.value)

"""
takes python ast call node and converts to generic ast format
example print('hello'):
    exampleIn Call(func=Name(id='print'), args=[Str(s='hello')], keywords=[])
    exampleOut {'type': 'funcCall', 'value': {'type': 'logStatement'}, 'args': [{'type': 'str', 'value': 'hello'}]}
"""
def call_to_gast(node):
    gast = {}
    gast["type"] = "funcCall"
    gast["value"] = pr.node_to_gast(node.func)
    gast["args"] = pr.node_to_gast(node.args)

    return gast

"""
handles attributes for python expressions
"""
def attribute_to_gast(node):
    gast = {"value": pr.node_to_gast(node.value)}
     
    # The tool only currently supports the built in functions below 
    # TODO add other built in function translations
    if node.attr == "append":
        gast["type"] = "builtInAttribute"
        gast["id"] = "appendStatement"
        return gast
    if node.attr == "pop":
        gast["type"] = "builtInAttribute"
        gast["id"] = "popStatement"
        return gast
    gast["type"] = "attribute"
    gast["id"] = node.attr
    return gast

def function_def_to_gast(node):
    gast = {"type": "functionDeclaration"}
    gast["id"] = pr.node_to_gast(node.name)
    gast["params"] = pr.node_to_gast(node.args)
    gast["body"] = pr.node_to_gast(node.body)
    return gast