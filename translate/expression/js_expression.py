import js_helpers as h
import js_router

"""
Takes javascript expressions and converts them to the generic
ast format
"""
def jsexpr_to_gast(node):
    gast = {}
    if node.type == "CallExpression":
        # handle callee
        if node.callee.type == "MemberExpression":
            if (h.memExp_to_str(node.callee) == "console.log"):
                gast["type"] = "logStatement"
            else:
                gast["type"] = "customStatement"
        else:
            gast["type"] = "customStatement"

        # handle args
        gast["args"] = h.jsargs_to_strlist(node.arguments)
    return gast

def expr(node):
    return js_router.node_to_gast(node.expression)

"""
takes python ast call node and converts to generic ast format
example print('hello'):
    exampleIn Call(func=Name(id='print'), args=[Str(s='hello')], keywords=[])
    exampleOut {'type': 'logStatement', 'args': ['hello']}
"""
def call(node):
    gast = {}
    gast["type"] = name(js_router.node_to_gast(node.callee))
    gast["args"] = js_router.node_to_gast(node.arguments)
    return gast

"""
takes ast.name node from python ast and converts to string 
represenation for the generic ast
"""
def name(node):
    if node == "console.log":
        return "logStatement"
    else:
        return "customStatement"
