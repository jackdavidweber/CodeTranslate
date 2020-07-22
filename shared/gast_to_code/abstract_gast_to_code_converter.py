from abc import ABC, abstractmethod


class AbstractGastToCodeConverter(ABC):
    @abstractmethod
    def get_response(self):
        pass

    @abstractmethod
    def handle_log_statement(gast):
        pass

    @abstractmethod
    def handle_var_assign(gast):
        pass

    @abstractmethod
    def handle_bool(gast):
        pass

    @abstractmethod
    def handle_if(gast):
        pass

    @abstractmethod
    def handle_functions(gast):
        pass
