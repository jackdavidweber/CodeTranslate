
# general_helpers
def value_to_str(val):
    if type(val) == str:
        return '"' + val + '"'
    else:
        return str(val)

"""
Helper for lists of gast
Default is to put comma and space btwn each stringified gast
    i.e. list_helper({str_gast}, {str_gast}, out_lang) --> str, str
Can specify different btwn string with third parameter
    i.e. list_helper({str_gast}, {str_gast}, out_lang, "**") --> str**str
"""
def list_helper(gast_list, out_lang, btwn_str = ", "):
    out = ""
    for gast in gast_list:
        out += gast_router(gast, out_lang)
        out += btwn_str
    
    num_btwn_chars = len(btwn_str)
    return out[:-num_btwn_chars] # remove \nS
        

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
    if gast["type"] == "arr":
        return gast_router(gast["elts"], out_lang)
    if gast["type"] == "str":
        return '"' + gast["value"] + '"'
    if gast["type"] == "bool":
        return out["bool"][out_lang](gast)

    # commonly used

    #Other
    if gast["type"] == "root":
        return list_helper(gast["body"], out_lang, "\n")
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
                        },
                        {
                            "type": "num",
                            "value": 5
                        }
                    ]
                }
            ]
        }

new_gast_log_assign = {
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
        },
        {
            "type": "logStatement",
            "args": [
                {
                    "type": "str",
                    "value": "hello world"
                },
                {
                    "type": "num",
                    "value": 5
                }
            ]
        }
		]
}

new_gast_arr = {
	"type": "arr",
	"elts": 
		[
            {
                "type": "str",
                "value": "hello"
            },
            {
                "type": "arr",
                "elts":
                    [
                        {
                            "type": "num",
                            "value": 1
                        },
                        {
                            "type": "num",
                            "value": 2
                        }
                    ]
            }
		]
}


print(gast_router(new_gast_log_assign, "py"))
# print(gast_router(new_gast_arr, "js"))
