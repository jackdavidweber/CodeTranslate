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