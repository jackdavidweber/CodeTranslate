import javalang
import java.code_to_gast.java_router as java_router
"""
takes js string and converts it to a generic AST
"""


def java_to_gast(java_input):
    input_ast = ''

    try:
        # wrap input code in a class and function
        class_wrapper = '''
        class Test {{
            public static void main(String[] args) {{
                {java_input}
            }}
        }}'''.format(java_input=java_input)
        input_ast = javalang.parse.parse(class_wrapper)
    except:
        "Error: code could not compile"

    return java_router.node_to_gast(input_ast)
