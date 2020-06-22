import ast
from ..helpers.jack_py_helpers import *


def node_to_gast(node):
    # Base Cases
    if type(node) == ast.Str:
        return node.s
    elif type(node) == ast.Num:
        return node.n

    # Base Cases with embedded recursion / if statements
    elif type(node) == ast.BinOp: #FIXME: I treat this as a base case even though there are if statements inside.
        return binOp_to_str(node)
    elif type(node) == ast.Name:
        return name(node)

    # List of Nodes to list of gast
    elif type(node) == list:
        return node_list(node)

    # Other
    elif type(node) == ast.Module:
        return module(node)

    elif type(node) == ast.Expr:
        return expr(node)
    elif type(node) == ast.Assign:
        return assign(node)
    elif type(node) == ast.Call:
        return call(node)
    else:
        print("nothing hit")
        return "nothing hit"