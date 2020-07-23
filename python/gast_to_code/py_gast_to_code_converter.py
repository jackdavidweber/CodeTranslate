from shared.gast_to_code.abstract_gast_to_code_converter import AbstractGastToCodeConverter
import shared.gast_to_code.gast_to_code_router as router
import shared.gast_to_code.general_helpers as general_helpers
import py_built_in_functions
from shared.gast_to_code.error_handler import ErrorHandler


class PyGastToCodeConverter(AbstractGastToCodeConverter):
    name = "Python"
    is_beta = False
    is_input_lang = True
    is_output_lang = True
    error_handler = ErrorHandler()

    def handle_bool(gast):
        if gast["value"] == 1:
            return "True"
        else:
            return "False"

    def handle_if(gast, lvl=0):
        test = router.gast_to_code(gast["test"], "py")
        body_indent = "\n\t" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "py", body_indent,
                                           lvl + 1)

        out = 'if (' + test + '):' + body_indent + body

        # orelse can either be empty, or be an elif or be an else
        if len(gast["orelse"]) == 0:
            pass
        elif gast["orelse"][0]["type"] == "if":
            out += "\nel" + router.gast_to_code(gast["orelse"], "py", lvl)
        else:
            out += "\nelse:\n\t" + general_helpers.list_helper(
                gast["orelse"], "py", "\n\t", lvl)

        return out

    def handle_none(gast):
        return "None"

    def handle_while(gast, lvl=0):
        test = router.gast_to_code(gast["test"], "py")

        body_indent = "\n\t" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "py", body_indent,
                                           lvl + 1)

        out = 'while (' + test + '):' + body_indent + body
        return out

    def handle_for_range(gast, lvl=0):
        # start value
        start_value = gast["init"]["varValue"]["value"]
        start = str(start_value)

        # incrementor
        incrementor_op = gast["update"]["op"]

        # Normal aug assign expression
        if "right" in gast["update"]:
            incrementor_value = gast["update"]["right"]["value"]
            if incrementor_op == "-=":
                incrementor = "-" + str(incrementor_value)
            elif incrementor_op == "+=":
                incrementor = str(incrementor_value)
            else:
                incrementor = "unsupported update expression"

        # ++ or -- expression
        else:
            if incrementor_op == "++":
                incrementor = "1"
                incrementor_value = 1
            elif incrementor_op == "--":
                incrementor = "-1"
                incrementor_value = -1
            else:
                incrementor = "unsupported update operation"

        # end value
        end_value = gast["test"]["right"]["value"]
        end_comparator = gast["test"]["op"]
        if end_comparator == "<=":
            end_value += incrementor_value
        elif end_comparator == ">=":
            end_value -= incrementor_value
        end = str(end_value)

        var_name = gast["init"]["varId"]["value"]
        range_str = "range (" + start + ", " + end + ", " + incrementor + ")"

        body_indent = "\n\t" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "py", body_indent,
                                           lvl + 1)

        out = "for " + var_name + " in " + range_str + ":" + body_indent + body
        return out

    def handle_for_of(gast, lvl=0):
        arr_str = router.gast_to_code(gast["iter"], "py")
        var_name = gast["init"]["value"]

        body_indent = "\n\t" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "py", body_indent,
                                           lvl + 1)

        out = "for " + var_name + " in " + arr_str + ":" + body_indent + body
        return out

    def handle_log_statement(gast):
        return "print"

    def handle_var_assign(gast):
        value = router.gast_to_code(gast["varValue"], "py")
        return router.gast_to_code(gast["varId"], "py") + " = " + value

    def handle_aug_assign(gast):
        if "right" in gast:
            return router.gast_to_code(
                gast["left"],
                "py") + " " + gast["op"] + " " + router.gast_to_code(
                    gast["right"], "py")
        elif gast["op"] == "++":
            return router.gast_to_code(gast["left"], "py") + " += 1"
        else:
            return router.gast_to_code(gast["left"], "py") + " -= 1"

    def handle_func_call(gast):
        return router.gast_to_code(gast["value"],
                                   "py") + "(" + router.gast_to_code(
                                       gast["args"], "py") + ")"

    def handle_subscript(gast):
        return router.gast_to_code(gast["value"],
                                   "py") + "[" + router.gast_to_code(
                                       gast["index"], "py") + "]"

    def handle_name(gast):
        return gast["value"]

    def handle_attribute(gast):
        return router.gast_to_code(gast["value"], "py") + "." + gast["id"]

    def handle_built_in_attribute(gast):
        return router.gast_to_code(
            gast["value"],
            "py") + "." + py_built_in_functions.py_built_in_functions(
                gast["id"]).name

    def handle_dict(gast):
        return "{" + router.gast_to_code(gast["elements"], "py") + "}"

    def handle_property(gast):
        return router.gast_to_code(gast["key"],
                                   "py") + ": " + router.gast_to_code(
                                       gast["value"], "py")

    def handle_bool_op(gast):
        op = " and " if gast["op"] == "&&" else " or "
        left = router.gast_to_code(gast["left"], "py")
        right = router.gast_to_code(gast["right"], "py")
        return left + op + right

    def handle_unary_op(gast):
        return "not " + router.gast_to_code(gast["arg"], "py")

    def handle_function_declaration(gast, lvl):
        name = router.gast_to_code(gast["id"], "py")
        args = router.gast_to_code(gast["params"], "py")

        body_indent = "\n\t" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "py", body_indent,
                                           lvl + 1)

        out = "def " + name
        out += "(" + args + "):" + body_indent

        out += body
        return out

    def handle_arrow_func(gast, lvl=0):
        args = router.gast_to_code(gast["params"], "py")
        # lamda functions can only have one expression in body
        if len(gast["body"]) == 0:
            body = ""
        else:
            body = " " + router.gast_to_code(gast["body"][0], "py")

        if args == "":
            out = "lambda:"
        else:
            out = "lambda " + args + ":"

        out += body

        return out

    def handle_return_statement(gast):
        return "return " + router.gast_to_code(gast["value"], "py")

    def handle_assign_pattern(gast):
        return router.gast_to_code(gast["left"],
                                   "py") + " = " + router.gast_to_code(
                                       gast["right"], "py")

    def handle_arr(gast):
        return "[" + router.gast_to_code(gast["elements"], "py") + "]"
