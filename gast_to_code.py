
# general_helpers
def value_to_str(val):
    if type(val) == str:
        return '"' + val + '"'
    else:
        return str(val)

def list_helper(gast_list, out_lang):
    out = ""
    for gast in gast_list:
        out += gast_router(gast, out_lang)
        out += "\n"
    
    return out[:-1] # remove \nS


        

def list_to_csv_str(l):
    s = ""
    for i in l:
        if type(i) == str:
            i = '"' + i + '"'
        s += str(i) + ", "
    
    return s[:-2] # remove last comma and space

# py_specific_helpers
def py_logStatement(gast):
    arg_string = list_to_csv_str(gast["args"])
    return "print(" + arg_string + ")"

def py_varAssign(gast):
    value = value_to_str(gast["varValue"])
    return gast["varId"] + " = " + value

# js_specific_helpers
def js_logStatement(gast):
    arg_string = list_to_csv_str(gast["args"])
    return "console.log(" + arg_string + ")"

def js_varAssign(gast):
    value = value_to_str(gast["varValue"])
    return "const " + gast["varId"] + " = " + value

def py_bool(gast):
    if gast["value"] == 1:
        return "True"
    else:
        return "False"

def js_bool(gast):
    if gast["value"] == 1:
        return "true"
    else:
        return "false"


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
    # Primitives
    if gast["type"] == "num":
        return str(gast["value"])
    if gast["type"] == "str":
        return '"' + gast["value"] + '"'
    if gast["type"] == "bool":
        return out["bool"][out_lang](gast)

    #Other
    if gast["type"] == "root":
        return list_helper(gast["body"], out_lang)
    elif gast["type"] == "logStatement":
        return out["logStatement"][out_lang](gast)

    elif gast["type"] == "varAssign":
        return out["varAssign"][out_lang](gast)

old_gast = {
            "type": "root",
            "body": [
                {
                    "type": "logStatement",
                    "args": ["hello world"]
                }
            ]   
        }

new_gast = {
            "type": "root",
            "body": [
                {
                    "type": "logStatement",
                    "args": [
                        {
                            "type": "str",
                            "value": "hello world"
                        }
                    ]
                }
            ]
        }


print(gast_router(old_gast, "py"))
