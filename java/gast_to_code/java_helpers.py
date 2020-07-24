import shared.gast_to_code.gast_to_code_router as router


def gast_to_java_type(gast, error_handler):
    """
    Takes gast primitive node and converts to
    string representing java type
    """
    gast_type = gast["type"]

    if gast_type == "num":
        java_type = "int"
    elif gast_type == "str":
        java_type = "String"
    elif gast_type == "bool":
        java_type = "boolean"
    elif gast_type == "arr":
        java_type = arr_type_helper(gast["elements"],
                                    error_handler=error_handler)
    else:
        java_type = "CustomType"

    return java_type


def arr_type_helper(gast_arr, error_handler):
    """
    Returns the string representing type of the items in the array.
    Returns error if multiple types in same array or if array is empty
    """
    if len(gast_arr) == 0:
        return error_handler.impossible_translation()
    node = gast_arr[0]

    for i in range(1, len(gast_arr)):
        if gast_arr[i]["type"] != node["type"]:
            return error_handler.impossible_translation()

    return gast_to_java_type(node, error_handler=error_handler) + "[]"


def java_node_list_helper(gast_list,
                          is_returning_functions,
                          csv_delimiter=", ",
                          lvl=0):
    """
    Almost identical to regular list_helper however is_returning_functions is passed in
    as a boolean to determine whether the list_helper ignores functions or ignores non-functions
    """

    out = ""

    for i in range(0, len(gast_list)):
        if is_returning_functions and gast_list[i][
                "type"] == "functionDeclaration":
            out += router.gast_to_code(gast_list[i], "java", lvl)
            if i < len(gast_list) - 1:  # don't add delimiter for last item
                out += csv_delimiter

        elif (not is_returning_functions
             ) and gast_list[i]["type"] != "functionDeclaration":
            out += router.gast_to_code(gast_list[i], "java", lvl)
            if i < len(gast_list) - 1:  # don't add delimiter for last item
                out += csv_delimiter

    return out
