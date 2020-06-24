import js_assign as a
import js_expression

"""
Takes js and converts to generic ast node
"""

def js_to_node(node, gast):
    if node.type == "ExpressionStatement":
        gast["body"].append(js_expression.jsexpr_to_gast(node.expression))
    if node.type == "VariableDeclaration":
        gast["body"].append(a.jsassign_to_gast(node.declarations))
    return gast



