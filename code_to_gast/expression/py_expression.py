import py_router as pr
import astor

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
    gast = {"type": "attribute", "id": node.attr}
    gast["value"] = pr.node_to_gast(node.value)
    return gast

def function_def_to_gast(node):
    gast = {"type": "functionDeclaration"}
    gast["id"] = {"type": "name", "value": node.name}
    gast["params"] = pr.node_to_gast(node.args)
    gast["body"] = pr.node_to_gast(node.body)
    return gast