import shared.gast_to_code.gast_to_code_router as router
from shared.gast_to_code.abstract_gast_to_code_converter import AbstractGastToCodeConverter

class JavaGastToCodeConverter(AbstractGastToCodeConverter):
    pretty_name = "Java"

    def handle_bool(gast):
        if gast["value"] == 1:
            return "true"
        else:
            return "false"

    def handle_if(gast, lvl=0):
        pass

    def handle_none(gast):
        pass

    def handle_while(gast, lvl=0):
        pass

    def handle_for_range(gast, lvl=0):
        pass

    def handle_for_of(gast, lvl=0):
        pass

    def handle_log_statement(gast):
        return "System.out.println"

    def handle_var_assign(gast):
        var_id = router.gast_to_code(gast["varId"], "java")
        var_value = router.gast_to_code(gast["varValue"], "java")
        var_type = gast["varValue"]["type"]
        
        if var_type == "num":
            kind = "int"
        elif var_type == "str":
            kind = "String"
        elif var_type == "bool":
            kind = "boolean"
        else:
            kind = "customType"
 
        return kind + " " + var_id + " = " + var_value

    def handle_aug_assign(gast):
        pass

    def handle_func_call(gast):
        return router.gast_to_code(gast["value"], "java") + "(" + router.gast_to_code(gast["args"], "java") + ")"

    def handle_subscript(gast):
        pass

    def handle_name(gast):
        return gast["value"]

    def handle_attribute(gast):
        pass

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