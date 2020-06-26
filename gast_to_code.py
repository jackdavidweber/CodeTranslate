
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
    arg_string = gast_router(gast["args"],"py")
    return "print(" + arg_string + ")"

def py_varAssign(gast):
    value = gast_router(gast["varValue"], "py")
    return gast["varId"] + " = " + value

# js_specific_helpers
def js_logStatement(gast):
    arg_string = gast_router(gast["args"],"py")
    return "console.log(" + arg_string + ")"

def js_varAssign(gast):
    kind = gast["kind"]
    varId = gast["varId"]
    varValue = gast_router(gast["varValue"], "js")
    
    return kind + " " + varId + " = " + varValue

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
    if type(gast) == list:
        return list_helper(gast, out_lang)

    # Primitives
    if gast["type"] == "num":
        return str(gast["value"])
    if gast["type"] == "str":
        return '"' + gast["value"] + '"'
    if gast["type"] == "bool":
        return out["bool"][out_lang](gast)

    # commonly used

    #Other
    if gast["type"] == "root":
        return gast_router(gast["body"], out_lang)
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

new_gast_log = {
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

new_gast_assign = {
	"type": "root",
	"body": [
		{
			"type": "varAssign",
			"kind": "let",
			"varId": "x",
            "varValue": 
                {
                    "type": "num",
                    "value": 5
                }
        }
		]
}



print(gast_router(new_gast_log, "js"))
