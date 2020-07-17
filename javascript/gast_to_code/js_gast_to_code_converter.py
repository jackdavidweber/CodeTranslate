from shared.gast_to_code.abstract_gast_to_code_converter import AbstractGastToCodeConverter
import shared.gast_to_code.general_helpers as general_helpers
import js_built_in_functions
import shared.gast_to_code.gast_to_code_router as router


class JsGastToCodeConverter(AbstractGastToCodeConverter):
    pretty_name = "Javascript"

    def handle_bool(gast):
        if gast["value"] == 1:
            return "true"
        else:
            return "false"

    def handle_if(gast, lvl=0):
        test = router.gast_to_code(gast["test"], "js")
        body_indent = "\n\t" + "\t"*lvl
        closing_brace_indent = "\n" + "\t"*lvl
        body = general_helpers.list_helper(gast["body"], "js", body_indent, lvl+1)

        out = 'if (' + test + ') {' + body_indent + body + closing_brace_indent + "}"

        # orelse can either be empty, or be an elif or be an else
        if len(gast["orelse"]) == 0:
            pass
        elif gast["orelse"][0]["type"] == "if":
            out += " else " + router.gast_to_code(gast["orelse"], "js")
        else:
            out += " else {\n\t" + general_helpers.list_helper(gast["orelse"], "js", "\n\t") + "\n}"

        return out

    def handle_none(gast):
        return "null"

    def handle_while(gast, lvl=0):
        test = router.gast_to_code(gast["test"], "js")

        body_indent = "\n\t" + "\t"*lvl
        closing_brace_indent = "\n" + "\t"*lvl
        body = general_helpers.list_helper(gast["body"], "js", body_indent, lvl+1)

        out = 'while (' + test + ') {' + body_indent + body + closing_brace_indent + "}"
        return out

    def handle_for_range(gast, lvl=0):
        loop_init = router.gast_to_code(gast["init"], "js")
        loop_test = router.gast_to_code(gast["test"], "js")
        loop_update = router.gast_to_code(gast["update"], "js")

        body_indent = "\n\t" + "\t"*lvl
        closing_brace_indent = "\n" + "\t"*lvl
        body = general_helpers.list_helper(gast["body"], "js", body_indent, lvl+1)

        return "for (" + loop_init + "; " + loop_test + "; " + loop_update + ") {" + body_indent + body + closing_brace_indent + "}"

    def handle_for_of(gast, lvl=0):
        arr_str = router.gast_to_code(gast["iter"], "js")
        var_name = gast["init"]["value"]

        body_indent = "\n\t" + "\t"*lvl
        closing_brace_indent = "\n" + "\t"*lvl
        body = general_helpers.list_helper(gast["body"], "js", body_indent, lvl+1)

        out = "for (" + var_name + " of " + arr_str + ") {" + body_indent + body + closing_brace_indent + "}"
        return out

    def handle_log_statement(gast):
        return "console.log"

    def handle_var_assign(gast):
        kind = gast["kind"]
        varId = router.gast_to_code(gast["varId"], "js")
        varValue = router.gast_to_code(gast["varValue"], "js")

        if gast["varId"]["type"] == "subscript":
            return varId + " = " + varValue
        return kind + " " + varId + " = " + varValue

    def handle_aug_assign(gast):
        return router.gast_to_code(gast["left"], "js") + " " + gast["op"] + " " + router.gast_to_code(gast["right"], "js")

    def handle_func_call(gast):
        return router.gast_to_code(gast["value"], "js") + "(" + router.gast_to_code(gast["args"], "js") + ")"

    def handle_subscript(gast):
        return router.gast_to_code(gast["value"], "js") + "[" + router.gast_to_code(gast["index"], "js") + "]"

    def handle_name(gast):
        return gast["value"]

    def handle_attribute(gast):
        return router.gast_to_code(gast["value"], "js") + "." + gast["id"]

    def handle_built_in_attribute(gast):
        return router.gast_to_code(gast["value"], "js") + "." + js_built_in_functions.js_built_in_functions(gast["id"]).name

    def handle_dict(gast):
        return "{" + router.gast_to_code(gast["elements"], "js") + "}"

    def handle_property(gast):
        return router.gast_to_code(gast["key"], "js") + ": " + router.gast_to_code(gast["value"], "js")

    def handle_bool_op(gast):
        return general_helpers.gast_to_node_bin_op_helper(gast, "js")

    def handle_unary_op(gast):
        return "!" + router.gast_to_code(gast["arg"], "js")

    def handle_function_declaration(gast, lvl=0):
        name = router.gast_to_code(gast["id"], "js")
        args = router.gast_to_code(gast["params"], "js")

        body_indent = "\n\t" + "\t"*lvl
        closing_brace_indent = "\n" + "\t"*lvl
        body = general_helpers.list_helper(gast["body"], "js", body_indent, lvl+1)
        out = "function " + name
        out += "(" + args + ") {" + body_indent + body + closing_brace_indent + "}"

        return out

    def handle_return_statement(gast):
        return "return " + router.gast_to_code(gast["value"], "js")

    def handle_assign_pattern(gast):
        return router.gast_to_code(gast["left"], "js") + " = " + router.gast_to_code(gast["right"], "js")

    def handle_arr(gast):
        return "[" + router.gast_to_code(gast["elements"], "js") + "]"
