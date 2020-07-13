from python.gast_to_code.py_helpers import *
from shared.gast_to_code.abstract_gast_to_code_converter import AbstractGastToCodeConverter

class PyGastToCodeConverter(AbstractGastToCodeConverter):
    
    def handle_bool(gast):
        return gast_to_py_bool(gast)
    
    def handle_if(gast, lvl):
        return gast_to_py_if(gast, lvl)

    def handle_none(gast):
        return "None"

    def handle_while(gast, lvl):
        return gast_to_py_while(gast, lvl)

    def handle_for_range(gast, lvl):
        return gast_to_py_forRange(gast, lvl)

    def handle_for_of(gast, lvl):
        return gast_to_py_forOf(gast, lvl)

    def handle_log_statement(gast):
        return "print"

    def handle_var_assign(gast):
        return gast_to_py_var_assign(gast)

    def handle_aug_assign(gast):
        return gast_to_py_aug_assign(gast)

    def handle_func_call(gast):
        return gast_to_py_functions(gast)

    def handle_subscript(gast):
        return gast_to_py_subscript(gast)
    
    def handle_name(gast):
        return gast["value"]
    
    def handle_attribute(gast):
        return gast_to_py_attribute(gast)
    
    def handle_built_in_attribute(gast):
        return gast_to_py_built_in_attribute(gast)
    
    def handle_dict(gast):
        return gast_to_py_dict(gast)
    
    def handle_property(gast):
        return gast_to_py_property(gast)
    
    def handle_bool_op(gast):
        return gast_to_py_bool_op(gast)
    
    def handle_unary_op(gast):
        return gast_to_py_unary_op(gast)
    
    def handle_function_declaration(gast, lvl):
        return gast_to_py_func_declarations(gast, lvl)
    
    def handle_return_statement(gast):
        return gast_to_py_return_statement(gast)
    
    def handle_assign_pattern(gast):
        return gast_to_py_assign_pattern(gast)