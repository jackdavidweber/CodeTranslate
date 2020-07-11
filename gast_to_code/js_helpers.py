import gast_to_code.gast_to_code_router as router
import gast_to_code.general_helpers as general_helpers
import js_built_in_functions

def gast_to_js_dict(gast):
    return "{" + router.gast_to_code(gast["elements"], "js") + "}"

def gast_to_js_property(gast):
    return router.gast_to_code(gast["key"], "js") + ": " + router.gast_to_code(gast["value"], "js")

def gast_to_js_var_assign(gast):
    kind = gast["kind"]
    varId = router.gast_to_code(gast["varId"], "js")
    varValue = router.gast_to_code(gast["varValue"], "js")

    if gast["varId"]["type"] == "subscript":
        return varId + " = " + varValue
    return kind + " " + varId + " = " + varValue

def gast_to_js_aug_assign(gast):
    return router.gast_to_code(gast["left"], "js") + " " + gast["op"] + " " + router.gast_to_code(gast["right"], "js")

def gast_to_js_functions(gast):
    return router.gast_to_code(gast["value"], "js") + "(" + router.gast_to_code(gast["args"], "js") + ")"

def gast_to_js_attribute(gast):
    return router.gast_to_code(gast["value"], "js") + "." + gast["id"] 

def gast_to_js_built_in_attribute(gast):
    return router.gast_to_code(gast["value"], "js") + "." + js_built_in_functions.js_built_in_functions(gast["id"]).name

def gast_to_js_bool_op(gast):
    return general_helpers.gast_to_node_bin_op_helper(gast, "js")

def gast_to_js_unary_op(gast):
    return "!" + router.gast_to_code(gast["arg"], "js")

def gast_to_js_bool(gast):
    if gast["value"] == 1:
        return "true"
    else:
        return "false"

def gast_to_js_if(gast, lvl=0):
    test = router.gast_to_code(gast["test"], "js")
    body_indent = "\n\t" + "\t"*lvl
    closing_brace_indent = "\n" + "\t"*lvl
    body = general_helpers.list_helper(gast["body"], "js", body_indent, lvl+1)

    out = 'if (' + test + ') {' + body_indent + body + closing_brace_indent + "}"

    # orelse can either be empty, or be an elif or be an else
    if len(gast["orelse"]) == 0:
        pass
    elif gast["orelse"][0]["type"] == "if":
        out += " else " + router.gast_to_code(gast["orelse"], "js")
    else:
        out += " else {\n\t" + general_helpers.list_helper(gast["orelse"], "js", "\n\t") + "\n}"

    return out

def gast_to_js_func_declarations(gast, lvl=0):
    name = router.gast_to_code(gast["id"], "js")
    args = router.gast_to_code(gast["params"], "js")
    body = general_helpers.list_helper(gast["body"], "js", "\n\t")
    out = "function " + name
    out += "(" + args + ") {\n\t"

    out += body

    out += "\n}"
    return out

def gast_to_js_return_statement(gast):
    return "return " + router.gast_to_code(gast["value"], "js")

def gast_to_js_assign_pattern(gast):
    return router.gast_to_code(gast["left"], "js") + " = " + router.gast_to_code(gast["right"], "js")

def gast_to_js_while(gast, lvl=0):
    test = router.gast_to_code(gast["test"], "js")
    body = general_helpers.list_helper(gast["body"], "js", "\n\t")
    
    out = 'while (' + test + ') {\n\t' + body + "\n}"
    return out

def gast_to_js_forRange(gast, lvl=0):
    loop_init = router.gast_to_code(gast["init"], "js")
    loop_test = router.gast_to_code(gast["test"], "js")
    loop_update = router.gast_to_code(gast["update"], "js")
    body = general_helpers.list_helper(gast["body"], "js", "\n\t")

    return "for (" + loop_init + "; " + loop_test + "; " + loop_update + ") {\n\t" + body + "\n}"

def gast_to_js_forOf(gast, lvl=0):
    arr_str = router.gast_to_code(gast["iter"], "js")
    var_name = gast["init"]["value"]
    body = general_helpers.list_helper(gast["body"], "js", "\n\t")

    out = "for (" + var_name + " of " + arr_str + ") {\n\t" + body + "\n}"
    return out

def gast_to_js_subscript(gast):
    return router.gast_to_code(gast["value"], "js") + "[" + router.gast_to_code(gast["index"], "js") + "]"
