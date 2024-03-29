import shared.gast_to_code.gast_to_code_router as router
import shared.gast_to_code.general_helpers as general_helpers
import py_built_in_functions
from shared.gast_to_code.error_handler import ErrorHandler
import python.code_to_gast.py_main as py_main


class PyGastToCodeConverter():
    name = "Python"
    is_beta = False
    is_input_lang = True
    is_output_lang = True

    def __init__(self):
        self.error_handler = ErrorHandler()

    def get_error_handler(self):
        return self.error_handler

    def code_to_gast(self, code_input):
        return py_main.py_to_gast(code_input)

    def gast_to_code_post_processing(self, code_output):
        return code_output  # since there is no post-processing

    def handle_bool(self, gast):
        if gast["value"] == 1:
            return "True"
        else:
            return "False"

    def handle_if(self, gast, lvl=0):
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

    def handle_none(self, gast):
        return "None"

    def handle_while(self, gast, lvl=0):
        test = router.gast_to_code(gast["test"], "py")

        body_indent = "\n\t" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "py", body_indent,
                                           lvl + 1)

        out = 'while (' + test + '):' + body_indent + body
        return out

    def handle_for_range(self, gast, lvl=0):
        # deals with init TODO: streamline java and javascript to gast to make this easier
        if (type(gast["init"]) == dict and gast["init"]["type"] == "varAssign"):
            start = str(gast["init"]["varValue"]["value"])
            var_name = gast["init"]["varId"]["value"]

        elif (type(gast["init"]) == dict and "right" in gast["init"] and
              "left" in gast["init"]):
            start = str(gast["init"]["right"]["value"])
            var_name = gast["init"]["left"]["value"]
        else:
            start = self.error_handler.unsupported_feature()
            var_name = self.error_handler.unsupported_feature()

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
                incrementor = self.error_handler.unsupported_feature()

        # ++ or -- expression
        else:
            if incrementor_op == "++":
                incrementor = "1"
                incrementor_value = 1
            elif incrementor_op == "--":
                incrementor = "-1"
                incrementor_value = -1
            else:
                incrementor = self.error_handler.unsupported_feature()

        # end value
        end_value = gast["test"]["right"]["value"]
        end_comparator = gast["test"]["op"]
        if end_comparator == "<=":
            end_value += incrementor_value
        elif end_comparator == ">=":
            end_value -= incrementor_value
        end = str(end_value)

        range_str = "range (" + start + ", " + end + ", " + incrementor + ")"

        body_indent = "\n\t" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "py", body_indent,
                                           lvl + 1)

        out = "for " + var_name + " in " + range_str + ":" + body_indent + body
        return out

    def handle_for_of(self, gast, lvl=0):
        arr_str = router.gast_to_code(gast["iter"], "py")
        var_name = gast["init"]["value"]

        body_indent = "\n\t" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "py", body_indent,
                                           lvl + 1)

        out = "for " + var_name + " in " + arr_str + ":" + body_indent + body
        return out

    def handle_log_statement(self, gast):
        return "print"

    def handle_var_assign(self, gast):
        value = router.gast_to_code(gast["varValue"], "py")
        return router.gast_to_code(gast["varId"], "py") + " = " + value

    def handle_aug_assign(self, gast):
        if "right" in gast:
            return router.gast_to_code(
                gast["left"],
                "py") + " " + gast["op"] + " " + router.gast_to_code(
                    gast["right"], "py")
        elif gast["op"] == "++":
            return router.gast_to_code(gast["left"], "py") + " += 1"
        else:
            return router.gast_to_code(gast["left"], "py") + " -= 1"

    def handle_func_call(self, gast):
        return router.gast_to_code(gast["value"],
                                   "py") + "(" + router.gast_to_code(
                                       gast["args"], "py") + ")"

    def handle_subscript(self, gast):
        return router.gast_to_code(gast["value"],
                                   "py") + "[" + router.gast_to_code(
                                       gast["index"], "py") + "]"

    def handle_name(self, gast):
        return gast["value"]

    def handle_attribute(self, gast):
        return router.gast_to_code(gast["value"], "py") + "." + gast["id"]

    def handle_built_in_attribute(self, gast):
        return router.gast_to_code(
            gast["value"],
            "py") + "." + py_built_in_functions.py_built_in_functions(
                gast["id"]).name

    def handle_dict(self, gast):
        return "{" + router.gast_to_code(gast["elements"], "py") + "}"

    def handle_property(self, gast):
        return router.gast_to_code(gast["key"],
                                   "py") + ": " + router.gast_to_code(
                                       gast["value"], "py")

    def handle_bool_op(self, gast):
        op = " and " if gast["op"] == "&&" else " or "
        left = router.gast_to_code(gast["left"], "py")
        right = router.gast_to_code(gast["right"], "py")
        return left + op + right

    def handle_unary_op(self, gast):
        return "not " + router.gast_to_code(gast["arg"], "py")

    def handle_function_declaration(self, gast, lvl):
        name = router.gast_to_code(gast["id"], "py")
        args = router.gast_to_code(gast["params"], "py")

        body_indent = "\n\t" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "py", body_indent,
                                           lvl + 1)

        out = "def " + name
        out += "(" + args + "):" + body_indent

        out += body
        return out

    def handle_arrow_func(self, gast, lvl=0):
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

    def handle_return_statement(self, gast):
        return "return " + router.gast_to_code(gast["value"], "py")

    def handle_assign_pattern(self, gast):
        return router.gast_to_code(gast["left"],
                                   "py") + " = " + router.gast_to_code(
                                       gast["right"], "py")

    def handle_arr(self, gast):
        return "[" + router.gast_to_code(gast["elements"], "py") + "]"

    def handle_root(self, gast):
        return general_helpers.list_helper(gast["body"], "py", "\n")
