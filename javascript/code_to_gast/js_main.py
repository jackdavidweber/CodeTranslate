import esprima
import javascript.code_to_gast.js_router as js_router
"""
takes js string and converts it to a generic AST
"""


def js_to_gast(js_input, error_handler):
    input_ast = ''
    try:
        input_ast = esprima.parseScript(js_input, {"tokens": False})
    except:
        output_str = error_handler.compilation()
        return output_str
    return js_router.node_to_gast(input_ast)
