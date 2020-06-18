import ast
import astor

def pyexpr_to_gast(node, gast):
    if type(node.value) == ast.Call: # FIXME: should type of call be embedded in the gast?
        gast["type"] = "callexpr"
        if type(node.value.func) == ast.Name:
            if node.value.func.id == "print":
                gast["id"] = "log"
                return gast
            else:
                gast["id"] = node.value.func.id
                return gast

def py_to_gast(python_input_filename):
    input_ast =  astor.code_to_ast.parse_file(python_input_filename)
    
    # TODO: can add more fields to the generic ast
    gast = {
        "type": None,
        "id": None,
    }

    # NOTE: with current implementation, it will just go until it sees something it recognizes
    # eventually can implement nested structures
    for node in input_ast.body:
        if type(node) == ast.Expr:
            return pyexpr_to_gast(node, gast)

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
    for potential_match in ds:
        if potential_match['gast'] == gast:
            return potential_match[outputLanguage]


ds = [
    {
        'gast': {'type': 'callexpr', 'id': 'log'},
        'js': 'console.log()',
        'py': 'print()'
    }
]

fileName = "/home/jackweber/cjs_capstone/experimental/jackPython/sampleCode.py"
print(translator(fileName, ds, 'py', 'js'))