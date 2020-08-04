import java.code_to_gast.java_router as java_router


def assign_to_gast(node):
    """
    Handles java var declarations to generic AST node
    """
    gast = {"type": "varAssign", "kind": "let"}
    gast["varValue"] = java_router.node_to_gast(node.initializer)
    # var name stored as string but we don't want to return gast string node
    gast["varId"] = {"type": "name", "value": node.name}
    return gast


def member_reference_to_gast(node):
    """
    Handles increment and decrement operators
    """
    gast = {"type": "augAssign"}
    if len(node.postfix_operators) == 0:
        return {"type": "error", "value": "unsupported"}
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
