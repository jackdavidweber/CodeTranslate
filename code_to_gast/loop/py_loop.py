import py_router as pr
import ast

def while_statement_to_gast(node):
    gast = {}
    gast["type"] = "whileStatement"
    gast["body"] = pr.node_to_gast(node.body)
    gast["test"] = pr.node_to_gast(node.test)
    return gast

"""
Converts python for statements to gast
Includes:
    ForRangeStatements: for i in range(0,10,1)
    ForOfStatements: for elem in [1,2,3]
"""
def for_statement_to_gast(node):
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
        step_node = args[2]
        
        """
        python stores step as ast.UnaryOp for negative numbers and
        ast.Num for positive numbers. This logic takes care of this.
        TODO: figure out a less "hacky" way of solving this problem
        """
        if type(step_node) == ast.UnaryOp:
            step_num = -1 * step_node.operand.n
        else:
            step_num = step_node.n

    # if there are only 2 arguments
    else:
        step_num = 1

    # store the start and end number (in py ast node form) of the loop
    start_node = args[0]
    end_node = args[1]

    gast["init"] = for_range_statement_init_helper(node.target, start_node)
    gast["test"] = for_range_statement_test_helper(node.target, start_node, end_node)
    gast["update"] = for_range_statement_update_helper(node.target, step_num)
    gast["body"] = pr.node_to_gast(node.body)
    return (gast)

"""
Takes a node representing start of loop and the variable node.
returns a gast node representing value for the init key in forRangeStatement gast
Example: ast.parse("for i in range(0,10,2)")
    input: var_node = ast.Name(i), start_node = ast.Num(0),
    output: {'type': 'varAssign', 'kind': 'let', 'varId': {'type': 'name', 'value': 'i'}, 'varValue': {'type': 'num', 'value': 0}}
"""
def for_range_statement_init_helper(var_node, start_node):
    gast = {}
    gast["type"] = "varAssign"
    gast["kind"] = "let"
    gast["varId"] = pr.node_to_gast(var_node)
    gast["varValue"] = pr.node_to_gast(start_node)
    return gast

"""
Takes a variable node, start node and end node. Returns gast node
representing value for the test key in forRangeStatement gast
Example: ast.parse("for i in range(0,10,2)")
    input: var_node = ast.Name(i), start_node = ast.Num(0), end_node = ast.Num(10)
    output: {'type': 'binOp', 'left': {'type': 'name', 'value': 'i'}, 'op': '<', 'right': {'type': 'num', 'value': 10}}
"""
def for_range_statement_test_helper(var_node, start_node, end_node):
    # first need to figure out whether to use "<" or ">"
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

"""
takes a variable node and an integer that represents the step. Returns
a gast node representing value for the update key in forRangeStatement gast
Example: ast.parse("for i in range(0,10,2)")
    input: var_node = ast.Name(i), step_num = 2
    output: {'type': 'augAssign', 'left': {'type': 'name', 'value': 'i'}, 'op': '+=', 'right': {'type': 'num', 'value': 2}}
"""
def for_range_statement_update_helper(var_node, step_num):
    if step_num < 0:
        op_str = "-="
        right_gast = {
            "type": "num",
            "value": -1 * step_num # FIXME: this feels very hacky
        }
    else:
        op_str = "+="
        right_gast = {
            "type": "num",
            "value": step_num
        }
    gast = {}
    gast["type"] = "augAssign"
    gast["left"] = pr.node_to_gast(var_node)
    gast["op"] = op_str
    gast["right"] = right_gast
    return gast
