from javascript.gast_to_code.js_helpers import *
from shared.gast_to_code.abstract_gast_to_code_converter import AbstractGastToCodeConverter

class JsGastToCodeConverter(AbstractGastToCodeConverter):

    def handle_bool(gast):
        return gast_to_js_bool(gast)
    
    def handle_if(gast, lvl):
        return gast_to_js_if(gast, lvl)

    def handle_none(gast):
        return "null"

    def handle_while(gast, lvl):
        return gast_to_js_while(gast, lvl)

    def handle_for_range(gast, lvl):
        return gast_to_js_forRange(gast, lvl)

    def handle_for_of(gast, lvl):
        return gast_to_js_forOf(gast, lvl)

    def handle_log_statement(gast):
        return "console.log"

    def handle_var_assign(gast):
        return gast_to_js_var_assign(gast)

    def handle_aug_assign(gast):
        return gast_to_js_aug_assign(gast)

    def handle_func_call(gast):
        return gast_to_js_functions(gast)

    def handle_subscript(gast):
        return gast_to_js_subscript(gast)
    
    def handle_name(gast):
        return gast["value"]
    
    def handle_attribute(gast):
        return gast_to_js_attribute(gast)
    
    def handle_built_in_attribute(gast):
        return gast_to_js_built_in_attribute(gast)
    
    def handle_dict(gast):
        return gast_to_js_dict(gast)
    
    def handle_property(gast):
        return gast_to_js_property(gast)
    
    def handle_bool_op(gast):
        return gast_to_js_bool_op(gast)
    
    def handle_unary_op(gast):
        return gast_to_js_unary_op(gast)
    
    def handle_function_declaration(gast, lvl):
        return gast_to_js_func_declarations(gast, lvl)
    
    def handle_return_statement(gast):
        return gast_to_js_return_statement(gast)
    
    def handle_assign_pattern(gast):
        return gast_to_js_assign_pattern(gast)