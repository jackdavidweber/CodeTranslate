import sys
import ast
import helpers.py_helpers as h
import py_expression as e
import py_assign as a

def node_to_gast(node):
    # Base Cases
    if type(node) == ast.Str:
        return node.s
    elif type(node) == ast.Num:
        return node.n
    elif type(node) == ast.NameConstant:
        return node.value

    # Base Cases with embedded recursion / if statements
    elif type(node) == ast.BinOp: #FIXME: I treat this as a base case even though there are if statements inside.
        return h.binOp_to_str(node)
    elif type(node) == ast.Name:
        return e.name(node)

    # List of Nodes to list of gast
    elif type(node) == list:
        return h.node_list(node)

    # Other
    elif type(node) == ast.Module:
        return h.module(node)

    elif type(node) == ast.Expr:
        return e.expr(node)
    elif type(node) == ast.Assign:
        return a.assign(node)
    elif type(node) == ast.Call:
        return e.call(node)
    else:
        print("nothing hit")
        return "nothing hit"