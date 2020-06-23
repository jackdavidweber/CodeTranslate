import sys

sys.path.insert(1,'routers')
import py_router as pr

"""
takes python ast assigns and converts them to generic ast format
note, that this assumes only a single assignment (i.e. x = 4)
for now, it does not work for things link x,y = 4,5
example:
    exampleIn Assign(targets=[Name(id='x')], value=Num(n=5))
    exampleOut {'type': 'varAssign', 'varId': 'customStatement', 'varValue': 5}
"""
def assign(node):
    gast = {}
    gast["type"] = "varAssign"
    gast["varId"] = pr.node_to_gast(node.targets[0]) # FIXME: understand when targets won't be 0
    gast["varValue"] = pr.node_to_gast(node.value)

    return gast
