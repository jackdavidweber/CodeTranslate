import java.code_to_gast.java_router as java_router

'''
Takes method invocation ie function declaration and translates to
gAST node of type funcCall
'''
def method_invocation_to_gast(node):
    
    gast = {"type": "funcCall"}
    gast["args"] = java_router.node_to_gast(node.arguments)
    
    #TODO: change logic and add support for functions called on objects
    if node.qualifier == "System.out" and node.member == "println":
        gast["value"] = {"type": "logStatement"}
    else:
        # function not called on object
        if not node.qualifier:
            gast["value"] = {"type": "name", "value": node.member}
        else:
            object_list = (node.qualifier.split("."))
            object_list.append(node.member)
            gast["value"] = functionHelper(object_list)
    return gast

def functionHelper(object_list):
    gast = {}
    gast["type"] = "attribute"
    gast["id"] = object_list.pop()

    if len(object_list) == 1:
        gast["value"] = {"type": "name", "id": object_list.pop()}
    else: 
        gast["value"] = functionHelper(object_list)
    
    return gast


'''
Takes class declaration and turns into start of gast
Currently allows support for one function and only 
converts statements inside that function
'''
def class_declaration_to_gast(node):
    gast = {"type": "root"}
    # only support for one function currently
    gast["body"] = java_router.node_to_gast(node.body[0])
    return gast
