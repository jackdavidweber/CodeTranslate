import java.code_to_gast.java_router as java_router
'''
Takes list of nodes and converts to a 
list of equivalent gast nodes
'''


def node_list_to_gast_list(node):
    gast_list = []
    for i in range(0, len(node)):
        gast_list.append(java_router.node_to_gast(node[i]))
    return gast_list


'''
Takes an array of java ast nodes and converts to gast array node
'''


def array_to_gast(node):
    gast = {"type": "arr"}
    gast_list = []
    for i in range(0, len(node)):
        gast_list.append(java_router.node_to_gast(node[i]))

    gast["elements"] = gast_list
    return gast


def bin_op_to_gast(node):
    gast = {"type": "binOp"}
    gast["left"] = java_router.node_to_gast(node.operandl.member)
    gast["op"] = node.operator
    gast["right"] = java_router.node_to_gast(node.operandr)
    return gast