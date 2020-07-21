import shared.gast_to_code.gast_to_code_router as router
import shared.gast_to_code.general_helpers as general_helpers
from shared.gast_to_code.abstract_gast_to_code_converter import AbstractGastToCodeConverter
import java.gast_to_code.java_helpers as java_helpers


class JavaGastToCodeConverter(AbstractGastToCodeConverter):
    name = "Java"
    is_beta = True
    is_input_lang = True
    is_output_lang = True

    def handle_bool(gast):
        if gast["value"] == 1:
            return "true"
        else:
            return "false"

    def handle_if(gast, lvl=0):
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

    def handle_none(gast):
        return "null"

    def handle_while(gast, lvl=0):
        pass

    def handle_for_range(gast, lvl=0):
        loop_init = router.gast_to_code(gast["init"], "java")
        loop_test = router.gast_to_code(gast["test"], "java")
        loop_update = router.gast_to_code(gast["update"], "java")

        body_indent = "\n\t" + "\t" * lvl
        closing_brace_indent = "\n" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "java", body_indent,
                                           lvl + 1)

        return "for (" + loop_init + "; " + loop_test + "; " + loop_update + ") {" + body_indent + body + closing_brace_indent + "}"

    def handle_for_of(gast, lvl=0):
        arr_str = router.gast_to_code(gast["iter"], "java")
        var_name = gast["init"]["value"]

        body_indent = "\n\t" + "\t" * lvl
        closing_brace_indent = "\n" + "\t" * lvl
        body = general_helpers.list_helper(gast["body"], "java", body_indent,
                                           lvl + 1)

        out = "for (" + var_name + " : " + arr_str + ") {" + body_indent + body + closing_brace_indent + "}"
        return out

    def handle_log_statement(gast):
        return "System.out.println"

    def handle_var_assign(gast):
        var_id = router.gast_to_code(gast["varId"], "java")
        var_value = router.gast_to_code(gast["varValue"], "java")

        kind = java_helpers.gast_to_java_type(gast["varValue"])

        return kind + " " + var_id + " = " + var_value

    def handle_aug_assign(gast):
        if "right" in gast:
            return router.gast_to_code(
                gast["left"],
                "java") + " " + gast["op"] + " " + router.gast_to_code(
                    gast["right"], "java")
        else:
            return router.gast_to_code(gast["left"], "java") + gast["op"]

    # TODO(taiga#149) gast_to_code should not be able to return System.out.println(1, 2)
    def handle_func_call(gast):
        # handles logstatement for single array
        if gast["value"]["type"] == "logStatement" and len(
                gast["args"]) == 1 and gast["args"][0]["type"] == "arr":
            log_statement = router.gast_to_code(gast["value"], "java")
            type_declaration = java_helpers.gast_to_java_type(gast["args"][0])
            arr = router.gast_to_code(gast["args"], "java")
            return log_statement + "(Arrays.toString(new " + type_declaration + " " + arr + "))"

        return router.gast_to_code(gast["value"],
                                   "java") + "(" + router.gast_to_code(
                                       gast["args"], "java") + ")"

    def handle_subscript(gast):
        pass

    def handle_name(gast):
        ''' 
        NOTE: some places store {"type": "name", "value": "s"} while others have
        {"type": "name", "id" : "s"} in gAST but both get routed to this func.
        We may want to re-evaluate gAST structure regarding funcs and vars
        '''
        if "value" in gast:
            return gast["value"]
        return gast["id"]

    def handle_attribute(gast):
        return router.gast_to_code(gast["value"], "java") + "." + gast["id"]

    def handle_built_in_attribute(gast):
        pass

    def handle_dict(gast):
        pass

    def handle_property(gast):
        pass

    def handle_bool_op(gast):
        pass

    def handle_unary_op(gast):
        pass

    def handle_function_declaration(gast, lvl=0):
        pass

    def handle_return_statement(gast):
        pass

    def handle_assign_pattern(gast):
        pass

    def handle_arr(gast):
        return "{" + router.gast_to_code(gast["elements"], "java") + "}"
