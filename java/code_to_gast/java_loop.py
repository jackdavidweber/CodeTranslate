import java.code_to_gast.java_router as java_router
import javalang

def for_loop_to_gast(node):
    if type(node.control) == javalang.tree.ForControl:
        return for_range_to_gast(node)
    else:
        return for_of_to_gast(node)

def for_range_to_gast(node):
    gast = {"type": "forRangeStatement"}
    gast["body"] = java_router.node_to_gast(node.body)
    gast["init"] = java_router.node_to_gast(node.control.init)
    gast["test"] = java_router.node_to_gast(node.control)
    gast["update"] = java_router.node_to_gast(node.control.update[0])
    return gast