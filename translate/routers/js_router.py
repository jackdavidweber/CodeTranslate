import js_assign
import js_expression
import js_helpers
import esprima

"""
Takes js and converts to generic ast node
"""

def node_to_gast(node):
    #  check if list before calling type to avoid error
    if type(node) == list:
        return js_helpers.node_list(node)
    # base cases
    if node.type == "Literal":
        # must check bool first since bool is instance of int
        if isinstance(node.value, bool):
            if node.raw == "true":
                node.value = 1
            else:
                node.value = 0
            return {"type": "bool", "value": node.value}
        elif isinstance(node.value, int):
            return {"type": "num", "value": node.value}
        elif isinstance(node.value, str):
            return {"type": "str", "value": node.value}
        else:
            return "Unsupported prim"
    elif node.type == "Identifier":
        # identifier has quotes around name
        return node.name
    elif node.type == "BinaryExpression":
        return js_helpers.binOp_to_str(node)
    #statements
    elif node.type == "VariableDeclaration":
        return js_assign.jsassign_to_gast(node)
    elif node.type == "ExpressionStatement":
        return js_expression.convert_expression_to_gast(node)
    elif node.type == "CallExpression":
        return js_expression.call_expression_to_gast(node)
    elif node.type == "MemberExpression":
        return js_helpers.memExp_to_str(node)
    elif node.type == "Program":
        return js_helpers.program_to_gast(node)
    elif node.type == "ArrayExpression":
        return js_helpers.js_array_expression(node)
    else:
        # not supported
        return "No match"



