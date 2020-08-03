class Unittest():

    def __init__(self, code, language, is_input=True, is_output=True):
        self.language = language
        self.code = code
        self.is_input = is_input
        self.is_output = is_output

    def get_lang(self):
        return self.language

    def get_code(self):
        return self.code

    def get_input(self):
        return self.is_input

    def get_output(self):
        return self.is_output
