import sys
sys.path.insert(1,'routers')
import py_router as pr

"""
Takes python ast.expr node and converts them to the generic
ast format
example print('hello')
    exampleIn Expr(value=Call(func=Name(id='print'), args=[Str(s='hello')], keywords=[]))
    exampleOut {'type': 'logStatement', 'args': ['hello']}
"""
def expr(node):
    return pr.node_to_gast(node.value)

"""
takes python ast call node and converts to generic ast format
example print('hello'):
    exampleIn Call(func=Name(id='print'), args=[Str(s='hello')], keywords=[])
    exampleOut {'type': 'logStatement', 'args': ['hello']}
"""
def call(node):
    gast = {}
    gast["type"] = pr.node_to_gast(node.func)
    gast["args"] = pr.node_to_gast(node.args)

    return gast

"""
takes ast.name node from python ast and converts to string 
represenation for the generic ast
"""
def name(node):
    if node.id == "print":
        return "logStatement"
    else:
        return "customStatement"
      