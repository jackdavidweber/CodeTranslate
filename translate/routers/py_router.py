import sys
import ast
import helpers.py_helpers as helpers
import py_expression as expression
import py_assign as assign
import py_conditional as conditional

"""
router that all nodes in the python AST are passed through recursively
"""
def node_to_gast(node):
    # Base Cases
    if type(node) == ast.Str:
        return helpers.string(node)
    elif type(node) == ast.Num:
        return helpers.num(node)
    elif type(node) == ast.NameConstant:
        return helpers.name_constant(node)

    # Helpers
    elif type(node) == ast.Module:
        return helpers.module(node)
    elif type(node) == ast.BinOp:
        return helpers.binOp(node)
    elif type(node) == ast.BoolOp:
        return helpers.boolOp(node)
    elif type(node) == ast.List:
        return helpers.array(node)
    elif type(node) == list:
        return helpers.node_list(node)
    elif type(node) == ast.Name:
        return helpers.name(node)

    # Expressions
    elif type(node) == ast.Expr:
        return expression.expr(node)
    elif type(node) == ast.Call:
        return expression.call(node)
    elif type(node) == ast.Attribute:
        return expression.attribute(node)

    # Assigns
    elif type(node) == ast.Assign:
        return assign.assign(node)

    # Conditionals
    elif type(node) == ast.If:
        return conditional.if_statement(node)


    else:
        return {"type": "error", "value": "unsupported"}