
class JsGastToCodeConverter(AbstractGastToCodeConverter):

    def handle_log_statement(gast):
        return "console.log"
    