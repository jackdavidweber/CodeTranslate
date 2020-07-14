import javalang
import java.code_to_gast.java_router as java_router

"""
takes js string and converts it to a generic AST
"""
def java_to_gast(java_input):
    input_ast = javalang.parse.parse(java_input)
    return java_router.node_to_gast(input_ast)