import esprima
import sys

sys.path.insert(1, '/home/stephwalsh/capstone/cjs_capstone/translate/var_declare')
import js_var_declare as a

program = "let my_container = 20"

"""
Takes js and converts to generic ast 
"""
def js_to_gast(program):
    input_ast =  esprima.parseScript(program, { "tokens": True })
    # TODO: can add more fields to the generic ast
    gast = {"type": "root", "body": []}

    # NOTE: with current implementation, it will just go until it sees something it recognizes
    # eventually can implement nested structures
    for node in input_ast.body:
      #if node.type == "ExpressionStatement":
       # gast["body"].append(a.jsexpr_to_gast(node.expression))
      if node.type == "VariableDeclaration":
        gast["body"].append(a.jsassign_to_gast(node.declarations))
    return gast


print(js_to_gast(program))