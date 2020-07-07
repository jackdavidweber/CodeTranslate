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

def gast_to_py_dict(gast):
    return "{" + gast_to_code(gast["elements"], "py") + "}"

def gast_to_js_dict(gast):
    return "{" + gast_to_code(gast["elements"], "js") + "}"

def gast_to_py_property(gast):
    return gast_to_code(gast["key"], "py") + ": " + gast_to_code(gast["value"], "py")

def gast_to_js_property(gast):
    return gast_to_code(gast["key"], "js") + ": " + gast_to_code(gast["value"], "js")

# assign helpers
def gast_to_py_var_assign(gast):
    value = gast_to_code(gast["varValue"], "py")
    return gast_to_code(gast["varId"], "py") + " = " + value

def gast_to_js_var_assign(gast):
    kind = gast["kind"]
    varId = gast_to_code(gast["varId"], "js")
    varValue = gast_to_code(gast["varValue"], "js")
    return kind + " " + varId + " = " + varValue

def gast_to_py_aug_assign(gast):
    return gast_to_code(gast["left"], "py") + " " + gast["op"] + " " + gast_to_code(gast["right"], "py")

def gast_to_js_aug_assign(gast):
    return gast_to_code(gast["left"], "js") + " " + gast["op"] + " " + gast_to_code(gast["right"], "js")

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

def gast_to_js_func_declarations(gast):
    name = gast_to_code(gast["id"], "js")
    args = gast_to_code(gast["params"], "js")
    body = list_helper(gast["body"], "js", "\n\t")
    out = "function " + name
    out += "(" + args + ") {\n\t"

    out += body

    out += "\n}"
    return out

def gast_to_py_func_declarations(gast):
    name = gast_to_code(gast["id"], "py")
    args = gast_to_code(gast["params"], "py")
    body = list_helper(gast["body"], "py", "\n\t")
    out = "def " + name
    out += "(" + args + "):\n\t"

    out += body

    return out

def gast_to_py_return_statement(gast):
    return "return " + gast_to_code(gast["value"], "py")

def gast_to_js_return_statement(gast):
    return "return " + gast_to_code(gast["value"], "js")

def gast_to_py_assign_pattern(gast):
    return gast_to_code(gast["left"], "py") + " = " + gast_to_code(gast["right"], "py")

def gast_to_js_assign_pattern(gast):
    return gast_to_code(gast["left"], "js") + " = " + gast_to_code(gast["right"], "js")

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

def gast_to_py_forRange(gast):
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

    range_str = "range (" + start + ", " + end + ", " + incrementor + ")"

    return gast_to_py_for_helper(gast, range_str)

def gast_to_py_forOf(gast):
    arr_str = gast_to_code(gast["iter"], "py")
    
    return gast_to_py_for_helper(gast, arr_str)


def gast_to_py_for_helper(gast, in_str):
    var_name = gast["init"]["varId"]["value"]
    body = list_helper(gast["body"], "py", "\n\t")

    out = "for " + var_name + " in " + in_str + ":\n\t" + body

    return out


def gast_to_js_forRange(gast):
    loop_init = gast_to_code(gast["init"], "js")
    loop_test = gast_to_code(gast["test"], "js")
    loop_update = gast_to_code(gast["update"], "js")
    body = list_helper(gast["body"], "js", "\n\t")

    return "for (" + loop_init + "; " + loop_test + "; " + loop_update + ") {\n\t" + body + "\n}"


out = {
    "logStatement": {
        "py": "print",
        "js": "console.log"
    },
    "varAssign": {
        "py": gast_to_py_var_assign,
        "js": gast_to_js_var_assign,
    },
    "augAssign": {
        "py": gast_to_py_aug_assign,
        "js": gast_to_js_aug_assign
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
    },
    "functionDeclaration": {
        "py": gast_to_py_func_declarations,
        "js": gast_to_js_func_declarations
    },
    "returnStatement": {
        "py": gast_to_py_return_statement,
        "js": gast_to_js_return_statement
    },
    "assignPattern": {
        "py": gast_to_py_assign_pattern,
        "js": gast_to_js_assign_pattern
    },
    "whileStatement": {
        "py": gast_to_py_while,
        "js": gast_to_js_while
    },
    "forRangeStatement": {
        "py": gast_to_py_forRange,
        "js": gast_to_js_forRange
    },
    "dict": {
        "py": gast_to_py_dict,
        "js": gast_to_js_dict
    },
    "property": {
        "py": gast_to_py_property,
        "js": gast_to_js_property
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
        return "[" + gast_to_code(gast["elements"], out_lang) + "]"
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
        return out["whileStatement"][out_lang](gast)
    elif gast["type"] == "forRangeStatement":
        return out["forRangeStatement"][out_lang](gast)

    # Other
    elif gast["type"] == "root":
        return list_helper(gast["body"], out_lang, "\n")
    elif gast["type"] == "break":
        return "break"
    elif gast["type"] == "continue":
        return "continue"
    elif gast["type"] == "logStatement":
        return out["logStatement"][out_lang]
    elif gast["type"] == "varAssign":
        return out["varAssign"][out_lang](gast)
    elif gast["type"] == "augAssign":
        return out["augAssign"][out_lang](gast)
    
    elif gast["type"] == "funcCall":
        return out["funcCall"][out_lang](gast)
    elif gast["type"] == "name":
        return gast["value"]
    elif gast["type"] == "attribute":
        return out["attribute"][out_lang](gast)

    elif gast["type"] == "dict":
        return out["dict"][out_lang](gast)
    elif gast["type"] == "property":
        return out["property"][out_lang](gast)

    elif gast["type"] == "binOp":
        return gast_to_node_bin_op_helper(gast, out_lang)
    elif gast["type"] == "boolOp":
        return out["boolOp"][out_lang](gast)
    elif gast["type"] == "unaryOp":
        return out["unaryOp"][out_lang](gast)
    elif gast["type"] == "functionDeclaration":
        return out["functionDeclaration"][out_lang](gast)
    elif gast["type"] == "returnStatement":
        return out["returnStatement"][out_lang](gast)
    elif gast["type"] == "assignPattern":
        return out["assignPattern"][out_lang](gast) 
    elif gast["type"] == "error":
        if gast["value"] == "unsupported":
            # Error string
            return "Feature not supported"
        return "Error"


input_gast = {
    "type": "forRangeStatement",
    "init": 
    {
        "type": "varAssign",
        "kind": "let",
        "varId":
        {
            "type": "name",
            "value": "i"
        },
        "varValue":
        {
            "type": "num",
            "value": 0
        }

    },
    "test": 
    {
        "type": "binOp",
        "left": 
        {
            "type": "name",
            "value": "i"
        },
        "op": "<",
        "right": 
        {
            "type": "num",
            "value": 10
        }
    },
    "update": 
    {
        "type": "augAssign",
        "left":
        {
            "type": "name",
            "value": "i"
        },
        "op": "+=",
        "right": 
        {
            "type": "num",
            "value": 2
        }
    },
    "body": 
    [
        {
            "type": "num",
            "value": 5
        }
    ]
}

print(gast_to_code(input_gast, "js"))
