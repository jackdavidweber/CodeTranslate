import ast
import python.code_to_gast.py_router as py_router


def py_to_gast(python_input):
    """
    takes pyton code and converts it to a node
    node is then dealt with by node_to_gast 
    """
    input_ast = ''
    try:
        input_ast = ast.parse(python_input)
    except:
        # this will signal to translate that error occurred
        return None

    return py_router.node_to_gast(input_ast)
