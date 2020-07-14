import bashlex
import bash.code_to_gast.bash_router as bash_router

def bash_to_gast(bash_input):
    input_ast = ''
    try:
        input_ast = bashlex.parse(bash_input)
        print(input_ast)
    except:
        return 'Error: code could not compile'
    
    return bash_router.node_to_gast(input_ast)
    