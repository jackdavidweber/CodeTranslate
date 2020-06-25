
# general_helpers
def value_to_str(val, out_lang):
    print(type(val))
    if type(val) == str:
        return '"' + val + '"'
    elif type(val) == bool: 
        if out_lang == 'js':
            return 'true' if val else 'false'
        elif out_lang == 'py':
            return str(val)
    else:
        return str(val)

def body(gast_list, out_lang):
    out = ""
    for gast in gast_list:
        out += gast_router(gast, out_lang)
        out += "\n"

    return out[:-1] # remove \nS

def list_to_csv_str(l, out_lang):
    s = ""
    for i in l:
        s += value_to_str(i, out_lang) + ", "
    
    return s[:-2] # remove last comma and space

# py_specific_helpers
def py_logStatement(gast, out_lang):
    arg_string = list_to_csv_str(gast["args"], out_lang)
    return "print(" + arg_string + ")"

def py_varAssign(gast, out_lang):
    value = value_to_str(gast["varValue"], out_lang)
    return gast["varId"] + " = " + value

# js_specific_helpers
def js_logStatement(gast, out_lang):
    arg_string = list_to_csv_str(gast["args"], out_lang)
    return "console.log(" + arg_string + ")"

def js_varAssign(gast, out_lang):
    value = value_to_str(gast["varValue"], out_lang)
    return "const " + gast["varId"] + " = " + value

out = {
    "logStatement": {
        "py": py_logStatement,
        "js": js_logStatement
    },
    "varAssign": {
        "py": py_varAssign,
        "js": js_varAssign,
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
    if gast["type"] == "root":
        return body(gast["body"], out_lang)

    elif gast["type"] == "logStatement":
        return out["logStatement"][out_lang](gast, out_lang)

    elif gast["type"] == "varAssign":
        return out["varAssign"][out_lang](gast, out_lang)

print(gast_router({'type': 'root', 'body': [{'type': 'varAssign', 'varId': 'x', 'varValue': True}]}, 'py'))