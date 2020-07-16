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

