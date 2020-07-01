import ast
import py_router as pr


"""
handles primitive number base cases
example: 7
    exampleIn: Num(n=7)
    exampleOut: {"type": "num", "value": 7} 
"""
def num(node):
    return {"type": "num", "value": node.n}


"""
handles primitive string base case
example: "hello"
    exampleIn: Str(s='hello')
    exampleOut: {'type': 'str', 'value': 'hello'}
"""
def string(node):
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
def name_constant(node):
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
def array(node):
    gast = {"type": "arr"}
    list_elem = []
    for elem in ast.iter_child_nodes(node):
        if type(elem) != ast.Load:
            list_elem.append(pr.node_to_gast(elem))
    gast["elts"] = list_elem
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
        ast.Not: "!"
    }
    return op_to_str_map[type(op)]


"""
converts a python ast BoolOp into a readable string recursively
example: True and False
    exampleIn: BoolOp(op=And(), values=[NameConstant(value=True), NameConstant(value=False)])
    exampleOut: {'type': 'boolOp', 'op': '&&', 'left': {'type': 'bool', 'value': 1}, 'right': {'type': 'bool', 'value': 0}}
"""
def boolOp(node):
    op = pyop_to_str(node.op)
    return boolOpHelper(node.values, op)

def boolOpHelper(node_list, op_str):
    gast = {}
    gast["type"] = "boolOp"
    gast["left"] = pr.node_to_gast(node_list[0])
    gast["op"] = op_str

    if len(node_list[1:]) > 1:
        gast["right"] = boolOpHelper(node_list[1:], op_str)
    else:
        gast["right"] = pr.node_to_gast(node_list[1])
    
    return gast


"""
converts a python ast BinOp and to a readable string recursively 
example 3+4:
    exampleIn BinOp(left=Num(n=3), op=Add, right=Num(n=4))
    exampleOut {'type': 'binOp', 'op': '+', 'left': {'type': 'num', 'value': 3}, 'right': {'type': 'num', 'value': 4}}
"""
def binOp(node):
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
def module(node):
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
def node_list(node):
    gast_list = []
    for i in range(0, len(node)):
        gast_list.append(pr.node_to_gast(node[i]))

    return gast_list

"""
takes ast.name node from python ast and converts to string represenation for the generic ast
"""
def name(node):
    if node.id == "print":
        return {"type": "logStatement"}
    return {"type": "name", "value": node.id}   

"""
takes node of type unaryOp and converts it to our generic ast represenations
"""
def unaryOp(node):
    return {"type": "unaryOp", "op": pyop_to_str(node.op), "arg": pr.node_to_gast(node.operand)}