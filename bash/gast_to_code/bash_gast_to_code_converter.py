from shared.gast_to_code.abstract_gast_to_code_converter import AbstractGastToCodeConverter
import shared.gast_to_code.general_helpers as general_helpers
import shared.gast_to_code.gast_to_code_router as router


class BashGastToCodeConverter(AbstractGastToCodeConverter):
    pretty_name = "Bash"
   
    def handle_bool(gast):
        if gast["value"] == 1:
            return "true"
        else:
            return "false"
    
    def handle_log_statement(gast):
        return "echo"
    
    def handle_func_call(gast):
        # bash has no way to directly print arrays. This logic returns an error for such behavior
        if gast["value"]["type"] == "logStatement" and general_helpers.arr_in_list(gast["args"]):
            return "impossibleTranslationError: direct translation does not exist" # TODO: streamline error message as part of refactor

        return router.gast_to_code(gast["value"], "bash") + " " + router.gast_to_code(gast["args"], "bash")

    def handle_arr(gast):
        # This logic returns an error for nested arrays which are not supported in bash
        if general_helpers.arr_in_list(gast["elements"]):
            return "impossibleTranslationError: direct translation does not exist" # TODO: streamline error message as part of refactor

        return "(" + router.gast_to_code(gast["elements"], "py") + ")"
