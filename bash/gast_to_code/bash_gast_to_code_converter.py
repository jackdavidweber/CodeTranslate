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
        return router.gast_to_code(gast["value"], "bash") + " " + router.gast_to_code(gast["args"], "bash")

    def handle_if(gast, lvl=0):
        test = router.gast_to_code(gast["test"], "bash")
        body_indent = "\n\t" + "\t"*lvl
        closing_exp_indent = "\n" + "\t"*lvl
        body = general_helpers.list_helper(gast["body"], "bash", body_indent, lvl+1)
        
        out = "if [[ " + test + " ]]; then" + body_indent + body + closing_exp_indent

        if len(gast["orelse"]) == 0:
            out += "fi"
        elif gast["orelse"][0]["type"] == "if":
            out += "el" + router.gast_to_code(gast["orelse"], "bash")
        else:
            out += "else\n\t" + general_helpers.list_helper(gast["orelse"], "bash", "\n\t") + "\nfi"

        return out