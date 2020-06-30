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
        out += gast_router(gast_list[i], out_lang)

        if i< len(gast_list) - 1 : # don't add delimiter for last item
            out += csv_delimiter
    
    return out
        

def binOp_helper(gast, out_lang):
    op = " " + str(gast["op"]) + " "
    left = gast_router(gast["left"], out_lang)
    right = gast_router(gast["right"], out_lang)

    return left + op + right

# py_specific_helpers
def py_logStatement(gast):
    arg_string = gast_router(gast["args"],"py")
    return "print(" + arg_string + ")"

def py_varAssign(gast):
    value = gast_router(gast["varValue"], "py")
    return gast["varId"] + " = " + value

def py_bool(gast):
    if gast["value"] == 1:
        return "True"
    else:
        return "False"

def py_boolOp(gast):
    op = " and " if gast["op"] == "&&" else " or "
    left = gast_router(gast["left"], "py")
    right = gast_router(gast["right"], "py")

    return left + op + right

# js_specific_helpers
def js_logStatement(gast):
    arg_string = gast_router(gast["args"],"js")
    return "console.log(" + arg_string + ")"

def js_varAssign(gast):
    kind = gast["kind"]
    varId = gast["varId"]
    varValue = gast_router(gast["varValue"], "js")
    
    return kind + " " + varId + " = " + varValue

def js_bool(gast):
    if gast["value"] == 1:
        return "true"
    else:
        return "false"

def js_boolOp(gast):
    return binOp_helper(gast, "js")

out = {
    "logStatement": {
        "py": py_logStatement,
        "js": js_logStatement
    },
    "varAssign": {
        "py": py_varAssign,
        "js": js_varAssign,
    },
    "bool": {
        "py": py_bool,
        "js": js_bool,
    },
    "boolOp": {
        "py": py_boolOp,
        "js": js_boolOp
    "none": {
        "py": "None",
        "js": "null" # TODO look at undefined in JS 
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
def gast_router(gast, out_lang):
    if type(gast) == list:
        return list_helper(gast, out_lang)

    # Primitives
    elif gast["type"] == "num":
        return str(gast["value"])
    elif gast["type"] == "arr":
        return "[" + gast_router(gast["elts"], out_lang) + "]" # TODO: replace acronym elts with elements
    elif gast["type"] == "str":
        return '"' + gast["value"] + '"'
    elif gast["type"] == "bool":
        return out["bool"][out_lang](gast)
    elif gast["type"] == "none":
        return out["none"][out_lang]

    #Other
    elif gast["type"] == "root":
        return list_helper(gast["body"], out_lang, "\n")
    elif gast["type"] == "logStatement":
        return out["logStatement"][out_lang](gast)
    elif gast["type"] == "varAssign":
        return out["varAssign"][out_lang](gast)
    elif gast["type"] == "binOp":
        return binOp_helper(gast, out_lang)
    elif gast["type"] == "boolOp":
        return out["boolOp"][out_lang](gast)

