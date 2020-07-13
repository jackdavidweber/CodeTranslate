from python.gast_to_code.py_helpers import *

class PyGastToCodeConverter(AbstractGastToCodeConverter):


    
    def handle_bool(gast):
        return gast_to_py_bool(gast)
    
    def handle_if(gast):
        return gast_to_py_if(gast)

    def handle_none(gast):
        return "None"

    def handle_while(gast, lvl)):
        return gast_to_py_while

    def handle_for_range(gast, lvl):
        return gast_to_py_forRange(gast, lvl)

    def handle_for_of(gast, lvl):
        return gast_to_py_forof

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