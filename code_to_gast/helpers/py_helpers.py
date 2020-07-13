import ast
import code_to_gast.routers.py_router as pr


"""
handles primitive number base cases
example: 7
    exampleIn: Num(n=7)
    exampleOut: {"type": "num", "value": 7} 
"""
def num_to_gast(node):
    return {"type": "num", "value": node.n}


"""
handles primitive string base case
example: "hello"
    exampleIn: Str(s='hello')
    exampleOut: {'type': 'str', 'value': 'hello'}
"""
def string_to_gast(node):
    return {"type": "str", "value": node.s}


"""
handles primitive boolean and None base cases
example: True
    exampleIn: NameConstant(value=True)
    exampleOut: {'type': 'bool', 'value': 1}
example: None
    exampleIn: NameConstant(value=None)
    exampleOut: {'type': 'none'}
"""
def name_constant_to_gast(node):
    gast =  {"type": "bool"} 
    if node.value == True:
        gast["value"] = 1
    elif node.value == False:
        gast["value"] = 0
    else:
        gast["type"] = "none"
    return gast


"""
takes an array of elements and recursively calls node_to_gast on each element
"""
def array_to_gast(node):
    gast = {"type": "arr"}
    list_elem = []
    for elem in ast.iter_child_nodes(node):
        if type(elem) != ast.Load:
            list_elem.append(pr.node_to_gast(elem))
    gast["elements"] = list_elem
    return gast

"""
takes a dictionary converts it for the generic AST 
"""
def dictionary_to_gast(node):
    gast = {"type": "dict", "elements": []}

    for i in range(len(node.keys)):
        prop = {"type": "property"}
        prop["key"] = pr.node_to_gast(node.keys[i])
        prop["value"] = pr.node_to_gast(node.values[i])
        gast["elements"].append(prop)
    return gast


"""
converts python ast operations to common string representation
"""
def pyop_to_str(op):
    op_to_str_map = {
        ast.Add: "+", 
        ast.Mult: "*", 
        ast.Div: "/", 
        ast.Sub: "-",
        ast.BitAnd: "&", 
        ast.BitOr: "|", 
        ast.And: "&&", 
        ast.Or: "||",
        ast.Not: "!",
        ast.Gt: ">",
        ast.GtE: ">=",
        ast.Lt: "<",
        ast.LtE: "<=",
        ast.Eq: "=="

    }
    return op_to_str_map[type(op)]


"""
TODO: fix this docstring
converts a python ast BoolOp into a readable string recursively
example: True and False
    exampleIn: BoolOp(op=And(), values=[NameConstant(value=True), NameConstant(value=False)])
    exampleOut: {'type': 'boolOp', 'op': '&&', 'left': {'type': 'bool', 'value': 1}, 'right': {'type': 'bool', 'value': 0}}
"""
def bool_op_to_gast(node):
    op = pyop_to_str(node.op)
    return bool_op_helper(node.values, op)

"""
Recursively handles case where Python creates a list of literals
"""
def bool_op_helper(node_list, op_str):
    gast = {}
    gast["type"] = "boolOp"
    gast["left"] = pr.node_to_gast(node_list[0])
    gast["op"] = op_str

    if len(node_list[1:]) > 1:
        gast["right"] = bool_op_helper(node_list[1:], op_str)
    else:
        gast["right"] = pr.node_to_gast(node_list[1])
    return gast


"""
converts a python ast BinOp and to a readable string recursively 
example 3+4:
    exampleIn BinOp(left=Num(n=3), op=Add, right=Num(n=4))
    exampleOut {'type': 'binOp', 'op': '+', 'left': {'type': 'num', 'value': 3}, 'right': {'type': 'num', 'value': 4}}
"""
def bin_op_to_gast(node):
    gast = {"type": "binOp", "op": pyop_to_str(node.op)}
    gast["left"] = pr.node_to_gast(node.left)
    gast["right"] = pr.node_to_gast(node.right)
    return gast

    
