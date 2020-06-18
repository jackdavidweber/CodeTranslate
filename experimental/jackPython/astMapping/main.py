import ast
import astor

def pyexpr_to_gast(node):
    gast = {}
    if type(node.value) == ast.Call: # FIXME: should type of call be embedded in the gast?
        if type(node.value.func) == ast.Name:
            if node.value.func.id == "print":
                gast["type"] = "logStatement"
                return gast
            else:
                gast["type"] = "customStatement"
                return gast

def py_to_gast(python_input_filename):
    input_ast =  astor.code_to_ast.parse_file(python_input_filename)
    
    # TODO: can add more fields to the generic ast
    gast = {"type": "root", "body": []}

    # NOTE: with current implementation, it will just go until it sees something it recognizes
    # eventually can implement nested structures
    for node in input_ast.body:
        if type(node) == ast.Expr:
            gast["body"].append(pyexpr_to_gast(node))
    
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
    elif(inputLanguage == 'js'):
        return 
    else:
        return

    for node in gast["body"]:
        print(astToJsMap[node["type"]])

astToJsMap = {
    "logStatement": "console.log()"
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
print(py_to_gast(fileName))
print(translator(fileName, ds, 'py', 'js'))