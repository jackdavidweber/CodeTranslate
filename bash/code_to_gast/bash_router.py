import bashlex

def node_to_gast(node):

    print (type(node))
    if type(node) == list:
       node_list = []
       for part in node:
           node_list.append(node_to_gast(part))
       return node_list
    elif type(node) == bashlex.ast.node:
       print(node[0])