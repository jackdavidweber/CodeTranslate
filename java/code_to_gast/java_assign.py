import java.code_to_gast.java_router as java_router
"""
Handles java var declarations to generic AST node
"""


def assign_to_gast(node):
    gast = {"type": "varAssign", "kind": "let"}
    gast["varValue"] = java_router.node_to_gast(node.initializer)
    # var name stored as string but we don't want to return gast string node
    gast["varId"] = {"type": "name", "value": node.name}
    return gast


"""
Handles increment and decrement operators
"""


def member_reference_to_gast(node):
    gast = {"type": "augAssign"}
    gast["left"] = java_router.node_to_gast(node.member)
    gast["op"] = node.postfix_operators[0]
    return gast


def aug_assign_to_gast(node):
    """
    Handles augmented assignment in java but not the incrementor and decrementor operations
    """
    gast = {"type": "augAssign"}
    gast["left"] = java_router.node_to_gast(node.expressionl.member)
    gast["op"] = node.type
    gast["right"] = java_router.node_to_gast(node.value)
    return gast