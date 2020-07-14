import python.code_to_gast.py_router as pr
import py_built_in_functions as built_in

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
    attribute = node.attr
    if attribute in {func.name for func in built_in.py_built_in_functions}:
        gast["type"] = "builtInAttribute"
        gast["id"] = built_in.py_built_in_functions[attribute].value
        return gast

    gast["type"] = "attribute"
    gast["id"] = attribute
    return gast

def function_def_to_gast(node):
    gast = {"type": "functionDeclaration"}
    gast["id"] = pr.node_to_gast(node.name)
    gast["params"] = pr.node_to_gast(node.args)
    gast["body"] = pr.node_to_gast(node.body)
    return gast

def subscript_to_gast(node):
    gast = {"type": "subscript"}
    gast["index"] = pr.node_to_gast(node.slice.value) 
    gast["value"] =  pr.node_to_gast(node.value) # TODO expand to cover slices of a list
    return gast