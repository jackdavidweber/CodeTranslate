import javascript.code_to_gast.js_helpers as js_helpers
import javascript.code_to_gast.js_router as js_router


def assign_to_gast(node):
    """
    Handles js var declarations to generic AST node
    """
    gast = {}
    gast["type"] = "varAssign"
    # only works with single assignment
    gast["kind"] = node.kind
    gast["varId"] = js_router.node_to_gast(node.declarations[0].id)
    gast["varValue"] = js_router.node_to_gast(node.declarations[0].init)
    return gast


def aug_assign_to_gast(node):
    """
    Handles augmented assignment to generic AST node
    example:
        js code: x += 1
        gast: {'type': 'augAssign', 'left': {'type': 'name', 'value': 'x'}, 'op': '+=', 'right': {'type': 'num', 'value': 1}}
    """
    gast = {"type": "augAssign"}
    gast["left"] = js_router.node_to_gast(node.left)
    gast["op"] = node.operator
    gast['right'] = js_router.node_to_gast(node.right)
    return gast
