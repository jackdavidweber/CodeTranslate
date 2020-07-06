import sys
import ast
import helpers.py_helpers as helpers
import py_expression as expression
import py_assign as assign
import py_conditional as conditional
import py_loop as loop


"""
router that all nodes in the python AST are passed through recursively
"""
def node_to_gast(node):
    # Base Cases
    if type(node) == ast.Str:
        return helpers.string_to_gast(node)
    elif type(node) == ast.Num:
        return helpers.num_to_gast(node)
    elif type(node) == ast.NameConstant:
        return helpers.name_constant_to_gast(node)

    # Helpers
    elif type(node) == ast.Module:
        return helpers.module_to_gast(node)
    elif type(node) == ast.BinOp:
        return helpers.bin_op_to_gast(node)
    elif type(node) == ast.BoolOp:
        return helpers.bool_op_to_gast(node)
    elif type(node) == ast.List:
        return helpers.array_to_gast(node)
    elif type(node) == list:
        return helpers.node_list_to_gast(node)
    elif type(node) == ast.Name:
        return helpers.name_to_gast(node)
    elif type(node) == ast.UnaryOp:
        return helpers.unary_op_to_gast(node)
    elif type(node) == ast.Compare:
        return helpers.compare_to_gast(node)

    # Expressions
    elif type(node) == ast.Expr:
        return expression.expr_to_gast(node)
    elif type(node) == ast.Call:
        return expression.call_to_gast(node)
    elif type(node) == ast.Attribute:
        return expression.attribute_to_gast(node)

    # Assigns
    elif type(node) == ast.Assign:
        return assign.assign_to_gast(node)

    # Conditionals
    elif type(node) == ast.If:
        return conditional.if_statement_to_gast(node)


    else:
        return {"type": "error", "value": "unsupported"}