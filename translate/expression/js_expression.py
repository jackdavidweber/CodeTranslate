import js_helpers as h

"""
Takes javascript expressions and converts them to the generic
ast format
"""

def jsexpr_to_gast(node):
    gast = {}
    if node.type == "CallExpression":
        # handle callee
        if node.callee.type == "MemberExpression":
            if (h.memExp_to_str(node.callee) == "console.log"):
                gast["type"] = "logStatement"
            else:
                gast["type"] = "customStatement"
        else:
            gast["type"] = "customStatement"

        # handle args
        gast["args"] = h.jsargs_to_strlist(node.arguments)
    return gast
