

def list_to_csv_str(l):
    s = ""
    for i in l: 
        s += str(i) + ", " # FIXME: consider using join instead
    
    return s[:-2] # remove last comma and space


def logStatement(gast):
    arg_string = list_to_csv_str(gast["args"])
    return "console.log(" + arg_string + ")"


def value_to_str(val):
    if type(val) == str:
        return '"' + val + '"'
    else:
        return str(val)


def varAssign(gast):
    value = value_to_str(gast["varValue"])
    
    return "const " + gast["varId"] + " = " + value # TODO: rethink const


def body(gast_list):
    out = ""
    for gast in gast_list:
        out += gast_router(gast)
        out += "\n"

    return out[:-1] # remove \nS


def gast_router(gast):
    if gast["type"] == "root":
        return body(gast["body"])

    elif gast["type"] == "logStatement":
        return logStatement(gast)

    elif gast["type"] == "varAssign":
        return varAssign(gast)
    


gast =  {
            "type": "root",
            "body": [
                {
                    "type": "logStatement",
                    "args": ["hello world", "hi", 3]
                },
                {
                    "type": "varAssign",
                    "varId": "x",
                    "varValue": 5
                }
            ]   
        }


print(gast_router(gast))
