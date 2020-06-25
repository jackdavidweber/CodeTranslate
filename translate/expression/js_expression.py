import js_helpers
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
            if (js_helpers.memExp_to_str(node.callee) == "console.log"):
                gast["type"] = "logStatement"
            else:
                gast["type"] = "customStatement"
        else:
            gast["type"] = "customStatement"

        # handle args
        gast["args"] = js_helpers.jsargs_to_strlist(node.arguments)
    return gast

def convert_expression_to_gast(node):
    return js_router.node_to_gast(node.expression)

"""
takes python ast call node and converts to generic ast format
example print('hello'):
    exampleIn Call(func=Name(id='print'), args=[Str(s='hello')], keywords=[])
    exampleOut {'type': 'logStatement', 'args': ['hello']}
"""
def call_expression_to_gast(node):
    gast = {}
    gast["type"] = name_to_gast_label(js_router.node_to_gast(node.callee))
    gast["args"] = js_router.node_to_gast(node.arguments)
    return gast

"""
takes ast.name node from python ast and converts to string 
represenation for the generic ast
"""
def name_to_gast_label(node):
    if node == "console.log":
        return "logStatement"
    else:
        return "customStatement"
