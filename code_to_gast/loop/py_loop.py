import py_router as pr
import ast

def while_statement_to_gast(node):
    gast = {}
    gast["type"] = "whileStatement"
    gast["body"] = pr.node_to_gast(node.body)
    gast["test"] = pr.node_to_gast(node.test)
    return gast

def for_statement_to_gast(node):
    # first identify whether forRange or forOf
    if type(node.iter) == ast.Call:
        return for_range_statement_to_gast(node)
    else: 
        return for_of_statement_to_gast(node)

def for_of_statement_to_gast(node):
    gast = {}
    gast["type"] = "forOfStatement"
    gast["init"] = pr.node_to_gast(node.target)
    gast["iter"] = pr.node_to_gast(node.iter)
    gast["body"] = pr.node_to_gast(node.body)
    return gast


def for_range_statement_to_gast(node):
    gast = {}
    gast["type"] = "forRangeStatement"

    args = node.iter.args
    if len(args) < 2 or len(args) > 3:
        return "unsupported: too many args in loop" # TODO: streamline messages
    elif len(args) == 3:
        step_num = args[2].n
    else:
        step_num = 1 # TODO: figure out how to do this using ast nodes

    start_node = args[0]
    end_node = args[1]

    gast["init"] = for_range_statement_init_helper(node.target, start_node)
    gast["test"] = for_range_statement_test_helper(node.target, start_node, end_node)
    gast["update"] = for_range_statement_update_helper(node.target, step_num)
    gast["body"] = pr.node_to_gast(node.body)

    return (gast)

"""
Takes a node representing start of loop and the variable node.
returns a dict representing value for the init key in forRangeStatements
"""
def for_range_statement_init_helper(var_node, start_node):
    gast = {}
    gast["type"] = "varAssign"
    gast["kind"] = "let"
    gast["varId"] = pr.node_to_gast(var_node)
    gast["varValue"] = pr.node_to_gast(start_node)
    return gast

def for_range_statement_test_helper(var_node, start_node, end_node):
    # first need to figure out whether test expr is < or >
    start_val = start_node.n
    end_val = end_node.n
    if start_val <= end_val:
        op_str = "<"
    else:
        op_str = ">"

    gast = {}
    gast["type"] = "binOp"
    gast["left"] = pr.node_to_gast(var_node)
    gast["op"] = op_str
    gast["right"] = pr.node_to_gast(end_node)
    return gast

def for_range_statement_update_helper(var_node, step_num):
    if step_num < 0:
        op_str = "-="
    else:
        op_str = "+="
    
    gast = {}
    gast["type"] = "augAssign"
    gast["left"] = pr.node_to_gast(var_node)
    gast["op"] = op_str
    gast["right"] = {
        "type": "num",
        "value": step_num
    }
    return gast