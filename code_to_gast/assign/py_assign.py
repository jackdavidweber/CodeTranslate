import py_router as pr

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
