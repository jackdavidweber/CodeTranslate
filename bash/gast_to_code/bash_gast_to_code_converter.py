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
        ''' 
        temporary solution since gast needs to be fixed to handle vars and func names
        differently - this goes through and manually distinguishes using rules 
        '''
        args = router.gast_to_code(gast["args"], "bash")
        updated_args = ""
        for elm in args.split(" "):
            if elm == "":
                continue
            if elm.startswith('"'):
                updated_args += elm + " "
                continue
            if elm.isnumeric():
                updated_args += elm + " "
                continue
            new_elm = '"$' + elm + '"'
            updated_args += new_elm + " " 
            # remove trailing space
        updated_args = updated_args[:-1]

        return router.gast_to_code(gast["value"], "bash") + " " + updated_args

    def handle_name(gast):
        return gast["value"]