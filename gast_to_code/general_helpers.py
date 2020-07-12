import gast_to_code.gast_to_code_router as router

"""
Helper for lists of gast
Default is to put comma and space btwn each stringified gast
    i.e. list_helper({str_gast}, {str_gast}, out_lang) --> str, str
Can specify different btwn string with third parameter
    i.e. list_helper({str_gast}, {str_gast}, out_lang, "**") --> str**str
"""
def list_helper(gast_list, out_lang, csv_delimiter=", ", lvl=0):
    out = ""

    for i in range(0, len(gast_list)):
        out += router.gast_to_code(gast_list[i], out_lang, lvl)

        if i < len(gast_list) - 1:  # don't add delimiter for last item
            out += csv_delimiter

    return out


def gast_to_node_bin_op_helper(gast, out_lang):
    op = " " + str(gast["op"]) + " "
    left = router.gast_to_code(gast["left"], out_lang)
    right = router.gast_to_code(gast["right"], out_lang)
    return left + op + right
