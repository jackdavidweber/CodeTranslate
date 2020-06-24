import ast
import py_router as pr


"""
converts python ast operations to common string representation
TODO: add in boolean logic
"""
def pyop_to_str(op):
    if type(op) == ast.Add:
        return "+"
    elif type(op) == ast.Mult:
        return "*"
    elif type(op) == ast.Div:
        return "/"
    elif type(op) == ast.Sub:
        return "-"


"""
converts a python ast BinOp and converts it to a readable string recursively 
example 3+4:
    exampleIn BinOp(left=Num(n=3), op=Add, right=Num(n=4))
    exampleOut '3+4'
"""
def binOp_to_str(node):
    if type(node.left) == ast.BinOp:
        s = binOp_to_str(node.left) + pyop_to_str(node.op) + str(node.right.n)
    else:
        # base case: if left is just a number, operate on left wrt right
        s = str(node.left.n) + pyop_to_str(node.op) + str(node.right.n)

    return s
    
"""
takes ast node of type module and returns
a generic ast for that node
example print("hello"):
    node (input): Module(body=[Expr(value=Call(func=Name(id='print'), args=[Str(s='hello')], keywords=[]))])
    gast (output): {'type': 'root', 'body': [{'type': 'logStatement', 'args': ['hello']}]}
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
    gast (output): [{'type': 'logStatement', 'args': ['hello']}]
example array of strings:
    input: [Str(s='hello'), Str(s='world')]
    output:['hello', 'world']
"""
def node_list(node):
    gast_list = []
    for i in range(0, len(node)):
        gast_list.append(pr.node_to_gast(node[i]))

    return gast_list
