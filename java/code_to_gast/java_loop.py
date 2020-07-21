import java.code_to_gast.java_router as java_router
import javalang

def for_loop_to_gast(node):
    """
    Decides what type of for loop it is based on its children
    """
    if type(node.control) == javalang.tree.ForControl:
        return for_range_to_gast(node)
    else:
        return for_of_to_gast(node)

def for_range_to_gast(node):
    """
    Handle java range loops recursively using the router
    """
    gast = {"type": "forRangeStatement"}
    gast["body"] = java_router.node_to_gast(node.body)
    gast["init"] = java_router.node_to_gast(node.control.init)
    gast["test"] = java_router.node_to_gast(node.control.condition)
    gast["update"] = java_router.node_to_gast(node.control.update[0])
    return gast

def for_of_to_gast(node):
    """
    Handle java for of loops that iterate over elements in an array, dictionary, etc.
    """
    gast = {"type": "forOfStatement"}
    # TODO revaluate how we do variable assignment to account for this type of var assignment
    gast["init"] = java_router.node_to_gast(node.control.var.declarators[0].name)
    gast["body"] = java_router.node_to_gast(node.body)
    gast["iter"] = java_router.node_to_gast(node.control.iterable.member)
    return gast

def while_statement_to_gast(node):
    """
    Handle while statements in java to gast
    """
    gast = {"type": "whileStatement"}
    gast["body"] = java_router.node_to_gast(node.body)
    gast["test"] = java_router.node_to_gast(node.condition)
    return gast
