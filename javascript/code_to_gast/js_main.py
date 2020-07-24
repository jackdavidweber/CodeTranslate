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
        # this will signal to translate that error occurred
        return None
    return js_router.node_to_gast(input_ast)
