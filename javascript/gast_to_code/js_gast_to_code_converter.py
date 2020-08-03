import shared.gast_to_code.general_helpers as general_helpers
import js_built_in_functions
import shared.gast_to_code.gast_to_code_router as router
from shared.gast_to_code.error_handler import ErrorHandler
import javascript.code_to_gast.js_main as js_main


class JsGastToCodeConverter():
    name = "Javascript"
    is_beta = False
    is_input_lang = True
    is_output_lang = True

    def __init__(self):
        self.error_handler = ErrorHandler()

    def get_error_handler(self):
        return self.error_handler

    def code_to_gast(self, code_input):
        return js_main.js_to_gast(code_input)

    def handle_bool(self, gast):
        if gast["value"] == 1:
            return "true"
        else:
            return "false"

    def handle_if(self, gast, lvl=0):
        test = router.gast_to_code(gast["test"], "js")
        body_indent = "\n\t" + "\t" * lvl
        closing_brace_indent = "\n" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "js", body_indent,
                                           lvl + 1)

        out = 'if (' + test + ') {' + body_indent + body + closing_brace_indent + "}"

        # orelse can either be empty, or be an elif or be an else
        if len(gast["orelse"]) == 0:
            pass
        elif gast["orelse"][0]["type"] == "if":
            out += " else " + router.gast_to_code(gast["orelse"], "js")
        else:
            out += " else {\n\t" + general_helpers.list_helper(
                gast["orelse"], "js", "\n\t") + "\n}"

        return out

    def handle_none(self, gast):
        return "null"

    def handle_while(self, gast, lvl=0):
        test = router.gast_to_code(gast["test"], "js")

        body_indent = "\n\t" + "\t" * lvl
        closing_brace_indent = "\n" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "js", body_indent,
                                           lvl + 1)

        out = 'while (' + test + ') {' + body_indent + body + closing_brace_indent + "}"
        return out

    def handle_for_range(self, gast, lvl=0):
        loop_init = router.gast_to_code(gast["init"], "js")
        loop_test = router.gast_to_code(gast["test"], "js")
        loop_update = router.gast_to_code(gast["update"], "js")

        body_indent = "\n\t" + "\t" * lvl
        closing_brace_indent = "\n" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "js", body_indent,
                                           lvl + 1)

        return "for (" + loop_init + "; " + loop_test + "; " + loop_update + ") {" + body_indent + body + closing_brace_indent + "}"

    def handle_for_of(self, gast, lvl=0):
        arr_str = router.gast_to_code(gast["iter"], "js")
        var_name = gast["init"]["value"]

        body_indent = "\n\t" + "\t" * lvl
        closing_brace_indent = "\n" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "js", body_indent,
                                           lvl + 1)

        out = "for (" + var_name + " of " + arr_str + ") {" + body_indent + body + closing_brace_indent + "}"
        return out

    def handle_log_statement(self, gast):
        return "console.log"

    def handle_var_assign(self, gast):
        kind = gast["kind"]
        varId = router.gast_to_code(gast["varId"], "js")
        varValue = router.gast_to_code(gast["varValue"], "js")

        if gast["varId"]["type"] == "subscript":
            return varId + " = " + varValue
        return kind + " " + varId + " = " + varValue

    def handle_aug_assign(self, gast):
        if "right" in gast:
            return router.gast_to_code(
                gast["left"],
                "js") + " " + gast["op"] + " " + router.gast_to_code(
                    gast["right"], "js")
        else:
            return router.gast_to_code(gast["left"], "js") + gast["op"]

    def handle_func_call(self, gast):
        return router.gast_to_code(gast["value"],
                                   "js") + "(" + router.gast_to_code(
                                       gast["args"], "js") + ")"

    def handle_arrow_func(self, gast, lvl=0):
        args = router.gast_to_code(gast["params"], "js")

        body_indent = "\n\t" + "\t" * lvl
        closing_brace_indent = "\n" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "js", body_indent,
                                           lvl + 1)
        out = "(" + args + ") => {"
        out += body_indent + body + closing_brace_indent + "}"

        return out

    def handle_subscript(self, gast):
        return router.gast_to_code(gast["value"],
                                   "js") + "[" + router.gast_to_code(
                                       gast["index"], "js") + "]"

    def handle_name(self, gast):
        return gast["value"]

    def handle_attribute(self, gast):
        return router.gast_to_code(gast["value"], "js") + "." + gast["id"]

    def handle_built_in_attribute(self, gast):
        return router.gast_to_code(
            gast["value"],
            "js") + "." + js_built_in_functions.js_built_in_functions(
                gast["id"]).name

    def handle_dict(self, gast):
        return "{" + router.gast_to_code(gast["elements"], "js") + "}"

    def handle_property(self, gast):
        return router.gast_to_code(gast["key"],
                                   "js") + ": " + router.gast_to_code(
                                       gast["value"], "js")

    def handle_bool_op(self, gast):
        return general_helpers.gast_to_node_bin_op_helper(gast, "js")

    def handle_unary_op(self, gast):
        return "!" + router.gast_to_code(gast["arg"], "js")

    def handle_function_declaration(self, gast, lvl=0):
        name = router.gast_to_code(gast["id"], "js")
        args = router.gast_to_code(gast["params"], "js")

        body_indent = "\n\t" + "\t" * lvl
        closing_brace_indent = "\n" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "js", body_indent,
                                           lvl + 1)
        out = "function " + name
        out += "(" + args + ") {" + body_indent + body + closing_brace_indent + "}"

        return out

    def handle_return_statement(self, gast):
        return "return " + router.gast_to_code(gast["value"], "js")

    def handle_assign_pattern(self, gast):
        return router.gast_to_code(gast["left"],
                                   "js") + " = " + router.gast_to_code(
                                       gast["right"], "js")

    def handle_arr(self, gast):
        return "[" + router.gast_to_code(gast["elements"], "js") + "]"

    def handle_root(self, gast):
        return general_helpers.list_helper(gast["body"], "js", "\n")
