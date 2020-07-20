import java.code_to_gast.java_router as java_router
import javalang

def if_to_gast(node):
    gast = {"type": "if"}
    gast["body"] = java_router.node_to_gast(node.then_statement)
    gast["test"] = java_router.node_to_gast(node.condition)
    if node.else_statement == None:
        gast["orelse"] = []
    elif type(node.else_statement) == javalang.tree.IfStatement:
        gast["orelse"] = [java_router.node_to_gast(node.else_statement)]
    else:
        gast["orelse"] = java_router.node_to_gast(node.else_statement)
    return gast