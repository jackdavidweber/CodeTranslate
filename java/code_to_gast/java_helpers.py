import java.code_to_gast.java_router as java_router


def node_list_to_gast_list(node):
    '''
    Takes list of nodes and converts to a 
    list of equivalent gast nodes
    '''
    gast_list = []
    for i in range(0, len(node)):
        gast_list.append(java_router.node_to_gast(node[i]))
    return gast_list


def array_to_gast(node):
    '''
    Takes an array of java ast nodes and converts to gast array node
    '''
    gast = {"type": "arr"}
    gast_list = []
    for i in range(0, len(node)):
        gast_list.append(java_router.node_to_gast(node[i]))

    gast["elements"] = gast_list
    return gast


def bin_op_to_gast(node):
    """
    Binops to gast for java 
    """
    gast = {"type": "binOp"}
    gast["left"] = java_router.node_to_gast(node.operandl.member)
    gast["op"] = node.operator
    gast["right"] = java_router.node_to_gast(node.operandr)
    return gast


def int_to_gast(node):
    """
    Handles int to gast for positive and negative whole numbers
    """
    if len(node.prefix_operators) > 0 and node.prefix_operators[0] == "-":
        return {"type": "num", "value": int(node.value) * -1}
    return {"type": "num", "value": int(node.value)}
