import js_helpers
import js_router

"""
parses through top level expression 
"""
def convert_expression_to_gast(node):
    return js_router.node_to_gast(node.expression)

"""
takes python ast call node and converts to generic ast format
example print('hello'):
    exampleIn Call(func=Name(id='print'), args=[Str(s='hello')], keywords=[])
    exampleOut {'type': 'funcCall', 'value': {'type': 'logStatement'}, 'args': [{'type': 'str', 'value': 'hello'}]}
"""
def call_expression_to_gast(node):
    gast = {}
    gast["type"] = "funcCall"
    gast["value"] = js_router.node_to_gast(node.callee)
    gast["args"] = js_router.node_to_gast(node.arguments)
    return gast


