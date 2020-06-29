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
        return helpers.boolean(node)

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

    # Expressions
    elif type(node) == ast.Name:
        return expression.name(node)
    elif type(node) == ast.Expr:
        return expression.expr(node)
    elif type(node) == ast.Call:
        return expression.call(node)

    # Assigns
    elif type(node) == ast.Assign:
        return assign.assign(node)

    # Conditionals
    elif type(node) == ast.If:
        return conditional.if_statement(node)


    else:
        print("nothing hit")
        return "nothing hit"