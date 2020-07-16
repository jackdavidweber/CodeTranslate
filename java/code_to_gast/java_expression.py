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
        gast["value"] = {"type": "customStatement"}
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
