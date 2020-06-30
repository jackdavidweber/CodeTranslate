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
        out += gast_to_node_router(gast_list[i], out_lang)

        if i< len(gast_list) - 1 : # don't add delimiter for last item
            out += csv_delimiter
    
    return out
        
def gast_to_py_varAssign(gast):
    value = gast_to_node_router(gast["varValue"], "py")
    return gast_to_node_router(gast["varId"], "py") + " = " + value

def gast_to_node_binOp_helper(gast, out_lang):
    op = " " + str(gast["op"]) + " "
    left = gast_to_node_router(gast["left"], out_lang)
    right = gast_to_node_router(gast["right"], out_lang)

    return left + op + right

# py_specific_helpers
def gast_to_py_logStatement(gast):
    arg_string = gast_to_node_router(gast["args"],"py")
    return "print(" + arg_string + ")"

def gast_to_py_bool(gast):
    if gast["value"] == 1:
        return "True"
    else:
        return "False"

def gast_to_py_boolOp(gast):
    op = " and " if gast["op"] == "&&" else " or "
    left = gast_to_node_router(gast["left"], "py")
    right = gast_to_node_router(gast["right"], "py")

    return left + op + right

# js_specific_helpers
def gast_to_js_logStatement(gast):
    arg_string = gast_to_node_router(gast["args"],"js")
    return "console.log(" + arg_string + ")"

def gast_to_js_varAssign(gast):
    kind = gast["kind"]
    varId = gast_to_node_router(gast["varId"], "js")
    varValue = gast_to_node_router(gast["varValue"], "js")
    return kind + " " + varId + " = " + varValue

def gast_to_py_functions(gast):
    return gast_to_node_router(gast["value"], "py") + "(" + gast_to_node_router(gast["args"], "py") + ")"

def gast_to_js_functions(gast):
    return gast_to_node_router(gast["value"], "js") + "(" + gast_to_node_router(gast["args"], "js") + ")"

def gast_to_py_attribute(gast):
    return gast_to_node_router(gast["value"], "py") + "." + gast["id"] 

def gast_to_js_attribute(gast):
    return gast_to_node_router(gast["value"], "js") + "." + gast["id"] 

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

def gast_to_py_if(gast):
    test = gast_to_node_router(gast["test"], "py")
    body = list_helper(gast["body"], "py", "\n\t") # FIXME: this probably will not work for double nesting

    out = 'if (' + test + '):\n\t' + body

    # orelse can either be empty, or be an elif or be an else
    if len(gast["orelse"]) == 0:
        pass
    elif gast["orelse"][0]["type"] == "if":
        out += "\nel" + gast_to_node_router(gast["orelse"], "py")
    else:
        out += "\nelse:\n\t" + list_helper(gast["orelse"], "py", "\n\t")

    return out

def gast_to_js_if(gast):
    test = gast_to_node_router(gast["test"], "js")
    body = list_helper(gast["body"], "js", "\n\t") # FIXME: this probably will not work for double nesting

    out = 'if (' + test + ') {\n\t' + body + "\n}"

    # orelse can either be empty, or be an elif or be an else
    if len(gast["orelse"]) == 0:
        pass
    elif gast["orelse"][0]["type"] == "if":
        out += " else " + gast_to_node_router(gast["orelse"], "js")
    else:
        out += " else {\n\t" + list_helper(gast["orelse"], "js", "\n\t") + "\n}"

    return out

  
def gast_to_js_boolOp(gast):
    return binOp_helper(gast, "js")

def gast_to_py_unaryOp(gast):
    return "not " + gast_to_node_router(gast["arg"], "py")

def gast_to_js_unaryOp(gast):
    return "!" + gast_to_node_router(gast["arg"], "js")

out = {
    "logStatement": {
        "py": "print",
        "js": "console.log"
    },
    "varAssign": {
        "py": gast_to_py_varAssign,
        "js": gast_to_js_varAssign,
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
        "py": gast_to_py_boolOp,
        "js": gast_to_js_boolOp
    },
    "none": {
        "py": "None",
        "js": "null" # TODO look at undefined in JS 
    },
    "unaryOp": {
        "py": gast_to_py_unaryOp,
        "js": gast_to_js_unaryOp
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
def gast_to_node_router(gast, out_lang):
    if type(gast) == list:
        return list_helper(gast, out_lang)

    # Primitives
    elif gast["type"] == "num":
        return str(gast["value"])
    elif gast["type"] == "arr":
        return "[" + gast_to_node_router(gast["elts"], out_lang) + "]" # TODO: replace acronym elts with elements
    elif gast["type"] == "str":
        return '"' + gast["value"] + '"'
    elif gast["type"] == "bool":
        return out["bool"][out_lang](gast)
    elif gast["type"] == "if":
        return out["if"][out_lang](gast)
    elif gast["type"] == "none":
        return out["none"][out_lang]

    #Other
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
        return gast_to_node_binOp_helper(gast, out_lang)
    elif gast["type"] == "boolOp":
        return out["boolOp"][out_lang](gast)
    elif gast["type"] == "unaryOp":
        return out["unaryOp"][out_lang](gast)