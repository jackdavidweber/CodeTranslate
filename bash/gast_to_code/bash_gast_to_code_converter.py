import shared.gast_to_code.general_helpers as general_helpers
import shared.gast_to_code.gast_to_code_router as router
import bash.gast_to_code.bash_helpers as bash_helpers
from shared.gast_to_code.error_handler import ErrorHandler


class BashGastToCodeConverter():
    name = "Bash"
    is_beta = True
    is_input_lang = False
    is_output_lang = True

    def __init__(self):
        self.error_handler = ErrorHandler()

    def get_error_handler(self):
        return self.error_handler

    def code_to_gast(self, code_input):
        return self.error_handler.invalid_arguments()

    def gast_to_code_post_processing(self, code_output):
        return code_output  # since there is no post-processing

    def handle_log_statement(self, gast):
        return "echo"

    def handle_func_call(self, gast):
        return router.gast_to_code(gast["value"],
                                   "bash") + " " + bash_helpers.bash_arg_helper(
                                       gast["args"])

    def handle_arr(self, gast):
        # This logic returns an error for nested arrays which are not supported in bash
        if general_helpers.arr_in_list(gast["elements"]):
            return self.error_handler.impossible_translation([
                "https://stackoverflow.com/a/11234169",
                "https://github.com/pppoe/Nested-Array-Bash"
            ])

        return "(" + router.gast_to_code(gast["elements"], "bash") + ")"

    def handle_if(self, gast, lvl=0):
        test = router.gast_to_code(gast["test"], "bash")
        body_indent = "\n\t" + "\t" * lvl
        closing_exp_indent = "\n" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "bash", body_indent,
                                           lvl + 1)

        out = "if [[ " + test + " ]]; then" + body_indent + body + closing_exp_indent

        if len(gast["orelse"]) == 0:
            out += "fi"
        elif gast["orelse"][0]["type"] == "if":
            out += "el" + router.gast_to_code(gast["orelse"], "bash")
        else:
            out += "else\n\t" + general_helpers.list_helper(
                gast["orelse"], "bash", "\n\t") + "\nfi"

        return out

    def handle_var_assign(self, gast):
        value = router.gast_to_code(gast["varValue"], "bash")
        return router.gast_to_code(gast["varId"], "bash") + " = " + value

    def handle_aug_assign(self, gast):
        if "right" in gast:
            return router.gast_to_code(
                gast["left"],
                "bash") + " " + gast["op"] + " " + router.gast_to_code(
                    gast["right"], "bash")
        else:
            return router.gast_to_code(gast["left"], "bash") + gast["op"]

    def handle_name(self, gast):
        return gast["value"]

    def handle_root(self, gast):
        return general_helpers.list_helper(gast["body"], "bash", "\n")

    def handle_bool(self, gast):
        return self.error_handler.impossible_translation([
            "https://stackoverflow.com/a/47092826",
            "https://github.com/Jeff-Russ/bash-boolean-helpers"
        ])

    def handle_none(self, gast):
        return self.error_handler.unsupported_feature()

    def handle_while(self, gast, lvl=0):
        return self.error_handler.unsupported_feature()

    def handle_for_range(self, gast, lvl=0):
        return self.error_handler.unsupported_feature()

    def handle_for_of(self, gast, lvl=0):
        return self.error_handler.unsupported_feature()

    def handle_subscript(self, gast):
        return self.error_handler.unsupported_feature()

    def handle_built_in_attribute(self, gast):
        return self.error_handler.unsupported_feature()

    def handle_dict(self, gast):
        return self.error_handler.unsupported_feature()

    def handle_property(self, gast):
        return self.error_handler.unsupported_feature()

    def handle_bool_op(self, gast):
        return self.error_handler.unsupported_feature()

    def handle_unary_op(self, gast):
        return self.error_handler.unsupported_feature()

    def handle_function_declaration(self, gast, lvl=0):
        return self.error_handler.unsupported_feature()

    def handle_return_statement(self, gast):
        return self.error_handler.unsupported_feature()

    def handle_assign_pattern(self, gast):
        return self.error_handler.unsupported_feature()

    def handle_arrow_func(self, gast):
        return self.error_handler.unsupported_feature()

    def handle_attribute(self, gast):
        return self.error_handler.unsupported_feature()
