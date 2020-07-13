
class PyGastToCodeConverter(AbstractGastToCodeConverter):

    def handle_log_statement(gast):
        return "print"