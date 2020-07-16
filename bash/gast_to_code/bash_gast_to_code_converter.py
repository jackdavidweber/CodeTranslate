from shared.gast_to_code.abstract_gast_to_code_converter import AbstractGastToCodeConverter
import shared.gast_to_code.general_helpers as general_helpers
import shared.gast_to_code.gast_to_code_router as router


class BashGastToCodeConverter(AbstractGastToCodeConverter):

    def handle_bool(gast):
        return "Bash does not support booleans"
    
    def handle_log_statement(gast):
        return "echo"
    
    def handle_func_call(gast):
        return router.gast_to_code(gast["value"], "bash") + " " + router.gast_to_code(gast["args"], "bash")

