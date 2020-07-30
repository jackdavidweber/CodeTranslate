import javalang
import java.code_to_gast.java_router as java_router
import java.code_to_gast.java_constants as java_constants


def java_to_gast(java_input):
    '''
    Input will be wrapped in a class and main function if no functions are present
    If functions are present it will be wrapped in a class 
    If a class declaration is given an error will be thrown 
    '''
    class_main_wrapped = '''
    class Test {{
        public static void {wrapper}(String[] args) {{
            {java_input}
        }}
    }}'''.format(wrapper=java_constants.ARTIFICIAL_WRAPPER,
                 java_input=java_input)

    class_wrapped = '''
    class Test {{
        {java_input}
    }}'''.format(java_input=java_input)

    # try to compile java with both wrappers - if one compiles start to build ast
    try:
        input_ast = javalang.parse.parse(class_main_wrapped)
    except:
        try:
            input_ast = javalang.parse.parse(class_wrapped)
        except:
            # this will signal to translate that error occurred
            return None

    return java_router.node_to_gast(input_ast)
