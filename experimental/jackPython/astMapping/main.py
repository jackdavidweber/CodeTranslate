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
    
"""
takes pyton file and converts it to a node
node is then dealt with by node_to_gast 
"""
def py_to_gast(python_input_filename):
    input_ast =  astor.code_to_ast.parse_file(python_input_filename)
    print(astor.dump_tree(input_ast))
    return node_to_gast(input_ast)

def module(node):
    gast = {"type": "root"}
    gast["body"] = node_to_gast(node.body)
    return gast

"""
takes a node that represents a list of nodes.
returns a list of gast
"""
def node_list(node):
    gast_list = []
    for i in range(0, len(node)):
        gast_list.append(node_to_gast(node[i]))
    
    return gast_list

"""
Takes python expressions and converts them to the generic
ast format
"""
def expr(node):
    return node_to_gast(node.value)

def call(node):
    gast = {}
    gast["type"] = node_to_gast(node.func)
    gast["args"] = node_to_gast(node.args)
    return gast

"""
takes python ast assigns and converts them to generic ast format
note, that this assumes only a single assignment (i.e. x = 4)
for now, it does not work for things link x,y = 4,5
"""
def assign(node):
    gast = {}
    gast["type"] = "varAssign"
    gast["varId"] = node_to_gast(node.targets[0]) # FIXME: understand when targets won't be 0
    gast["varValue"] = node_to_gast(node.value)
    return gast

def name(node):
    if node.id == "print":
        return "logStatement"
    else:
        return "customStatement"
                

def node_to_gast(node):
    # Base Cases
    if type(node) == ast.Str:
        return node.s
    elif type(node) == ast.Num:
        return node.n

    # Base Cases with embedded recursion / if statements
    elif type(node) == ast.BinOp: #FIXME: I treat this as a base case even though there are if statements inside.
        return binOp_to_str(node)
    elif type(node) == ast.Name:
        return name(node)

    # List of Nodes to list of gast
    elif type(node) == list:
        return node_list(node)

    # Other
    elif type(node) == ast.Module:
        return module(node)

    elif type(node) == ast.Expr:
        return expr(node)
    elif type(node) == ast.Assign:
        return assign(node)
    elif type(node) == ast.Call:
        return call(node)
    else:
        print("nothing hit")
        return "nothing hit"

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
        print(ds[node["type"]][outputLanguage])


#TODO: replace the mapping for each one with a function that returns the correct output string WITH arguments
ds = {
    "logStatement": {
        "py": "print()",
        "js": "console.log()"
    },
    "customStatement": {
        "py": "custom_function_name()",
        "js": "customFunctionName()"
    },
    "varAssign": {
        "py": "varName = assignment",
        "js": "const varName = assignment"
    }
}

fileName = "/home/jackweber/cjs_capstone/experimental/jackPython/sampleCode.py"
translator(fileName, ds, 'py', 'js')