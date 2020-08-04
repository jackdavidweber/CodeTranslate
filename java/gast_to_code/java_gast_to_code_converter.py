import shared.gast_to_code.gast_to_code_router as router
import shared.gast_to_code.general_helpers as general_helpers
import java.gast_to_code.java_helpers as java_helpers
from shared.gast_to_code.error_handler import ErrorHandler
import java.code_to_gast.java_main as java_main


class JavaGastToCodeConverter():
    name = "Java"
    is_beta = True
    is_input_lang = True
    is_output_lang = True

    def __init__(self):
        self.error_handler = ErrorHandler()

    def get_error_handler(self):
        return self.error_handler

    def code_to_gast(self, code_input):
        return java_main.java_to_gast(code_input)

    def handle_bool(self, gast):
        if gast["value"] == 1:
            return "true"
        else:
            return "false"

    def handle_if(self, gast, lvl=0):
        test = router.gast_to_code(gast["test"], "java")
        body_indent = "\n\t" + "\t" * lvl
        closing_brace_indent = "\n" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "java", body_indent,
                                           lvl + 1)

        out = 'if (' + test + ') {' + body_indent + body + closing_brace_indent + "}"

        if len(gast["orelse"]) == 0:
            pass
        elif gast["orelse"][0]["type"] == "if":
            out += " else " + router.gast_to_code(gast["orelse"], "java")
        else:
            out += " else {\n\t" + general_helpers.list_helper(
                gast["orelse"], "java", "\n\t") + "\n}"

        return out

    def handle_none(self, gast):
        return "null"

    def handle_while(self, gast, lvl=0):
        test = router.gast_to_code(gast["test"], "java")

        body_indent = "\n\t" + "\t" * lvl
        closing_brace_indent = "\n" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "java", body_indent,
                                           lvl + 1)

        out = 'while (' + test + ') {' + body_indent + body + closing_brace_indent + "}"
        return out

    def handle_for_range(self, gast, lvl=0):
        loop_init = router.gast_to_code(gast["init"], "java")
        loop_test = router.gast_to_code(gast["test"], "java")
        loop_update = router.gast_to_code(gast["update"], "java")

        body_indent = "\n\t" + "\t" * lvl
        closing_brace_indent = "\n" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "java", body_indent,
                                           lvl + 1)

        return "for (" + loop_init + "; " + loop_test + "; " + loop_update + ") {" + body_indent + body + closing_brace_indent + "}"

    def handle_for_of(self, gast, lvl=0):
        arr_str = router.gast_to_code(gast["iter"], "java")
        var_name = "GenericType " + gast["init"]["value"]

        body_indent = "\n\t" + "\t" * lvl
        closing_brace_indent = "\n" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "java", body_indent,
                                           lvl + 1)

        out = "for (" + var_name + " : " + arr_str + ") {" + body_indent + body + closing_brace_indent + "}"
        return out

    def handle_log_statement(self, gast):
        return "System.out.println"

    def handle_var_assign(self, gast):
        var_id = router.gast_to_code(gast["varId"], "java")
        var_value = router.gast_to_code(gast["varValue"], "java")

        kind = java_helpers.gast_to_java_type(gast["varValue"],
                                              error_handler=self.error_handler)

        return kind + " " + var_id + " = " + var_value

    def handle_aug_assign(self, gast):
        if "right" in gast:
            return router.gast_to_code(
                gast["left"],
                "java") + " " + gast["op"] + " " + router.gast_to_code(
                    gast["right"], "java")
        else:
            return router.gast_to_code(gast["left"], "java") + gast["op"]

    # TODO(taiga#149) gast_to_code should not be able to return System.out.println(1, 2)
    def handle_func_call(self, gast):
        # handles logstatement for single array
        if gast["value"]["type"] == "logStatement" and len(
                gast["args"]) == 1 and gast["args"][0]["type"] == "arr":
            log_statement = router.gast_to_code(gast["value"], "java")
            type_declaration = java_helpers.gast_to_java_type(
                gast["args"][0], error_handler=self.error_handler)
            arr = router.gast_to_code(gast["args"], "java")
            return log_statement + "(Arrays.toString(new " + type_declaration + " " + arr + "))"

        return router.gast_to_code(gast["value"],
                                   "java") + "(" + router.gast_to_code(
                                       gast["args"], "java") + ")"

    def handle_subscript(self, gast):
        return self.error_handler.unsupported_feature()

    def handle_name(self, gast):
        return gast["value"]

    def handle_attribute(self, gast):
        return router.gast_to_code(gast["value"], "java") + "." + gast["id"]

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

    '''
    Translates gAST node to java function. Whether a function is static or
    has a return type is not known so the strings unknown are used to represent
    this value. Additionally variable types are unknown so parameters have type
    CustomType
    '''

    def handle_function_declaration(self, gast, lvl=0):
        name = router.gast_to_code(gast["id"], "java")
        if len(gast["params"]) != 0:
            args = "CustomType "
            args += general_helpers.list_helper(gast["params"], "java",
                                                ", CustomType ")
        else:
            args = ""

        body_indent = "\n\t" + "\t" * lvl
        closing_brace_indent = "\n" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "java", body_indent,
                                           lvl + 1)

        out = "public unknown unknown " + name
        out += "(" + args + ") {" + body_indent + body + closing_brace_indent + "}"

        return out

    def handle_return_statement(self, gast):
        return self.error_handler.unsupported_feature()

    def handle_assign_pattern(self, gast):
        return self.error_handler.unsupported_feature()

    def handle_arrow_func(self, gast):
        return self.error_handler.unsupported_feature()

    def handle_arr(self, gast):
        return "{" + router.gast_to_code(gast["elements"], "java") + "}"

    '''
    This is called when the root of a java ast is found. The body of the 
    AST is handled seperately - the functions are handled and then the 
    statements outside of functions are handled. If there are both functions
    and body statements a class with the functions and a main function with 
    body statements is returned. If there is just body statements the translated
    body statements will be returned. 
    '''

    def handle_root(self, gast):
        function_output = java_helpers.java_node_list_helper(
            gast["body"], True, "\n\t", 1)

        # if no functions in gast, do not wrap java output code
        if len(function_output) == 0:
            return java_helpers.java_node_list_helper(gast["body"], False, "\n")

        # if there are functions in gast, wrap them in class and wrap non-functions in main
        else:
            main_output = java_helpers.java_node_list_helper(
                gast["body"], False, "\n\t\t", 2)

            out = "class Test {\n\t"
            out += function_output

            # only include main if there is main_output
            if main_output != "":
                out += "\n\tpublic static void main(String[] args) {\n\t\t"
                out += main_output
                out += "\n\t}"

            out += "\n}"

        return out
