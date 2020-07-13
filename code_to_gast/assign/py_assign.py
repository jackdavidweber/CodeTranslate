import code_to_gast.routers.py_router as pr
import ast

"""
takes python ast assigns and converts them to generic ast format
note, that this assumes only a single assignment (i.e. x = 4)
for now, it does not work for things link x,y = 4,5
example:
    exampleIn Assign(targets=[Name(id='x')], value=Num(n=5))
    exampleOut {'type': 'varAssign', 'kind': 'let', 'varId': {'type': 'name', 'value': 'x'}, 'varValue': 5}
"""
def assign_to_gast(node):
    gast = {}
    gast["type"] = "varAssign"
    gast["kind"] = "let"
    gast["varId"] = pr.node_to_gast(node.targets[0]) # FIXME: understand when targets won't be 0
    gast["varValue"] = pr.node_to_gast(node.value)

    return gast

"""
takes python ast and converts augmented assignment into generic AST
example:
    exampleIn: AugAssign(target=Name(id='x', ctx=Store()), op=Add(), value=Num(n=1))
    exampleOut: {'type': 'augAssign', 'left': {'type': 'name', 'value': 'x'}, 'op': '+=', 'right': {'type': 'num', 'value': 1}}
"""
def aug_assign_to_gast(node):
    gast = {"type": "augAssign"}
    gast["left"] = pr.node_to_gast(node.target)
    gast["op"] = augop_to_str(node.op)
    gast["right"] = pr.node_to_gast(node.value)
    return gast

"""
convert augmented assignment classes to strings
"""
def augop_to_str(op):
    op_to_str_map = {
        ast.Add: "+=", 
        ast.Mult: "*=", 
        ast.Div: "/=", 
        ast.Sub: "-=",
    }
    return op_to_str_map[type(op)]


