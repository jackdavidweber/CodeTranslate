import gast_to_code.py_helpers as py_helpers
import gast_to_code.js_helpers as js_helpers
import gast_to_code.general_helpers as general_helpers

"""
gast router that takes generic ast and the output language
that the gast needs to be converted to and executes the
conversion recursively
out_lang correspond to the language codes defined in datastructure:
javascript: js
python: py
"""
def gast_to_code(gast, out_lang, lvl=0):
    if type(gast) == list:
        return general_helpers.list_helper(gast, out_lang)

    # Primitives
    elif gast["type"] == "num":
        return str(gast["value"])
    elif gast["type"] == "arr":
        return "[" + gast_to_code(gast["elements"], out_lang) + "]"
    elif gast["type"] == "str":
        return '"' + gast["value"] + '"'
    elif gast["type"] == "bool":
        return out["bool"][out_lang](gast)
    elif gast["type"] == "if":
        return out["if"][out_lang](gast, lvl)
    elif gast["type"] == "none":
        return out["none"][out_lang]

    # Loops
    elif gast["type"] == "whileStatement":
        return out["whileStatement"][out_lang](gast, lvl)
    elif gast["type"] == "forRangeStatement":
        return out["forRangeStatement"][out_lang](gast, lvl)
    elif gast["type"] == "forOfStatement":
        return out["forOfStatement"][out_lang](gast, lvl)

    # Other
    elif gast["type"] == "root":
        return  general_helpers.list_helper(gast["body"], out_lang, "\n")
    elif gast["type"] == "break":
        return "break"
    elif gast["type"] == "continue":
        return "continue"
    elif gast["type"] == "logStatement":
        return out["logStatement"][out_lang]
    elif gast["type"] == "varAssign":
        return out["varAssign"][out_lang](gast)
    elif gast["type"] == "augAssign":
        return out["augAssign"][out_lang](gast)
    elif gast["type"] == "funcCall":
        return out["funcCall"][out_lang](gast)
    elif gast["type"] == "subscript":
        return out["subscript"][out_lang](gast)
    elif gast["type"] == "name":
        return gast["value"]
    elif gast["type"] == "attribute":
        return out["attribute"][out_lang](gast)
    elif gast["type"] == "builtInAttribute":
        return out["builtInAttribute"][out_lang](gast)
    elif gast["type"] == "dict":
        return out["dict"][out_lang](gast)
    elif gast["type"] == "property":
        return out["property"][out_lang](gast)
    elif gast["type"] == "binOp":
        return general_helpers.gast_to_node_bin_op_helper(gast, out_lang)
    elif gast["type"] == "boolOp":
        return out["boolOp"][out_lang](gast)
    elif gast["type"] == "unaryOp":
        return out["unaryOp"][out_lang](gast)
    elif gast["type"] == "functionDeclaration":
        return out["functionDeclaration"][out_lang](gast, lvl)
    elif gast["type"] == "returnStatement":
        return out["returnStatement"][out_lang](gast)
    elif gast["type"] == "assignPattern":
        return out["assignPattern"][out_lang](gast) 
    elif gast["type"] == "error":
        if gast["value"] == "unsupported":
            # Error string
            return "Feature not supported"
        return "Error"


out = {
    "logStatement": {
        "py": "print",
        "js": "console.log"
    },
    "varAssign": {
        "py": py_helpers.gast_to_py_var_assign,
        "js": js_helpers.gast_to_js_var_assign,
    },
    "augAssign": {
        "py": py_helpers.gast_to_py_aug_assign,
        "js": js_helpers.gast_to_js_aug_assign
    },
    "bool": {
        "py": py_helpers.gast_to_py_bool,
        "js": js_helpers.gast_to_js_bool,
    },
    "if": {
        "py": py_helpers.gast_to_py_if,
        "js": js_helpers.gast_to_js_if
    },
    "funcCall": {
        "py": py_helpers.gast_to_py_functions,
        "js": js_helpers.gast_to_js_functions
    },
    "attribute": {
        "py": py_helpers.gast_to_py_attribute,
        "js": js_helpers.gast_to_js_attribute
    },
    "builtInAttribute": {
        "py": py_helpers.gast_to_py_built_in_attribute,
        "js": js_helpers.gast_to_js_built_in_attribute
    },
    "boolOp": {
        "py": py_helpers.gast_to_py_bool_op,
        "js": js_helpers.gast_to_js_bool_op
    },
    "none": {
        "py": "None",
        "js": "null" # TODO look at undefined in JS 
    },
    "unaryOp": {
        "py": py_helpers.gast_to_py_unary_op,
        "js": js_helpers.gast_to_js_unary_op
    },
    "functionDeclaration": {
        "py": py_helpers.gast_to_py_func_declarations,
        "js": js_helpers.gast_to_js_func_declarations
    },
    "returnStatement": {
        "py": py_helpers.gast_to_py_return_statement,
        "js": js_helpers.gast_to_js_return_statement
    },
    "assignPattern": {
        "py": py_helpers.gast_to_py_assign_pattern,
        "js": js_helpers.gast_to_js_assign_pattern
    },
    "whileStatement": {
        "py": py_helpers.gast_to_py_while,
        "js": js_helpers.gast_to_js_while
    },
    "forRangeStatement": {
        "py": py_helpers.gast_to_py_forRange,
        "js": js_helpers.gast_to_js_forRange
    },
    "forOfStatement": {
        "py": py_helpers.gast_to_py_forOf,
        "js": js_helpers.gast_to_js_forOf
    },
    "dict": {
        "py": py_helpers.gast_to_py_dict,
        "js": js_helpers.gast_to_js_dict
    },
    "property": {
        "py": py_helpers.gast_to_py_property,
        "js": js_helpers.gast_to_js_property
    },
    "subscript": {
        "py": py_helpers.gast_to_py_subscript,
        "js": js_helpers.gast_to_js_subscript
    }
}