"""
takes ast node of type module and returns
a generic ast for that node
example print("hello"):
    node (input): Module(body=[Expr(value=Call(func=Name(id='print'), args=[Str(s='hello')], keywords=[]))])
    gast (output): {'type': 'root', 'body': [{'type': 'funcCall', 'value': {'type': 'logStatement'}, 'args': [{'type': 'str', 'value': 'hello'}]}]}
"""
def module_to_gast(node):
    gast = {"type": "root"}
    gast["body"] = pr.node_to_gast(node.body)
    return gast


"""
takes a node that represents a list of nodes.
returns a list of gast
example print("hello"):
    node (input): [Expr(value=Call(func=Name(id='print'), args=[Str(s='hello')], keywords=[]))]
    gast (output): [{'type': 'funcCall', 'value': {'type': 'logStatement'}, args': [{'type': 'str', 'value': 'hello'}]}]
example array of strings:
    input: [Str(s='hello'), Str(s='world')]
    output:[{'type': 'str', 'value': 'hello'}, {'type': 'str', 'value': 'world'}]
"""
def node_list_to_gast(node):
    gast_list = []
    for i in range(0, len(node)):
        gast_list.append(pr.node_to_gast(node[i]))

    return gast_list

"""
takes ast.name node from python ast and converts to string represenation for the generic ast
"""
def name_to_gast(node):
    if node.id == "print":
        return {"type": "logStatement"}
    return {"type": "name", "value": node.id}   

"""
takes node of type unaryOp and converts it to our generic ast represenations
"""
def unary_op_to_gast(node):
    return {"type": "unaryOp", "op": pyop_to_str(node.op), "arg": pr.node_to_gast(node.operand)}

"""
takes argument from function declaration and makes into gast node
"""
def arg_to_gast(node):
    return pr.node_to_gast(node.arg)

"""
Python native string class is the type of function names and arguments. String literals are handled by str_to_gast()
This function takes the name of an identifer and turns it into a gast node 
"""
def str_to_gast(node):
    return {"type": "name", "value": node}

"""
Turns return statement into gast
"""
def return_statement_to_gast(node):
    return {"type": "returnStatement", "value": pr.node_to_gast(node.value)}

"""
Handles args of function declarations with default values
"""
def function_args_to_gast(node):
    return arg_helper(node.args, node.defaults, [])

def arg_helper(arg_list, default_list, param_list): 
    # if arg_list empty return
    if not arg_list:
        return param_list
    # if default list empty arg not assigned
    if not default_list:
        param_list.insert(0, pr.node_to_gast(arg_list.pop()))
        return arg_helper(arg_list, default_list, param_list)
    else:
        gast = {"type": "assignPattern"}
        gast["left"] = pr.node_to_gast(arg_list.pop())
        gast["right"] = pr.node_to_gast(default_list.pop())
        param_list.insert(0, gast)
        return arg_helper(arg_list, default_list, param_list)

"""
takes node of type Compare and converts it to our generic ast representation
example:
    Example In: Compare(left=Num(n=1), ops=[Gt()], comparators=[Num(n=1), Num(n=2)])
    Example Out: {'type': 'binOp', 'left': {'type': 'num', 'value': 1}, 'op': '>', 'right': {'type': 'num', 'value': 2}}
"""
def compare_to_gast(node):
    # create list of comparators. (1>2>=3 would create list [1,2,3])
    comparator_list = node.comparators
    comparator_list.insert(0, node.left) # this is necessary since pyAST stores leftmost comparator seperately

    # create list of operators. (1>2>=3 would create list [>, >=]
    op_list = node.ops

    return compare_helper(comparator_list, op_list)

# TODO: combine logic in bool_op_helper and compare_helper into single function
def compare_helper(node_list, op_list):
    gast = {}
    gast["type"] = "binOp"
    gast["left"] = pr.node_to_gast(node_list[0])
    gast["op"] = pyop_to_str(op_list[0])

    if len(node_list[1:]) > 1:
        gast["right"] = compare_helper(node_list[1:], op_list[1:])
    else:
        gast["right"] = pr.node_to_gast(node_list[1])

    return gast

"""
break statement to gast
"""
def break_to_gast(node):
    return {"type": "break"}

"""
continue statement to gast
"""
def continue_to_gast(node):
    return {"type": "continue"}

