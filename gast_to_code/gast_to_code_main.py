"""
Helper for lists of gast
Default is to put comma and space btwn each stringified gast
    i.e. list_helper({str_gast}, {str_gast}, out_lang) --> str, str
Can specify different btwn string with third parameter
    i.e. list_helper({str_gast}, {str_gast}, out_lang, "**") --> str**str
"""
def list_helper(gast_list, out_lang, csv_delimiter = ", "):
    out = ""
    for i in range (0, len(gast_list)):
        out += gast_to_code(gast_list[i], out_lang)

        if i< len(gast_list) - 1 : # don't add delimiter for last item
            out += csv_delimiter
    
    return out

# assign helpers
def gast_to_py_var_assign(gast):
    value = gast_to_code(gast["varValue"], "py")
    return gast_to_code(gast["varId"], "py") + " = " + value

def gast_to_js_var_assign(gast):
    kind = gast["kind"]
    varId = gast_to_code(gast["varId"], "js")
    varValue = gast_to_code(gast["varValue"], "js")
    return kind + " " + varId + " = " + varValue


# expression helpers
def gast_to_py_functions(gast):
    return gast_to_code(gast["value"], "py") + "(" + gast_to_code(gast["args"], "py") + ")"

def gast_to_js_functions(gast):
    return gast_to_code(gast["value"], "js") + "(" + gast_to_code(gast["args"], "js") + ")"

def gast_to_py_attribute(gast):
    return gast_to_code(gast["value"], "py") + "." + gast["id"] 

def gast_to_js_attribute(gast):
    return gast_to_code(gast["value"], "js") + "." + gast["id"] 


# Operation helpers
def gast_to_node_bin_op_helper(gast, out_lang):
    op = " " + str(gast["op"]) + " "
    left = gast_to_code(gast["left"], out_lang)
    right = gast_to_code(gast["right"], out_lang)
    return left + op + right

def gast_to_py_bool_op(gast):
    op = " and " if gast["op"] == "&&" else " or "
    left = gast_to_code(gast["left"], "py")
    right = gast_to_code(gast["right"], "py")
    return left + op + right

def gast_to_js_bool_op(gast):
    return gast_to_node_bin_op_helper(gast, "js")

def gast_to_py_unary_op(gast):
    return "not " + gast_to_code(gast["arg"], "py")

def gast_to_js_unary_op(gast):
    return "!" + gast_to_code(gast["arg"], "js")


# Boolean helpers
def gast_to_py_bool(gast):
    if gast["value"] == 1:
        return "True"
    else:
        return "False"

def gast_to_js_bool(gast):
    if gast["value"] == 1:
        return "true"
    else:
        return "false"


# Conditional helpers
def gast_to_py_if(gast):
    test = gast_to_code(gast["test"], "py")
    body = list_helper(gast["body"], "py", "\n\t") # FIXME: this probably will not work for double nesting

    out = 'if (' + test + '):\n\t' + body

    # orelse can either be empty, or be an elif or be an else
    if len(gast["orelse"]) == 0:
        pass
    elif gast["orelse"][0]["type"] == "if":
        out += "\nel" + gast_to_code(gast["orelse"], "py")
    else:
        out += "\nelse:\n\t" + list_helper(gast["orelse"], "py", "\n\t")

    return out

def gast_to_js_if(gast):
    test = gast_to_code(gast["test"], "js")
    body = list_helper(gast["body"], "js", "\n\t") # FIXME: this probably will not work for double nesting

    out = 'if (' + test + ') {\n\t' + body + "\n}"

    # orelse can either be empty, or be an elif or be an else
    if len(gast["orelse"]) == 0:
        pass
    elif gast["orelse"][0]["type"] == "if":
        out += " else " + gast_to_code(gast["orelse"], "js")
    else:
        out += " else {\n\t" + list_helper(gast["orelse"], "js", "\n\t") + "\n}"

    return out

# FIXME: may be a way to write helper functions that can be used btwn while and if
def gast_to_py_while(gast):
    test = gast_to_code(gast["test"], "py")
    body = list_helper(gast["body"], "py", "\n\t")

    out = 'while (' + test + '):\n\t' + body
    return out

def gast_to_js_while(gast):
    test = gast_to_code(gast["test"], "js")
    body = list_helper(gast["body"], "js", "\n\t")
    
    out = 'while (' + test + ') {\n\t' + body + "\n}"
    return out

out = {
    "logStatement": {
        "py": "print",
        "js": "console.log"
    },
    "varAssign": {
        "py": gast_to_py_var_assign,
        "js": gast_to_js_var_assign,
    },
    "bool": {
        "py": gast_to_py_bool,
        "js": gast_to_js_bool,
    },
    "if": {
        "py": gast_to_py_if,
        "js": gast_to_js_if
    },
    "funcCall": {
        "py": gast_to_py_functions,
        "js": gast_to_js_functions
    },
    "attribute": {
        "py": gast_to_py_attribute,
        "js": gast_to_js_attribute
    },
    "boolOp": {
        "py": gast_to_py_bool_op,
        "js": gast_to_js_bool_op
    },
    "none": {
        "py": "None",
        "js": "null" # TODO look at undefined in JS 
    },
    "unaryOp": {
        "py": gast_to_py_unary_op,
        "js": gast_to_js_unary_op
    }
    "whileStatement": {
        "py": gast_to_py_while,
        "js": gast_to_js_while
    }
}

"""
gast router that takes generic ast and the output language
that the gast needs to be converted to and executes the
conversion recursively
out_lang correspond to the language codes defined in datastructure:
javascript: js
python: py
"""
def gast_to_code(gast, out_lang):
    if type(gast) == list:
        return list_helper(gast, out_lang)

    # Primitives
    elif gast["type"] == "num":
        return str(gast["value"])
    elif gast["type"] == "arr":
        return "[" + gast_to_code(gast["elts"], out_lang) + "]" # TODO: replace acronym elts with elements
    elif gast["type"] == "str":
        return '"' + gast["value"] + '"'
    elif gast["type"] == "bool":
        return out["bool"][out_lang](gast)
    elif gast["type"] == "if":
        return out["if"][out_lang](gast)
    elif gast["type"] == "none":
        return out["none"][out_lang]

    # Loops
    elif gast["type"] == "whileStatement":
        return out["whileStatement"](out_lang)

    # Other
    elif gast["type"] == "root":
        return list_helper(gast["body"], out_lang, "\n")
    elif gast["type"] == "logStatement":
        return out["logStatement"][out_lang]
    elif gast["type"] == "varAssign":
        return out["varAssign"][out_lang](gast)
    
    elif gast["type"] == "funcCall":
        return out["funcCall"][out_lang](gast)
    elif gast["type"] == "name":
        return gast["value"]
    elif gast["type"] == "attribute":
        return out["attribute"][out_lang](gast)

    elif gast["type"] == "binOp":
        return gast_to_node_bin_op_helper(gast, out_lang)
    elif gast["type"] == "boolOp":
        return out["boolOp"][out_lang](gast)
    elif gast["type"] == "unaryOp":
        return out["unaryOp"][out_lang](gast)
    elif gast["type"] == "error":
        if gast["value"] == "unsupported":
            # Error string
            return "Feature not supported"
        return "Error"