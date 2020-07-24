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
        java_type = "customType"

    return java_type


def arr_type_helper(gast_arr, error_handler):
    """
    Returns the string representing type of the items in the array.
    Returns error if multiple types in same array or if array is empty
    """
    if len(gast_arr) == 0:
        return error_handler.impossible_translation()
    print(gast_arr)
    node = gast_arr[0]

    for i in range(1, len(gast_arr)):
        if gast_arr[i]["type"] != node["type"]:
            return error_handler.impossible_translation()

    return gast_to_java_type(node, error_handler=error_handler) + "[]"
