import gast_to_code.gast_to_code_router as router
import gast_to_code.general_helpers as general_helpers
import py_built_in_functions

def gast_to_py_dict(gast):
    return "{" + router.gast_to_code(gast["elements"], "py") + "}"

def gast_to_py_property(gast):
    return router.gast_to_code(gast["key"], "py") + ": " + router.gast_to_code(gast["value"], "py")

def gast_to_py_var_assign(gast):
    value = router.gast_to_code(gast["varValue"], "py")
    return router.gast_to_code(gast["varId"], "py") + " = " + value

def gast_to_py_aug_assign(gast):
    return router.gast_to_code(gast["left"], "py") + " " + gast["op"] + " " + router.gast_to_code(gast["right"], "py")


def gast_to_py_functions(gast):
    return router.gast_to_code(gast["value"], "py") + "(" + router.gast_to_code(gast["args"], "py") + ")"

def gast_to_py_attribute(gast):
    return router.gast_to_code(gast["value"], "py") + "." + gast["id"] 

def gast_to_py_built_in_attribute(gast):
    return router.gast_to_code(gast["value"], "py") + "." + py_built_in_functions.py_built_in_functions(gast["id"]).name

def gast_to_py_bool_op(gast):
    op = " and " if gast["op"] == "&&" else " or "
    left = router.gast_to_code(gast["left"], "py")
    right = router.gast_to_code(gast["right"], "py")
    return left + op + right

def gast_to_py_unary_op(gast):
    return "not " + router.gast_to_code(gast["arg"], "py")

def gast_to_py_bool(gast):
    if gast["value"] == 1:
        return "True"
    else:
        return "False"

def gast_to_py_if(gast, lvl=0):
    test = router.gast_to_code(gast["test"], "py")
    body_indent = "\n\t" + "\t"*lvl
    body = general_helpers.list_helper(gast["body"], "py", body_indent, lvl+1)

    out = 'if (' + test + '):' + body_indent + body

    # orelse can either be empty, or be an elif or be an else
    if len(gast["orelse"]) == 0:
        pass
    elif gast["orelse"][0]["type"] == "if":
        out += "\nel" + router.gast_to_code(gast["orelse"], "py", lvl)
    else:
        out += "\nelse:\n\t" + general_helpers.list_helper(gast["orelse"], "py", "\n\t", lvl)

    return out

def gast_to_py_func_declarations(gast, lvl=0):
    name = router.gast_to_code(gast["id"], "py")
    args = router.gast_to_code(gast["params"], "py")
    body = general_helpers.list_helper(gast["body"], "py", "\n\t")
    out = "def " + name
    out += "(" + args + "):\n\t"

    out += body

    return out


def gast_to_py_return_statement(gast):
    return "return " + router.gast_to_code(gast["value"], "py")

def gast_to_py_assign_pattern(gast):
    return router.gast_to_code(gast["left"], "py") + " = " + router.gast_to_code(gast["right"], "py")

def gast_to_py_while(gast, lvl=0):
    test = router.gast_to_code(gast["test"], "py")
    body = general_helpers.list_helper(gast["body"], "py", "\n\t")

    out = 'while (' + test + '):\n\t' + body
    return out

def gast_to_py_forRange(gast, lvl=0):
    # start value
    start_value = gast["init"]["varValue"]["value"]
    start = str(start_value)

    # incrementor
    incrementor_value = gast["update"]["right"]["value"]
    incrementor_op = gast["update"]["op"] 
    if incrementor_op == "-=":
        incrementor = "-" + str(incrementor_value)
    elif incrementor_op == "+=":
        incrementor = str(incrementor_value)
    else:
        incrementor = "unsupported update operation" # TODO: rethink this error message

    # end value
    end_value = gast["test"]["right"]["value"]
    end_comparator = gast["test"]["op"]
    if end_comparator == "<=":
        end_value += incrementor_value
    elif end_comparator == ">=":
        end_value -= incrementor_value
    end = str(end_value)

    var_name = gast["init"]["varId"]["value"]
    range_str = "range (" + start + ", " + end + ", " + incrementor + ")"
    body = general_helpers.list_helper(gast["body"], "py", "\n\t")
    out = "for " + var_name + " in " + range_str + ":\n\t" + body
    return out

def gast_to_py_forOf(gast, lvl=0):
    arr_str = router.gast_to_code(gast["iter"], "py")
    var_name = gast["init"]["value"]

    body_indent = "\n\t" + "\t"*lvl
    body = general_helpers.list_helper(gast["body"], "py", body_indent, lvl+1)

    out = "for " + var_name + " in " + arr_str + ":" + body_indent + body
    return out

  
def gast_to_py_subscript(gast):
    return router.gast_to_code(gast["value"], "py") + "[" + router.gast_to_code(gast["index"], "py") + "]"

