"""
Takes gast primitive node and converts to
string representing java type
"""


def gast_to_java_type(gast):
    gast_type = gast["type"]

    if gast_type == "num":
        java_type = "int"
    elif gast_type == "str":
        java_type = "String"
    elif gast_type == "bool":
        java_type = "boolean"
    elif gast_type == "arr":
        java_type = arr_type_helper(gast["elements"])
    else:
        java_type = "customType"

    return java_type


"""
Returns the string representing type of the items in the array.
Returns error if multiple types in same array or if array is empty
"""


def arr_type_helper(gast_arr):
    if len(gast_arr) == 0:
        return "impossibleTranslationError: direct translation does not exist"
    print(gast_arr)
    node = gast_arr[0]

    for i in range(1, len(gast_arr)):
        if gast_arr[i]["type"] != node["type"]:
            return "impossibleTranslationError: direct translation does not exist"

    return gast_to_java_type(node) + "[]"
