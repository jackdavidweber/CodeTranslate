import java.code_to_gast.java_router as java_router
import javalang

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
        # function called on object
        if node.qualifier:
            object_list = (node.qualifier.split("."))
            object_list.append(node.member)
            gast["value"] = list_to_attribute_value_node(object_list)
        else:
            gast["value"] = {"type": "name", "value": node.member}
    return gast

'''
Takes list of callees and members and from function called
on object and translates into gAST node
Ex: car.drive() -> {"type": "attribute", "id": "drive", "value": 
{"type": "name", "id": "car"}}
'''
def list_to_attribute_value_node(object_list):
    gast = {}
    gast["type"] = "attribute"
    gast["id"] = object_list.pop()

    if len(object_list) == 1:
        gast["value"] = {"type": "name", "id": object_list.pop()}
    else: 
        gast["value"] = list_to_attribute_value_node(object_list)
    
    return gast


'''
Takes class declaration and turns into start of gast
Currently allows support for one function and only 
converts statements inside that function
'''
def class_declaration_to_gast(node):
    gast = {"type": "root"}
    '''
    If the method in class is main function only translate that method and ignore function header
    We are assuming user only wants body of function translated
    ''' 
    if type(node.body[0]) == javalang.tree.MethodDeclaration and node.body[0].name == "artifical_wrapper_WkVHC":
        gast["body"] = java_router.node_to_gast(node.body[0].body) 
    else:
        gast["body"] = java_router.node_to_gast(node.body)
    return gast

def function_delcaration_to_gast(node):
    gast = {"type": "functionDeclaration"}
    gast["params"] = java_router.node_to_gast(node.parameters)
    gast["id"] = {"type": "name", "value": node.name}
    gast["body"] = java_router.node_to_gast(node.body)
    return gast

def formal_parameter_to_gast(node):
    return {"type": "name", "value": node.name}