import shared.gast_to_code.gast_to_code_router as router
'''
variables needed to be wrapped in quotes and have $ when parameters for function
'''


def handle_var_arg(gast):
    return '"$' + gast["value"] + '"'



def bash_arg_helper(gast_list):
    '''
    Called on func args only and return the correct translation since
    variables are written different when function params
    '''
    out = ""
    for i in range(0, len(gast_list)):
        if gast_list[i]["type"] == "name":
            out += handle_var_arg(gast_list[i])
        else:
            out += router.gast_to_code(gast_list[i], "bash")

        if i < len(gast_list) - 1:  # don't add delimiter for last item
            out += " "
    return out
