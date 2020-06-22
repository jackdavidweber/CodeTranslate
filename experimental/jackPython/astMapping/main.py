from py_to_gast import *

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

fileName = "/home/jackweber/cjs_capstone/experimental/jackPython/astMapping/sampleCode.py"
translator(fileName, ds, 'py', 'js')