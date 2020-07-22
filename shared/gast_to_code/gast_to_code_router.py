import shared.gast_to_code.general_helpers as general_helpers
from shared.gast_to_code.converter_registry import ConverterRegistry
"""
gast router that takes generic ast and the output language
that the gast needs to be converted to and executes the
conversion recursively
out_lang correspond to the language codes defined in datastructure:
javascript: js
python: py
"""


def gast_to_code(gast, out_lang, lvl=0):
    converter = ConverterRegistry.get_converter(out_lang)

    if type(gast) == list:
        # bash has no comma between function arguments
        if out_lang == "bash":
            return general_helpers.list_helper(gast, out_lang, " ")
        return general_helpers.list_helper(gast, out_lang)

    # Primitives
    elif gast["type"] == "num":
        return str(gast["value"])
    elif gast["type"] == "arr":
        return converter.handle_arr(gast)
    elif gast["type"] == "str":
        return '"' + gast["value"] + '"'
    elif gast["type"] == "bool":
        return converter.handle_bool(gast)
    elif gast["type"] == "if":
        return converter.handle_if(gast, lvl)
    elif gast["type"] == "none":
        return converter.handle_none(gast)

    # Loops
    elif gast["type"] == "whileStatement":
        return converter.handle_while(gast, lvl)
    elif gast["type"] == "forRangeStatement":
        return converter.handle_for_range(gast, lvl)
    elif gast["type"] == "forOfStatement":
        return converter.handle_for_of(gast, lvl)

    # Other
    elif gast["type"] == "root":
        return general_helpers.list_helper(gast["body"], out_lang, "\n")
    elif gast["type"] == "break":
        return "break"
    elif gast["type"] == "continue":
        return "continue"
    elif gast["type"] == "logStatement":
        return converter.handle_log_statement(gast)
    elif gast["type"] == "varAssign":
        return converter.handle_var_assign(gast)
    elif gast["type"] == "augAssign":
        return converter.handle_aug_assign(gast)
    elif gast["type"] == "funcCall":
        return converter.handle_func_call(gast)
    elif gast["type"] == "subscript":
        return converter.handle_subscript(gast)
    elif gast["type"] == "name":
        return converter.handle_name(gast)
    elif gast["type"] == "attribute":
        return converter.handle_attribute(gast)
    elif gast["type"] == "builtInAttribute":
        return converter.handle_built_in_attribute(gast)
    elif gast["type"] == "dict":
        return converter.handle_dict(gast)
    elif gast["type"] == "property":
        return converter.handle_property(gast)
    elif gast["type"] == "binOp":
        return general_helpers.gast_to_node_bin_op_helper(gast, out_lang)
    elif gast["type"] == "boolOp":
        return converter.handle_bool_op(gast)
    elif gast["type"] == "unaryOp":
        return converter.handle_unary_op(gast)
    elif gast["type"] == "functionDeclaration":
        return converter.handle_function_declaration(gast, lvl)
    elif gast["type"] == "returnStatement":
        return converter.handle_return_statement(gast)
    elif gast["type"] == "assignPattern":
        return converter.handle_assign_pattern(gast)
    elif gast["type"] == "arrowExpression":
        return converter.handle_arrow_func(gast)
    elif gast["type"] == "error":
        if gast["value"] == "unsupported":
            # Error string
            return "Feature not supported"
        return "Error"
