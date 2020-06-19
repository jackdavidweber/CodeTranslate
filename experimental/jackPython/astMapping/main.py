import ast
import astor

"""
converts python ast operations to common string representation
TODO: add in boolean logic
"""
def pyop_to_str(op):
    if type(op) == ast.Add:
        return "+"
    elif type(op) == ast.Mult:
        return "*"
    elif type(op) == ast.Div:
        return "/"
    elif type(op) == ast.Sub:
        return "-"

"""
converts a python ast BinOp and converts it to a readable string recursively 
"""
def binOp_to_str(bop):
    if type(bop.left) == ast.BinOp:
        s = binOp_to_str(bop.left) + pyop_to_str(bop.op) + str(bop.right.n)
    else:
        # base case: if left is just a number, operate on left wrt right
        s = str(bop.left.n) + pyop_to_str(bop.op) + str(bop.right.n)
    return s
    

def pyarg_to_str(arg):
    if type(arg) == ast.Str:
        return arg.s
    elif type(arg) == ast.Num:
        return arg.n
    elif type(arg) == ast.BinOp:
        return binOp_to_str(arg)
    else:
        return ""



"""
takes list of arguments in python ast and converts them to a list of
strings
"""
def pyargs_to_strlist(args):
    out = []
    for arg in args:
        out.append(pyarg_to_str(arg))
            
    return out

"""
Takes python expressions and converts them to the generic
ast format
"""
def pyexpr_to_gast(node):
    gast = {}
    if type(node.value) == ast.Call: # FIXME: should type of call be embedded in the gast?
        if type(node.value.func) == ast.Name:
            if node.value.func.id == "print":
                gast["type"] = "logStatement"
            else:
                gast["type"] = "customStatement"
            
            # add arguments and return
            gast["args"] =  pyargs_to_strlist(node.value.args)
            return gast

def pyassign_to_gast(node):
    pass


def py_to_gast(python_input_filename):
    input_ast =  astor.code_to_ast.parse_file(python_input_filename)
    print(astor.dump_tree(input_ast))
    # TODO: can add more fields to the generic ast
    gast = {"type": "root", "body": []}

    # NOTE: with current implementation, it will just go until it sees something it recognizes
    # eventually can implement nested structures
    for node in input_ast.body:
        if type(node) == ast.Expr:
            gast["body"].append(pyexpr_to_gast(node))
        if type(node) == ast.Assign:
            gast["body"].append(pyassign_to_gast(node))
    
    return gast

"""
Function for translating between input and output language.
inputLanguage and outputLanguage must be specified using two character codes
javascript: js
python: py
"""
def translator(input_filename, ds, inputLanguage, outputLanguage):
    if(inputLanguage == 'py'):
        gast = py_to_gast(input_filename)
        print(gast)
    elif(inputLanguage == 'js'):
        return 
    else:
        return

    for node in gast["body"]:
        print(astToJsMap[node["type"]][outputLanguage])

astToJsMap = {
    "logStatement": {
        "py": "print()",
        "js": "console.log()"
    },
    "customStatement": {
        "py": "custom_function_name()",
        "js": "customFunctionName()"
    },
}

ds = [
    {
        'gast': {'type': 'callexpr', 'id': 'custom'},
        'js': 'console.log()',
        'py': 'print()'
    },
    {'type': 'logStatement', 'args': "" }
]

fileName = "/home/jackweber/cjs_capstone/experimental/jackPython/sampleCode.py"
translator(fileName, ds, 'py', 'js')