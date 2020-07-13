
class PyGastToCodeConverter(AbstractGastToCodeConverter):

    def handle_log_statement(gast):
        return "print"
    
    def handle_var_assign(gast):
        value = router.gast_to_code(gast["varValue"])
        return router.gast_to_code(gast["varId"]) + " = " + value