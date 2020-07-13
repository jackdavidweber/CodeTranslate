import esprima
import javascript.code_to_gast.js_router as js_router

"""
takes js string and converts it to a generic AST
"""
def js_to_gast(js_input):
    input_ast = ''
    try:
        input_ast = esprima.parseScript(js_input, {"tokens": False})
    except:
        return "Error: code could not compile"
    return js_router.node_to_gast(input_ast)
